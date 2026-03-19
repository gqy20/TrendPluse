"""基于 Agent SDK 的日报总结增强器。"""

from __future__ import annotations

import json
import tempfile
import time
from collections import deque
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from trendpluse.history.daily_report_history import (
    DailyHistoryIndexBuilder,
)
from trendpluse.logger import get_logger
from trendpluse.models.agent_usage import AgentRunMetrics
from trendpluse.models.daily_summary import DailySummaryResult
from trendpluse.models.signal import DailyReport

logger = get_logger(__name__)


def _get_retryable_exceptions() -> tuple[type[Exception], ...]:
    """返回日报总结增强的可重试异常类型。"""
    exceptions: list[type[Exception]] = [ValidationError, RuntimeError, ValueError]
    try:
        from claude_agent_sdk import ClaudeSDKError
    except Exception:  # pragma: no cover - 依赖缺失时保持基础重试集合
        pass
    else:
        exceptions.append(ClaudeSDKError)
    return tuple(exceptions)


class DailySummaryAgent:
    """让 Agent 在全量历史语境下增强日报总结。"""

    _result_model = DailySummaryResult
    _retryable_exceptions = _get_retryable_exceptions()

    def __init__(
        self,
        *,
        reports_dir: str,
        history_index_path: str,
        model: str | None = None,
        max_turns: int = 20,
        max_budget_usd: float = 5.0,
        retry_max_attempts: int = 2,
        retry_wait_seconds: float = 0.0,
    ) -> None:
        self.reports_dir = Path(reports_dir)
        self.history_index_path = Path(history_index_path)
        self.model = model
        self.max_turns = max_turns
        self.max_budget_usd = max_budget_usd
        self.retry_max_attempts = retry_max_attempts
        self.retry_wait_seconds = retry_wait_seconds
        self._recent_cli_stderr: deque[str] = deque(maxlen=20)
        self._last_run_metrics: AgentRunMetrics | None = None

    def enhance(self, *, report: DailyReport, date) -> None:
        """增强日报总结字段。

        任何异常都向上抛出，由调用侧决定是否降级。
        """
        self.refresh_history_index()
        result = self._run_with_report_context(report)
        self._apply_result(report=report, result=result)

    async def enhance_async(self, *, report: DailyReport, date) -> None:
        """异步增强日报总结字段。"""
        self.refresh_history_index()
        result = await self._run_with_report_context_async(report)
        self._apply_result(report=report, result=result)

    @staticmethod
    def _apply_result(*, report: DailyReport, result: DailySummaryResult) -> None:
        """将增强结果统一回写到日报对象。"""
        report.summary_brief = result.summary_brief
        report.trend_status = result.trend_status
        report.trend_delta = result.trend_delta
        report.historical_basis_dates = result.historical_basis_dates
        report.historical_comparison = result.historical_comparison
        report.top_new_trends = result.top_new_trends
        report.top_continuing_trends = result.top_continuing_trends
        report.summary_confidence = result.confidence

    def get_last_run_metrics(self) -> AgentRunMetrics | None:
        """获取最近一次日报总结 Agent 的 usage 统计。"""
        return (
            self._last_run_metrics.model_copy(deep=True)
            if self._last_run_metrics
            else None
        )

    def refresh_history_index(self) -> None:
        """重建历史日报索引。"""
        builder = DailyHistoryIndexBuilder(
            reports_dir=self.reports_dir,
            index_path=self.history_index_path,
        )
        builder.build()

    def _handle_cli_stderr(self, line: str) -> None:
        """记录 Claude CLI 的 stderr，便于远端排障。"""
        self._recent_cli_stderr.append(line)
        logger.warning("DailySummaryAgent CLI stderr: %s", line)

    def _run_with_report_context(self, report: DailyReport) -> DailySummaryResult:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".json", delete=False
        ) as handle:
            handle.write(report.model_dump_json(indent=2, ensure_ascii=False))
            temp_path = Path(handle.name)

        try:
            last_exc: Exception | None = None
            for attempt in range(1, self.retry_max_attempts + 1):
                try:
                    response_text = self._run_agent_query(temp_path)
                    return DailySummaryResult.model_validate_json(response_text)
                except self._retryable_exceptions as exc:
                    last_exc = exc
                    if attempt >= self.retry_max_attempts:
                        break
                    logger.warning(
                        "日报总结增强失败，准备重试: attempt=%d/%d, error=%s",
                        attempt,
                        self.retry_max_attempts,
                        exc,
                    )
                    if self.retry_wait_seconds > 0:
                        time.sleep(self.retry_wait_seconds)
            assert last_exc is not None
            raise last_exc
        finally:
            temp_path.unlink(missing_ok=True)

    async def _run_with_report_context_async(
        self, report: DailyReport
    ) -> DailySummaryResult:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".json", delete=False
        ) as handle:
            handle.write(report.model_dump_json(indent=2, ensure_ascii=False))
            temp_path = Path(handle.name)

        try:
            last_exc: Exception | None = None
            for attempt in range(1, self.retry_max_attempts + 1):
                try:
                    response_text = await self._run_agent_query_async(temp_path)
                    return DailySummaryResult.model_validate_json(response_text)
                except self._retryable_exceptions as exc:
                    last_exc = exc
                    if attempt >= self.retry_max_attempts:
                        break
                    logger.warning(
                        "日报总结增强失败，准备重试: attempt=%d/%d, error=%s",
                        attempt,
                        self.retry_max_attempts,
                        exc,
                    )
                    if self.retry_wait_seconds > 0:
                        time.sleep(self.retry_wait_seconds)
            assert last_exc is not None
            raise last_exc
        finally:
            temp_path.unlink(missing_ok=True)

    def _run_agent_query(
        self,
        current_report_path: Path,
    ) -> str:
        import asyncio

        try:
            asyncio.get_running_loop()
        except RuntimeError:
            pass
        else:
            raise RuntimeError(
                "检测到正在运行的事件循环，请改用 enhance_async() 或 "
                "_run_with_report_context_async()。"
            )

        return asyncio.run(self._run_agent_query_async(current_report_path))

    async def _run_agent_query_async(
        self,
        current_report_path: Path,
    ) -> str:
        try:
            from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
        except Exception as exc:  # pragma: no cover
            raise RuntimeError(
                "未安装 claude-agent-sdk，请先安装依赖后再运行。"
            ) from exc

        prompt = self._build_prompt(current_report_path)
        self._recent_cli_stderr.clear()
        options = ClaudeAgentOptions(
            model=self.model,
            allowed_tools=["Read", "Glob", "LS", "Grep"],
            output_format=self._build_output_format(),
            max_turns=self.max_turns,
            max_budget_usd=self.max_budget_usd,
            stderr=self._handle_cli_stderr,
        )

        result_text: str | None = None
        structured_output: Any = None
        self._last_run_metrics = None
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, ResultMessage):
                self._last_run_metrics = AgentRunMetrics.from_sdk_result(
                    model=self.model,
                    session_id=message.session_id,
                    num_turns=message.num_turns,
                    duration_ms=message.duration_ms,
                    duration_api_ms=message.duration_api_ms,
                    total_cost_usd=message.total_cost_usd,
                    usage=message.usage,
                )
                if message.structured_output is not None:
                    structured_output = message.structured_output
                if isinstance(message.result, str) and message.result.strip():
                    result_text = message.result.strip()
        if structured_output is not None:
            if isinstance(structured_output, str):
                return structured_output
            return json.dumps(structured_output, ensure_ascii=False)
        if result_text:
            return result_text
        raise RuntimeError("DailySummaryAgent 未返回任何结果")

    def _build_prompt(self, current_report_path: Path) -> str:
        return (
            "你是日报总结智能体。你的目标不是复述历史，而是判断今天的"
            "趋势在全量历史中的位置。\n\n"
            "请按以下顺序工作：\n"
            f"1. 先读取历史日报索引：{self.history_index_path}\n"
            f"2. 再读取今天的日报草稿：{current_report_path}\n"
            f"3. 历史日报原文目录：{self.reports_dir}\n"
            "4. 你可以自行决定需要回读哪些历史日报原文，不要只局限于最近几天\n\n"
            "要求：\n"
            "- 历史日报都可以作为参考范围\n"
            "- 但最终 summary_brief 必须聚焦“今天发生了什么，以及相对历史意味着什么”\n"
            "- 先读索引建立全局认识，再自主挑选需要深读的历史日报\n"
            "- 不要把前一天的趋势原样当成今天的新趋势\n"
            "- 如果今天是延续趋势，明确指出延续和新增推进点\n"
            "- 所有输出必须使用中文\n\n"
            "请返回 JSON，字段必须严格符合 schema。\n"
        )

    @staticmethod
    def _build_output_format() -> dict[str, Any]:
        return {
            "type": "json_schema",
            "schema": DailySummaryResult.model_json_schema(),
        }
