"""日报总结增强测试。"""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

import pytest

from trendpluse.app.report_finalizer import DailyReportFinalizer
from trendpluse.models.agent_usage import AgentMetricsSummary, AgentRunMetrics
from trendpluse.models.issue_agent import IssueAgentReport
from trendpluse.models.signal import DailyReport, ReportStats


class _FakeSummaryEnhancer:
    def __init__(self) -> None:
        self.calls: list[tuple[DailyReport, datetime]] = []

    def enhance(self, *, report: DailyReport, date: datetime) -> None:
        self.calls.append((report, date))
        report.summary_brief = "今天的趋势相对历史出现了新的推进。"
        report.trend_status = "continuing"
        report.historical_basis_dates = ["2026-03-10", "2026-03-11"]

    def get_last_run_metrics(self) -> AgentRunMetrics:
        return AgentRunMetrics(
            model="sonnet",
            session_id="summary-sync",
            num_turns=2,
            duration_ms=800,
            duration_api_ms=600,
            total_cost_usd=0.11,
            usage={"total_tokens": 80},
            raw_usage={"total_tokens": 80},
        )


class _FakeAsyncSummaryEnhancer:
    def __init__(self) -> None:
        self.calls: list[tuple[DailyReport, datetime]] = []

    async def enhance_async(self, *, report: DailyReport, date: datetime) -> None:
        self.calls.append((report, date))
        report.summary_brief = "异步增强后的总结。"
        report.trend_status = "continuing"
        report.historical_basis_dates = ["2026-03-12"]

    def get_last_run_metrics(self) -> AgentRunMetrics:
        return AgentRunMetrics(
            model="sonnet",
            session_id="summary-async",
            num_turns=1,
            duration_ms=500,
            duration_api_ms=400,
            total_cost_usd=0.07,
            usage={"total_tokens": 40},
            raw_usage={"total_tokens": 40},
        )


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
    assert report.daily_summary_agent_run_metrics is not None
    assert report.daily_summary_agent_run_metrics.usage.total_tokens == 80
    assert report.agent_metrics_summary is not None
    assert report.agent_metrics_summary.total_cost_usd == 0.11
    assert (
        publisher.saved_reports[0].summary_brief == "今天的趋势相对历史出现了新的推进。"
    )


@pytest.mark.asyncio
async def test_daily_report_finalizer_async_applies_enhancer() -> None:
    """异步 finalizer 应在 running loop 中完成摘要增强并保存结果。"""
    enhancer = _FakeAsyncSummaryEnhancer()
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

    await finalizer.finalize_daily_report_async(
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
    assert report.summary_brief == "异步增强后的总结。"
    assert publisher.saved_reports[0].summary_brief == "异步增强后的总结。"


def test_daily_report_finalizer_merges_issue_and_summary_agent_metrics() -> None:
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
        issue_insights=IssueAgentReport(
            agent_metrics_summary=AgentMetricsSummary(
                run_count=2,
                models=["sonnet"],
                total_turns=4,
                total_duration_ms=1500,
                total_api_duration_ms=1200,
                total_cost_usd=0.33,
                usage={"total_tokens": 220, "tool_uses": 2, "duration_ms": 1500},
            )
        ),
    )

    finalizer._enhance_summary(report=report, date=datetime(2026, 3, 12))
    finalizer._refresh_agent_metrics(report)

    assert report.agent_metrics_summary is not None
    assert report.agent_metrics_summary.run_count == 3
    assert report.agent_metrics_summary.total_cost_usd == 0.44
    assert report.agent_metrics_summary.usage.total_tokens == 300
