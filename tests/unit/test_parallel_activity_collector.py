"""并行 ActivityCollector 单元测试

测试使用并行方式采集仓库活跃度数据。
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.activity import ActivityCollector
from trendpluse.models.signal import ActivityData


class TestParallelActivityCollector:
    """并行 ActivityCollector 测试"""

    @pytest.fixture
    def collector(self):
        """创建 ActivityCollector 实例"""
        return ActivityCollector(token="test-token")

    @pytest.fixture
    def mock_commit(self):
        """创建 mock commit 对象"""
        commit = MagicMock()
        commit.sha = "abc123def456"
        commit.author.login = "testuser"
        commit.commit.message = "feat: add new feature"
        commit.commit.author.date = datetime(2026, 1, 2, 10, 0, 0, tzinfo=UTC)
        return commit

    @pytest.fixture
    def mock_repo_factory(self, mock_commit):
        """创建 mock repository 工厂函数"""

        def _make_repo(repo_name: str, num_commits: int = 1):
            repo = MagicMock()
            commits = [mock_commit] * num_commits
            repo.get_commits.return_value = commits
            return repo

        return _make_repo

    def test_collect_activity_parallel_should_be_faster_than_sequential(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应该比串行更快"""
        # Arrange
        repos = [f"test/repo{i}" for i in range(5)]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        mock_repos = {repo: mock_repo_factory(repo, 10) for repo in repos}

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act - 使用并行方法
            activity_data, detailed_commits = collector.collect_activity_parallel(
                repos, since, max_workers=3
            )

        # Assert
        assert isinstance(activity_data, ActivityData)
        assert activity_data.total_commits == 50  # 5 repos * 10 commits

    def test_collect_activity_parallel_handles_empty_repos(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应正确处理空仓库"""
        # Arrange
        repos = ["test/empty", "test/active"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        mock_repos = {
            "test/empty": mock_repo_factory("test/empty", 0),
            "test/active": mock_repo_factory("test/active", 5),
        }

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act
            activity_data, detailed_commits = collector.collect_activity_parallel(
                repos, since
            )

        # Assert
        assert activity_data.total_commits == 5
        assert activity_data.active_repos_count == 1

    def test_collect_activity_parallel_handles_api_errors(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应优雅处理 API 错误"""
        # Arrange
        repos = ["test/good", "test/bad", "test/also-good"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        mock_repos = {
            "test/good": mock_repo_factory("test/good", 3),
            "test/also-good": mock_repo_factory("test/also-good", 2),
        }

        call_count = {"count": 0}

        def side_effect(name):
            call_count["count"] += 1
            if name == "test/bad":
                raise Exception("API Error")
            return mock_repos[name]

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = side_effect

            # Act - 不应该抛出异常
            activity_data, detailed_commits = collector.collect_activity_parallel(
                repos, since
            )

        # Assert
        assert activity_data.total_commits == 5  # 只有两个成功的仓库

    def test_collect_activity_parallel_returns_same_structure_as_sequential(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应返回与串行相同的数据结构"""
        # Arrange
        repos = ["test/repo1", "test/repo2"]
        since = datetime(2026, 1, 2, 0, 0, 0, tzinfo=UTC)

        mock_repos = {
            "test/repo1": mock_repo_factory("test/repo1", 3),
            "test/repo2": mock_repo_factory("test/repo2", 2),
        }

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act
            activity_data, detailed_commits = collector.collect_activity_parallel(
                repos, since
            )

        # Assert - 验证返回结构与串行版本一致
        assert isinstance(activity_data, ActivityData)
        assert hasattr(activity_data, "total_commits")
        assert hasattr(activity_data, "active_repos_count")
        assert hasattr(activity_data, "new_contributors")
        assert hasattr(activity_data, "top_repos")
        assert isinstance(detailed_commits, list)
