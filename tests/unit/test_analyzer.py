"""AI 分析器单元测试"""

from unittest.mock import Mock, patch

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import DailyReport, Signal


class TestTrendAnalyzer:
    """测试趋势信号分析器"""

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_init_with_api_key(self, mock_from_anthropic):
        """测试：使用 API key 初始化"""
        # Arrange & Act
        analyzer = TrendAnalyzer(api_key="test_key")

        # Assert
        assert analyzer is not None
        mock_from_anthropic.assert_called_once()

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_analyze_single_pr(self, mock_from_anthropic):
        """测试：分析单个 PR 提取信号"""
        # Arrange
        mock_signal = Signal(
            id="test-1",
            title="新功能：支持 Python 3.13",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="扩展了对最新 Python 版本的支持",
            sources=["https://github.com/anthropics/skills/pull/123"],
            related_repos=["anthropics/skills"],
        )

        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_signal
        mock_from_anthropic.return_value = mock_client

        analyzer = TrendAnalyzer(api_key="test_key")

        pr_details = {
            "number": 123,
            "title": "支持 Python 3.13",
            "body": "添加了 Python 3.13 支持",
            "author": "alice",
            "url": "https://github.com/anthropics/skills/pull/123",
            "repo_name": "anthropics/skills",
        }

        # Act
        signal = analyzer.analyze_pr(pr_details)

        # Assert
        assert signal.title == "新功能：支持 Python 3.13"
        assert signal.type == "capability"
        assert signal.impact_score == 4

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_analyze_multiple_prs(self, mock_from_anthropic):
        """测试：批量分析多个 PR"""
        # Arrange
        mock_signal_1 = Signal(
            id="test-1",
            title="功能 A",
            type="capability",
            category="engineering",
            impact_score=3,
            why_it_matters="重要",
            sources=["https://github.com/owner/repo/pull/1"],
            related_repos=["owner/repo"],
        )

        mock_signal_2 = Signal(
            id="test-2",
            title="功能 B",
            type="workflow",
            category="research",
            impact_score=5,
            why_it_matters="非常重要",
            sources=["https://github.com/owner/repo/pull/2"],
            related_repos=["owner/repo"],
        )

        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = [
            mock_signal_1,
            mock_signal_2,
        ]
        mock_from_anthropic.return_value = mock_client

        analyzer = TrendAnalyzer(api_key="test_key")

        pr_list = [
            {
                "number": 1,
                "title": "PR 1",
                "url": "https://github.com/owner/repo/pull/1",
                "repo_name": "owner/repo",
            },
            {
                "number": 2,
                "title": "PR 2",
                "url": "https://github.com/owner/repo/pull/2",
                "repo_name": "owner/repo",
            },
        ]

        # Act
        signals = analyzer.analyze_prs(pr_list)

        # Assert
        assert len(signals) == 2
        assert signals[0].title == "功能 A"
        assert signals[1].title == "功能 B"

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_generate_daily_report(self, mock_from_anthropic):
        """测试：生成每日报告"""
        # Arrange
        mock_report = DailyReport(
            date="2026-01-02",
            summary_brief="今日共分析 5 个 PR，发现 3 个高影响信号",
            engineering_signals=[
                Signal(
                    id="test-1",
                    title="功能 X",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="重要",
                    sources=["url"],
                    related_repos=["repo"],
                )
            ],
            research_signals=[],
            stats={
                "total_prs_analyzed": 5,
                "total_releases": 1,
                "high_impact_signals": 3,
            },
        )

        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_report
        mock_from_anthropic.return_value = mock_client

        analyzer = TrendAnalyzer(api_key="test_key")

        signals = [
            Signal(
                id="test-1",
                title="功能 X",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="重要",
                sources=["url"],
                related_repos=["repo"],
            )
        ]

        # Act
        report = analyzer.generate_report(signals, date="2026-01-02")

        # Assert
        assert report.date == "2026-01-02"
        assert len(report.engineering_signals) == 1
        # stats 由实现重新计算，基于输入信号
        assert report.stats["total_prs_analyzed"] == 1  # 传入的 signals 数量
        assert report.stats["high_impact_signals"] == 1  # impact_score >= 4 的信号数量

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_filter_high_impact_signals(self, mock_from_anthropic):
        """测试：筛选高影响信号"""
        # Arrange
        mock_client = Mock()
        mock_from_anthropic.return_value = mock_client

        analyzer = TrendAnalyzer(api_key="test_key")

        signals = [
            Signal(
                id="low",
                title="低影响",
                type="capability",
                category="engineering",
                impact_score=2,
                why_it_matters="一般",
                sources=["url"],
                related_repos=["repo"],
            ),
            Signal(
                id="high",
                title="高影响",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="重要",
                sources=["url"],
                related_repos=["repo"],
            ),
        ]

        # Act
        high_impact = analyzer.filter_high_impact(signals, threshold=4)

        # Assert
        assert len(high_impact) == 1
        assert high_impact[0].id == "high"

    @patch("trendpluse.analyzers.trend_analyzer.instructor.from_anthropic")
    def test_categorize_signals(self, mock_from_anthropic):
        """测试：按类型分类信号"""
        # Arrange
        mock_client = Mock()
        mock_from_anthropic.return_value = mock_client

        analyzer = TrendAnalyzer(api_key="test_key")

        signals = [
            Signal(
                id="eng-1",
                title="工程信号",
                type="capability",
                category="engineering",
                impact_score=3,
                why_it_matters="重要",
                sources=["url"],
                related_repos=["repo"],
            ),
            Signal(
                id="res-1",
                title="研究信号",
                type="eval",
                category="research",
                impact_score=4,
                why_it_matters="重要",
                sources=["url"],
                related_repos=["repo"],
            ),
        ]

        # Act
        categorized = analyzer.categorize_signals(signals)

        # Assert
        assert len(categorized["engineering"]) == 1
        assert len(categorized["research"]) == 1
        assert categorized["engineering"][0].id == "eng-1"
        assert categorized["research"][0].id == "res-1"
