"""运行辅助测试。"""

from __future__ import annotations

import asyncio
from datetime import datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

from trendpluse.app.runtime import (
    build_daily_output_path,
    build_weekly_output_path,
    build_weekly_output_path_from_week_id,
    run_daily_pipeline,
    run_weekly_pipeline,
)


def test_build_daily_output_path_uses_settings_output_dir() -> None:
    """日报输出路径应跟随 settings.output_dir。"""
    settings = SimpleNamespace(output_dir="reports/daily")

    output_path = build_daily_output_path(settings, datetime(2026, 3, 6))

    assert str(output_path) == "reports/daily/report-2026-03-06.md"


def test_build_weekly_output_path_uses_week_id() -> None:
    """周报输出路径应写入 weekly 目录。"""
    output_path = build_weekly_output_path(datetime(2026, 3, 8))

    assert str(output_path) == "reports/weekly/weekly-2026-W10.md"


def test_build_weekly_output_path_from_week_id_uses_report_week_id() -> None:
    """周报输出路径可直接根据周标识生成。"""
    output_path = build_weekly_output_path_from_week_id("2026-W09")

    assert str(output_path) == "reports/weekly/weekly-2026-W09.md"


@patch("trendpluse.app.runtime.TrendPulsePipeline")
def test_run_daily_pipeline_returns_report_and_output_path(
    mock_pipeline_cls: Mock,
) -> None:
    """日报运行辅助应返回报告和输出路径。"""
    settings = SimpleNamespace(output_dir="reports/daily")
    report = SimpleNamespace()
    pipeline = mock_pipeline_cls.return_value
    pipeline.run_daily_async = AsyncMock(return_value=report)

    result = asyncio.run(run_daily_pipeline(settings, datetime(2026, 3, 6)))

    pipeline.run_daily_async.assert_awaited_once()
    assert result.report is report
    assert str(result.output_path) == "reports/daily/report-2026-03-06.md"


@patch("trendpluse.app.runtime.TrendPulsePipeline")
def test_run_weekly_pipeline_returns_report_and_output_path(
    mock_pipeline_cls: Mock,
) -> None:
    """周报运行辅助应返回报告和输出路径。"""
    settings = SimpleNamespace(output_dir="reports/daily")
    report = SimpleNamespace(week_id="2026-W10")
    pipeline = mock_pipeline_cls.return_value
    pipeline.run_weekly.return_value = report

    result = run_weekly_pipeline(settings, datetime(2026, 3, 8))

    pipeline.run_weekly.assert_called_once()
    assert result.report is report
    assert str(result.output_path) == "reports/weekly/weekly-2026-W10.md"
