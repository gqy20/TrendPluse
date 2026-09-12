"""日报收尾编排。"""

from __future__ import annotations

from typing import Any, cast

from trendpluse.models.agent_usage import AgentMetricsSummary
from trendpluse.models.report_inputs import DailyPipelineInputs
from trendpluse.models.signal import ActivityData, DailyReport, ReleasesData


class DailyReportFinalizer:
    """负责日报对象补全、保存与通知。"""

    def __init__(self, *, builder, publisher, summary_enhancer=None) -> None:
        self.builder = builder
        self.publisher = publisher
        self.summary_enhancer = summary_enhancer

    async def finalize_daily_report_async(
        self,
        *,
        report: DailyReport,
        date,
        daily_inputs: DailyPipelineInputs,
        pr_signals: list[Any],
    ) -> None:
        """异步填充日报对象并保存发送。"""
        self.builder.finalize_daily_report(
            report=report,
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        await self._enhance_summary_async(report=report, date=date)
        self._refresh_agent_metrics(report)
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

    async def handle_empty_report_async(
        self,
        date,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """异步保存并发送空报告。"""
        report = self.generate_empty_report(
            date=date,
            activity_data=activity_data,
            commit_signals=commit_signals,
            releases_data=releases_data,
        )
        await self._enhance_summary_async(report=report, date=date)
        self._refresh_agent_metrics(report)
        self.publisher.save_daily(report, date)
        self._refresh_history_index()
        self.publisher.notify_daily(report)
        return report

    async def _enhance_summary_async(self, *, report, date) -> None:
        """在异步流程中保存前尝试增强日报总结。"""
        if self.summary_enhancer is None:
            return

        enhance_async = getattr(self.summary_enhancer, "enhance_async", None)
        try:
            if callable(enhance_async):
                await enhance_async(report=report, date=date)
            else:
                self.summary_enhancer.enhance(report=report, date=date)
            getter = getattr(self.summary_enhancer, "get_last_run_metrics", None)
            if callable(getter):
                report.daily_summary_agent_run_metrics = getter()
        except Exception as exc:  # pragma: no cover - 防御性日志
            from trendpluse.logger import get_logger

            get_logger(__name__).warning(
                "日报总结增强失败，回退原摘要: %s: %s",
                type(exc).__name__,
                exc,
            )

    @staticmethod
    def _refresh_agent_metrics(report: DailyReport) -> None:
        """刷新日报级 Agent usage 聚合统计（含全流程 LLM 消耗）。"""
        issue_summary = (
            report.issue_insights.agent_metrics_summary
            if report.issue_insights is not None
            else None
        )
        report.agent_metrics_summary = AgentMetricsSummary.combine(
            runs=[report.daily_summary_agent_run_metrics],
            summaries=[issue_summary, report.daily_llm_usage],
        )

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
