"""报告发布器测试。"""

from __future__ import annotations

from datetime import datetime

from trendpluse.models.signal import DailyReport
from trendpluse.reports.publisher import ReportPublisher


def test_report_publisher_writes_daily_json(tmp_path) -> None:
    """发布器应写出日报 JSON(唯一格式)。"""
    publisher = ReportPublisher(
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = DailyReport(date="2026-03-06", summary_brief="summary")

    output_path = publisher.save_daily(report, datetime(2026, 3, 6))

    assert output_path.endswith("daily/report-2026-03-06.json")
    assert (tmp_path / "daily" / "report-2026-03-06.json").exists()
