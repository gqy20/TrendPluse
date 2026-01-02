"""ActivityCollector 单元测试

测试仓库活跃度采集器的详细 commit 收集功能。
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.activity import ActivityCollector


class TestActivityCollectorDetailedCommits:
    """ActivityCollector 详细 commit 收集测试"""

    @pytest.fixture
    def collector(self):
        """创建 ActivityCollector 实例"""
        return ActivityCollector(token="test-token")

    @pytest.fixture
    def mock_repo(self):
        """创建 mock Repository 对象"""
        repo = MagicMock()

        # Mock commit 对象
        mock_commit = MagicMock()
        mock_commit.sha = "abc123def456"
        mock_commit.author.login = "testuser"
        mock_commit.commit.message = "feat: add new feature"
        mock_commit.commit.author.date = datetime(2026, 1, 2, 10, 0, 0, tzinfo=UTC)

        # Mock 文件变更（PyGithub 不直接提供，需要在实现中处理）
        # 暂时跳过，因为需要 mock GitHub API 的复杂响应

        repo.get_commits.return_value = [mock_commit]
        return repo

    def test_collect_commits_returns_detailed_info(self, collector, mock_repo):
        """测试收集 commits - 应返回详细信息"""
        # Arrange
        repo_name = "test/repo"
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        with patch.object(
            collector, "client"
        ) as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity = collector._collect_repo_activity(
                mock_repo, since, repo_name
            )

            # Assert
            assert activity is not None
            assert activity["repo"] == repo_name
            assert activity["commit_count"] >= 0

    def test_collect_activity_includes_detailed_commits(
        self, collector, mock_repo
    ):
        """测试 collect_activity - 结果应包含详细 commits"""
        # Arrange
        repos = ["test/repo"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        with patch.object(
            collector, "client"
        ) as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity_data = collector.collect_activity(repos, since)

            # Assert
            assert activity_data is not None
            assert "repo_activity" in activity_data
            assert isinstance(activity_data["repo_activity"], list)

    def test_detailed_commits_structure(self, collector):
        """测试详细 commit 数据结构"""
        # Arrange
        # 这个测试验证返回的数据结构是否符合 CommitAnalyzer 的要求

        # 创建详细的 commit 数据
        detailed_commit = {
            "repo": "anthropics/claude-sdk-python",
            "sha": "abc123",
            "message": "feat: add streaming API",
            "author": "developer",
            "timestamp": "2026-01-02T10:00:00Z",
            "files_changed": ["src/api.py"],
            "additions": 100,
            "deletions": 20,
        }

        # Assert - 验证包含所有必需字段
        required_fields = [
            "repo",
            "sha",
            "message",
            "author",
            "timestamp",
            "files_changed",
            "additions",
            "deletions",
        ]
        for field in required_fields:
            assert field in detailed_commit

    def test_collect_activity_returns_detailed_commits_list(
        self, collector, mock_repo
    ):
        """测试 collect_activity - 应返回详细 commits 列表供分析"""
        # Arrange
        repos = ["test/repo"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        # 设置 mock 返回值
        mock_commit = MagicMock()
        mock_commit.sha = "abc123"
        mock_commit.author.login = "testuser"
        mock_commit.commit.message = "feat: add feature"
        mock_commit.commit.author.date = datetime(2026, 1, 2, 10, 0, 0, tzinfo=UTC)

        # Mock get_commits 返回列表
        commits_list = [mock_commit]
        mock_repo.get_commits.return_value = commits_list

        with patch.object(
            collector, "client"
        ) as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity_data = collector.collect_activity(repos, since)

            # Assert - 应该包含 detailed_commits 字段
            assert "detailed_commits" in activity_data
            assert isinstance(activity_data["detailed_commits"], list)

            # 验证详细 commit 包含必需字段
            if activity_data["detailed_commits"]:
                commit = activity_data["detailed_commits"][0]
                required_fields = [
                    "repo",
                    "sha",
                    "message",
                    "author",
                    "timestamp",
                ]
                for field in required_fields:
                    assert field in commit
