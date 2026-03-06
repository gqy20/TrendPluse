"""周报工作流。"""

from __future__ import annotations

from trendpluse.analyzers.weekly_aggregator import WeeklyAggregator  # noqa: F401
from trendpluse.app.weekly import WeeklyPipelineApp


class WeeklyReportWorkflow(WeeklyPipelineApp):
    """负责周报加载、聚合与输出。"""
