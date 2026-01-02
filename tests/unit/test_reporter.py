"""报告生成器单元测试"""

from trendpluse.models.signal import DailyReport, Signal
from trendpluse.reporters.markdown_reporter import MarkdownReporter


class TestMarkdownReporter:
    """测试 Markdown 报告生成器"""

    def test_render_single_signal(self):
        """测试：渲染单个信号"""
        # Arrange
        reporter = MarkdownReporter()

        signal = Signal(
            id="test-1",
            title="新功能：支持 Python 3.13",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="扩展了对最新 Python 版本的支持",
            sources=["https://github.com/anthropics/skills/pull/123"],
            related_repos=["anthropics/skills"],
        )

        # Act
        markdown = reporter.render_signal(signal)

        # Assert
        assert "新功能：支持 Python 3.13" in markdown
        assert "capability" in markdown
        assert "⭐⭐⭐⭐" in markdown  # 4 stars
        assert "https://github.com/anthropics/skills/pull/123" in markdown

    def test_render_daily_report(self):
        """测试：渲染每日报告"""
        # Arrange
        reporter = MarkdownReporter()

        report = DailyReport(
            date="2026-01-02",
            summary_brief="今日共分析 5 个 PR，发现 3 个高影响信号",
            engineering_signals=[
                Signal(
                    id="eng-1",
                    title="工程信号 A",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="重要",
                    sources=["url1"],
                    related_repos=["repo1"],
                )
            ],
            research_signals=[
                Signal(
                    id="res-1",
                    title="研究信号 B",
                    type="eval",
                    category="research",
                    impact_score=5,
                    why_it_matters="非常重要",
                    sources=["url2"],
                    related_repos=["repo2"],
                )
            ],
            stats={
                "total_prs_analyzed": 5,
                "total_releases": 1,
                "high_impact_signals": 3,
            },
        )

        # Act
        markdown = reporter.render_report(report)

        # Assert
        assert "# TrendPulse 每日报告 - 2026-01-02" in markdown
        assert "今日共分析 5 个 PR，发现 3 个高影响信号" in markdown
        assert "🔧 工程信号" in markdown  # emoji + 文本
        assert "🔬 研究信号" in markdown  # emoji + 文本
        assert "工程信号 A" in markdown
        assert "研究信号 B" in markdown
        assert "## 📊 统计信息" in markdown  # 实际的标题

    def test_render_signal_list(self):
        """测试：渲染信号列表"""
        # Arrange
        reporter = MarkdownReporter()

        signals = [
            Signal(
                id="test-1",
                title="信号 1",
                type="capability",
                category="engineering",
                impact_score=3,
                why_it_matters="重要",
                sources=["url1"],
                related_repos=["repo1"],
            ),
            Signal(
                id="test-2",
                title="信号 2",
                type="workflow",
                category="research",
                impact_score=5,
                why_it_matters="非常重要",
                sources=["url2"],
                related_repos=["repo2"],
            ),
        ]

        # Act
        markdown = reporter.render_signals(signals, category="工程")

        # Assert
        assert "🔧 工程信号" in markdown  # emoji + 文本
        assert "信号 1" in markdown
        assert "信号 2" in markdown

    def test_get_impact_emoji(self):
        """测试：获取影响评分表情"""
        # Arrange
        reporter = MarkdownReporter()

        # Act & Assert
        assert reporter.get_impact_emoji(1) == "⭐"
        assert reporter.get_impact_emoji(2) == "⭐⭐"
        assert reporter.get_impact_emoji(3) == "⭐⭐⭐"
        assert reporter.get_impact_emoji(4) == "⭐⭐⭐⭐"
        assert reporter.get_impact_emoji(5) == "⭐⭐⭐⭐⭐"

    def test_get_type_emoji(self):
        """测试：获取信号类型表情"""
        # Arrange
        reporter = MarkdownReporter()

        # Act & Assert
        assert reporter.get_type_emoji("capability") == "🚀"
        assert reporter.get_type_emoji("abstraction") == "🎨"
        assert reporter.get_type_emoji("workflow") == "⚙️"
        assert reporter.get_type_emoji("eval") == "📊"
        assert reporter.get_type_emoji("safety") == "🛡️"
        assert reporter.get_type_emoji("performance") == "⚡"
        assert reporter.get_type_emoji("commit") == "💾"

    def test_render_report_with_commit_signals(self):
        """测试：渲染包含 commit 信号的每日报告"""
        # Arrange
        reporter = MarkdownReporter()

        report = DailyReport(
            date="2026-01-02",
            summary_brief="今日分析结果",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[
                Signal(
                    id="commit-1",
                    title="新增流式 API 支持",
                    type="commit",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="提供了实时流式响应能力",
                    sources=["https://github.com/anthropics/claude-sdk-python/commit/abc123"],
                    related_repos=["anthropics/claude-sdk-python"],
                )
            ],
            stats={
                "total_prs_analyzed": 0,
                "total_commits_analyzed": 10,
                "high_impact_signals": 1,
            },
        )

        # Act
        markdown = reporter.render_report(report)

        # Assert
        assert "💾 Commit 信号" in markdown
        assert "新增流式 API 支持" in markdown
        assert "total_commits_analyzed" in markdown or "10" in markdown

    def test_save_to_file(self, tmp_path):
        """测试：保存到文件"""
        # Arrange
        reporter = MarkdownReporter()

        report = DailyReport(
            date="2026-01-02",
            summary_brief="测试报告",
            engineering_signals=[],
            research_signals=[],
            stats={},
        )

        output_path = tmp_path / "report.md"

        # Act
        reporter.save_report(report, str(output_path))

        # Assert
        assert output_path.exists()
        content = output_path.read_text()
        assert "TrendPulse 每日报告 - 2026-01-02" in content
