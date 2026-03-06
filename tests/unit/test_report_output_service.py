"""报告输出服务测试。"""

from datetime import datetime

from trendpluse.models.signal import DailyReport, WeeklyReport
from trendpluse.workflows.report_output import ReportOutputService


class DummyReporter:
    """测试用 Reporter。"""

    def __init__(self) -> None:
        self.daily_calls: list[tuple[DailyReport, str]] = []
        self.weekly_calls: list[tuple[WeeklyReport, str]] = []

    def save_report(self, report: DailyReport, output_path: str) -> None:
        self.daily_calls.append((report, output_path))

    def save_weekly_report(self, report: WeeklyReport, output_path: str) -> None:
        self.weekly_calls.append((report, output_path))


class DummyNotifier:
    """测试用 Notifier。"""

    def __init__(self) -> None:
        self.reports: list[DailyReport] = []

    def send_report(self, report: DailyReport) -> None:
        self.reports.append(report)


def test_save_daily_report_uses_configured_output_dir(tmp_path) -> None:
    """测试日报输出使用配置目录。"""
    reporter = DummyReporter()
    service = ReportOutputService(
        reporter=reporter,
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = DailyReport(date="2026-03-06", summary_brief="test")

    service.save_daily(report, datetime(2026, 3, 6))

    assert reporter.daily_calls[0][1].endswith("daily/report-2026-03-06.md")
    json_path = tmp_path / "daily" / "report-2026-03-06.json"
    assert json_path.exists()
    assert "2026-03-06" in json_path.read_text(encoding="utf-8")


def test_notify_daily_report_is_delegated() -> None:
    """测试日报通知委托给 notifier。"""
    notifier = DummyNotifier()
    service = ReportOutputService(
        reporter=DummyReporter(),
        daily_output_dir="reports/daily",
        weekly_output_dir="reports/weekly",
        notifier=notifier,
    )
    report = DailyReport(date="2026-03-06", summary_brief="test")

    service.notify_daily(report)

    assert notifier.reports == [report]
