"""Daily/Weekly 运行辅助。"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.config import Settings
from trendpluse.models.signal import DailyReport, WeeklyReport


@dataclass(frozen=True)
class DailyRunResult:
    """日报运行结果。"""

    report: DailyReport
    output_path: Path


@dataclass(frozen=True)
class WeeklyRunResult:
    """周报运行结果。"""

    report: WeeklyReport
    output_path: Path


def build_daily_output_path(settings: Settings, date: datetime) -> Path:
    """构建日报输出路径。"""
    return Path(settings.output_dir) / f"report-{date.strftime('%Y-%m-%d')}.md"


def build_weekly_output_path(date: datetime) -> Path:
    """构建周报输出路径。"""
    week_id = WeeklyReport.get_week_id(date)
    return Path("reports/weekly") / f"weekly-{week_id}.md"


async def run_daily_pipeline(
    settings: Settings,
    date: datetime | None = None,
) -> DailyRunResult:
    """运行日报流程并返回结果。"""
    actual_date = date or datetime.now()
    pipeline = TrendPulsePipeline(settings=settings)
    report = await pipeline.run_daily_async(date=actual_date)
    return DailyRunResult(
        report=report,
        output_path=build_daily_output_path(settings, actual_date),
    )


def run_weekly_pipeline(
    settings: Settings,
    date: datetime | None = None,
) -> WeeklyRunResult:
    """运行周报流程并返回结果。"""
    actual_date = date or datetime.now()
    pipeline = TrendPulsePipeline(settings=settings)
    report = pipeline.run_weekly(date=actual_date)
    return WeeklyRunResult(
        report=report,
        output_path=build_weekly_output_path(actual_date),
    )
