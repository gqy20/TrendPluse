"""SDKCommitAnalyzer 单元测试。

基于 TDD：先写测试，再实现功能。
"""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import BaseModel, Field

from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial

# ============ 测试模型 ============


class CommitSignalItem(BaseModel):
    """单个 commit 分析结果项。"""

    title: str
    type: str
    category: str
    impact_score: int = Field(ge=1, le=5)
    why_it_matters: str
    commit_sha: str
    related_repos: list[str] = Field(default_factory=list)
    trends: list[str] = Field(default_factory=list)
    tech_details: dict[str, Any] = Field(default_factory=dict)


class CommitSignalsResult(BaseModel):
    """批量 commit 分析结果。"""

    signals: list[CommitSignalItem]
    analyzed_count: int


# ============ 测试数据 ============


@pytest.fixture
def sample_commits():
    """示例 commit 数据。"""
    return [
        {
            "repo": "anthropics/claude-sdk-python",
            "sha": "abc123def456",
            "message": "feat: add streaming API support for real-time responses",
            "author": "developer1",
            "timestamp": "2026-01-02T10:00:00Z",
            "files_changed": 5,
            "additions": 150,
            "deletions": 20,
        },
        {
            "repo": "anthropics/claude-sdk-python",
            "sha": "def456abc789",
            "message": "fix: resolve timeout issue in stream handler",
            "author": "developer2",
            "timestamp": "2026-01-02T11:00:00Z",
            "files_changed": 2,
            "additions": 10,
            "deletions": 5,
        },
        {
            "repo": "anthropics/claude-sdk-python",
            "sha": "ghi789jkl012",
            "message": "perf: optimize tokenization for Chinese text processing",
            "author": "developer3",
            "timestamp": "2026-01-02T12:00:00Z",
            "files_changed": 8,
            "additions": 300,
            "deletions": 50,
        },
    ]


@pytest.fixture
def sample_materials(sample_commits):
    """转换为 AnalysisMaterial。"""
    return [AnalysisMaterial.from_commit_details(commit) for commit in sample_commits]


# ============ SDKCommitAnalyzer 测试 ============


class TestSDKCommitAnalyzerInit:
    """初始化测试。"""

    def test_create_with_defaults(self):
        """默认参数创建。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        assert analyzer.max_turns == 30
        assert analyzer.max_budget_usd == 3.0
        assert analyzer.batch_size == 200
        assert analyzer.allowed_tools == ["Read", "Grep"]

    def test_create_with_custom_params(self):
        """自定义参数创建。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer(
            model="sonnet",
            max_turns=50,
            max_budget_usd=5.0,
            batch_size=100,
        )

        assert analyzer.model == "sonnet"
        assert analyzer.max_turns == 50
        assert analyzer.max_budget_usd == 5.0
        assert analyzer.batch_size == 100


class TestWriteCommitsFile:
    """commits 文件生成测试。"""

    def test_write_commits_creates_markdown_file(self, sample_commits, tmp_path):
        """生成 markdown 格式的 commits 文件。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()
        work_dir = tmp_path / "test_work"
        work_dir.mkdir()

        file_path = analyzer._write_commits_file(work_dir, sample_commits)

        assert Path(file_path).exists()
        content = Path(file_path).read_text()
        assert "abc123def456" in content
        assert "feat: add streaming API" in content
        assert "anthropics/claude-sdk-python" in content

    def test_write_commits_includes_required_fields(self, sample_commits, tmp_path):
        """文件包含所有必需字段。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()
        work_dir = tmp_path / "test_work"
        work_dir.mkdir()

        file_path = analyzer._write_commits_file(work_dir, sample_commits)
        content = Path(file_path).read_text()

        # 检查关键字段
        for commit in sample_commits:
            assert commit["sha"] in content
            assert commit["message"] in content
            assert commit["repo"] in content


class TestBuildPrompt:
    """Prompt 构建测试。"""

    def test_prompt_contains_file_path(self, tmp_path):
        """prompt 包含文件路径。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()
        commits_file = str(tmp_path / "commits.md")

        prompt = analyzer._build_prompt(commits_file, 3)

        assert commits_file in prompt
        assert "streaming" in prompt.lower() or "分析" in prompt

    def test_prompt_includes_output_schema(self, tmp_path):
        """prompt 包含输出格式说明。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()
        commits_file = str(tmp_path / "commits.md")

        prompt = analyzer._build_prompt(commits_file, 3)

        assert "commit_sha" in prompt
        assert "title" in prompt
        assert "type" in prompt


class TestMaterialToCommit:
    """材料转换测试。"""

    def test_converts_material_to_commit_dict(self, sample_materials, sample_commits):
        """正确转换 AnalysisMaterial 到 commit dict。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()
        result = analyzer._material_to_commit(sample_materials[0])

        assert result["sha"] == sample_commits[0]["sha"]
        assert result["message"] == sample_commits[0]["message"]
        assert result["repo"] == sample_commits[0]["repo"]
        assert result["author"] == sample_commits[0]["author"]


class TestSplitBatches:
    """分批处理测试。"""

    def test_split_single_batch(self, sample_commits):
        """单个批次。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer(batch_size=10)
        batches = analyzer._split_batches(sample_commits)

        assert len(batches) == 1
        assert batches[0] == sample_commits

    def test_split_multiple_batches(self, sample_commits):
        """多个批次。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer(batch_size=2)
        batches = analyzer._split_batches(sample_commits)

        assert len(batches) == 2
        assert len(batches[0]) == 2
        assert len(batches[1]) == 1


class TestValidateAndMatch:
    """验证和 SHA 匹配测试。"""

    def test_match_signals_to_commits(self, sample_commits):
        """正确匹配 signals 到 commits。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        result = CommitSignalsResult(
            signals=[
                CommitSignalItem(
                    title="流式 API 新功能",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="提升用户体验",
                    commit_sha="abc123def456",
                    related_repos=[],
                    trends=["streaming"],
                    tech_details={},
                ),
                CommitSignalItem(
                    title="超时修复",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="提升稳定性",
                    commit_sha="def456abc789",
                    related_repos=[],
                    trends=["bugfix"],
                    tech_details={},
                ),
            ],
            analyzed_count=2,
        )

        signals = analyzer._validate_and_match(result, sample_commits)

        assert len(signals) == 2
        # 检查 sources 构建正确
        assert any(
            "abc123def456" in s.sources[0] for s in signals if hasattr(s, "sources")
        )

    def test_unmatched_sha_returns_empty(self, sample_commits):
        """无法匹配的 SHA 返回空。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        result = CommitSignalsResult(
            signals=[
                CommitSignalItem(
                    title="未知提交",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="未知",
                    commit_sha="nonexistent_sha",
                    related_repos=[],
                    trends=[],
                    tech_details={},
                ),
            ],
            analyzed_count=1,
        )

        signals = analyzer._validate_and_match(result, sample_commits)

        # SHA 不匹配时应跳过，返回空列表
        assert len(signals) == 0


class TestAnalyzeMaterialsAsync:
    """异步分析测试。"""

    @pytest.mark.asyncio
    async def test_analyze_empty_materials(self):
        """空材料返回空列表。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        with patch.object(analyzer, "query_engine") as mock_engine:
            result = await analyzer.analyze_materials_async([])

        assert result == []
        mock_engine.query_async.assert_not_called()

    @pytest.mark.asyncio
    async def test_analyze_returns_list_of_signals(self, sample_materials):
        """返回 Signal 列表。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        mock_result = CommitSignalsResult(
            signals=[
                CommitSignalItem(
                    title="流式 API",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="改进实时响应",
                    commit_sha="abc123def456",
                    related_repos=[],
                    trends=["streaming"],
                    tech_details={},
                ),
            ],
            analyzed_count=1,
        )

        mock_query_result = MagicMock()
        mock_query_result.output = mock_result

        with patch.object(analyzer, "query_engine") as mock_engine:
            mock_engine.query_async = AsyncMock(return_value=mock_query_result)
            result = await analyzer.analyze_materials_async(sample_materials)

        assert isinstance(result, list)
        assert all(isinstance(s, Signal) for s in result)

    @pytest.mark.asyncio
    async def test_analyze_creates_temp_file(self, sample_materials, tmp_path):
        """分析时创建临时文件。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        mock_result = CommitSignalsResult(signals=[], analyzed_count=0)
        mock_query_result = MagicMock()
        mock_query_result.output = mock_result

        with patch.object(analyzer, "query_engine") as mock_engine:
            mock_engine.query_async = AsyncMock(return_value=mock_query_result)
            await analyzer.analyze_materials_async(sample_materials)

        # 验证临时文件被清理（工作目录应该为空）
        # 由于是 tempfile.mkdtemp()，需要检查是否有残留

    @pytest.mark.asyncio
    async def test_analyze_handles_batch_splitting(self, sample_materials):
        """正确处理分批。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        # 3 个 commits，批次大小 2，应该分 2 批
        analyzer = SDKCommitAnalyzer(batch_size=2)

        mock_result = CommitSignalsResult(signals=[], analyzed_count=0)
        mock_query_result = MagicMock()
        mock_query_result.output = mock_result

        with patch.object(analyzer, "query_engine") as mock_engine:
            mock_engine.query_async = AsyncMock(return_value=mock_query_result)
            await analyzer.analyze_materials_async(sample_materials)

        # 2 批，每批调用一次 query_async
        assert mock_engine.query_async.call_count == 2


class TestSyncAnalyze:
    """同步分析测试。"""

    def test_sync_analyze_works_without_event_loop(self, sample_materials):
        """无事件循环时同步调用正常。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        mock_result = CommitSignalsResult(
            signals=[
                CommitSignalItem(
                    title="测试",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="测试",
                    commit_sha="abc123def456",
                    related_repos=[],
                    trends=[],
                    tech_details={},
                ),
            ],
            analyzed_count=1,
        )

        mock_query_result = MagicMock()
        mock_query_result.output = mock_result

        with patch.object(analyzer, "query_engine") as mock_engine:
            mock_engine.query_async = AsyncMock(return_value=mock_query_result)
            result = analyzer.analyze_materials(sample_materials)

        assert isinstance(result, list)
        assert len(result) == 1

    def test_sync_analyze_raises_when_event_loop_exists(self, sample_materials):
        """检测到事件循环时抛出错误。"""
        from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer

        analyzer = SDKCommitAnalyzer()

        async def run_test():
            return analyzer.analyze_materials(sample_materials)

        async def main():
            with pytest.raises(RuntimeError, match="事件循环"):
                await run_test()

        asyncio.run(main())
