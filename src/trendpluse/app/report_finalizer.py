"""日报收尾编排。"""

from __future__ import annotations

from typing import Any, cast

from trendpluse.models.report_inputs import DailyPipelineInputs
from trendpluse.models.signal import ActivityData, DailyReport, ReleasesData


class DailyReportFinalizer:
    """负责日报对象补全、保存与通知。"""

    def __init__(self, *, builder, publisher, summary_enhancer=None) -> None:
        self.builder = builder
        self.publisher = publisher
        self.summary_enhancer = summary_enhancer

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
        self._enhance_summary(report=report, date=date)
        self.publisher.save_daily(report, date)
        self._refresh_history_index()
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
        self._enhance_summary(report=report, date=date)
        self.publisher.save_daily(report, date)
        self._refresh_history_index()
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

    def _enhance_summary(self, *, report, date) -> None:
        """在保存前尝试增强日报总结。"""
        if self.summary_enhancer is None:
            return
        try:
            self.summary_enhancer.enhance(report=report, date=date)
        except Exception as exc:  # pragma: no cover - 防御性日志
            from trendpluse.logger import get_logger

            get_logger(__name__).warning("日报总结增强失败，回退原摘要: %s", exc)

    def _refresh_history_index(self) -> None:
        """在日报保存后更新历史索引。"""
        if self.summary_enhancer is None:
            return
        refresh = getattr(self.summary_enhancer, "refresh_history_index", None)
        if refresh is None:
            return
        try:
            refresh()
        except Exception:  # pragma: no cover - 防御性日志
            pass
