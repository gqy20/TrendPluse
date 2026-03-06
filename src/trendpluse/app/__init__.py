"""应用编排模块。"""

from trendpluse.app.bootstrap import (
    AnalyzerComponents,
    AppComponents,
    CollectorComponents,
    ReportingComponents,
    build_analyzer_components,
    build_app_components,
    build_collector_components,
    build_reporting_components,
)
from trendpluse.app.daily import DailyPipelineApp
from trendpluse.app.discovery import discover, load_monitored_repos
from trendpluse.app.issue_agent import IssueWorkflowCoordinator
from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.app.release_processor import ReleaseProcessor, ReleaseWorkflowResult
from trendpluse.app.report_finalizer import DailyReportFinalizer
from trendpluse.app.runtime import (
    DailyRunResult,
    WeeklyRunResult,
    run_daily_pipeline,
    run_weekly_pipeline,
)
from trendpluse.app.weekly import WeeklyPipelineApp

__all__ = [
    "ReportingComponents",
    "CollectorComponents",
    "AnalyzerComponents",
    "AppComponents",
    "discover",
    "DailyPipelineApp",
    "DailyRunResult",
    "DailyReportFinalizer",
    "IssueWorkflowCoordinator",
    "load_monitored_repos",
    "TrendPulsePipeline",
    "ReleaseProcessor",
    "ReleaseWorkflowResult",
    "run_daily_pipeline",
    "run_weekly_pipeline",
    "WeeklyRunResult",
    "WeeklyPipelineApp",
    "build_analyzer_components",
    "build_app_components",
    "build_collector_components",
    "build_reporting_components",
]
