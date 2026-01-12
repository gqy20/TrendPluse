"""并行 GitHubEventsCollector 单元测试

测试使用并行方式获取 GitHub 事件。
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.github_events import GitHubEventsCollector


class TestParallelGitHubEventsCollector:
    """并行 GitHubEventsCollector 测试"""

    @pytest.fixture
    def collector(self):
        """创建 GitHubEventsCollector 实例"""
        return GitHubEventsCollector(token="test-token")

    @pytest.fixture
    def mock_pr_factory(self):
        """创建 mock PR 工厂函数"""

        def _make_pr(num: int, hours_ago: int = 1):
            pr = MagicMock()
            pr.number = num
            pr.title = f"PR {num}"
            pr.body = f"Body for PR {num}"
            pr.created_at = datetime.now(UTC) - timedelta(hours=hours_ago)
            return pr

        return _make_pr

    @pytest.fixture
    def mock_repo_factory(self, mock_pr_factory):
        """创建 mock repository 工厂函数"""

        def _make_repo(repo_name: str, num_prs: int = 3):
            repo = MagicMock()
            prs = [mock_pr_factory(i, i) for i in range(num_prs)]
            repo.get_pulls.return_value = iter(prs)
            return repo

        return _make_repo

    def test_fetch_events_handles_multiple_repos(self, collector, mock_repo_factory):
        """测试：并行获取应正确处理多个仓库"""
        # Arrange
        repos = [f"test/repo{i}" for i in range(3)]
        since = datetime.now(UTC) - timedelta(hours=5)

        mock_repos = {repo: mock_repo_factory(repo, 3) for repo in repos}

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act
            events = collector.fetch_events(repos, since)

        # Assert
        assert len(events) == 9  # 3 repos * 3 PRs

    def test_fetch_events_filters_by_date(self, collector, mock_pr_factory):
        """测试：并行获取应按日期过滤"""
        # Arrange - 使用固定时间避免竞态条件
        base_time = datetime(2026, 1, 12, 12, 0, 0, tzinfo=UTC)
        since = base_time - timedelta(hours=2)

        repos = ["test/repo"]

        # 创建一些旧的和新的 PRs
        old_pr = MagicMock()
        old_pr.number = 1
        old_pr.title = "Old PR"
        old_pr.body = "Old body"
        old_pr.created_at = base_time - timedelta(hours=5)  # 5 小时前，早于 since

        new_pr = MagicMock()
        new_pr.number = 2
        new_pr.title = "New PR"
        new_pr.body = "New body"
        new_pr.created_at = base_time - timedelta(hours=1)  # 1 小时前，晚于 since

        mock_repo = MagicMock()
        # 注意：get_pulls 按时间降序返回，所以新的在前
        mock_repo.get_pulls.return_value = iter([new_pr, old_pr])

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            events = collector.fetch_events(repos, since)

        # Assert - 只应该返回新的 PR
        assert len(events) == 1
        assert events[0]["payload"]["pull_request"]["number"] == 2

    def test_fetch_events_handles_api_errors(self, collector, mock_repo_factory):
        """测试：并行获取应优雅处理 API 错误"""
        # Arrange
        repos = ["test/good", "test/bad", "test/also-good"]
        since = datetime.now(UTC) - timedelta(hours=5)

        mock_repos = {
            "test/good": mock_repo_factory("test/good", 2),
            "test/also-good": mock_repo_factory("test/also-good", 1),
        }

        def side_effect(name):
            if name == "test/bad":
                raise Exception("API Error")
            return mock_repos[name]

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = side_effect

            # Act - 不应该抛出异常
            events = collector.fetch_events(repos, since)

        # Assert - 只有两个成功的仓库
        assert len(events) == 3  # 2 + 1 PRs

    def test_fetch_events_returns_same_structure_as_sequential(
        self, collector, mock_repo_factory
    ):
        """测试：并行获取应返回与串行相同的数据结构"""
        # Arrange
        repos = ["test/repo1", "test/repo2"]
        since = datetime.now(UTC) - timedelta(hours=5)

        mock_repos = {
            "test/repo1": mock_repo_factory("test/repo1", 1),
            "test/repo2": mock_repo_factory("test/repo2", 2),
        }

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act
            events = collector.fetch_events(repos, since)

        # Assert - 验证返回结构与串行版本一致
        assert isinstance(events, list)
        for event in events:
            assert "type" in event
            assert event["type"] == "PullRequestEvent"
            assert "repo" in event
            assert "payload" in event
            assert "created_at" in event
