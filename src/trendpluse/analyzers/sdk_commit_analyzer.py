"""SDK Commit 分析器。

使用 Claude Agent SDK 的工具调用能力分析 commit 数据。
- commit 信息写入临时文件（每批独立文件）
- SDK 通过 Read/Grep 读取分析，PreToolUse hook 限制只能访问本批文件
- 返回结构化信号列表
"""

from __future__ import annotations

import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError

from trendpluse.analyzers.structured_query import QueryResult, StructuredQuery
from trendpluse.logger import get_logger
from trendpluse.models.agent_usage import AgentMetricsSummary, AgentRunMetrics
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial
from trendpluse.prompts import render_prompt

logger = get_logger(__name__)

# 有效的信号类型
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


# ============ SDK 输出模型 ============


class CommitSignalItem(BaseModel):
    """单个 commit 分析结果项。"""

    title: str = Field(description="信号标题（5-10字）")
    type: SIGNAL_TYPES = Field(
        description="信号类型：capability/abstraction/workflow/eval/safety/performance"
    )
    category: SIGNAL_CATEGORIES = Field(description="分类：engineering/research")
    impact_score: int = Field(ge=1, le=5, description="影响评分 1-5")
    why_it_matters: str = Field(description="重要性说明（1-2句话）")
    commit_sha: str = Field(description="对应的 commit SHA（精确匹配）")
    related_repos: list[str] = Field(default_factory=list, description="相关仓库")
    trends: list[str] = Field(default_factory=list, description="趋势关键词")
    tech_details: dict[str, Any] = Field(default_factory=dict, description="技术细节")


class CommitSignalsResult(BaseModel):
    """批量 commit 分析结果。"""

    signals: list[CommitSignalItem] = Field(default_factory=list)
    analyzed_count: int = Field(default=0, description="分析的 commit 数量")


# ============ SDKCommitAnalyzer 实现 ============


class SDKCommitAnalyzer:
    """基于 SDK 工具调用的 Commit 分析器。

    使用 Claude Agent SDK 的 Read/Grep 工具读取 commit 文件，
    自主分析并返回结构化信号。
    """

    def __init__(
        self,
        *,
        model: str | None = None,
        max_turns: int = 30,
        max_budget_usd: float = 10.0,
        batch_size: int = 200,
    ) -> None:
        """初始化分析器。

        Args:
            model: 模型名称（可选，默认使用 SDK 配置）
            max_turns: 最大交互轮次（默认 30）
            max_budget_usd: 最大预算（默认 $10.0，可由
                COMMIT_AGENT_MAX_BUDGET_USD 配置）
            batch_size: 每批处理的 commit 数量（默认 200）
        """
        self.model = model
        logger.info("SDKCommitAnalyzer 初始化 model=%s", self.model)
        self.max_turns = max_turns
        self.max_budget_usd = max_budget_usd
        self.batch_size = batch_size
        self.allowed_tools = ["Read", "Grep"]

        # 各批次 Agent usage 记录
        self._run_metrics: list[AgentRunMetrics] = []

        # 初始化 SDK 查询引擎
        self.query_engine = StructuredQuery[CommitSignalsResult](
            output_model=CommitSignalsResult,
            model=model,
            allowed_tools=self.allowed_tools,
            max_turns=max_turns,
            max_budget_usd=max_budget_usd,
        )

    def get_llm_metrics_summary(self) -> AgentMetricsSummary | None:
        """获取各批次累计的 Agent usage 聚合统计。"""
        return AgentMetricsSummary.from_runs(self._run_metrics)

    def _material_to_commit(self, material: AnalysisMaterial) -> dict[str, Any]:
        """将分析材料转换为 commit 字典。"""
        return {
            "repo": material.source_ref.repo,
            "sha": material.source_ref.external_id,
            "message": material.raw_payload.get("message", material.title),
            "author": material.author,
            "timestamp": material.created_at or "",
            "files_changed": material.source_ref.metadata.get("files_changed", 0),
            "additions": material.source_ref.metadata.get("additions", 0),
            "deletions": material.source_ref.metadata.get("deletions", 0),
        }

    def _split_batches(
        self, commits: list[dict[str, Any]], batch_size: int | None = None
    ) -> list[list[dict[str, Any]]]:
        """将 commits 分批。"""
        size = batch_size or self.batch_size
        return [commits[i : i + size] for i in range(0, len(commits), size)]

    def _write_commits_file(
        self,
        work_dir: Path | str,
        commits: list[dict[str, Any]],
        suffix: str = "",
    ) -> str:
        """生成 markdown 格式的 commits 文件。

        Args:
            work_dir: 工作目录
            commits: commit 数据列表
            suffix: 文件名后缀（分批时为 -batch-N，确保每批独立文件）

        Returns:
            生成的文件路径
        """
        work_path = Path(work_dir)
        file_path = work_path / f"commits{suffix}.md"

        lines = [
            "# GitHub Commits Analysis",
            "",
            f"**Total Commits:** {len(commits)}",
            f"**Generated:** {datetime.now().isoformat()}",
            "",
            "---",
            "",
        ]

        for idx, commit in enumerate(commits, 1):
            lines.extend(
                [
                    f"## Commit {idx}",
                    "",
                    f"**SHA:** `{commit.get('sha', 'N/A')}`",
                    f"**Repo:** {commit.get('repo', 'N/A')}",
                    f"**Author:** {commit.get('author', 'Unknown')}",
                    f"**Time:** {commit.get('timestamp', 'N/A')}",
                    f"**Files Changed:** {commit.get('files_changed', 0)}",
                    f"**Additions:** +{commit.get('additions', 0)}",
                    f"**Deletions:** -{commit.get('deletions', 0)}",
                    "",
                    "### Message",
                    "",
                    "```",
                    f"{commit.get('message', '')}",
                    "```",
                    "",
                    "---",
                    "",
                ]
            )

        file_path.write_text("\n".join(lines), encoding="utf-8")
        return str(file_path)

    def _build_prompt(self, commits_file: str, batch_size: int) -> str:
        """构建分析 prompt。"""
        return render_prompt(
            "sdk_commit_analyzer.commit_analysis",
            commits_file=commits_file,
        )

    def _validate_and_match(
        self, result: CommitSignalsResult, commits: list[dict[str, Any]]
    ) -> list[Signal]:
        """验证 signals 并匹配到对应的 commits。

        Args:
            result: SDK 返回的分析结果
            commits: 原始 commit 数据

        Returns:
            验证通过的 Signal 列表
        """
        signals = []
        commits_by_sha = {c.get("sha"): c for c in commits}

        for idx, item in enumerate(result.signals):
            # 尝试通过 SHA 匹配
            matching_commit = commits_by_sha.get(item.commit_sha)

            if not matching_commit:
                logger.debug(f"CommitSignalItem SHA {item.commit_sha} 无法匹配，跳过")
                continue

            try:
                repo = matching_commit.get("repo", "")
                commit_sha = item.commit_sha
                commit_url = f"https://github.com/{repo}/commit/{commit_sha}"

                # 合并 related_repos
                merged_repos = list(set([repo] + item.related_repos))

                # 构建 Signal
                signal = Signal(
                    id=f"signal-{idx}",
                    title=item.title,
                    type=item.type,
                    category=item.category,
                    impact_score=item.impact_score,
                    why_it_matters=item.why_it_matters,
                    sources=[commit_url],
                    related_repos=merged_repos,
                )
                signals.append(signal)

            except ValidationError as e:
                logger.debug(f"Signal 验证失败: {e}")
                continue

        return signals

    async def analyze_materials_async(
        self, materials: list[AnalysisMaterial]
    ) -> list[Signal]:
        """异步分析 commit 材料列表。

        每批写入独立的 commits 文件，SDK 只能看到本批数据
        （PreToolUse hook 白名单），避免跨批 SHA 混淆与 token 浪费。

        Args:
            materials: AnalysisMaterial 列表

        Returns:
            Signal 列表
        """
        if not materials:
            return []

        # 转换为 commit 格式
        commits = [self._material_to_commit(m) for m in materials]

        # 创建临时工作目录
        work_dir = tempfile.mkdtemp(prefix="commit_analyzer_")

        try:
            # 分批处理：每批写独立文件
            batches = self._split_batches(commits)
            all_signals: list[Signal] = []

            for batch_index, batch in enumerate(batches, 1):
                batch_file = self._write_commits_file(
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
            # 清理临时目录
            shutil.rmtree(work_dir, ignore_errors=True)

    async def _analyze_batch(
        self,
        batch: list[dict[str, Any]],
        commits_file: str,
        *,
        batch_index: int = 1,
        total_batches: int = 1,
    ) -> list[Signal]:
        """分析单个批次。

        Args:
            batch: 当前批次的 commits
            commits_file: 本批 commits 文件路径（agent 只能访问它）
            batch_index: 批次序号（1 起，用于日志）
            total_batches: 总批数

        Returns:
            当前批次的 signals
        """
        prompt = self._build_prompt(commits_file, len(batch))

        # 本批白名单：agent 只能读本批文件
        original_whitelist = self.query_engine.file_whitelist
        self.query_engine.file_whitelist = {str(Path(commits_file).resolve())}
        try:
            result: QueryResult[
                CommitSignalsResult
            ] = await self.query_engine.query_async(prompt)
        except Exception as e:
            logger.warning(
                "Commit 批次分析失败 (batch %d/%d, commits=%d): %s: %s",
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
        batch_shas = {c.get("sha") for c in batch}
        matched = [s for s in raw_signals if s.commit_sha in batch_shas]
        hallucinated = len(raw_signals) - len(matched)
        research_count = sum(1 for s in matched if s.category == "research")

        # 批次可见性：产出与 SHA 匹配率一目了然（修复"成功但零产出"盲区）
        logger.info(
            "Commit batch %d/%d done (commits=%d, raw_signals=%d, "
            "matched=%d, sha_mismatch=%d, research=%d, turns=%s, tokens=%s)",
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
            logger.warning(
                "Commit batch %d/%d: %d 个信号的 SHA 不在本批内（LLM 幻觉，已过滤）",
                batch_index,
                total_batches,
                hallucinated,
            )

        return self._validate_and_match(result.output, batch)
