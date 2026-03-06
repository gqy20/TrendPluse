"""工作流兼容导出层。"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

__all__ = [
    "DailyPipelineInputs",
    "DailyReportFinalizer",
    "IssueWorkflowService",
    "ReleaseWorkflowService",
    "ReportOutputService",
    "WeeklyReportWorkflow",
]

if TYPE_CHECKING:
    from trendpluse.models.report_inputs import DailyPipelineInputs
    from trendpluse.workflows.daily_report_finalizer import DailyReportFinalizer
    from trendpluse.workflows.issue_workflow import IssueWorkflowService
    from trendpluse.workflows.release_workflow import ReleaseWorkflowService
    from trendpluse.workflows.report_output import ReportOutputService
    from trendpluse.workflows.weekly_report_workflow import WeeklyReportWorkflow


def __getattr__(name: str) -> Any:
    """按需加载兼容导出，避免包级联导入。"""
    if name == "DailyPipelineInputs":
        from trendpluse.models.report_inputs import DailyPipelineInputs

        return DailyPipelineInputs
    if name == "DailyReportFinalizer":
        from trendpluse.workflows.daily_report_finalizer import DailyReportFinalizer

        return DailyReportFinalizer
    if name == "IssueWorkflowService":
        from trendpluse.workflows.issue_workflow import IssueWorkflowService

        return IssueWorkflowService
    if name == "ReleaseWorkflowService":
        from trendpluse.workflows.release_workflow import ReleaseWorkflowService

        return ReleaseWorkflowService
    if name == "ReportOutputService":
        from trendpluse.workflows.report_output import ReportOutputService

        return ReportOutputService
    if name == "WeeklyReportWorkflow":
        from trendpluse.workflows.weekly_report_workflow import WeeklyReportWorkflow

        return WeeklyReportWorkflow
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
