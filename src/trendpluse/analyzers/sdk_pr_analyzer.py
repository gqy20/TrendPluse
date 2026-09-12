"""SDK PR 分析器。

使用 Claude Agent SDK 的工具调用能力分析 PR 候选数据。
- 候选全量写入临时文件（每批独立文件，重要性判断归 AI 探索）
- SDK 通过 Read/Grep 自主 triage + 深读，PreToolUse hook 限制只能访问本批文件
- pr_number 校验：LLM 输出的引用必须真实存在，编造被确定性过滤
"""

from __future__ import annotations

import asyncio
import shutil
import tempfile
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field

from trendpluse.analyzers.structured_query import QueryResult, StructuredQuery
from trendpluse.logger import get_logger
from trendpluse.models.agent_usage import AgentMetricsSummary, AgentRunMetrics
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial
from trendpluse.prompts import render_prompt

logger = get_logger(__name__)

SIGNAL_TYPES = Literal[
    "capability",
    "abstraction",
    "workflow",
    "eval",
    "safety",
    "performance",
    "commit",
    "release",
]

SIGNAL_CATEGORIES = Literal["engineering", "research"]


class PRSignalItem(BaseModel):
    """单个 PR 分析结果项。"""

    pr_number: int = Field(description="PR 编号（精确匹配文件数据）")
    repo: str = Field(description="仓库 owner/repo（与文件一致）")
    title: str = Field(description="信号标题（5-10字）")
    type: SIGNAL_TYPES = Field(
        description="信号类型：capability/abstraction/workflow/eval/safety/performance"
    )
    category: SIGNAL_CATEGORIES = Field(description="分类：engineering/research")
    impact_score: int = Field(ge=1, le=5, description="影响评分 1-5")
    why_it_matters: str = Field(description="重要性说明（1-2句话）")
    related_repos: list[str] = Field(default_factory=list, description="相关仓库")
    trends: list[str] = Field(default_factory=list, description="趋势关键词")


class PRSignalsResult(BaseModel):
    """批量 PR 分析结果。"""

    signals: list[PRSignalItem] = Field(default_factory=list)


class SDKPRAnalyzer:
    """基于 SDK 工具调用的 PR 分析器。

    对齐 SDKCommitAnalyzer 的已验证模式：每批独立文件 + 文件白名单
    hook + 引用确定性校验 + 批次可见性日志。与旧 TrendAnalyzer 的
    per-PR instructor 路径区别：候选不截断全量入文件，重要性筛选
    由 agent 探索完成（Read/Grep triage），而非代码预设。
    """

    def __init__(
        self,
        *,
        model: str | None = None,
        max_turns: int = 30,
        max_budget_usd: float = 10.0,
        batch_size: int = 40,
    ) -> None:
        self.model = model
        logger.info("SDKPRAnalyzer 初始化 model=%s", self.model)
        self.max_turns = max_turns
        self.max_budget_usd = max_budget_usd
        self.batch_size = batch_size
        self.allowed_tools = ["Read", "Grep"]

        # 各批次 Agent usage 记录
        self._run_metrics: list[AgentRunMetrics] = []

        self.query_engine = StructuredQuery[PRSignalsResult](
            output_model=PRSignalsResult,
            model=model,
            allowed_tools=self.allowed_tools,
            max_turns=max_turns,
            max_budget_usd=max_budget_usd,
        )

    def get_llm_metrics_summary(self) -> AgentMetricsSummary | None:
        """获取各批次累计的 Agent usage 聚合统计。"""
        return AgentMetricsSummary.from_runs(self._run_metrics)

    def _split_batches(
        self, prs: list[dict[str, Any]], batch_size: int | None = None
    ) -> list[list[dict[str, Any]]]:
        """将 PR 分批（批数随候选数伸缩，无上限截断）。"""
        size = batch_size or self.batch_size
        return [prs[i : i + size] for i in range(0, len(prs), size)]

    def _write_prs_file(
        self,
        work_dir: Path | str,
        prs: list[dict[str, Any]],
        suffix: str = "",
    ) -> str:
        """生成 markdown 格式的 PR 数据文件（全量字段，AI 按需读取）。"""
        work_path = Path(work_dir)
        file_path = work_path / f"prs{suffix}.md"

        lines = [
            "# GitHub PRs Analysis",
            "",
            f"**Total PRs:** {len(prs)}",
            "",
            "---",
            "",
        ]

        for idx, pr in enumerate(prs, 1):
            labels_text = ", ".join(pr.get("labels", [])) or "无"
            lines.extend(
                [
                    f"## PR {idx}",
                    "",
                    f"**Repo:** {pr.get('repo', 'N/A')}",
                    f"**Number:** {pr.get('number', 'N/A')}",
                    f"**Title:** {pr.get('title', 'N/A')}",
                    f"**Author:** {pr.get('author', 'Unknown')}",
                    f"**State:** {pr.get('state', 'N/A')}"
                    + (" (merged)" if pr.get("merged") else ""),
                    f"**Files Changed:** {pr.get('changed_files', 0)}",
                    f"**Additions:** +{pr.get('additions', 0)}",
                    f"**Deletions:** -{pr.get('deletions', 0)}",
                    f"**Labels:** {labels_text}",
                    f"**URL:** {pr.get('url', '')}",
                    "",
                    "### Description",
                    "",
                    str(pr.get("body") or "").strip() or "（无描述）",
                    "",
                    "---",
                    "",
                ]
            )

        file_path.write_text("\n".join(lines), encoding="utf-8")
        return str(file_path)

    def _validate_and_match(
        self, result: PRSignalsResult, prs: list[dict[str, Any]]
    ) -> list[Signal]:
        """按 (repo, pr_number) 确定性校验并转换为 Signal。"""
        prs_by_key = {(str(p.get("repo")), str(p.get("number"))): p for p in prs}

        signals: list[Signal] = []
        for idx, item in enumerate(result.signals):
            matching = prs_by_key.get((str(item.repo), str(item.pr_number)))
            if matching is None:
                logger.debug(
                    "PRSignalItem (repo=%s, pr_number=%s) 无法匹配，跳过",
                    item.repo,
                    item.pr_number,
                )
                continue

            merged_repos = list({item.repo, *(item.related_repos or [])})
            signals.append(
                Signal(
                    id=f"pr-signal-{idx}",
                    title=item.title,
                    type=item.type,
                    category=item.category,
                    impact_score=item.impact_score,
                    why_it_matters=item.why_it_matters,
                    sources=[matching.get("url", "")] if matching.get("url") else [],
                    related_repos=merged_repos,
                )
            )
        return signals

    @staticmethod
    def _material_to_pr(material: AnalysisMaterial) -> dict[str, Any]:
        """将 PR 分析材料转换为 prs 文件数据（body 为读取器获取的全文）。"""
        payload = material.raw_payload or {}
        labels = [
            label.get("name")
            for label in payload.get("labels", [])
            if isinstance(label, dict) and label.get("name")
        ]
        try:
            number: int | str = int(material.source_ref.external_id)
        except (TypeError, ValueError):
            number = str(material.source_ref.external_id)
        return {
            "repo": material.source_ref.repo,
            "number": number,
            "title": material.title,
            "body": material.body,
            "author": material.author or "Unknown",
            "state": payload.get("state", ""),
            "merged": payload.get("merged", False),
            "draft": payload.get("draft", False),
            "changed_files": payload.get("changed_files", 0),
            "additions": payload.get("additions", 0),
            "deletions": payload.get("deletions", 0),
            "labels": labels,
            "url": material.source_ref.url,
        }

    async def analyze_materials_async(
        self, materials: list[AnalysisMaterial]
    ) -> list[Signal]:
        """异步分析 PR 材料列表（全量，无截断）。

        与旧 TrendAnalyzer.analyze_materials_async 同签名，可作平替。
        """
        if not materials:
            return []
        prs = [self._material_to_pr(m) for m in materials]
        return await self._analyze_prs_shared(prs)

    async def _analyze_prs_shared(self, prs: list[dict[str, Any]]) -> list[Signal]:
        """共享分批分析流程（材料/候选两个入口复用）。"""
        work_dir = tempfile.mkdtemp(prefix="pr_analyzer_")

        try:
            batches = self._split_batches(prs)
            all_signals: list[Signal] = []

            for batch_index, batch in enumerate(batches, 1):
                batch_file = self._write_prs_file(
                    work_dir, batch, suffix=f"-batch-{batch_index}"
                )
                batch_signals = await self._analyze_batch(
                    batch,
                    batch_file,
                    batch_index=batch_index,
                    total_batches=len(batches),
                )
                all_signals.extend(batch_signals)

            return all_signals

        finally:
            shutil.rmtree(work_dir, ignore_errors=True)

    async def _analyze_batch(
        self,
        batch: list[dict[str, Any]],
        prs_file: str,
        *,
        batch_index: int = 1,
        total_batches: int = 1,
    ) -> list[Signal]:
        """分析单个批次。"""
        prompt = render_prompt(
            "sdk_pr_analyzer.pr_signal_extraction",
            prs_file=prs_file,
            batch_size=len(batch),
        )

        original_whitelist = self.query_engine.file_whitelist
        self.query_engine.file_whitelist = {str(Path(prs_file).resolve())}
        try:
            result: QueryResult[PRSignalsResult] = await self.query_engine.query_async(
                prompt
            )
        except Exception as e:
            logger.warning(
                "PR 批次分析失败 (batch %d/%d, prs=%d): %s: %s",
                batch_index,
                total_batches,
                len(batch),
                type(e).__name__,
                str(e)[:200],
            )
            return []
        finally:
            self.query_engine.file_whitelist = original_whitelist

        if result.metrics is not None:
            self._run_metrics.append(result.metrics)

        raw_signals = result.output.signals
        batch_keys = {(str(p.get("repo")), str(p.get("number"))) for p in batch}
        matched = [
            s for s in raw_signals if (str(s.repo), str(s.pr_number)) in batch_keys
        ]
        hallucinated = len(raw_signals) - len(matched)

        research_count = sum(1 for s in matched if s.category == "research")

        logger.info(
            "PR batch %d/%d done (prs=%d, raw_signals=%d, matched=%d, "
            "ref_mismatch=%d, research=%d, turns=%s, tokens=%s)",
            batch_index,
            total_batches,
            len(batch),
            len(raw_signals),
            len(matched),
            hallucinated,
            research_count,
            result.metrics.num_turns if result.metrics else "-",
            result.metrics.usage.total_tokens if result.metrics else "-",
        )
        if hallucinated:
            mismatched_refs = [
                f"{s.repo}#{s.pr_number}"
                for s in raw_signals
                if (str(s.repo), str(s.pr_number)) not in batch_keys
            ]
            logger.warning(
                "PR batch %d/%d: %d 个信号的 (repo, pr_number) 不在本批内"
                "（LLM 幻觉，已过滤）: %s",
                batch_index,
                total_batches,
                hallucinated,
                ", ".join(mismatched_refs[:5]),
            )

        # 同一 PR 只保留首条信号（prompt 约束的确定性兜底）
        seen_keys: set[tuple[str, int]] = set()
        deduped: list[PRSignalItem] = []
        for s in matched:
            key = (s.repo, s.pr_number)
            if key in seen_keys:
                continue
            seen_keys.add(key)
            deduped.append(s)
        if len(deduped) < len(matched):
            logger.warning(
                "PR batch %d/%d: %d 个信号引用了已产出的 PR（重复归属，已去重）",
                batch_index,
                total_batches,
                len(matched) - len(deduped),
            )
            matched = deduped

        return self._validate_and_match(PRSignalsResult(signals=matched), batch)

    def analyze_materials(self, materials: list[AnalysisMaterial]) -> list[Signal]:
        """同步封装。"""
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            pass
        else:
            raise RuntimeError(
                "检测到正在运行的事件循环，请改用 analyze_materials_async()。",
            )
        return asyncio.run(self.analyze_materials_async(materials))
