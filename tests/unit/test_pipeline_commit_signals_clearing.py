"""测试聚合后 commit_signals 被正确清空

这是修复报告重复显示 Commit 信号问题的测试。
"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.models.signal import ActivityData, ReleasesData, Signal
from trendpluse.pipeline import TrendPulsePipeline


class MockSignalDeduplicator:
    """Mock SignalDeduplicator for testing"""

    def __init__(self, *args, **kwargs):
        pass

    def deduplicate(self, signals):
        return signals


class TestCommitSignalsClearing:
    """测试聚合后 commit_signals 被正确清空"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubPRReader")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_aggregated_commit_signals_should_be_cleared(
        self,
        mock_collector,
        mock_filter,
        mock_reader,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
    ):
        """测试：聚合后 commit_signals 应该被清空

        场景：当 TrendAnalyzer.aggregate_and_generate_report() 返回的报告包含
        非空的 commit_signals 时，Pipeline 应该强制清空这些字段，避免在
        Markdown 报告中重复显示。

        为什么需要这个测试：
        - TrendAnalyzer 尝试清空 commit_signals，但 LLM 返回的对象可能
          不遵守这个操作
        - MarkdownReporter 会独立检查并渲染 commit_signals
        - 这导致工程信号/研究信号和 Commit 信号重复显示
        """
        # Arrange - 配置所有 Mock
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["test/repo"]
        mock_settings_instance.max_candidates = 20
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        # 配置 PR 数据（有 PR 触发聚合流程）
        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_filter.return_value = mock_filter_instance

        mock_reader_instance = Mock()
        mock_reader_instance.refs_from_candidates.return_value = [Mock()]
        mock_reader_instance.read_many.return_value = [Mock()]
        mock_reader.return_value = mock_reader_instance

        # 配置活跃度数据
        mock_activity_collector_instance = Mock()
        mock_activity_data = ActivityData(
            total_commits=5,
            active_repos_count=1,
            top_repos=[],
        )
        detailed_commits = [
            {
                "repo": "test/repo",
                "sha": "abc123",
                "message": "feat: new feature",
                "author": "testuser",
                "timestamp": "2026-01-12T10:00:00Z",
            }
        ]
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        # 配置 Release 数据
        mock_release_collector_instance = Mock()
        mock_releases_data = ReleasesData(
            total_count=0,
            unique_repos_count=0,
            releases=[],
        )
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        # 配置 Commit 分析器（返回一些信号）
        mock_commit_analyzer_instance = Mock()
        mock_commit_signal = Signal(
            id="commit-1",
            title="Commit Signal",
            type="capability",
            impact_score=4,
            category="engineering",
            why_it_matters="Test commit signal",
            related_repos=["test/repo"],
            sources=["https://github.com/test/repo/commit/abc123"],
        )
        mock_commit_analyzer_instance.analyze_materials.return_value = [
            mock_commit_signal
        ]
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        # 配置 Release 分析器
        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        # 配置 Trend Analyzer
        mock_pr_signal = Signal(
            id="pr-1",
            title="PR Signal",
            type="capability",
            impact_score=5,
            category="engineering",
            why_it_matters="Test PR signal",
            related_repos=["test/repo"],
            sources=["https://github.com/test/repo/pull/1"],
        )
        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_materials.return_value = [mock_pr_signal]

        # 关键：模拟 LLM 返回的对象保留了 commit_signals（这是 Bug）
        # 实际中，instructor + LLM 可能不会遵守代码中的清空操作
        mock_report_obj = Mock()
        mock_report_obj.date = "2026-01-12"
        mock_report_obj.engineering_signals = [mock_pr_signal]
        mock_report_obj.research_signals = []
        # 模拟 LLM 没有清空 commit_signals（问题所在）
        mock_report_obj.commit_signals = [mock_commit_signal]
        mock_report_obj.activity = {}
        mock_report_obj.stats = {"total_prs_analyzed": 1}
        mock_report_obj.model_dump_json = Mock(return_value='{"date": "2026-01-12"}')
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )
        mock_analyzer.return_value = mock_analyzer_instance

        # 配置 Reporter
        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        # Act
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 12))

        # Assert
        assert report is not None
        # 验证：聚合后 commit_signals 必须被清空
        # 这是修复报告重复显示的核心断言
        assert report.commit_signals == [], (
            f"commit_signals 应该被清空，但实际包含: {report.commit_signals}"
        )
        # 验证工程信号仍然存在（没有被错误清空）
        assert len(report.engineering_signals) > 0, "engineering_signals 不应该为空"

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubPRReader")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_release_signals_should_be_preserved(
        self,
        mock_collector,
        mock_filter,
        mock_reader,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
    ):
        """测试：聚合后 release_signals 不应被清空。"""
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["test/repo"]
        mock_settings_instance.max_candidates = 20
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_filter.return_value = mock_filter_instance

        mock_reader_instance = Mock()
        mock_reader_instance.refs_from_candidates.return_value = [Mock()]
        mock_reader_instance.read_many.return_value = [Mock()]
        mock_reader.return_value = mock_reader_instance

        mock_activity_collector_instance = Mock()
        mock_activity_data = ActivityData(
            total_commits=1,
            active_repos_count=1,
            top_repos=[],
        )
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            [],
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_releases_data = ReleasesData(
            total_count=1,
            unique_repos_count=1,
            releases=[],
        )
        detailed_releases = [
            {
                "repo": "test/repo",
                "tag_name": "v1.0.0",
                "name": "v1.0.0",
                "html_url": "https://github.com/test/repo/releases/tag/v1.0.0",
                "version_info": {"major": 1, "minor": 0, "patch": 0},
            }
        ]
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            detailed_releases,
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        release_signal = Signal(
            id="release-1",
            title="test/repo 发布 v1.0.0",
            type="release",
            impact_score=4,
            category="engineering",
            why_it_matters="重要版本发布",
            related_repos=["test/repo"],
            sources=["https://github.com/test/repo/releases/tag/v1.0.0"],
        )
        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = [release_signal]
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_pr_signal = Signal(
            id="pr-1",
            title="PR Signal",
            type="capability",
            impact_score=5,
            category="engineering",
            why_it_matters="Test PR signal",
            related_repos=["test/repo"],
            sources=["https://github.com/test/repo/pull/1"],
        )
        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_materials.return_value = [mock_pr_signal]

        mock_report_obj = Mock()
        mock_report_obj.date = "2026-01-12"
        mock_report_obj.engineering_signals = [mock_pr_signal]
        mock_report_obj.research_signals = []
        mock_report_obj.commit_signals = []
        mock_report_obj.release_signals = [release_signal]
        mock_report_obj.activity = {}
        mock_report_obj.stats = {"total_prs_analyzed": 1}
        mock_report_obj.model_dump_json = Mock(return_value='{"date": "2026-01-12"}')
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )
        mock_analyzer.return_value = mock_analyzer_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 12))

        assert report.commit_signals == []
        assert len(report.release_signals) == 1
        assert report.release_signals[0].id == "release-1"
