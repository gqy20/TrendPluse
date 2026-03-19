"""Agent SDK usage 与成本统计模型。"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from pydantic import BaseModel, Field


def _coerce_int(value: Any) -> int:
    """将 usage 数值安全转换为非负整数。"""
    if isinstance(value, bool):
        return 0
    if isinstance(value, int | float):
        return max(0, int(value))
    return 0


def _coerce_float(value: Any) -> float:
    """将成本数值安全转换为非负浮点数。"""
    if isinstance(value, bool):
        return 0.0
    if isinstance(value, int | float):
        return max(0.0, float(value))
    return 0.0


class AgentUsageBreakdown(BaseModel):
    """对 SDK usage 中常见数值字段做标准化抽取。"""

    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)
    cache_creation_input_tokens: int = Field(default=0, ge=0)
    cache_read_input_tokens: int = Field(default=0, ge=0)
    total_tokens: int = Field(default=0, ge=0)
    tool_uses: int = Field(default=0, ge=0)
    duration_ms: int = Field(default=0, ge=0)

    @classmethod
    def from_usage(cls, usage: Mapping[str, Any] | None) -> AgentUsageBreakdown:
        """从 SDK usage 原始数据构建标准化统计。"""
        raw = dict(usage or {})
        total_tokens = _coerce_int(raw.get("total_tokens"))
        input_tokens = _coerce_int(raw.get("input_tokens"))
        output_tokens = _coerce_int(raw.get("output_tokens"))
        cache_creation_input_tokens = _coerce_int(
            raw.get("cache_creation_input_tokens")
        )
        cache_read_input_tokens = _coerce_int(raw.get("cache_read_input_tokens"))
        if total_tokens == 0:
            total_tokens = (
                input_tokens
                + output_tokens
                + cache_creation_input_tokens
                + cache_read_input_tokens
            )
        return cls(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_creation_input_tokens=cache_creation_input_tokens,
            cache_read_input_tokens=cache_read_input_tokens,
            total_tokens=total_tokens,
            tool_uses=_coerce_int(raw.get("tool_uses")),
            duration_ms=_coerce_int(raw.get("duration_ms")),
        )

    @classmethod
    def aggregate(cls, items: Iterable[AgentUsageBreakdown]) -> AgentUsageBreakdown:
        """聚合多次 usage 统计。"""
        totals = cls()
        for item in items:
            totals.input_tokens += item.input_tokens
            totals.output_tokens += item.output_tokens
            totals.cache_creation_input_tokens += item.cache_creation_input_tokens
            totals.cache_read_input_tokens += item.cache_read_input_tokens
            totals.total_tokens += item.total_tokens
            totals.tool_uses += item.tool_uses
            totals.duration_ms += item.duration_ms
        return totals


class AgentRunMetrics(BaseModel):
    """单次 Agent 调用的 usage 与成本。"""

    model: str | None = Field(default=None)
    session_id: str | None = Field(default=None)
    num_turns: int = Field(default=0, ge=0)
    duration_ms: int = Field(default=0, ge=0)
    duration_api_ms: int = Field(default=0, ge=0)
    total_cost_usd: float = Field(default=0.0, ge=0.0)
    usage: AgentUsageBreakdown = Field(default_factory=AgentUsageBreakdown)
    raw_usage: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_sdk_result(
        cls,
        *,
        model: str | None,
        session_id: Any,
        num_turns: Any,
        duration_ms: Any,
        duration_api_ms: Any,
        total_cost_usd: Any,
        usage: Mapping[str, Any] | None,
    ) -> AgentRunMetrics:
        """从 SDK ResultMessage 提取统计。"""
        raw_usage = dict(usage or {})
        return cls(
            model=model,
            session_id=str(session_id) if isinstance(session_id, str) else None,
            num_turns=_coerce_int(num_turns),
            duration_ms=_coerce_int(duration_ms),
            duration_api_ms=_coerce_int(duration_api_ms),
            total_cost_usd=_coerce_float(total_cost_usd),
            usage=AgentUsageBreakdown.from_usage(raw_usage),
            raw_usage=raw_usage,
        )


class AgentMetricsSummary(BaseModel):
    """多次 Agent 调用的聚合统计。"""

    run_count: int = Field(default=0, ge=0)
    models: list[str] = Field(default_factory=list)
    total_turns: int = Field(default=0, ge=0)
    total_duration_ms: int = Field(default=0, ge=0)
    total_api_duration_ms: int = Field(default=0, ge=0)
    total_cost_usd: float = Field(default=0.0, ge=0.0)
    usage: AgentUsageBreakdown = Field(default_factory=AgentUsageBreakdown)

    @classmethod
    def from_runs(
        cls, runs: Iterable[AgentRunMetrics | None]
    ) -> AgentMetricsSummary | None:
        """从多次调用结果聚合 usage 统计。"""
        valid_runs = [run for run in runs if isinstance(run, AgentRunMetrics)]
        if not valid_runs:
            return None

        models = sorted(
            {
                run.model.strip()
                for run in valid_runs
                if isinstance(run.model, str) and run.model.strip()
            }
        )
        return cls(
            run_count=len(valid_runs),
            models=models,
            total_turns=sum(run.num_turns for run in valid_runs),
            total_duration_ms=sum(run.duration_ms for run in valid_runs),
            total_api_duration_ms=sum(run.duration_api_ms for run in valid_runs),
            total_cost_usd=round(
                sum(run.total_cost_usd for run in valid_runs),
                6,
            ),
            usage=AgentUsageBreakdown.aggregate([run.usage for run in valid_runs]),
        )

    @classmethod
    def combine(
        cls,
        *,
        runs: Iterable[AgentRunMetrics | None] = (),
        summaries: Iterable[AgentMetricsSummary | None] = (),
    ) -> AgentMetricsSummary | None:
        """合并单次运行与已聚合摘要。"""
        parts = [
            summary for summary in summaries if isinstance(summary, AgentMetricsSummary)
        ]
        run_summary = cls.from_runs(runs)
        if run_summary is not None:
            parts.append(run_summary)
        if not parts:
            return None

        models = sorted(
            {
                model
                for part in parts
                for model in part.models
                if isinstance(model, str) and model.strip()
            }
        )
        return cls(
            run_count=sum(part.run_count for part in parts),
            models=models,
            total_turns=sum(part.total_turns for part in parts),
            total_duration_ms=sum(part.total_duration_ms for part in parts),
            total_api_duration_ms=sum(part.total_api_duration_ms for part in parts),
            total_cost_usd=round(
                sum(part.total_cost_usd for part in parts),
                6,
            ),
            usage=AgentUsageBreakdown.aggregate([part.usage for part in parts]),
        )
