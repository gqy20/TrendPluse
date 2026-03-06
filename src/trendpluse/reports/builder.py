"""报告构建器。"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleasesData,
    ReportStats,
)

if TYPE_CHECKING:
    from trendpluse.models.report_inputs import DailyPipelineInputs


class DailyReportBuilder:
    """负责补全日报对象并生成统计信息。"""

    def __init__(
        self,
        *,
        settings: Any,
        issue_insights_loader: Callable[[str], Any],
    ) -> None:
        self.settings = settings
        self.issue_insights_loader = issue_insights_loader

    def finalize_daily_report(
        self,
        *,
        report: DailyReport,
        date,
        daily_inputs: DailyPipelineInputs,
        pr_signals: list[Any],
    ) -> DailyReport:
        """填充日报对象。"""
        if not isinstance(report.release_signals, list) or not report.release_signals:
            report.release_signals = daily_inputs.release_signals
        report.commit_signals = []
        report.activity = daily_inputs.activity_data
        report.releases = daily_inputs.releases_data
        report.breaking_changes = (
            daily_inputs.breaking_changes if daily_inputs.breaking_changes else None
        )
        report.monitored_repos = self.settings.github_repos
        report.issue_insights = self.issue_insights_loader(date.strftime("%Y-%m-%d"))
        self.finalize_report_stats(
            report=report,
            pr_signals_count=len(pr_signals),
            commit_signals_count=len(daily_inputs.commit_signals),
            release_signals_count=len(daily_inputs.release_signals),
            total_commits_analyzed=len(daily_inputs.detailed_commits),
            total_releases=daily_inputs.releases_data.total_count,
            total_releases_analyzed=len(daily_inputs.detailed_releases),
            total_breaking_changes=len(daily_inputs.breaking_changes),
        )
        return report

    def generate_empty_report(
        self,
        date,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """生成空报告。"""
        date_str = date.strftime("%Y-%m-%d")
        commit_count = len(commit_signals) if commit_signals else 0
        release_count = releases_data.total_count if releases_data else 0

        if commit_count == 0 and release_count == 0:
            summary_brief = f"今日 ({date_str}) 未发现符合条件的趋势信号。"
        else:
            summary_brief = (
                f"今日 ({date_str}) 发现 {commit_count} 个 Commit 信号，"
                f"{release_count} 个 Release 信号。"
            )

        high_impact_count = 0
        if commit_signals:
            high_impact_count = sum(
                1
                for signal in commit_signals
                if getattr(signal, "impact_score", 0) >= 4
            )

        engineering_signals: list = []
        research_signals: list = []
        if commit_signals:
            for signal in commit_signals:
                if signal.category == "engineering":
                    engineering_signals.append(signal)
                elif signal.category == "research":
                    research_signals.append(signal)

        report = DailyReport(
            date=date_str,
            summary_brief=summary_brief,
            engineering_signals=engineering_signals,
            research_signals=research_signals,
            commit_signals=[],
        )

        if activity_data:
            report.activity = activity_data
        if releases_data:
            report.releases = releases_data

        report.monitored_repos = self.settings.github_repos
        report.issue_insights = self.issue_insights_loader(date.strftime("%Y-%m-%d"))
        self.finalize_report_stats(
            report=report,
            pr_signals_count=0,
            commit_signals_count=commit_count,
            release_signals_count=release_count,
            total_commits_analyzed=activity_data.total_commits if activity_data else 0,
            total_releases=releases_data.total_count if releases_data else 0,
            total_releases_analyzed=releases_data.total_count if releases_data else 0,
            total_breaking_changes=0,
            override_high_impact=high_impact_count,
        )
        return report

    def finalize_report_stats(
        self,
        report: DailyReport,
        *,
        pr_signals_count: int,
        commit_signals_count: int,
        release_signals_count: int,
        total_commits_analyzed: int,
        total_releases: int,
        total_releases_analyzed: int,
        total_breaking_changes: int,
        override_high_impact: int | None = None,
    ) -> None:
        """统一生成日报统计字段。"""
        engineering_signals = (
            report.engineering_signals
            if isinstance(report.engineering_signals, list)
            else []
        )
        research_signals = (
            report.research_signals if isinstance(report.research_signals, list) else []
        )
        commit_signals = (
            report.commit_signals if isinstance(report.commit_signals, list) else []
        )
        release_signals = (
            report.release_signals if isinstance(report.release_signals, list) else []
        )

        all_signals = (
            engineering_signals + research_signals + commit_signals + release_signals
        )
        unique_repos: set[str] = set()
        for signal in all_signals:
            related_repos = getattr(signal, "related_repos", [])
            if not isinstance(related_repos, list):
                continue
            for repo in related_repos:
                if isinstance(repo, str) and repo.strip():
                    unique_repos.add(repo.strip().lower())
        if report.releases:
            for release in report.releases.releases:
                if release.repo:
                    unique_repos.add(release.repo.strip().lower())

        high_impact_count = (
            override_high_impact
            if override_high_impact is not None
            else sum(
                1
                for signal in all_signals
                if isinstance(getattr(signal, "impact_score", 0), int)
                and getattr(signal, "impact_score", 0) >= 4
            )
        )

        report.stats = ReportStats(
            total_signals=pr_signals_count
            + commit_signals_count
            + release_signals_count,
            pr_count=pr_signals_count,
            commit_count=commit_signals_count,
            release_count=release_signals_count,
            unique_repos=len(unique_repos),
            total_prs_analyzed=pr_signals_count,
            total_commits_analyzed=total_commits_analyzed,
            total_releases=total_releases,
            total_releases_analyzed=total_releases_analyzed,
            high_impact_signals=high_impact_count,
            total_breaking_changes=total_breaking_changes,
        )
