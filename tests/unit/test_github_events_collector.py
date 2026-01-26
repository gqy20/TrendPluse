"""GitHub Events 采集器单元测试"""

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock, patch

from trendpluse.collectors.github_events import GitHubEventsCollector


class TestGitHubEventsCollector:
    """测试 GitHub Events 采集器"""

    def test_init_with_token(self):
        """测试：使用 token 初始化"""
        # Arrange & Act
        with patch("trendpluse.collectors.base.Github"):
            collector = GitHubEventsCollector(token="test_token")

        # Assert
        assert collector is not None

    def test_init_without_token(self):
        """测试：不使用 token 初始化"""
        # Arrange & Act
        with patch("trendpluse.collectors.base.Github"):
            collector = GitHubEventsCollector()

        # Assert
        assert collector is not None

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_returns_list(self, mock_github):
        """测试：fetch_events 应该返回事件列表"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.labels = []
        mock_user = Mock()
        mock_user.login = "test_user"
        mock_pr.user = mock_user
        mock_pr.additions = 10
        mock_pr.deletions = 5
        mock_pr.changed_files = 2
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

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_filters_by_date(self, mock_github):
        """测试：应该按日期过滤"""
        # Arrange
        mock_repo = Mock()
        old_pr = Mock()
        old_pr.created_at = datetime.now(UTC) - timedelta(days=10)
        old_pr.labels = []
        mock_user = Mock()
        mock_user.login = "test_user"
        old_pr.user = mock_user
        old_pr.additions = 1
        old_pr.deletions = 1
        old_pr.changed_files = 1

        recent_pr = Mock()
        recent_pr.created_at = datetime.now(UTC)
        recent_pr.labels = []
        recent_pr.user = mock_user
        recent_pr.additions = 10
        recent_pr.deletions = 5
        recent_pr.changed_files = 2

        mock_repo.get_pulls.return_value = [recent_pr, old_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert - 应该只返回最近的 PR
        assert len(events) == 1

    @patch("trendpluse.collectors.base.Github")
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

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_handles_multiple_repos(self, mock_github):
        """测试：应该处理多个仓库"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.created_at = datetime.now(UTC)
        mock_pr.labels = []
        mock_user = Mock()
        mock_user.login = "test_user"
        mock_pr.user = mock_user
        mock_pr.additions = 1
        mock_pr.deletions = 1
        mock_pr.changed_files = 1

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

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_event_format_compatible_with_filter(self, mock_github):
        """测试：事件格式应与 EventFilter 兼容"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.labels = []
        mock_user = Mock()
        mock_user.login = "test_user"
        mock_pr.user = mock_user
        mock_pr.additions = 10
        mock_pr.deletions = 5
        mock_pr.changed_files = 2
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

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_includes_merged_field(self, mock_github):
        """测试：事件应包含 merged 字段"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.merged = True
        mock_pr.labels = []  # 空标签列表
        mock_user = Mock()
        mock_user.login = "alice"
        mock_pr.user = mock_user
        mock_pr.additions = 10
        mock_pr.deletions = 5
        mock_pr.changed_files = 2
        mock_pr.created_at = datetime.now(UTC)

        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        event = events[0]
        pr_data = event["payload"]["pull_request"]
        assert "merged" in pr_data
        assert pr_data["merged"] is True

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_includes_labels(self, mock_github):
        """测试：事件应包含 labels 字段"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.merged = False
        mock_pr.created_at = datetime.now(UTC)

        # Mock labels
        mock_label_1 = Mock()
        mock_label_1.name = "enhancement"
        mock_label_2 = Mock()
        mock_label_2.name = "feature"
        mock_pr.labels = [mock_label_1, mock_label_2]

        # Mock user
        mock_user = Mock()
        mock_user.login = "bob"
        mock_pr.user = mock_user
        mock_pr.additions = 10
        mock_pr.deletions = 5
        mock_pr.changed_files = 2

        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        event = events[0]
        pr_data = event["payload"]["pull_request"]
        assert "labels" in pr_data
        assert len(pr_data["labels"]) == 2
        assert pr_data["labels"][0]["name"] == "enhancement"
        assert pr_data["labels"][1]["name"] == "feature"

    @patch("trendpluse.collectors.base.Github")
    def test_fetch_events_includes_author_and_changes(self, mock_github):
        """测试：事件应包含作者和变更统计"""
        # Arrange
        mock_repo = Mock()
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Test PR"
        mock_pr.body = "Test body"
        mock_pr.merged = True
        mock_pr.labels = []  # 空标签列表
        mock_user = Mock()
        mock_user.login = "charlie"
        mock_pr.user = mock_user
        mock_pr.additions = 100
        mock_pr.deletions = 50
        mock_pr.changed_files = 5
        mock_pr.created_at = datetime.now(UTC)

        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github.return_value.get_repo.return_value = mock_repo

        collector = GitHubEventsCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        event = events[0]
        pr_data = event["payload"]["pull_request"]
        assert pr_data["author"] == "charlie"
        assert pr_data["additions"] == 100
        assert pr_data["deletions"] == 50
        assert pr_data["changed_files"] == 5
