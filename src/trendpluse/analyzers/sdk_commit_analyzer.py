"""SDK Commit 分析器。

使用 Claude Agent SDK 的工具调用能力分析 commit 数据。
- commit 信息写入临时文件
- SDK 通过 Read/Grep 自主读取分析
- 返回结构化信号列表
"""

from __future__ import annotations

import asyncio
import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError

from trendpluse.analyzers.structured_query import QueryResult, StructuredQuery
from trendpluse.logger import get_logger
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial

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


# ============ Prompt 模板 ============


COMMIT_ANALYSIS_PROMPT = """\
你是一个技术趋势分析专家。请分析 GitHub commits 数据，提取有价值的技术趋势信号。

## 任务
1. 首先读取 {commits_file} 文件了解 commit 数据
2. 仔细分析每个 commit 的技术内容
3. 识别有价值的技术趋势信号

## 趋势类型
- capability: 🚀 新功能/能力
- performance: ⚡ 性能优化
- safety: 🛡️ 安全性增强
- abstraction: 🎨 抽象/架构改进
- workflow: ⚙️ 工作流优化
- eval: 📊 评估/测试改进

## 输出要求
返回 JSON 格式的 signals 数组，每个 signal 必须包含：
- commit_sha: 精确匹配输入数据中的 sha 值（必需）
- title: 5-10 字简短标题（中文）
- type: 上述趋势类型之一
- category: engineering 或 research
- impact_score: 1-5 的整数评分
- why_it_matters: 说明为什么重要（中文，1-2句话）
- related_repos: 相关仓库列表（可选）
- trends: 趋势关键词列表（可选）
- tech_details: 技术细节字典（可选）

如果分析认为没有有价值的趋势，返回空数组。

## 重要提示
- 必须完整阅读文件，不能遗漏任何 commit
- commit_sha 必须精确匹配输入数据中的 sha 字段值
- 所有文本内容必须使用中文
- 只返回真正有价值的趋势（避免琐碎修复）
"""


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
        max_budget_usd: float = 3.0,
        batch_size: int = 200,
    ) -> None:
        """初始化分析器。

        Args:
            model: 模型名称（可选，默认使用 SDK 配置）
            max_turns: 最大交互轮次（默认 30）
            max_budget_usd: 最大预算（默认 $3.0）
            batch_size: 每批处理的 commit 数量（默认 200）
        """
        self.model = model
        self.max_turns = max_turns
        self.max_budget_usd = max_budget_usd
        self.batch_size = batch_size
        self.allowed_tools = ["Read", "Grep"]

        # 初始化 SDK 查询引擎
        self.query_engine = StructuredQuery[CommitSignalsResult](
            output_model=CommitSignalsResult,
            model=model,
            allowed_tools=self.allowed_tools,
            max_turns=max_turns,
            max_budget_usd=max_budget_usd,
        )

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
        self, work_dir: Path | str, commits: list[dict[str, Any]]
    ) -> str:
        """生成 markdown 格式的 commits 文件。

        Args:
            work_dir: 工作目录
            commits: commit 数据列表

        Returns:
            生成的文件路径
        """
        work_path = Path(work_dir)
        file_path = work_path / "commits.md"

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
        return COMMIT_ANALYSIS_PROMPT.format(
            commits_file=commits_file, batch_size=batch_size
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
            # 写入 commits 文件
            commits_file = self._write_commits_file(work_dir, commits)

            # 分批处理
            batches = self._split_batches(commits)
            all_signals: list[Signal] = []

            for batch in batches:
                batch_signals = await self._analyze_batch(batch, commits_file)
                all_signals.extend(batch_signals)

            return all_signals

        finally:
            # 清理临时目录
            shutil.rmtree(work_dir, ignore_errors=True)

    async def _analyze_batch(
        self, batch: list[dict[str, Any]], commits_file: str
    ) -> list[Signal]:
        """分析单个批次。

        Args:
            batch: 当前批次的 commits
            commits_file: commits 文件路径

        Returns:
            当前批次的 signals
        """
        prompt = self._build_prompt(commits_file, len(batch))

        try:
            result: QueryResult[
                CommitSignalsResult
            ] = await self.query_engine.query_async(prompt)

            # 验证和匹配
            return self._validate_and_match(result.output, batch)

        except Exception as e:
            logger.warning(f"批次分析失败: {type(e).__name__}: {e}")
            return []

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
