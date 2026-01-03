"""CommitAnalyzer 单元测试

测试 commit 分析器的核心功能。
"""

from typing import Any
from unittest.mock import patch

import pytest

from trendpluse.models.signal import Signal


class TestCommitAnalyzer:
    """CommitAnalyzer 测试类"""

    @pytest.fixture
    def analyzer(self):
        """创建 CommitAnalyzer 实例"""
        from trendpluse.analyzers.commit_analyzer import CommitAnalyzer

        return CommitAnalyzer(
            api_key="test-key",
            model="test-model",
            base_url="https://test.api",
        )

    def test_init_with_required_params(self, analyzer):
        """测试初始化 - 验证必需参数"""
        assert analyzer.api_key == "test-key"
        assert analyzer.model == "test-model"
        assert analyzer.base_url == "https://test.api"

    @pytest.fixture
    def sample_commit_data(self):
        """示例 commit 数据"""
        return [
            {
                "repo": "anthropics/claude-sdk-python",
                "sha": "abc123",
                "message": "feat: add new streaming API support",
                "author": "developer1",
                "timestamp": "2026-01-02T10:00:00Z",
                "files_changed": ["src/api.py", "tests/test_api.py"],
                "additions": 150,
                "deletions": 20,
            },
            {
                "repo": "anthropics/claude-sdk-python",
                "sha": "def456",
                "message": "fix: resolve timeout issue in stream handler",
                "author": "developer2",
                "timestamp": "2026-01-02T11:00:00Z",
                "files_changed": ["src/stream.py"],
                "additions": 10,
                "deletions": 5,
            },
        ]

    def test_analyze_commits_returns_signals(self, analyzer, sample_commit_data):
        """测试分析 commits - 应返回信号列表"""
        # Arrange
        expected_signal_count = 1  # Mock 响应只有 1 个信号

        # Act
        with patch.object(
            analyzer, "_call_llm", return_value=self._mock_llm_response()
        ):
            signals = analyzer.analyze_commits(sample_commit_data)

        # Assert
        assert isinstance(signals, list)
        assert len(signals) == expected_signal_count
        assert all(isinstance(signal, Signal) for signal in signals)

    def test_analyze_commits_with_empty_list(self, analyzer):
        """测试分析空 commit 列表 - 应返回空列表"""
        # Arrange
        empty_commits: list[dict[str, Any]] = []

        # Act
        signals = analyzer.analyze_commits(empty_commits)

        # Assert
        assert signals == []

    def test_analyze_commits_sets_correct_signal_type(
        self, analyzer, sample_commit_data
    ):
        """测试分析结果 - 信号类型应有效"""
        # Act
        with patch.object(
            analyzer, "_call_llm", return_value=self._mock_llm_response()
        ):
            signals = analyzer.analyze_commits(sample_commit_data)

        # Assert
        valid_types = [
            "capability",
            "abstraction",
            "workflow",
            "eval",
            "safety",
            "performance",
            "commit",
        ]
        assert all(signal.type in valid_types for signal in signals)

    def test_analyze_commits_includes_stats_in_signals(
        self, analyzer, sample_commit_data
    ):
        """测试分析结果 - 信号应包含统计信息"""
        # Act
        with patch.object(
            analyzer, "_call_llm", return_value=self._mock_llm_response()
        ):
            signals = analyzer.analyze_commits(sample_commit_data)

        # Assert
        for signal in signals:
            assert signal.impact_score >= 1
            assert signal.impact_score <= 5
            assert len(signal.related_repos) > 0
            assert len(signal.sources) > 0

    def _mock_llm_response(self):
        """Mock LLM 响应"""
        return """[
    {
        "title": "新增流式 API 支持",
        "type": "capability",
        "category": "engineering",
        "impact_score": 4,
        "why_it_matters": "提供了实时流式响应能力，显著改善用户体验",
        "related_repos": ["anthropics/claude-sdk-python"],
        "trends": ["新增流式API", "性能优化"],
        "tech_details": {"feature_type": "API增强", "complexity": "中等"}
    }
]"""

    def test_analyze_commits_handles_llm_error_gracefully(
        self, analyzer, sample_commit_data
    ):
        """测试 LLM 错误处理 - 应返回空列表而不是崩溃"""
        # Arrange
        with patch.object(
            analyzer, "_call_llm", side_effect=Exception("LLM API Error")
        ):
            # Act
            signals = analyzer.analyze_commits(sample_commit_data)

            # Assert - 应该优雅地处理错误
            assert signals == []

    def test_parse_signals_includes_commit_repo_in_related_repos(self, analyzer):
        """测试解析信号 - commit 所在仓库必须始终在 related_repos 中"""
        # Arrange
        commits = [
            {
                "repo": "cline/cline",
                "sha": "abc123",
                "message": "feat: add context awareness",
            },
            {
                "repo": "anthropics/claude-code-action",
                "sha": "def456",
                "message": "fix: update integration",
            },
        ]

        # AI 返回的 related_repos 不包含 commit 所在仓库
        llm_response = """[
            {
                "title": "Agent 上下文感知",
                "type": "capability",
                "category": "engineering",
                "impact_score": 5,
                "why_it_matters": "AI Agent 从被动执行向主动感知演进",
                "related_repos": ["google-gemini/gemini-cli"],
                "trends": ["上下文感知"],
                "tech_details": {"feature_type": "Agent", "complexity": "高"}
            },
            {
                "title": "GitHub Action 集成优化",
                "type": "workflow",
                "category": "engineering",
                "impact_score": 3,
                "why_it_matters": "改进 CI/CD 集成体验",
                "related_repos": ["continuedev/continue"],
                "trends": ["DevOps"],
                "tech_details": {"feature_type": "集成", "complexity": "低"}
            }
        ]"""

        # Act
        signals = analyzer._parse_signals(llm_response, commits)

        # Assert - commit 所在仓库必须被添加到 related_repos
        assert len(signals) == 2

        # 第一个信号：commit 来自 cline/cline，必须出现在 related_repos 中
        assert "cline/cline" in signals[0].related_repos
        assert "google-gemini/gemini-cli" in signals[0].related_repos
        assert signals[0].sources[0] == "https://github.com/cline/cline/commit/abc123"

        # 第二个信号：commit 来自 anthropics/claude-code-action
        assert "anthropics/claude-code-action" in signals[1].related_repos
        assert "continuedev/continue" in signals[1].related_repos
        assert (
            signals[1].sources[0]
            == "https://github.com/anthropics/claude-code-action/commit/def456"
        )
