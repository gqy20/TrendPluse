"""测试聚合后 commit_signals 被正确清空

这是修复报告重复显示 Commit 信号问题的测试。
"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.models.signal import ActivityData, ReleasesData, Signal


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
    settings.github_repos = ["test/repo"]
    settings.max_candidates = 20
    settings.days_to_lookback = 1
    settings.enable_parallel_collection = False
    settings.max_parallel_workers = 4
    settings.include_prereleases = False
    settings.output_dir = "reports/daily"
    settings.feishu_webhook_url = ""
    settings.feishu_at_mobiles_list = []
    for key, value in overrides.items():
        setattr(settings, key, value)
    return settings


def _mock_pipeline_inputs(
    mock_collector,
    mock_filter,
    mock_reader,
    *,
    detailed_commits=None,
    detailed_releases=None,
    total_commits=5,
    active_repos_count=1,
    total_releases=0,
    unique_release_repos=0,
):
    """配置 PR、活跃度和 release 输入。"""
    collector = Mock()
    collector.fetch_events.return_value = [
        {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
    ]
    mock_collector.return_value = collector

    event_filter = Mock()
    event_filter.filter_candidates.return_value = [
        {"type": "PullRequestEvent", "repo": {"name": "test/repo"}}
    ]
    mock_filter.return_value = event_filter

    reader = Mock()
    reader.refs_from_candidates.return_value = [Mock()]
    reader.read_many.return_value = [Mock()]
    mock_reader.return_value = reader

    activity_collector = Mock()
    activity_collector.collect_activity_graphql.return_value = (
        ActivityData(
            total_commits=total_commits,
            active_repos_count=active_repos_count,
            top_repos=[],
        ),
        detailed_commits or [],
    )

    release_collector = Mock()
    release_collector.collect_releases.return_value = (
        ReleasesData(
            total_count=total_releases,
            unique_repos_count=unique_release_repos,
            releases=[],
        ),
        detailed_releases or [],
    )

    return activity_collector, release_collector


def _mock_material_analyzer(mock_factory, signals):
    """配置 analyze_materials 返回指定信号列表的 analyzer。"""
    analyzer = Mock()
    analyzer.analyze_materials.return_value = signals
    mock_factory.return_value = analyzer
    return analyzer


def _build_mock_report(
    *,
    engineering_signals,
    commit_signals,
    stats,
    release_signals=None,
):
    """构造报告 mock。"""
    report = Mock()
    report.date = "2026-01-12"
    report.engineering_signals = engineering_signals
    report.research_signals = []
    report.commit_signals = commit_signals
    report.release_signals = release_signals or []
    report.activity = {}
    report.stats = stats
    report.model_dump_json = Mock(return_value='{"date": "2026-01-12"}')
    return report


class TestCommitSignalsClearing:
    """测试聚合后 commit_signals 被正确清空"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.CommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

        # 配置活跃度数据
        detailed_commits = [
            {
                "repo": "test/repo",
                "sha": "abc123",
                "message": "feat: new feature",
                "author": "testuser",
                "timestamp": "2026-01-12T10:00:00Z",
            }
        ]
        (
            mock_activity_collector_instance,
            mock_release_collector_instance,
        ) = _mock_pipeline_inputs(
            mock_collector,
            mock_filter,
            mock_reader,
            detailed_commits=detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance
        mock_release_collector.return_value = mock_release_collector_instance

        # 配置 Commit 分析器（返回一些信号）
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
        _mock_material_analyzer(mock_commit_analyzer, [mock_commit_signal])

        # 配置 Release 分析器
        _mock_material_analyzer(mock_release_analyzer, [])

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
        mock_analyzer_instance = _mock_material_analyzer(
            mock_analyzer, [mock_pr_signal]
        )

        # 关键：模拟 LLM 返回的对象保留了 commit_signals（这是 Bug）
        # 实际中，instructor + LLM 可能不会遵守代码中的清空操作
        mock_report_obj = _build_mock_report(
            engineering_signals=[mock_pr_signal],
            commit_signals=[mock_commit_signal],
            stats={"total_prs_analyzed": 1},
        )
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )

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
    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.MarkdownReporter")
    @patch("trendpluse.app.pipeline.ActivityCollector")
    @patch("trendpluse.app.pipeline.ReleaseCollector")
    @patch("trendpluse.app.pipeline.CommitAnalyzer")
    @patch("trendpluse.app.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.app.pipeline.TrendAnalyzer")
    @patch("trendpluse.app.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.app.pipeline.GitHubPRReader")
    @patch("trendpluse.app.pipeline.EventFilter")
    @patch("trendpluse.app.pipeline.GitHubEventsCollector")
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
        mock_settings.return_value = _build_mock_settings()

        detailed_releases = [
            {
                "repo": "test/repo",
                "tag_name": "v1.0.0",
                "name": "v1.0.0",
                "html_url": "https://github.com/test/repo/releases/tag/v1.0.0",
                "version_info": {"major": 1, "minor": 0, "patch": 0},
            }
        ]
        (
            mock_activity_collector_instance,
            mock_release_collector_instance,
        ) = _mock_pipeline_inputs(
            mock_collector,
            mock_filter,
            mock_reader,
            total_commits=1,
            active_repos_count=1,
            total_releases=1,
            unique_release_repos=1,
            detailed_releases=detailed_releases,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance
        mock_release_collector.return_value = mock_release_collector_instance

        _mock_material_analyzer(mock_commit_analyzer, [])

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
        _mock_material_analyzer(mock_release_analyzer, [release_signal])

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
        mock_analyzer_instance = _mock_material_analyzer(
            mock_analyzer, [mock_pr_signal]
        )

        mock_report_obj = _build_mock_report(
            engineering_signals=[mock_pr_signal],
            commit_signals=[],
            release_signals=[release_signal],
            stats={"total_prs_analyzed": 1},
        )
        mock_analyzer_instance.aggregate_and_generate_report.return_value = (
            mock_report_obj
        )

        mock_reporter_instance = Mock()
        mock_reporter.return_value = mock_reporter_instance

        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 12))

        assert report.commit_signals == []
        assert len(report.release_signals) == 1
        assert report.release_signals[0].id == "release-1"
