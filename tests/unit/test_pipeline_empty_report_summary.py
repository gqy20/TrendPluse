"""测试空报告的摘要生成逻辑

验证当有 commit/release 信号时，摘要应该动态反映实际情况，
而不是硬编码"未发现信号"。
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


class TestEmptyReportSummary:
    """测试空报告的摘要生成"""

    # 注意：patch 装饰器从下往上应用，参数从上往下对应
    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_empty_report_with_no_signals(
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
        mock_write_text,
    ):
        """测试：无信号时摘要正确"""
        # Arrange - 设置 mock settings
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
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

        # Mock 空信号列表
        mock_commit_signals: list[Signal] = []
        mock_release_signals: list[Signal] = []

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, new_contributors=2, top_repos=[]
        )

        # Mock 详细 commits 数据（用于 commit 分析）
        mock_detailed_commits = [
            {
                "sha": f"abc{i}",
                "repo": "test/repo",
                "message": f"Test commit {i}",
                "author": "test",
                "date": "2026-01-02",
            }
            for i in range(3)  # 3 个 commits
        ]

        # Mock release 数据
        mock_releases_data = ReleasesData(
            total_count=0, unique_repos_count=0, releases=[]
        )

        # 设置 mock 行为
        mock_ghec_instance = Mock()
        mock_ghec_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_ghec_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = (
            mock_activity_data,
            mock_detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = mock_commit_signals
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = (
            mock_release_signals
        )
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = "今日 (2026-01-02) 未发现符合条件的趋势信号。"
        assert report.summary_brief == expected_summary

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_empty_report_with_only_commit_signals(
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
        mock_write_text,
    ):
        """测试：只有 commit 信号时摘要正确"""
        # Arrange - 设置 mock settings
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
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

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

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, new_contributors=2, top_repos=[]
        )

        # Mock 详细 commits 数据（用于 commit 分析）
        mock_detailed_commits = [
            {
                "sha": f"abc{i}",
                "repo": "test/repo",
                "message": f"Test commit {i}",
                "author": "test",
                "date": "2026-01-02",
            }
            for i in range(3)  # 3 个 commits
        ]

        # Mock release 数据
        mock_releases_data = ReleasesData(
            total_count=0, unique_repos_count=0, releases=[]
        )

        # 设置 mock 行为
        mock_ghec_instance = Mock()
        mock_ghec_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_ghec_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = (
            mock_activity_data,
            mock_detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = mock_commit_signals
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = (
            mock_release_signals
        )
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 3 个 Commit 信号，0 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_empty_report_with_only_release_signals(
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
        mock_write_text,
    ):
        """测试：只有 release 信号时摘要正确"""
        # Arrange - 设置 mock settings
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
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

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

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, new_contributors=2, top_repos=[]
        )

        # Mock 详细 commits 数据（用于 commit 分析）
        mock_detailed_commits = [
            {
                "sha": f"abc{i}",
                "repo": "test/repo",
                "message": f"Test commit {i}",
                "author": "test",
                "date": "2026-01-02",
            }
            for i in range(3)  # 3 个 commits
        ]

        # Mock release 数据
        mock_releases_data = ReleasesData(
            total_count=2, unique_repos_count=1, releases=[]
        )

        # 设置 mock 行为
        mock_ghec_instance = Mock()
        mock_ghec_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_ghec_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = (
            mock_activity_data,
            mock_detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = mock_commit_signals
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = (
            mock_release_signals
        )
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 0 个 Commit 信号，2 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_empty_report_with_both_signal_types(
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
        mock_write_text,
    ):
        """测试：同时有 commit 和 release 信号时摘要正确"""
        # Arrange - 设置 mock settings
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
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

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

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, new_contributors=2, top_repos=[]
        )

        # Mock 详细 commits 数据（用于 commit 分析）
        mock_detailed_commits = [
            {
                "sha": f"abc{i}",
                "repo": "test/repo",
                "message": f"Test commit {i}",
                "author": "test",
                "date": "2026-01-02",
            }
            for i in range(3)  # 3 个 commits
        ]

        # Mock release 数据
        mock_releases_data = ReleasesData(
            total_count=1, unique_repos_count=1, releases=[]
        )

        # 设置 mock 行为
        mock_ghec_instance = Mock()
        mock_ghec_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_ghec_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = (
            mock_activity_data,
            mock_detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = mock_commit_signals
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = (
            mock_release_signals
        )
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证摘要
        expected_summary = (
            "今日 (2026-01-02) 发现 5 个 Commit 信号，1 个 Release 信号。"
        )
        assert report.summary_brief == expected_summary

    @patch("pathlib.Path.write_text")
    @patch("trendpluse.pipeline.Settings")
    @patch("trendpluse.pipeline.MarkdownReporter")
    @patch("trendpluse.pipeline.ActivityCollector")
    @patch("trendpluse.pipeline.ReleaseCollector")
    @patch("trendpluse.pipeline.CommitAnalyzer")
    @patch("trendpluse.pipeline.ReleaseAnalyzer")
    @patch("trendpluse.pipeline.TrendAnalyzer")
    @patch("trendpluse.pipeline.SignalDeduplicator", MockSignalDeduplicator)
    @patch("trendpluse.pipeline.GitHubDetailFetcher")
    @patch("trendpluse.pipeline.EventFilter")
    @patch("trendpluse.pipeline.GitHubEventsCollector")
    def test_empty_report_stats_with_high_impact_signals(
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
        mock_write_text,
    ):
        """测试：空报告应该统计高影响 commit 信号"""
        # Arrange - 设置 mock settings
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
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

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

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, new_contributors=2, top_repos=[]
        )

        # Mock 详细 commits 数据（用于 commit 分析）
        mock_detailed_commits = [
            {
                "sha": f"abc{i}",
                "repo": "test/repo",
                "message": f"Test commit {i}",
                "author": "test",
                "date": "2026-01-02",
            }
            for i in range(3)  # 3 个 commits
        ]

        # Mock release 数据
        mock_releases_data = ReleasesData(
            total_count=0, unique_repos_count=0, releases=[]
        )

        # 设置 mock 行为
        mock_ghec_instance = Mock()
        mock_ghec_instance.fetch_events.return_value = []
        mock_collector.return_value = mock_ghec_instance

        mock_activity_collector_instance = Mock()
        mock_activity_collector_instance.collect_activity.return_value = (
            mock_activity_data,
            mock_detailed_commits,
        )
        mock_activity_collector.return_value = mock_activity_collector_instance

        mock_release_collector_instance = Mock()
        mock_release_collector_instance.collect_releases.return_value = (
            mock_releases_data,
            [],
        )
        mock_release_collector.return_value = mock_release_collector_instance

        mock_commit_analyzer_instance = Mock()
        mock_commit_analyzer_instance.analyze_commits.return_value = mock_commit_signals
        mock_commit_analyzer.return_value = mock_commit_analyzer_instance

        mock_release_analyzer_instance = Mock()
        mock_release_analyzer_instance.analyze_releases.return_value = []
        mock_release_analyzer.return_value = mock_release_analyzer_instance

        mock_analyzer_instance = Mock()
        mock_analyzer_instance.analyze_prs.return_value = []
        mock_analyzer.return_value = mock_analyzer_instance

        # Act
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证高影响信号统计
        assert report.stats["high_impact_signals"] == 2  # 2个高影响信号
        assert report.stats["total_commits_analyzed"] == 100
