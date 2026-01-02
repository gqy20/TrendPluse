"""CommitAnalyzer 单元测试

测试 commit 分析器的核心功能。
"""

from unittest.mock import MagicMock, patch

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

    def test_analyze_commits_returns_signals(
        self, analyzer, sample_commit_data
    ):
        """测试分析 commits - 应返回信号列表"""
        # Arrange
        expected_signal_count = 2

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
        empty_commits = []

        # Act
        signals = analyzer.analyze_commits(empty_commits)

        # Assert
        assert signals == []

    def test_analyze_commits_sets_correct_signal_type(
        self, analyzer, sample_commit_data
    ):
        """测试分析结果 - 信号类型应为 commit"""
        # Act
        with patch.object(
            analyzer, "_call_llm", return_value=self._mock_llm_response()
        ):
            signals = analyzer.analyze_commits(sample_commit_data)

        # Assert
        assert all(signal.type == "commit" for signal in signals)

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
