"""应用编排模块。"""

from trendpluse.app.bootstrap import ReportingComponents, build_reporting_components
from trendpluse.app.daily import DailyPipelineApp
from trendpluse.app.issue_agent import IssueWorkflowCoordinator
from trendpluse.app.release_processor import ReleaseProcessor, ReleaseWorkflowResult
from trendpluse.app.report_finalizer import DailyReportFinalizer
from trendpluse.app.weekly import WeeklyPipelineApp

__all__ = [
    "ReportingComponents",
    "DailyPipelineApp",
    "DailyReportFinalizer",
    "IssueWorkflowCoordinator",
    "ReleaseProcessor",
    "ReleaseWorkflowResult",
    "WeeklyPipelineApp",
    "build_reporting_components",
]
