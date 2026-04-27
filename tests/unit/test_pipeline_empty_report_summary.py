"""测试空报告的摘要生成逻辑

验证当有 commit/release 信号时，摘要应该动态反映实际情况，
而不是硬编码"未发现信号"。
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
    settings.github_repos = ["anthropics/skills"]
    settings.max_candidates = 20
    settings.days_to_lookback = 1
    settings.enable_parallel_collection = False
    settings.max_parallel_workers = 4
    settings.include_prereleases = False
    settings.output_dir = "reports/daily"
    settings.feishu_webhook_url = None
    settings.feishu_at_mobiles_list = []
    for key, value in overrides.items():
        setattr(settings, key, value)
    return settings


def _build_detailed_commits(count=3):
    """构造测试用 commit 明细。"""
    return [
        {
            "sha": f"abc{i}",
            "repo": "test/repo",
            "message": f"Test commit {i}",
            "author": "test",
            "date": "2026-01-02",
        }
        for i in range(count)
    ]


def _mock_activity_collection(
    mock_activity_collector,
    *,
    total_commits=100,
    active_repos_count=5,
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
        detailed_commits or _build_detailed_commits(),
    )
    mock_activity_collector.return_value = collector
    return collector


def _mock_release_collection(
    mock_release_collector,
    *,
    total_count=0,
    unique_repos_count=0,
):
    """配置 ReleaseCollector 返回值。"""
    collector = Mock()
    collector.collect_releases.return_value = (
        ReleasesData(
            total_count=total_count,
            unique_repos_count=unique_repos_count,
            releases=[],
        ),
        [],
    )
    mock_release_collector.return_value = collector
    return collector


def _mock_material_analyzer(mock_factory, signals):
    """配置 analyze_materials 返回指定信号列表的 analyzer。"""
    analyzer = Mock()
    analyzer.analyze_materials.return_value = signals
    mock_factory.return_value = analyzer
    return analyzer


def _mock_empty_events_collector(mock_collector):
    """配置无事件输入。"""
    collector = Mock()
    collector.fetch_events.return_value = []
    mock_collector.return_value = collector
    return collector


class TestEmptyReportSummary:
    """测试空报告的摘要生成"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
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
    def test_empty_report_with_no_signals(
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
        """测试：无信号时摘要正确"""
        # Arrange - 设置 mock settings
        mock_settings.return_value = _build_mock_settings()

        # Mock 空信号列表
        mock_commit_signals: list[Signal] = []
        mock_release_signals: list[Signal] = []

        # Mock 活跃度数据
        _mock_empty_events_collector(mock_collector)
        _mock_activity_collection(mock_activity_collector)
        _mock_release_collection(mock_release_collector)
        _mock_material_analyzer(mock_commit_analyzer, mock_commit_signals)
        _mock_material_analyzer(mock_release_analyzer, mock_release_signals)
        _mock_material_analyzer(mock_analyzer, [])

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = "今日 (2026-01-02) 未发现符合条件的趋势信号。"
        assert report.summary_brief == expected_summary

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
    def test_empty_report_with_only_commit_signals(
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
        """测试：只有 commit 信号时摘要正确"""
        # Arrange - 设置 mock settings
        mock_settings.return_value = _build_mock_settings()

        # 创建 mock commit 信号
        mock_commit_signals = [
            Signal(
                id="commit-0",
                title="Commit Signal 0",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc0"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-1",
                title="Commit Signal 1",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc1"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-2",
                title="Commit Signal 2",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc2"],
                related_repos=["test/repo"],
            ),
        ]

        # Mock release 信号为空
        mock_release_signals: list[Signal] = []

        _mock_empty_events_collector(mock_collector)
        _mock_activity_collection(mock_activity_collector)
        _mock_release_collection(mock_release_collector)
        _mock_material_analyzer(mock_commit_analyzer, mock_commit_signals)
        _mock_material_analyzer(mock_release_analyzer, mock_release_signals)
        _mock_material_analyzer(mock_analyzer, [])

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 3 个 Commit 信号，0 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

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
    def test_empty_report_with_only_release_signals(
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
        """测试：只有 release 信号时摘要正确"""
        # Arrange - 设置 mock settings
        mock_settings.return_value = _build_mock_settings()

        # Mock commit 信号为空
        mock_commit_signals: list[Signal] = []

        # Mock release 信号
        mock_release_signals = [
            Signal(
                id="release-0",
                title="Release Signal 0",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="Test release signal",
                sources=["https://github.com/test/repo/releases/tag/v0.0.0"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="release-1",
                title="Release Signal 1",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="Test release signal",
                sources=["https://github.com/test/repo/releases/tag/v1.0.0"],
                related_repos=["test/repo"],
            ),
        ]

        _mock_empty_events_collector(mock_collector)
        _mock_activity_collection(mock_activity_collector)
        _mock_release_collection(
            mock_release_collector,
            total_count=2,
            unique_repos_count=1,
        )
        _mock_material_analyzer(mock_commit_analyzer, mock_commit_signals)
        _mock_material_analyzer(mock_release_analyzer, mock_release_signals)
        _mock_material_analyzer(mock_analyzer, [])

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 0 个 Commit 信号，2 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

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
    def test_empty_report_with_both_signal_types(
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
        """测试：同时有 commit 和 release 信号时摘要正确"""
        # Arrange - 设置 mock settings
        mock_settings.return_value = _build_mock_settings()

        # 创建 mock commit 信号（5个）
        mock_commit_signals = [
            Signal(
                id=f"commit-{i}",
                title=f"Commit Signal {i}",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test signal",
                sources=[f"https://github.com/test/repo/commit/abc{i}"],
                related_repos=["test/repo"],
            )
            for i in range(5)
        ]

        # Mock release 信号（1个）
        mock_release_signals = [
            Signal(
                id="release-0",
                title="Release Signal 0",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="Test release signal",
                sources=["https://github.com/test/repo/releases/tag/v1.0.0"],
                related_repos=["test/repo"],
            )
        ]

        _mock_empty_events_collector(mock_collector)
        _mock_activity_collection(mock_activity_collector)
        _mock_release_collection(
            mock_release_collector,
            total_count=1,
            unique_repos_count=1,
        )
        _mock_material_analyzer(mock_commit_analyzer, mock_commit_signals)
        _mock_material_analyzer(mock_release_analyzer, mock_release_signals)
        _mock_material_analyzer(mock_analyzer, [])

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 5 个 Commit 信号，1 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

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
    def test_empty_report_stats_with_high_impact_signals(
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
        """测试：空报告应该统计高影响 commit 信号"""
        # Arrange - 设置 mock settings
        mock_settings.return_value = _build_mock_settings()

        # 创建包含高影响信号的 commit 信号列表
        mock_commit_signals = [
            Signal(
                id="commit-1",
                title="High Impact Signal",
                type="capability",
                category="engineering",
                impact_score=5,  # 高影响
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc1"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-2",
                title="Medium Impact Signal",
                type="capability",
                category="engineering",
                impact_score=3,  # 非高影响
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc2"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-3",
                title="Another High Impact Signal",
                type="capability",
                category="engineering",
                impact_score=4,  # 高影响（>=4）
                why_it_matters="Test signal",
                sources=["https://github.com/test/repo/commit/abc3"],
                related_repos=["test/repo"],
            ),
        ]

        _mock_empty_events_collector(mock_collector)
        _mock_activity_collection(mock_activity_collector)
        _mock_release_collection(mock_release_collector)
        _mock_material_analyzer(mock_commit_analyzer, mock_commit_signals)
        _mock_material_analyzer(mock_release_analyzer, [])
        _mock_material_analyzer(mock_analyzer, [])

        # Act
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证高影响信号统计
        assert report.stats.high_impact_signals == 2  # 2个高影响信号
        assert report.stats.total_commits_analyzed == 100
