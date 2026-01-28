"""测试空报告的信号分类逻辑

验证 commit_signals 应该根据其 category 属性被正确分类到
engineering_signals 和 research_signals 中。
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


class TestSignalCategorization:
    """测试信号分类"""

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
    def test_commit_signals_categorized_in_empty_report(
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
        """测试：空报告中 commit_signals 应该被分类到 engineering/research"""
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
        mock_settings_instance.enable_parallel_collection = False
        mock_settings_instance.max_parallel_workers = 4
        mock_settings_instance.include_prereleases = False
        mock_settings_instance.feishu_webhook_url = None
        mock_settings_instance.feishu_at_mobiles_list = []
        mock_settings.return_value = mock_settings_instance

        # 创建包含 engineering 和 research 类型的 commit 信号
        mock_commit_signals: list[Signal] = [
            Signal(
                id="commit-1",
                title="Engineering Signal",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test engineering signal",
                sources=["https://github.com/test/repo/commit/abc1"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-2",
                title="Research Signal",
                type="capability",
                category="research",
                impact_score=5,
                why_it_matters="Test research signal",
                sources=["https://github.com/test/repo/commit/abc2"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="commit-3",
                title="Another Engineering Signal",
                type="capability",
                category="engineering",
                impact_score=3,
                why_it_matters="Test engineering signal 2",
                sources=["https://github.com/test/repo/commit/abc3"],
                related_repos=["test/repo"],
            ),
        ]

        # Mock 活跃度数据
        mock_activity_data = ActivityData(
            total_commits=100, active_repos_count=5, top_repos=[]
        )

        # Mock 详细 commits 数据
        mock_detailed_commits = [
            {
                "sha": "abc1",
                "repo": "test/repo",
                "message": "Test commit 1",
                "author": "test",
                "date": "2026-01-02",
            },
            {
                "sha": "abc2",
                "repo": "test/repo",
                "message": "Test commit 2",
                "author": "test",
                "date": "2026-01-02",
            },
            {
                "sha": "abc3",
                "repo": "test/repo",
                "message": "Test commit 3",
                "author": "test",
                "date": "2026-01-02",
            },
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
        mock_activity_collector_instance.collect_activity_graphql.return_value = (
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

        # Act - 运行 pipeline
        pipeline = TrendPulsePipeline()
        report = pipeline.run_daily(date=datetime(2026, 1, 2))

        # Assert - 验证 commit_signals 被清空（避免重复显示）
        assert len(report.commit_signals) == 0
        assert report.commit_signals == []

        # Assert - 验证 commit_signals 被正确分类
        assert len(report.engineering_signals) == 2  # 2个 engineering信号
        assert len(report.research_signals) == 1  # 1个 research信号

        # 验证具体信号
        engineering_titles = [s.title for s in report.engineering_signals]
        research_titles = [s.title for s in report.research_signals]

        assert "Engineering Signal" in engineering_titles
        assert "Another Engineering Signal" in engineering_titles
        assert "Research Signal" in research_titles
