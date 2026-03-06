"""Pipeline 主流程单元测试"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.models.signal import ActivityData, ReleasesData
from trendpluse.pipeline import TrendPulsePipeline


class MockSignalDeduplicator:
    """Mock SignalDeduplicator for testing"""

    def __init__(self, *args, **kwargs):
        pass

    def deduplicate(self, signals):
        return signals


class TestTrendPulsePipeline:
    """测试 TrendPulse 主流程"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ReleaseMaterialBuilder")
    @patch("trendpluse.pipeline.CommitMaterialBuilder")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubPRReader")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_init_creates_components(
        self,
        mock_collector,
        mock_filter,
        mock_reader,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_collector,
        mock_activity_collector,
        mock_commit_material_builder,
        mock_release_material_builder,
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings_instance.llm_retry_max_attempts = 3
        mock_settings_instance.llm_retry_wait_min = 1
        mock_settings_instance.llm_retry_wait_max = 10
        mock_settings.return_value = mock_settings_instance

        # Act
        pipeline = TrendPulsePipeline()

        # Assert
        assert pipeline is not None
        mock_collector.assert_called_once_with(token="test_token")
        mock_activity_collector.assert_called_once_with(token="test_token")
        mock_release_collector.assert_called_once_with(token="test_token")
        mock_filter.assert_called_once()
        mock_reader.assert_called_once_with(token="test_token")
        mock_commit_material_builder.assert_called_once()
        mock_release_material_builder.assert_called_once()
        mock_commit_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
            retry_max_attempts=3,
            retry_wait_min=1,
            retry_wait_max=10,
        )
        mock_release_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
            retry_max_attempts=3,
            retry_wait_min=1,
            retry_wait_max=10,
        )
        mock_analyzer.assert_called_once_with(
            api_key="test_api_key",
            model="glm-4.7",
            base_url="https://open.bigmodel.cn/api/anthropic",
            retry_max_attempts=3,
            retry_wait_min=1,
            retry_wait_max=10,
        )
        mock_reporter.assert_called_once()

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.ReleaseSummarizer")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubPRReader")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_run_daily(
        self,
        mock_collector,
        mock_filter,
        mock_reader,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_summarizer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
        mock_write_text,
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings_instance.llm_retry_max_attempts = 3
        mock_settings_instance.llm_retry_wait_min = 1
        mock_settings_instance.llm_retry_wait_max = 10
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
        # 构造 ActivityData
        mock_activity_data = ActivityData(
            total_commits=5,
            active_repos_count=1,
            top_repos=[],
        )
        detailed_commits = [
            {
                "repo": "anthropics/skills",
                "sha": "abc123",
                "message": "feat: add new feature",
                "author": "testuser",
                "timestamp": "2026-01-02T10:00:00Z",
            }
        ]
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        # 构造 ReleasesData
        mock_releases_data = ReleasesData(
            total_count=0,
            unique_repos_count=0,
            releases=[],
        )
        detailed_releases: list[dict] = []
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            detailed_releases,
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_release_summarizer_instance = Mock()
        mock_release_summarizer_instance.summarize_materials.return_value = {}
        mock_release_summarizer.return_value = mock_release_summarizer_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
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

        mock_reader_instance = Mock()
        mock_reader_instance.refs_from_candidates.return_value = [Mock()]
        mock_reader_instance.read_many.return_value = [Mock()]
        mock_reader.return_value = mock_reader_instance

        mock_analyzer_instance = Mock()
        mock_signal = Mock()
        mock_signal.id = "test-1"
        mock_signal.title = "测试信号"
        mock_analyzer_instance.analyze_materials.return_value = [mock_signal]

        # 创建一个支持属性赋值的报告对象
        mock_report_obj = Mock()
        mock_report_obj.date = "2026-01-02"
        mock_report_obj.engineering_signals = [mock_signal]
        mock_report_obj.research_signals = []
        mock_report_obj.commit_signals = []
        mock_report_obj.activity = {}
        mock_report_obj.stats = {"total_prs_analyzed": 1}
        # 添加 model_dump_json 方法返回 JSON 字符串
        mock_report_obj.model_dump_json = Mock(
            return_value='{"date": "2026-01-02", "engineering_signals": []}'
        )
        # 为新方法添加 mock
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )
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
        mock_reader_instance.refs_from_candidates.assert_called_once_with(
            mock_filter_instance.filter_candidates.return_value,
        )
        mock_reader_instance.read_many.assert_called_once_with(
            mock_reader_instance.refs_from_candidates.return_value,
            max_workers=4,
        )
        mock_analyzer_instance.analyze_materials.assert_called_once()
        mock_analyzer_instance.aggregate_and_generate_report.assert_called_once()
        mock_reporter_instance.save_report.assert_called_once()
        # 验证 commit 分析被调用
        mock_commit_analyzer_instance.analyze_materials.assert_called_once()

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.ReleaseSummarizer")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubPRReader")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_run_daily_uses_release_material_summarizer(
        self,
        mock_collector,
        mock_filter,
        mock_reader,
        mock_analyzer,
        mock_release_analyzer,
        mock_commit_analyzer,
        mock_release_summarizer,
        mock_release_collector,
        mock_activity_collector,
        mock_reporter,
        mock_settings,
        mock_write_text,
    ):
        """测试：release 总结应走材料接口。"""
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings_instance.llm_retry_max_attempts = 3
        mock_settings_instance.llm_retry_wait_min = 1
        mock_settings_instance.llm_retry_wait_max = 10
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            ActivityData(total_commits=0, active_repos_count=0, top_repos=[]),
            [],
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_releases_data = ReleasesData(
            total_count=1,
            unique_repos_count=1,
            releases=[],
        )
        detailed_releases = [
            {
                "repo": "anthropics/skills",
                "tag_name": "v1.0.0",
                "name": "v1.0.0",
                "body": "Release notes",
                "html_url": "https://github.com/anthropics/skills/releases/tag/v1.0.0",
            }
        ]
        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            detailed_releases,
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_release_summarizer_instance = Mock()
        mock_release_summarizer_instance.summarize_materials.return_value = {}
        mock_release_summarizer.return_value = mock_release_summarizer_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_reader.return_value = Mock()
        mock_analyzer.return_value = Mock()
        mock_reporter.return_value = Mock()

        pipeline = TrendPulsePipeline()
        pipeline.run_daily(date=datetime(2026, 1, 2))

        mock_release_summarizer_instance.summarize_materials.assert_called_once()

    @patch("pathlib.Path.write_text")
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
    def test_run_daily_with_no_events(
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
        mock_write_text,
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = ""
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        # 构造 ActivityData
        mock_activity_data = ActivityData(
            total_commits=5,
            active_repos_count=1,
            top_repos=[],
        )
        detailed_commits = [
            {
                "repo": "anthropics/skills",
                "sha": "abc123",
                "message": "feat: add new feature",
                "author": "testuser",
                "timestamp": "2026-01-02T10:00:00Z",
            }
        ]
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        # 构造 ReleasesData
        mock_releases_data = ReleasesData(
            total_count=0,
            unique_repos_count=0,
            releases=[],
        )
        detailed_releases: list[dict] = []
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            detailed_releases,
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_reader_instance = Mock()
        mock_reader.return_value = mock_reader_instance

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
        # 添加 model_dump_json 方法返回 JSON 字符串
        mock_report_obj.model_dump_json = Mock(
            return_value='{"date": "2026-01-02", "engineering_signals": []}'
        )
        # 为新方法添加 mock
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )
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
        mock_reader_instance.read_many.assert_not_called()
        mock_analyzer_instance.analyze_materials.assert_not_called()
        # commit 分析仍应被调用
        mock_commit_analyzer_instance.analyze_materials.assert_called_once()

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
    def test_handle_empty_report_saves_and_notifies(
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
        """测试：空报告会保存和通知

        验证当没有候选事件时，pipeline 会：
        1. 生成空报告
        2. 保存报告到文件
        3. 发送通知（如果配置了）
        """
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = None  # 不配置通知
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        mock_activity_data = ActivityData(
            total_commits=5,
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
            total_count=0,
            unique_repos_count=0,
            releases=[],
        )
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()

        # Act
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证报告被保存
        mock_reporter_instance.save_report.assert_called_once()
        assert report is not None

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
    def test_handle_empty_report_with_pr_details(
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
        """测试：没有 PR 详情时的空报告处理

        验证当筛选后有候选事件但没有 PR 详情时，也会生成空报告。
        """
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = None
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        mock_activity_data = ActivityData(
            total_commits=0,
            active_repos_count=0,
            top_repos=[],
        )
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            [],
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

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

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        # 有候选事件但筛选后为空
        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()

        # Act
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert
        mock_reporter_instance.save_report.assert_called_once()
        assert report is not None

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
    def test_handle_empty_report_with_no_signals(
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
        """测试：有 PR 详情但没有分析出信号时的空报告处理

        验证当 AI 分析没有产生信号时，也会生成空报告。
        """
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
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.output_dir = "reports/daily"
        mock_settings_instance.feishu_webhook_url = None
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        mock_activity_collector_instance = Mock()
        mock_activity_data = ActivityData(
            total_commits=0,
            active_repos_count=0,
            top_repos=[],
        )
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
            mock_activity_data,
            [],
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

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

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_materials.return_value = []
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_materials.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_filter.return_value = mock_filter_instance

        mock_reader_instance = Mock()
        mock_reader_instance.refs_from_candidates.return_value = [Mock()]
        mock_reader_instance.read_many.return_value = [Mock()]
        mock_reader.return_value = mock_reader_instance

        # AI 分析没有产生信号
        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_materials.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()

        # Act
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert
        mock_reporter_instance.save_report.assert_called_once()
        assert report is not None
        # 验证 AI 分析被调用了
        mock_analyzer_instance.analyze_materials.assert_called_once()
