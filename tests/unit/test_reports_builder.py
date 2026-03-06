"""报告构建器测试。"""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

from trendpluse.models.signal import ActivityData, ReleasesData, Signal
from trendpluse.reports.builder import DailyReportBuilder


def _build_builder():
    settings = SimpleNamespace(github_repos=["owner/repo"])
    return DailyReportBuilder(
        settings=settings,
        issue_insights_loader=lambda _date: {"quality_status": "ok"},
    )


def test_generate_empty_report_uses_dynamic_summary() -> None:
    """空报告摘要应根据 commit/release 数动态生成。"""
    builder = _build_builder()
    commit_signals = [
        Signal(
            id="commit-1",
            title="commit",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="important",
            sources=["https://example.com/commit-1"],
            related_repos=["owner/repo"],
        )
    ]
    releases = ReleasesData(total_count=2, unique_repos_count=1, releases=[])

    report = builder.generate_empty_report(
        date=datetime(2026, 3, 6),
        activity_data=ActivityData(total_commits=3, active_repos_count=1, top_repos=[]),
        commit_signals=commit_signals,
        releases_data=releases,
    )

    assert (
        report.summary_brief
        == "今日 (2026-03-06) 发现 1 个 Commit 信号，2 个 Release 信号。"
    )
    assert report.monitored_repos == ["owner/repo"]
    assert report.issue_insights == {"quality_status": "ok"}
    assert report.stats.commit_count == 1
    assert report.stats.release_count == 2
    assert report.stats.high_impact_signals == 1
