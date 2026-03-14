"""MarkdownReporter 周报渲染测试

测试 MarkdownReporter 的周报渲染功能。
"""

from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import (
    CoreTrend,
    RepoActivity,
    Signal,
    WeeklyActivity,
    WeeklyReport,
)


class TestRenderWeeklyReport:
    """测试周报渲染"""

    def test_render_weekly_report_full(self):
        """测试渲染完整周报"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief=(
                "第 05 周共分析 7 天数据，发现 10 个趋势信号，3 个高影响信号。"
            ),
            engineering_signals=[
                Signal(
                    id="sig-1",
                    title="异步架构成为标配",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="重要趋势",
                    sources=["https://github.com/test/pr/1"],
                    related_repos=["test/repo"],
                )
            ],
            research_signals=[],
            daily_reports_count=7,
            total_prs_analyzed=50,
            high_impact_signals=3,
            total_commits=100,
            total_releases=5,
            weekly_activity=WeeklyActivity(
                total_commits=100,
                active_repos_count=3,
                top_repos=[
                    RepoActivity(
                        repo="test/repo", commits=50, top_contributors=["user1"]
                    )
                ],
            ),
        )

        # Act
        markdown = reporter.render_weekly_report(report)

        # Assert - 验证关键元素存在
        assert "# TrendPulse 周报" in markdown
        assert "2026-01-20" in markdown
        assert "2026-01-26" in markdown
        assert "第 05 周共分析 7 天数据" in markdown
        assert "## 📊 本周总览" in markdown
        assert "## 🔥 核心趋势" in markdown
        assert "异步架构成为标配" in markdown
        assert "## 重点信号" in markdown
        assert "## 🏆 活跃度排名" in markdown

    def test_render_weekly_report_minimal(self):
        """测试渲染最小周报（无信号无活跃度）"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="本周暂无数据。",
            weekly_activity=None,
        )

        # Act
        markdown = reporter.render_weekly_report(report)

        # Assert
        assert "# TrendPulse 周报" in markdown
        assert "本周暂无数据" in markdown
        assert "## 📊 本周总览" in markdown

    def test_render_weekly_stats(self):
        """测试渲染统计概览"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试",
            daily_reports_count=5,
            total_prs_analyzed=30,
            high_impact_signals=2,
            total_commits=80,
            total_releases=3,
        )

        # Act
        stats = reporter._render_weekly_stats(report)

        # Assert
        assert "## 📊 本周总览" in stats
        assert "| 包含日报数 | 5 天 |" in stats
        assert "| 分析 PR 数 | 30 |" in stats
        assert "| 高影响信号 | 2 |" in stats
        assert "| 总 Commit 数 | 80 |" in stats
        assert "| 总 Release 数 | 3 |" in stats

    def test_render_core_trends(self):
        """测试渲染核心趋势（使用 AI 分组）"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试",
            core_trends=[
                CoreTrend(
                    title="异步架构普及",
                    theme="architecture",
                    description="多个项目采用异步架构",
                    signal_ids=["sig-1", "sig-2"],
                    impact_level=5,
                ),
                CoreTrend(
                    title="AI 工具链创新",
                    theme="tooling",
                    description="AI 辅助开发工具快速迭代",
                    signal_ids=["sig-3"],
                    impact_level=4,
                ),
            ],
        )

        # Act
        trends = reporter._render_core_trends(report)

        # Assert
        assert "## 🔥 核心趋势" in trends
        assert "### 1. 异步架构普及" in trends
        assert "### 2. AI 工具链创新" in trends
        assert "**主题**: 🏗️ `architecture`" in trends
        assert "**主题**: 🛠️ `tooling`" in trends
        assert "**影响**: ⭐⭐⭐⭐⭐" in trends
        assert "**相关信号数**: 2" in trends
        assert "**相关信号数**: 1" in trends

    def test_render_core_trends_fallback_to_signals(self):
        """测试核心趋势降级到信号列表（无 AI 分组时）"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试",
            core_trends=[],  # 空 AI 分组
            engineering_signals=[
                Signal(
                    id="sig-1",
                    title="趋势A",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="重要",
                    sources=["https://github.com/test/pr/1"],
                    related_repos=["test/repo"],
                ),
            ],
        )

        # Act
        trends = reporter._render_core_trends(report)

        # Assert - 应该降级到信号列表
        assert "## 🔥 核心趋势" in trends
        assert "### 1. 趋势A" in trends
        assert "**类型**: 🚀 `capability`" in trends
        assert "**影响**: ⭐⭐⭐⭐⭐" in trends

    def test_render_core_trends_empty(self):
        """测试空核心趋势"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试",
            core_trends=[],
            engineering_signals=[],
            research_signals=[],
        )

        # Act
        trends = reporter._render_core_trends(report)

        # Assert
        assert "## 🔥 核心趋势" in trends
        assert "本周暂无核心趋势" in trends

    def test_render_weekly_activity(self):
        """测试渲染周活跃度"""
        # Arrange
        reporter = MarkdownReporter()

        activity = WeeklyActivity(
            total_commits=200,
            active_repos_count=5,
            top_repos=[
                RepoActivity(repo="repo1", commits=100, top_contributors=["user1"]),
                RepoActivity(repo="repo2", commits=50, top_contributors=["user2"]),
            ],
        )

        # Act
        markdown = reporter._render_weekly_activity(activity)

        # Assert
        assert "## 🏆 活跃度排名" in markdown
        assert "### 总览" in markdown
        assert "**总 Commit 数**: 200" in markdown
        assert "**活跃仓库数**: 5" in markdown
        assert "### TOP 10" in markdown
        assert "| 排名 | 仓库 | Commits |" in markdown


class TestSaveWeeklyReport:
    """测试保存周报"""

    def test_save_weekly_report(self, temp_file):
        """测试保存周报到文件"""
        # Arrange
        reporter = MarkdownReporter()

        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试周报",
        )

        # Act
        reporter.save_weekly_report(report, str(temp_file))

        # Assert
        assert temp_file.exists()
        content = temp_file.read_text()
        assert "# TrendPulse 周报" in content
        assert "2026-W05" in content
