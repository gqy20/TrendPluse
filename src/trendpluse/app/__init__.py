"""应用编排模块。"""

from trendpluse.app.discovery import discover, load_monitored_repos
from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.app.runtime import (
    DailyRunResult,
    WeeklyRunResult,
    run_daily_pipeline,
    run_weekly_pipeline,
)

__all__ = [
    "discover",
    "DailyRunResult",
    "load_monitored_repos",
    "TrendPulsePipeline",
    "run_daily_pipeline",
    "run_weekly_pipeline",
    "WeeklyRunResult",
]
