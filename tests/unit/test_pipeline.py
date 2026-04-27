"""Pipeline 主流程单元测试"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.models.signal import ActivityData, ReleasesData


class MockSignalDeduplicator:
    """Mock SignalDeduplicator for testing"""

    def __init__(self, *args, **kwargs):
        pass

    def deduplicate(self, signals):
        return signals


def _build_mock_settings(**overrides):
    """构造测试用 Settings mock。"""
    settings = Mock()
    settings.github_token = "test_token"
    settings.anthropic_api_key = "test_api_key"
    settings.anthropic_model = "glm-4.7"
    settings.anthropic_base_url = "https://open.bigmodel.cn/api/anthropic"
    settings.github_repos = ["anthropics/skills"]
    settings.max_candidates = 20
    settings.days_to_lookback = 1
    settings.enable_parallel_collection = False
    settings.max_parallel_workers = 4
    settings.include_prereleases = False
    settings.output_dir = "reports/daily"
    settings.feishu_webhook_url = ""
    settings.feishu_at_mobiles_list = []
    settings.llm_retry_max_attempts = 3
    settings.llm_retry_wait_min = 1
    settings.llm_retry_wait_max = 10
    for key, value in overrides.items():
        setattr(settings, key, value)
    return settings


def _mock_activity_collection(
    mock_activity_collector,
    *,
    total_commits=0,
    active_repos_count=0,
    detailed_commits=None,
):
    """配置 ActivityCollector 返回值。"""
    collector = Mock()
    collector.collect_activity_graphql.return_value = (
        ActivityData(
            total_commits=total_commits,
            active_repos_count=active_repos_count,
            top_repos=[],
        ),
        detailed_commits or [],
    )
    mock_activity_collector.return_value = collector
    return collector


def _mock_release_collection(
    mock_release_collector,
    *,
    total_count=0,
    unique_repos_count=0,
    detailed_releases=None,
):
    """配置 ReleaseCollector 返回值。"""
    collector = Mock()
    collector.collect_releases.return_value = (
        ReleasesData(
            total_count=total_count,
            unique_repos_count=unique_repos_count,
            releases=[],
        ),
        detailed_releases or [],
    )
    mock_release_collector.return_value = collector
    return collector


def _mock_empty_material_analyzer(mock_factory):
    """配置 analyze_materials 返回空列表的 analyzer。"""
    analyzer = Mock()
    analyzer.analyze_materials.return_value = []
    mock_factory.return_value = analyzer
    return analyzer


def _build_mock_report(*, stats=None):
    """构造带基础字段的报告 mock。"""
    report = Mock()
    report.date = "2026-01-02"
    report.engineering_signals = []
    report.research_signals = []
    report.commit_signals = []
    report.activity = {}
    report.stats = stats or {}
    report.model_dump_json = Mock(
        return_value='{"date": "2026-01-02", "engineering_signals": []}'
    )
    return report


class TestTrendPulsePipeline:
    """测试 TrendPulse 主流程"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ReleaseMaterialBuilder")
    @patch("trendpluse.app.pipeline.CommitMaterialBuilder")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

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
            model="glm-4.7",
            max_turns=30,
            max_budget_usd=3.0,
            batch_size=200,
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
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.ReleaseSummarizer")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

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

        detailed_commits = [
            {
                "repo": "anthropics/skills",
                "sha": "abc123",
                "message": "feat: add new feature",
                "author": "testuser",
                "timestamp": "2026-01-02T10:00:00Z",
            }
        ]
        _mock_activity_collection(
            mock_activity_collector,
            total_commits=5,
            active_repos_count=1,
            detailed_commits=detailed_commits,
        )

        detailed_releases: list[dict] = []
        _mock_release_collection(
            mock_release_collector,
            detailed_releases=detailed_releases,
        )

        mock_release_summarizer_instance = Mock()
        mock_release_summarizer_instance.summarize_materials.return_value = {}
        mock_release_summarizer.return_value = mock_release_summarizer_instance

        mock_commit_analyzer_instance = _mock_empty_material_analyzer(
            mock_commit_analyzer
        )
        _mock_empty_material_analyzer(mock_release_analyzer)

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

        mock_report_obj = _build_mock_report(stats={"total_prs_analyzed": 1})
        mock_report_obj.engineering_signals = [mock_signal]
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
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.ReleaseSummarizer")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        _mock_activity_collection(mock_activity_collector)

        detailed_releases = [
            {
                "repo": "anthropics/skills",
                "tag_name": "v1.0.0",
                "name": "v1.0.0",
                "body": "Release notes",
                "html_url": "https://github.com/anthropics/skills/releases/tag/v1.0.0",
            }
        ]
        _mock_release_collection(
            mock_release_collector,
            total_count=1,
            unique_repos_count=1,
            detailed_releases=detailed_releases,
        )

        mock_release_summarizer_instance = Mock()
        mock_release_summarizer_instance.summarize_materials.return_value = {}
        mock_release_summarizer.return_value = mock_release_summarizer_instance

        _mock_empty_material_analyzer(mock_commit_analyzer)
        _mock_empty_material_analyzer(mock_release_analyzer)

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
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        detailed_commits = [
            {
                "repo": "anthropics/skills",
                "sha": "abc123",
                "message": "feat: add new feature",
                "author": "testuser",
                "timestamp": "2026-01-02T10:00:00Z",
            }
        ]
        _mock_activity_collection(
            mock_activity_collector,
            total_commits=5,
            active_repos_count=1,
            detailed_commits=detailed_commits,
        )

        detailed_releases: list[dict] = []
        _mock_release_collection(
            mock_release_collector,
            detailed_releases=detailed_releases,
        )

        mock_commit_analyzer_instance = _mock_empty_material_analyzer(
            mock_commit_analyzer
        )
        _mock_empty_material_analyzer(mock_release_analyzer)

        mock_filter_instance = Mock()
        mock_filter_instance.filter_candidates.return_value = []
        mock_filter.return_value = mock_filter_instance

        mock_reader_instance = Mock()
        mock_reader.return_value = mock_reader_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_report_obj = _build_mock_report()
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

    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings(feishu_webhook_url=None)

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_collector_instance

        _mock_activity_collection(
            mock_activity_collector,
            total_commits=5,
            active_repos_count=1,
        )

        _mock_release_collection(mock_release_collector)

        _mock_empty_material_analyzer(mock_commit_analyzer)
        _mock_empty_material_analyzer(mock_release_analyzer)

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

    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings(feishu_webhook_url=None)

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        _mock_activity_collection(mock_activity_collector)

        _mock_release_collection(mock_release_collector)

        _mock_empty_material_analyzer(mock_commit_analyzer)
        _mock_empty_material_analyzer(mock_release_analyzer)

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

    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.SDKCommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings(feishu_webhook_url=None)

        mock_collector_instance = Mock()
        mock_collector_instance.fetch_events.return_value = [
            {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
        ]
        mock_collector.return_value = mock_collector_instance

        _mock_activity_collection(mock_activity_collector)

        _mock_release_collection(mock_release_collector)

        _mock_empty_material_analyzer(mock_commit_analyzer)
        _mock_empty_material_analyzer(mock_release_analyzer)

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
