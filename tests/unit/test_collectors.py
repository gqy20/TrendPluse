"""数据采集单元测试"""
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from trendpluse.collectors.gh_archive import GHArchiveCollector


class TestGHArchiveCollector:
    """测试 GH Archive 数据采集器"""

    def test_init_with_client(self):
        """测试：初始化采集器"""
        # Arrange & Act
        with patch("trendpluse.collectors.gh_archive.bigquery.Client"):
            collector = GHArchiveCollector()

        # Assert
        assert collector is not None

    @patch("trendpluse.collectors.gh_archive.bigquery.Client")
    def test_fetch_events_returns_list(self, mock_client):
        """测试：fetch_events 应该返回事件列表"""
        # Arrange
        # 创建 mock 行对象
        mock_row = Mock()
        mock_row.type = "PullRequestEvent"
        mock_row.repo_name = "anthropics/skills"
        mock_row.payload = {"number": 123}
        mock_row.created_at.isoformat.return_value = "2026-01-02T10:00:00Z"

        mock_job = Mock()
        mock_job.result.return_value = [mock_row]
        mock_client.return_value.query.return_value = mock_job

        collector = GHArchiveCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        assert isinstance(events, list)
        assert len(events) == 1
        assert events[0]["repo"]["name"] == "anthropics/skills"

    @patch("trendpluse.collectors.gh_archive.bigquery.Client")
    def test_fetch_events_filters_by_repos(self, mock_client):
        """测试：应该按仓库过滤"""
        # Arrange
        mock_client.return_value.query.return_value.result.return_value = []

        collector = GHArchiveCollector()
        repos = ["anthropics/skills", "anthropics/claude-quickstarts"]
        since = datetime.now() - timedelta(days=1)

        # Act
        collector.fetch_events(repos=repos, since=since)

        # Assert - 验证 SQL 查询包含仓库过滤
        call_args = mock_client.return_value.query.call_args
        sql = call_args[0][0]
        assert "anthropics/skills" in sql or "@repos" in sql

    @patch("trendpluse.collectors.gh_archive.bigquery.Client")
    def test_fetch_events_filters_by_date(self, mock_client):
        """测试：应该按日期过滤"""
        # Arrange
        mock_client.return_value.query.return_value.result.return_value = []

        collector = GHArchiveCollector()
        repos = ["anthropics/skills"]
        since = datetime(2026, 1, 1)

        # Act
        collector.fetch_events(repos=repos, since=since)

        # Assert - 验证查询包含时间过滤
        call_args = mock_client.return_value.query.call_args
        assert "since" in call_args[1] or "created_at" in call_args[0][0]

    @patch("trendpluse.collectors.gh_archive.bigquery.Client")
    def test_fetch_events_empty_result(self, mock_client):
        """测试：没有事件时应该返回空列表"""
        # Arrange
        mock_client.return_value.query.return_value.result.return_value = []

        collector = GHArchiveCollector()
        repos = ["anthropics/skills"]
        since = datetime.now() - timedelta(days=1)

        # Act
        events = collector.fetch_events(repos=repos, since=since)

        # Assert
        assert events == []
