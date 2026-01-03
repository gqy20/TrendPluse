"""Pipeline 主流程单元测试"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.pipeline import TrendPulsePipeline


class TestTrendPulsePipeline:
    """测试 TrendPulse 主流程"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_init_creates_components(
        self,
        mock_collector,
        mock_filter,
        mock_fetcher,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
    ):
        """测试：初始化创建所有组件"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings.return_value = mock_settings_instance

        # Act
        pipeline = TrendPulsePipeline()

        # Assert
        assert pipeline is not None
        mock_collector.assert_called_once_with(token="test_token")
        mock_activity_collector.assert_called_once_with(token="test_token")
        mock_release_collector.assert_called_once_with(token="test_token")
        mock_filter.assert_called_once()
        mock_fetcher.assert_called_once_with(token="test_token")
        mock_commit_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
        )
        mock_release_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
        )
        mock_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
        )
        mock_reporter.assert_called_once()

    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_run_daily(
        self,
        mock_collector,
        mock_filter,
        mock_fetcher,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
    ):
        """测试：运行每日分析流程"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
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

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = {
            "total_commits": 5,
            "active_repos": 1,
            "new_contributors": 2,
            "repo_activity": [],
            "detailed_commits": [
                {
                    "repo": "anthropics/skills",
                    "sha": "abc123",
                    "message": "feat: add new feature",
                    "author": "testuser",
                    "timestamp": "2026-01-02T10:00:00Z",
                }
            ],
            "period_start": "2026-01-02T00:00:00Z",
            "period_end": "2026-01-02T23:59:59Z",
        }
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = {
            "total_releases": 0,
            "repos_with_releases": 0,
            "repo_releases": [],
            "detailed_releases": [],
            "period_start": "2026-01-02T00:00:00Z",
            "period_end": "2026-01-02T23:59:59Z",
        }
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

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

        # 创建一个支持属性赋值的报告对象
        mock_report_obj = Mock()
        mock_report_obj.date = "2026-01-02"
        mock_report_obj.engineering_signals = [mock_signal]
        mock_report_obj.research_signals = []
        mock_report_obj.commit_signals = []
        mock_report_obj.activity = {}
        mock_report_obj.stats = {"total_prs_analyzed": 1}
        mock_analyzer_instance.generate_report.return_value = mock_report_obj
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
        # 验证 commit 分析被调用
        mock_commit_analyzer_instance.analyze_commits.assert_called_once()

    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_run_daily_with_no_events(
        self,
        mock_collector,
        mock_filter,
        mock_fetcher,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
    ):
        """测试：没有事件时的处理"""
        # Arrange
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = {
            "total_commits": 5,
            "active_repos": 1,
            "new_contributors": 2,
            "repo_activity": [],
            "detailed_commits": [
                {
                    "repo": "anthropics/skills",
                    "sha": "abc123",
                    "message": "feat: add new feature",
                    "author": "testuser",
                    "timestamp": "2026-01-02T10:00:00Z",
                }
            ],
            "period_start": "2026-01-02T00:00:00Z",
            "period_end": "2026-01-02T23:59:59Z",
        }
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = {
            "total_releases": 0,
            "repos_with_releases": 0,
            "repo_releases": [],
            "detailed_releases": [],
            "period_start": "2026-01-02T00:00:00Z",
            "period_end": "2026-01-02T23:59:59Z",
        }
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_fetcher_instance = Mock()
        mock_fetcher_instance.fetch_multiple_pr_details.return_value = []
        mock_fetcher.return_value = mock_fetcher_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        # 创建一个支持属性赋值的报告对象
        mock_report_obj = Mock()
        mock_report_obj.date = "2026-01-02"
        mock_report_obj.engineering_signals = []
        mock_report_obj.research_signals = []
        mock_report_obj.commit_signals = []
        mock_report_obj.activity = {}
        mock_report_obj.stats = {}
        mock_analyzer_instance.generate_report.return_value = mock_report_obj
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
        # 没有候选事件时应该跳过 PR 分析，但仍分析 commits
        mock_fetcher_instance.fetch_multiple_pr_details.assert_not_called()
        mock_analyzer_instance.analyze_prs.assert_not_called()
        # commit 分析仍应被调用
        mock_commit_analyzer_instance.analyze_commits.assert_called_once()
