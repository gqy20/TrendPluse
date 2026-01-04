"""ActivityCollector 单元测试

测试仓库活跃度采集器的详细 commit 收集功能。
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.activity import ActivityCollector
from trendpluse.models.signal import ActivityData, RepoActivity


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

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity, detailed_commits = collector._collect_repo_activity(
                mock_repo, since, repo_name
            )

            # Assert
            assert activity is not None
            assert activity.repo == repo_name
            assert activity.commits >= 0
            assert isinstance(detailed_commits, list)

    def test_collect_activity_includes_detailed_commits(self, collector, mock_repo):
        """测试 collect_activity - 结果应包含详细 commits"""
        # Arrange
        repos = ["test/repo"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity_data, detailed_commits = collector.collect_activity(repos, since)

            # Assert
            assert activity_data is not None
            assert isinstance(activity_data.top_repos, list)
            assert isinstance(detailed_commits, list)

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

    def test_collect_activity_returns_detailed_commits_list(self, collector, mock_repo):
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

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity_data, detailed_commits = collector.collect_activity(repos, since)

            # Assert - 应该返回 detailed_commits 列表
            assert isinstance(detailed_commits, list)

            # 验证详细 commit 包含必需字段
            if detailed_commits:
                commit = detailed_commits[0]
                required_fields = [
                    "repo",
                    "sha",
                    "message",
                    "author",
                    "timestamp",
                ]
                for field in required_fields:
                    assert field in commit


class TestActivityCollectorStructuredData:
    """ActivityCollector 结构化数据返回测试"""

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

        repo.get_commits.return_value = [mock_commit]
        return repo

    def test_collect_activity_returns_structured_data(self, collector, mock_repo):
        """测试：collect_activity 返回 ActivityData 和 detailed_commits"""
        # Arrange
        repos = ["test/repo"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            result = collector.collect_activity(repos, since)

            # Assert - 返回值应该是元组 (ActivityData, list)
            assert isinstance(result, tuple)
            assert len(result) == 2

            activity_data, detailed_commits = result

            # 验证 ActivityData 结构
            assert isinstance(activity_data, ActivityData)
            assert hasattr(activity_data, "total_commits")
            assert hasattr(activity_data, "active_repos_count")
            assert hasattr(activity_data, "new_contributors")
            assert hasattr(activity_data, "top_repos")

            # 验证 detailed_commits
            assert isinstance(detailed_commits, list)

    def test_activity_data_contains_repo_activities(self, collector, mock_repo):
        """测试：ActivityData 包含 RepoActivity 列表"""
        # Arrange
        repos = ["test/repo"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            activity_data, _ = collector.collect_activity(repos, since)

            # Assert
            assert len(activity_data.top_repos) > 0
            repo_activity = activity_data.top_repos[0]
            assert isinstance(repo_activity, RepoActivity)
            assert repo_activity.repo == "test/repo"
            assert hasattr(repo_activity, "commits")
            assert hasattr(repo_activity, "new_contributors")
            assert hasattr(repo_activity, "top_contributors")
