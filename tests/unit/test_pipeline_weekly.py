"""WeeklyReportWorkflow 周报功能测试。"""

from datetime import datetime
from unittest.mock import Mock, patch

from trendpluse.analyzers.weekly_aggregator import WeeklyAggregationResult
from trendpluse.config import Settings
from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    RepoActivity,
    Signal,
)
from trendpluse.workflows.weekly_report_workflow import WeeklyReportWorkflow


def create_workflow(settings: Settings) -> WeeklyReportWorkflow:
    """创建用于测试的周报工作流。"""
    return WeeklyReportWorkflow(
        settings=settings,
        output_service=Mock(),
    )


class TestGetLastWeekRange:
    """测试 get_last_week_range 方法。"""

    def test_get_last_week_range_from_tuesday(self):
        """测试从周中日期计算上周范围。"""
        workflow = create_workflow(Settings())
        date = datetime(2026, 1, 28)

        start_date, end_date = workflow.get_last_week_range(date)

        assert start_date == datetime(2026, 1, 19, 0, 0, 0)
        assert end_date == datetime(2026, 1, 25, 23, 59, 59, 999999)

    def test_get_last_week_range_from_monday(self):
        """测试从周初日期计算上周范围。"""
        workflow = create_workflow(Settings())
        date = datetime(2026, 1, 27)

        start_date, end_date = workflow.get_last_week_range(date)

        assert start_date == datetime(2026, 1, 19, 0, 0, 0)
        assert end_date == datetime(2026, 1, 25, 23, 59, 59, 999999)


class TestLoadDailyReports:
    """测试 load_daily_reports 方法。"""

    def test_load_existing_reports(self, temp_dir):
        """测试加载存在的日报。"""
        daily_output_dir = temp_dir / "reports" / "daily"
        daily_output_dir.mkdir(parents=True)
        workflow = create_workflow(Settings(output_dir=str(daily_output_dir)))

        start_date = datetime(2026, 1, 20)
        end_date = datetime(2026, 1, 20)

        report = DailyReport(
            date="2026-01-20",
            summary_brief="测试日报",
        )
        json_file = daily_output_dir / "report-2026-01-20.json"
        json_file.write_text(report.model_dump_json())

        reports = workflow.load_daily_reports(start_date, end_date)

        assert len(reports) == 1
        assert reports[0].date == "2026-01-20"

    def test_load_no_reports(self, temp_dir):
        """测试没有日报的情况。"""
        daily_output_dir = temp_dir / "reports" / "daily"
        daily_output_dir.mkdir(parents=True)
        workflow = create_workflow(Settings(output_dir=str(daily_output_dir)))
        start_date = datetime(2026, 1, 20)
        end_date = datetime(2026, 1, 20)

        reports = workflow.load_daily_reports(start_date, end_date)

        assert reports == []


class TestAggregateWeeklyReport:
    """测试 aggregate_weekly_report 方法。"""

    @patch(
        "trendpluse.workflows.weekly_report_workflow.WeeklyAggregator.aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[],
            summary_brief="测试摘要",
            total_signals=1,
        ),
    )
    def test_aggregate_single_daily_report(self, mock_aggregator):
        """测试聚合单个日报。"""
        workflow = create_workflow(Settings())

        daily_report = DailyReport(
            date="2026-01-20",
            summary_brief="测试日报",
            engineering_signals=[
                Signal(
                    id="sig-1",
                    title="测试信号",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="重要",
                    sources=["https://github.com/test/pr/1"],
                    related_repos=["test/repo"],
                )
            ],
            stats={
                "total_prs_analyzed": 10,
                "total_releases": 2,
            },
            activity=ActivityData(
                total_commits=30,
                active_repos_count=1,
                top_repos=[
                    RepoActivity(
                        repo="test/repo", commits=30, top_contributors=["user1"]
                    )
                ],
            ),
        )

        start_date = datetime(2026, 1, 20)
        end_date = datetime(2026, 1, 20)

        weekly = workflow.aggregate_weekly_report(
            daily_reports=[daily_report],
            start_date=start_date,
            end_date=end_date,
        )

        assert weekly.week_id == "2026-W04"
        assert weekly.start_date == "2026-01-20"
        assert weekly.end_date == "2026-01-20"
        assert weekly.daily_reports_count == 1
        assert weekly.total_prs_analyzed == 10
        assert weekly.total_commits == 30
        assert weekly.total_releases == 2
        assert len(weekly.engineering_signals) == 1
        assert weekly.weekly_activity is not None
        assert weekly.weekly_activity.total_commits == 30
        mock_aggregator.assert_called_once()

    @patch(
        "trendpluse.workflows.weekly_report_workflow.WeeklyAggregator.aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[],
            summary_brief="测试摘要",
            total_signals=1,
        ),
    )
    def test_aggregate_signal_deduplication(self, mock_aggregator):
        """测试信号去重。"""
        workflow = create_workflow(Settings())

        signal = Signal(
            id="sig-1",
            title="测试信号",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="重要",
            sources=["https://github.com/test/pr/1"],
            related_repos=["test/repo"],
        )

        daily_report1 = DailyReport(
            date="2026-01-20",
            summary_brief="测试日报1",
            engineering_signals=[signal],
            stats={"total_prs_analyzed": 10, "total_releases": 0},
        )
        daily_report2 = DailyReport(
            date="2026-01-21",
            summary_brief="测试日报2",
            engineering_signals=[signal],
            stats={"total_prs_analyzed": 10, "total_releases": 0},
        )

        weekly = workflow.aggregate_weekly_report(
            daily_reports=[daily_report1, daily_report2],
            start_date=datetime(2026, 1, 20),
            end_date=datetime(2026, 1, 21),
        )

        assert len(weekly.engineering_signals) == 1
        assert weekly.engineering_signals[0].id == "sig-1"
        mock_aggregator.assert_called_once()

    @patch(
        "trendpluse.workflows.weekly_report_workflow.WeeklyAggregator.aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[],
            summary_brief="测试摘要",
            total_signals=3,
        ),
    )
    def test_aggregate_multiple_daily_reports(self, mock_aggregator):
        """测试聚合多个日报。"""
        workflow = create_workflow(Settings())

        daily_reports = [
            DailyReport(
                date=f"2026-01-{20 + i}",
                summary_brief=f"测试日报{i}",
                engineering_signals=[
                    Signal(
                        id=f"sig-{i}",
                        title=f"信号{i}",
                        type="capability",
                        category="engineering",
                        impact_score=3,
                        why_it_matters="重要",
                        sources=[f"https://github.com/test/pr/{i}"],
                        related_repos=["test/repo"],
                    )
                ],
                stats={"total_prs_analyzed": 10, "total_releases": 0},
            )
            for i in range(3)
        ]

        weekly = workflow.aggregate_weekly_report(
            daily_reports=daily_reports,
            start_date=datetime(2026, 1, 20),
            end_date=datetime(2026, 1, 22),
        )

        assert weekly.daily_reports_count == 3
        assert weekly.total_prs_analyzed == 30
        assert len(weekly.engineering_signals) == 3
        mock_aggregator.assert_called_once()


class TestAggregateActivity:
    """测试 aggregate_activity 方法。"""

    def test_aggregate_activity_single_repo(self):
        """测试聚合单个仓库的活跃度。"""
        workflow = create_workflow(Settings())

        daily_reports = [
            DailyReport(
                date="2026-01-20",
                summary_brief="测试",
                activity=ActivityData(
                    total_commits=30,
                    active_repos_count=1,
                    top_repos=[
                        RepoActivity(
                            repo="test/repo",
                            commits=30,
                            top_contributors=["user1", "user2"],
                        )
                    ],
                ),
            )
        ]

        weekly_activity = workflow.aggregate_activity(daily_reports)

        assert weekly_activity.total_commits == 30
        assert weekly_activity.active_repos_count == 1
        assert len(weekly_activity.top_repos) == 1
        assert weekly_activity.top_repos[0].repo == "test/repo"
        assert weekly_activity.top_repos[0].commits == 30
        assert set(weekly_activity.top_repos[0].top_contributors) == {
            "user1",
            "user2",
        }

    def test_aggregate_activity_multiple_repos(self):
        """测试聚合多个仓库的活跃度。"""
        workflow = create_workflow(Settings())

        daily_reports = [
            DailyReport(
                date="2026-01-20",
                summary_brief="测试",
                activity=ActivityData(
                    total_commits=50,
                    active_repos_count=2,
                    top_repos=[
                        RepoActivity(
                            repo="repo1", commits=30, top_contributors=["user1"]
                        ),
                        RepoActivity(
                            repo="repo2", commits=20, top_contributors=["user2"]
                        ),
                    ],
                ),
            ),
            DailyReport(
                date="2026-01-21",
                summary_brief="测试",
                activity=ActivityData(
                    total_commits=50,
                    active_repos_count=2,
                    top_repos=[
                        RepoActivity(
                            repo="repo1", commits=25, top_contributors=["user3"]
                        ),
                        RepoActivity(
                            repo="repo2", commits=25, top_contributors=["user1"]
                        ),
                    ],
                ),
            ),
        ]

        weekly_activity = workflow.aggregate_activity(daily_reports)

        assert weekly_activity.total_commits == 100
        assert weekly_activity.active_repos_count == 2
        assert len(weekly_activity.top_repos) == 2
        assert weekly_activity.top_repos[0].repo == "repo1"
        assert weekly_activity.top_repos[0].commits == 55
        assert weekly_activity.top_repos[1].repo == "repo2"
        assert weekly_activity.top_repos[1].commits == 45
        assert set(weekly_activity.top_repos[0].top_contributors) == {
            "user1",
            "user3",
        }


class TestRunWeeklyOutput:
    """测试 run 方法的输出委托。"""

    @patch(
        "trendpluse.workflows.weekly_report_workflow.WeeklyAggregator.aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[],
            summary_brief="测试摘要",
            total_signals=1,
        ),
    )
    def test_run_delegates_output_to_service(self, _mock_aggregator, temp_dir):
        """测试周报输出委托给 ReportOutputService。"""
        daily_output_dir = temp_dir / "reports" / "daily"
        daily_output_dir.mkdir(parents=True)
        report = DailyReport(
            date="2026-01-20",
            summary_brief="测试日报",
            engineering_signals=[
                Signal(
                    id="sig-1",
                    title="测试信号",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="重要",
                    sources=["https://github.com/test/pr/1"],
                    related_repos=["test/repo"],
                )
            ],
        )
        (daily_output_dir / "report-2026-01-20.json").write_text(
            report.model_dump_json(),
            encoding="utf-8",
        )
        output_service = Mock()
        workflow = WeeklyReportWorkflow(
            settings=Settings(output_dir=str(daily_output_dir)),
            output_service=output_service,
        )

        weekly_report = workflow.run(datetime(2026, 1, 27))

        output_service.save_weekly.assert_called_once_with(
            weekly_report,
            datetime(2026, 1, 25, 23, 59, 59, 999999),
        )
