"""报告输出服务测试。"""

from datetime import datetime

from trendpluse.models.signal import DailyReport, WeeklyReport
from trendpluse.reports.publisher import ReportPublisher


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
    service = ReportPublisher(
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


def test_save_daily_report_json_ends_with_newline(tmp_path) -> None:
    """JSON 落盘应带末尾换行，与入库文件及 end-of-file-fixer 保持一致。

    回归背景：以前不写末尾换行，重写已跟踪的 report-*.json 时会产生
    仅差一个换行符的脏 diff。
    """
    service = ReportPublisher(
        reporter=DummyReporter(),
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = DailyReport(date="2026-03-06", summary_brief="test")

    service.save_daily(report, datetime(2026, 3, 6))

    raw = (tmp_path / "daily" / "report-2026-03-06.json").read_text(encoding="utf-8")
    assert raw.endswith("}\n")
    assert not raw.endswith("\n\n")


def test_save_weekly_report_json_ends_with_newline(tmp_path) -> None:
    """周报 JSON 同样应带末尾换行。"""
    service = ReportPublisher(
        reporter=DummyReporter(),
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = WeeklyReport(
        week_id="2026-W10",
        start_date="2026-03-02",
        end_date="2026-03-08",
        summary_brief="test",
    )

    service.save_weekly(report, datetime(2026, 3, 8))

    weekly_files = list((tmp_path / "weekly").glob("weekly-*.json"))
    assert len(weekly_files) == 1
    raw = weekly_files[0].read_text(encoding="utf-8")
    assert raw.endswith("}\n")


def test_notify_daily_report_is_delegated() -> None:
    """测试日报通知委托给 notifier。"""
    notifier = DummyNotifier()
    service = ReportPublisher(
        reporter=DummyReporter(),
        daily_output_dir="reports/daily",
        weekly_output_dir="reports/weekly",
        notifier=notifier,
    )
    report = DailyReport(date="2026-03-06", summary_brief="test")

    service.notify_daily(report)

    assert notifier.reports == [report]


def test_save_weekly_report_uses_configured_output_dir(tmp_path) -> None:
    """测试周报输出使用配置目录。"""
    reporter = DummyReporter()
    service = ReportPublisher(
        reporter=reporter,
        daily_output_dir=str(tmp_path / "daily"),
        weekly_output_dir=str(tmp_path / "weekly"),
    )
    report = WeeklyReport(
        week_id="2026-W10",
        start_date="2026-03-02",
        end_date="2026-03-08",
        summary_brief="test",
    )

    service.save_weekly(report, datetime(2026, 3, 8))

    assert reporter.weekly_calls[0][1].endswith("weekly/weekly-2026-W10.md")
    json_path = tmp_path / "weekly" / "weekly-2026-W10.json"
    assert json_path.exists()
    assert "2026-W10" in json_path.read_text(encoding="utf-8")
