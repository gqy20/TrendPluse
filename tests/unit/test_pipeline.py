"""Pipeline 主流程单元测试"""
from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.pipeline import TrendPulsePipeline


class TestTrendPulsePipeline:
    """测试 TrendPulse 主流程"""

    @patch("trendpluse.pipeline.GitHubEventsCollector")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.Settings")
    def test_init_creates_components(
        self,
        mock_settings,
        mock_reporter,
        mock_analyzer,
        mock_fetcher,
        mock_filter,
        mock_collector,
    ):
        """测试：初始化创建所有组件"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = "https://open.bigmodel.cn/api/anthropic"
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings.return_value = mock_settings_instance

        # Act
        pipeline = TrendPulsePipeline()

        # Assert
        assert pipeline is not None
        mock_collector.assert_called_once_with(token="test_token")
        mock_filter.assert_called_once()
        mock_fetcher.assert_called_once_with(token="test_token")
        mock_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
        )
        mock_reporter.assert_called_once()

    @patch("trendpluse.pipeline.GitHubEventsCollector")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.Settings")
    def test_run_daily(
        self,
        mock_settings,
        mock_reporter,
        mock_analyzer,
        mock_fetcher,
        mock_filter,
        mock_collector,
    ):
        """测试：运行每日分析流程"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings.return_value = mock_settings_instance

        # Mock 组件
        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {"pull_request": {"number": 1}},
            }
        ]
        mock_collector.return_value = mock_collector_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {"pull_request": {"number": 1}},
            }
        ]
        mock_filter.return_value = mock_filter_instance

        mock_fetcher_instance = Mock()
        mock_fetcher_instance.fetch_multiple_pr_details.return_value = [
            {"number": 1, "title": "PR 1", "repo_name": "anthropics/skills"}
        ]
        mock_fetcher.return_value = mock_fetcher_instance

        mock_analyzer_instance = Mock()
        mock_signal = Mock()
        mock_signal.id = "test-1"
        mock_signal.title = "测试信号"
        mock_analyzer_instance.analyze_prs.return_value = [mock_signal]
        mock_analyzer_instance.generate_report.return_value = Mock(
            date="2026-01-02",
            engineering_signals=[mock_signal],
            research_signals=[],
            stats={"total_prs_analyzed": 1},
        )
        mock_analyzer.return_value = mock_analyzer_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()

        # Act
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert
        assert report is not None
        mock_collector_instance.fetch_events.assert_called_once()
        mock_filter_instance.filter_candidates.assert_called_once()
        mock_fetcher_instance.fetch_multiple_pr_details.assert_called_once()
        mock_analyzer_instance.analyze_prs.assert_called_once()
        mock_analyzer_instance.generate_report.assert_called_once()
        mock_reporter_instance.save_report.assert_called_once()

    @patch("trendpluse.pipeline.GitHubEventsCollector")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.Settings")
    def test_run_daily_with_no_events(
        self,
        mock_settings,
        mock_reporter,
        mock_analyzer,
        mock_fetcher,
        mock_filter,
        mock_collector,
    ):
        """测试：没有事件时的处理"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_fetcher_instance = Mock()
        mock_fetcher_instance.fetch_multiple_pr_details.return_value = []
        mock_fetcher.return_value = mock_fetcher_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer_instance.generate_report.return_value = Mock(
            date="2026-01-02",
            engineering_signals=[],
            research_signals=[],
            stats={},
        )
        mock_analyzer.return_value = mock_analyzer_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()

        # Act
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert
        assert report is not None
        mock_collector_instance.fetch_events.assert_called_once()
        mock_filter_instance.filter_candidates.assert_called_once()
        # 没有候选事件时应该跳过后续步骤
        mock_fetcher_instance.fetch_multiple_pr_details.assert_not_called()
        mock_analyzer_instance.analyze_prs.assert_not_called()
