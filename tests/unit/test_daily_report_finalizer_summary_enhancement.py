"""日报总结增强测试。"""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

from trendpluse.app.report_finalizer import DailyReportFinalizer
from trendpluse.models.signal import DailyReport, ReportStats


class _FakeSummaryEnhancer:
    def __init__(self) -> None:
        self.calls: list[tuple[DailyReport, datetime]] = []

    def enhance(self, *, report: DailyReport, date: datetime) -> None:
        self.calls.append((report, date))
        report.summary_brief = "今天的趋势相对历史出现了新的推进。"
        report.trend_status = "continuing"
        report.historical_basis_dates = ["2026-03-10", "2026-03-11"]


class _FakePublisher:
    def __init__(self) -> None:
        self.saved_reports: list[DailyReport] = []
        self.notified_reports: list[DailyReport] = []

    def save_daily(self, report: DailyReport, date: datetime) -> str:
        self.saved_reports.append(report.model_copy(deep=True))
        return "reports/daily/report-2026-03-12.md"

    def notify_daily(self, report: DailyReport) -> None:
        self.notified_reports.append(report.model_copy(deep=True))


def test_daily_report_finalizer_applies_summary_enhancer_before_publish() -> None:
    """finalizer 应在保存前应用日报总结增强结果。"""
    enhancer = _FakeSummaryEnhancer()
    publisher = _FakePublisher()
    builder = SimpleNamespace(
        finalize_daily_report=lambda **_: None,
        generate_empty_report=lambda **_: None,
        finalize_report_stats=lambda **_: None,
    )
    finalizer = DailyReportFinalizer(
        builder=builder,
        publisher=publisher,
        summary_enhancer=enhancer,
    )
    report = DailyReport(
        date="2026-03-12",
        summary_brief="旧摘要",
        engineering_signals=[],
        research_signals=[],
        commit_signals=[],
        release_signals=[],
        stats=ReportStats(),
    )

    finalizer.finalize_daily_report(
        report=report,
        date=datetime(2026, 3, 12),
        daily_inputs=SimpleNamespace(
            activity_data=None,
            releases_data=None,
            breaking_changes=[],
            commit_signals=[],
            release_signals=[],
            detailed_commits=[],
            detailed_releases=[],
        ),
        pr_signals=[],
    )

    assert enhancer.calls
    assert report.summary_brief == "今天的趋势相对历史出现了新的推进。"
    assert report.trend_status == "continuing"
    assert report.historical_basis_dates == ["2026-03-10", "2026-03-11"]
    assert (
        publisher.saved_reports[0].summary_brief == "今天的趋势相对历史出现了新的推进。"
    )
