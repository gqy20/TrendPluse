"""报告发布器测试。"""

from __future__ import annotations

from datetime import datetime

from trendpluse.models.signal import DailyReport
from trendpluse.reports.publisher import ReportPublisher


class _DummyReporter:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []

    def save_report(self, report: DailyReport, output_path: str) -> None:
        self.calls.append((report.date, output_path))

    def save_weekly_report(self, report, output_path: str) -> None:
        self.calls.append((report.week_id, output_path))


def test_report_publisher_writes_daily_json(tmp_path) -> None:
    """发布器应写出日报 Markdown 路径与 JSON。"""
    reporter = _DummyReporter()
    publisher = ReportPublisher(
        reporter=reporter,
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = DailyReport(date="2026-03-06", summary_brief="summary")

    output_path = publisher.save_daily(report, datetime(2026, 3, 6))

    assert output_path.endswith("daily/report-2026-03-06.md")
    assert reporter.calls == [("2026-03-06", output_path)]
    assert (tmp_path / "daily" / "report-2026-03-06.json").exists()
