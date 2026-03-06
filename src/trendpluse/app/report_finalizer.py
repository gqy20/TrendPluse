"""日报收尾编排。"""

from __future__ import annotations

from typing import Any, cast

from trendpluse.models.report_inputs import DailyPipelineInputs
from trendpluse.models.signal import ActivityData, DailyReport, ReleasesData


class DailyReportFinalizer:
    """负责日报对象补全、保存与通知。"""

    def __init__(self, *, builder, publisher) -> None:
        self.builder = builder
        self.publisher = publisher

    def finalize_daily_report(
        self,
        *,
        report: DailyReport,
        date,
        daily_inputs: DailyPipelineInputs,
        pr_signals: list[Any],
    ) -> None:
        """填充日报对象并保存发送。"""
        self.builder.finalize_daily_report(
            report=report,
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        self.publisher.save_daily(report, date)
        self.publisher.notify_daily(report)

    def generate_empty_report(
        self,
        date,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """生成空报告。"""
        return cast(
            DailyReport,
            self.builder.generate_empty_report(
                date=date,
                activity_data=activity_data,
                commit_signals=commit_signals,
                releases_data=releases_data,
            ),
        )

    def handle_empty_report(
        self,
        date,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """保存并发送空报告。"""
        report = self.generate_empty_report(
            date=date,
            activity_data=activity_data,
            commit_signals=commit_signals,
            releases_data=releases_data,
        )
        self.publisher.save_daily(report, date)
        self.publisher.notify_daily(report)
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
        """兼容旧接口的统计委托。"""
        self.builder.finalize_report_stats(
            report=report,
            pr_signals_count=pr_signals_count,
            commit_signals_count=commit_signals_count,
            release_signals_count=release_signals_count,
            total_commits_analyzed=total_commits_analyzed,
            total_releases=total_releases,
            total_releases_analyzed=total_releases_analyzed,
            total_breaking_changes=total_breaking_changes,
            override_high_impact=override_high_impact,
        )
