"""周报数据模型测试

测试 WeeklyReport 和 WeeklyActivity 模型的功能。
"""

from datetime import datetime

from trendpluse.models.signal import (
    RepoActivity,
    Signal,
    WeeklyActivity,
    WeeklyReport,
)


class TestWeeklyReport:
    """测试 WeeklyReport 模型"""

    def test_create_minimal_weekly_report(self):
        """测试创建最小周报"""
        # Arrange & Act
        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="本周共分析 7 天数据。",
        )

        # Assert
        assert report.week_id == "2026-W05"
        assert report.start_date == "2026-01-20"
        assert report.end_date == "2026-01-26"
        assert report.summary_brief == "本周共分析 7 天数据。"
        assert report.engineering_signals == []
        assert report.research_signals == []
        assert report.daily_reports_count == 0

    def test_create_full_weekly_report(self):
        """测试创建完整周报"""
        # Arrange
        signal = Signal(
            id="test-123",
            title="测试信号",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="测试重要性",
            sources=["https://github.com/test/pr/1"],
            related_repos=["test/repo"],
        )

        activity = WeeklyActivity(
            total_commits=100,
            active_repos_count=5,
            top_repos=[
                RepoActivity(repo="test/repo", commits=50, top_contributors=["user1"])
            ],
        )

        # Act
        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="本周总览",
            engineering_signals=[signal],
            research_signals=[],
            daily_reports_count=7,
            total_prs_analyzed=50,
            high_impact_signals=3,
            total_commits=100,
            total_releases=5,
            weekly_activity=activity,
        )

        # Assert
        assert len(report.engineering_signals) == 1
        assert report.daily_reports_count == 7
        assert report.total_prs_analyzed == 50
        assert report.high_impact_signals == 3
        assert report.total_commits == 100
        assert report.total_releases == 5
        assert report.weekly_activity is not None
        assert report.weekly_activity.total_commits == 100

    def test_get_week_id_with_date(self):
        """测试从日期生成周标识"""
        # Arrange
        date = datetime(2026, 1, 27)  # 2026年1月27日是周二，ISO 第 5 周

        # Act
        week_id = WeeklyReport.get_week_id(date)

        # Assert
        # ISO 8601: 2026-01-27 周二，属于第 5 周
        assert week_id == "2026-W05"

    def test_get_week_id_monday(self):
        """测试周一日期的周标识"""
        # Arrange
        date = datetime(2026, 1, 27)  # 2026-01-27 是周二，ISO 第 5 周

        # Act
        week_id = WeeklyReport.get_week_id(date)

        # Assert
        assert week_id == "2026-W05"

    def test_get_week_id_year_boundary(self):
        """测试年份边界的周标识"""
        # Arrange - 2026年1月1日
        date = datetime(2026, 1, 1)

        # Act
        week_id = WeeklyReport.get_week_id(date)

        # Assert - 2026年1月1日是周四，属于 2025 年的第 53 周
        # 但 ISO 8601 规则：第一周包含该年1月4日
        # 2026年1月4日是周日，所以 2026-01-01 到 2026-01-03 属于 2025-W53
        # 这里我们用 Python 的 isocalendar() 结果
        year, week, _ = date.isocalendar()
        assert week_id == f"{year}-W{week:02d}"

    def test_weekly_report_serialization(self):
        """测试周报序列化和反序列化"""
        # Arrange
        report = WeeklyReport(
            week_id="2026-W05",
            start_date="2026-01-20",
            end_date="2026-01-26",
            summary_brief="测试摘要",
        )

        # Act
        json_str = report.model_dump_json()
        deserialized = WeeklyReport.model_validate_json(json_str)

        # Assert
        assert deserialized.week_id == report.week_id
        assert deserialized.start_date == report.start_date
        assert deserialized.end_date == report.end_date
        assert deserialized.summary_brief == report.summary_brief


class TestWeeklyActivity:
    """测试 WeeklyActivity 模型"""

    def test_create_weekly_activity(self):
        """测试创建周活跃度"""
        # Arrange & Act
        activity = WeeklyActivity(
            total_commits=500,
            active_repos_count=10,
            top_repos=[
                RepoActivity(
                    repo="anthropics/claude-code",
                    commits=100,
                    top_contributors=["user1", "user2"],
                ),
                RepoActivity(
                    repo="openai/openai-python",
                    commits=80,
                    top_contributors=["user3"],
                ),
            ],
        )

        # Assert
        assert activity.total_commits == 500
        assert activity.active_repos_count == 10
        assert len(activity.top_repos) == 2
        assert activity.top_repos[0].repo == "anthropics/claude-code"
        assert activity.top_repos[0].commits == 100
        assert activity.top_repos[0].top_contributors == ["user1", "user2"]

    def test_weekly_activity_serialization(self):
        """测试周活跃度序列化"""
        # Arrange
        activity = WeeklyActivity(
            total_commits=100,
            active_repos_count=1,
            top_repos=[
                RepoActivity(repo="test/repo", commits=100, top_contributors=["user1"])
            ],
        )

        # Act
        json_str = activity.model_dump_json()
        deserialized = WeeklyActivity.model_validate_json(json_str)

        # Assert
        assert deserialized.total_commits == activity.total_commits
        assert deserialized.active_repos_count == activity.active_repos_count
        assert len(deserialized.top_repos) == len(activity.top_repos)
