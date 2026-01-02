"""GitHub Events 采集器单元测试"""

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock, patch

from trendpluse.collectors.github_events import GitHubEventsCollector


class TestGitHubEventsCollector:
    """测试 GitHub Events 采集器"""

    def test_init_with_token(self):
        """测试：使用 token 初始化"""
        # Arrange & Act
        with patch("trendpluse.collectors.github_events.Github"):
            collector = GitHubEventsCollector(token="test_token")

        # Assert
        assert collector is not None

    def test_init_without_token(self):
        """测试：不使用 token 初始化"""
        # Arrange & Act
        with patch("trendpluse.collectors.github_events.Github"):
            collector = GitHubEventsCollector()

        # Assert
        assert collector is not None

    @patch("trendpluse.collectors.github_events.Github")
    def test_fetch_events_returns_list(self, mock_github):
        """测试：fetch_events 应该返回事件列表"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.created_at = datetime.now(UTC)

        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        assert isinstance(events, list)
        assert len(events) == 1
        assert events[0]["type"] == "PullRequestEvent"
        assert events[0]["repo"]["name"] == "anthropics/skills"

    @patch("trendpluse.collectors.github_events.Github")
    def test_fetch_events_filters_by_date(self, mock_github):
        """测试：应该按日期过滤"""
        # Arrange
        mock_repo = Mock()
        old_pr = Mock()
        old_pr.created_at = datetime.now(UTC) - timedelta(days=10)
        recent_pr = Mock()
        recent_pr.created_at = datetime.now(UTC)

        mock_repo.get_pulls.return_value = [recent_pr, old_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert - 应该只返回最近的 PR
        assert len(events) == 1

    @patch("trendpluse.collectors.github_events.Github")
    def test_fetch_events_empty_result(self, mock_github):
        """测试：没有事件时应该返回空列表"""
        # Arrange
        mock_repo = Mock()
        mock_repo.get_pulls.return_value = []
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        assert events == []

    @patch("trendpluse.collectors.github_events.Github")
    def test_fetch_events_handles_multiple_repos(self, mock_github):
        """测试：应该处理多个仓库"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.created_at = datetime.now(UTC)
        mock_repo.get_pulls.return_value = [mock_pr]

        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills", "anthropics/claude-quickstarts"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        assert len(events) == 2
        assert events[0]["repo"]["name"] == "anthropics/skills"
        assert events[1]["repo"]["name"] == "anthropics/claude-quickstarts"

    @patch("trendpluse.collectors.github_events.Github")
    def test_fetch_event_format_compatible_with_filter(self, mock_github):
        """测试：事件格式应与 EventFilter 兼容"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.created_at = datetime.now(UTC)

        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert - 验证事件格式包含必需字段
        event = events[0]
        assert "type" in event
        assert "repo" in event
        assert "payload" in event
        assert "created_at" in event
        assert event["repo"]["name"] == "anthropics/skills"
