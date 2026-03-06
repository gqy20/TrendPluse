"""周报工作流。"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from trendpluse.analyzers.weekly_aggregator import WeeklyAggregator
from trendpluse.logger import get_logger
from trendpluse.models.signal import (
    DailyReport,
    RepoActivity,
    WeeklyActivity,
    WeeklyReport,
)

logger = get_logger(__name__)


class WeeklyReportWorkflow:
    """负责周报加载、聚合与输出。"""

    def __init__(self, *, settings, output_service) -> None:
        self.settings = settings
        self.output_service = output_service

    def run(self, date: datetime | None = None) -> WeeklyReport:
        """运行周报生成流程。"""
        if date is None:
            date = datetime.now()

        start_date, end_date = self.get_last_week_range(date)
        daily_reports = self.load_daily_reports(start_date, end_date)
        if not daily_reports:
            raise ValueError(
                f"没有找到 {start_date.strftime('%Y-%m-%d')} "
                f"到 {end_date.strftime('%Y-%m-%d')} 的日报数据"
            )

        weekly_report = self.aggregate_weekly_report(
            daily_reports=daily_reports,
            start_date=start_date,
            end_date=end_date,
        )
        self.output_service.save_weekly(weekly_report, end_date)
        return weekly_report

    def get_last_week_range(self, date: datetime) -> tuple[datetime, datetime]:
        """获取上周的时间范围。"""
        weekday = date.weekday()
        this_monday = date - timedelta(days=weekday)
        last_monday = this_monday - timedelta(days=7)
        last_sunday = this_monday - timedelta(days=1)
        start_date = last_monday.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = last_sunday.replace(
            hour=23, minute=59, second=59, microsecond=999999
        )
        return start_date, end_date

    def load_daily_reports(
        self, start_date: datetime, end_date: datetime
    ) -> list[DailyReport]:
        """加载指定时间范围内的日报。"""
        reports: list[DailyReport] = []
        current_date = start_date
        daily_reports_dir = Path(self.settings.output_dir)

        while current_date <= end_date:
            filename = f"report-{current_date.strftime('%Y-%m-%d')}.json"
            json_path = daily_reports_dir / filename
            if json_path.exists():
                try:
                    content = json_path.read_text(encoding="utf-8")
                    reports.append(DailyReport.model_validate_json(content))
                except Exception as exc:
                    logger.warning(f"加载日报失败 {json_path}: {exc}")
            current_date += timedelta(days=1)

        return reports

    def aggregate_weekly_report(
        self,
        *,
        daily_reports: list[DailyReport],
        start_date: datetime,
        end_date: datetime,
    ) -> WeeklyReport:
        """聚合日报生成周报。"""
        week_id = WeeklyReport.get_week_id(end_date)
        all_signals = []
        seen_signal_ids: set[str] = set()

        for report in daily_reports:
            for signal in (
                report.engineering_signals
                + report.research_signals
                + report.commit_signals
                + report.release_signals
            ):
                if signal.id not in seen_signal_ids:
                    seen_signal_ids.add(signal.id)
                    all_signals.append(signal)

        aggregator = WeeklyAggregator(
            api_key=self.settings.anthropic_api_key,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        ai_result = aggregator.aggregate(all_signals)

        engineering_signals = [s for s in all_signals if s.category == "engineering"]
        research_signals = [s for s in all_signals if s.category == "research"]
        engineering_signals.sort(key=lambda s: s.impact_score, reverse=True)
        research_signals.sort(key=lambda s: s.impact_score, reverse=True)

        total_prs = sum(r.stats.total_prs_analyzed for r in daily_reports)
        high_impact = sum(1 for s in all_signals if s.impact_score >= 4)
        total_commits = sum(
            r.activity.total_commits for r in daily_reports if r.activity
        )
        total_releases = sum(r.stats.total_releases for r in daily_reports)
        weekly_activity = self.aggregate_activity(daily_reports)

        return WeeklyReport(
            week_id=week_id,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            summary_brief=ai_result.summary_brief,
            core_trends=ai_result.core_trends,
            engineering_signals=engineering_signals[:10],
            research_signals=research_signals[:10],
            daily_reports_count=len(daily_reports),
            total_prs_analyzed=total_prs,
            high_impact_signals=high_impact,
            total_commits=total_commits,
            total_releases=total_releases,
            weekly_activity=weekly_activity,
        )

    def aggregate_activity(self, daily_reports: list[DailyReport]) -> WeeklyActivity:
        """聚合周活跃度。"""
        repo_commits: dict[str, int] = {}
        repo_contributors: dict[str, set[str]] = {}

        for report in daily_reports:
            if report.activity and report.activity.top_repos:
                for repo in report.activity.top_repos:
                    if repo.repo not in repo_commits:
                        repo_commits[repo.repo] = 0
                        repo_contributors[repo.repo] = set()
                    repo_commits[repo.repo] += repo.commits
                    for contributor in repo.top_contributors:
                        repo_contributors[repo.repo].add(contributor)

        top_repos = [
            RepoActivity(
                repo=repo_name,
                commits=commits,
                top_contributors=list(repo_contributors[repo_name])[:3],
            )
            for repo_name, commits in sorted(
                repo_commits.items(), key=lambda item: item[1], reverse=True
            )
        ]

        return WeeklyActivity(
            total_commits=sum(repo_commits.values()),
            active_repos_count=len(repo_commits),
            top_repos=top_repos,
        )
