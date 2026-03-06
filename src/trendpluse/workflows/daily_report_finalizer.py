"""日报收尾兼容层。"""

from __future__ import annotations

from trendpluse.app.report_finalizer import (
    DailyReportFinalizer as AppDailyReportFinalizer,
)
from trendpluse.reports.builder import DailyReportBuilder


class DailyReportFinalizer(AppDailyReportFinalizer):
    """兼容旧命名的日报收尾器。"""

    def __init__(self, *, settings, issue_workflow, output_service) -> None:
        builder = DailyReportBuilder(
            settings=settings,
            issue_insights_loader=issue_workflow.load_insights,
        )
        super().__init__(builder=builder, publisher=output_service)
