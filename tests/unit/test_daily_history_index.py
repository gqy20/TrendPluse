"""历史日报索引测试。"""

from __future__ import annotations

import json
from pathlib import Path

from trendpluse.history.daily_report_history import (
    DailyHistoryIndexBuilder,
    load_daily_history_index,
)


def _write_daily_report(
    reports_dir: Path,
    *,
    date: str,
    summary_brief: str,
    engineering_titles: list[str],
    issue_summary: str | None = None,
) -> None:
    report = {
        "date": date,
        "summary_brief": summary_brief,
        "engineering_signals": [
            {
                "id": f"eng-{idx}",
                "title": title,
                "type": "capability",
                "category": "engineering",
                "impact_score": 4,
                "why_it_matters": "important",
                "sources": [f"https://example.com/{date}/{idx}"],
                "related_repos": ["owner/repo"],
            }
            for idx, title in enumerate(engineering_titles)
        ],
        "research_signals": [],
        "commit_signals": [],
        "release_signals": [],
        "stats": {
            "total_signals": len(engineering_titles),
            "pr_count": len(engineering_titles),
            "commit_count": 0,
            "release_count": 0,
            "unique_repos": 1,
            "total_prs_analyzed": len(engineering_titles),
            "total_commits_analyzed": 0,
            "total_releases": 0,
            "total_releases_analyzed": 0,
            "high_impact_signals": len(engineering_titles),
            "total_breaking_changes": 0,
        },
        "activity": {
            "total_commits": 3,
            "active_repos_count": 1,
            "top_repos": [
                {
                    "repo": "owner/repo",
                    "commits": 3,
                    "top_contributors": ["alice"],
                }
            ],
        },
        "releases": {
            "total_count": 0,
            "unique_repos_count": 0,
            "releases": [],
        },
        "issue_insights": (
            None
            if issue_summary is None
            else {
                "summary_brief": issue_summary,
                "top_pain_points": [],
                "repo_reports": [],
                "quality_status": "ok",
                "expected_files": 1,
                "parsed_files": 1,
                "failed_files": 0,
                "failed_samples": [],
            }
        ),
    }
    path = reports_dir / f"report-{date}.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def test_daily_history_index_builder_collects_reports_in_date_order(
    tmp_path: Path,
) -> None:
    """索引应从全量日报提取轻量摘要，并按日期排序。"""
    reports_dir = tmp_path / "reports" / "daily"
    reports_dir.mkdir(parents=True)
    index_path = tmp_path / "data" / "history" / "daily-report-index.json"

    _write_daily_report(
        reports_dir,
        date="2026-03-11",
        summary_brief="11 日摘要",
        engineering_titles=["流式工具调用"],
    )
    _write_daily_report(
        reports_dir,
        date="2026-03-13",
        summary_brief="13 日摘要",
        engineering_titles=["多 Agent 编排", "会话压缩"],
        issue_summary="Issue 主要集中在会话恢复失败",
    )

    builder = DailyHistoryIndexBuilder(reports_dir=reports_dir, index_path=index_path)

    result = builder.build()

    assert result.total_reports == 2
    assert [entry.date for entry in result.entries] == ["2026-03-11", "2026-03-13"]
    assert result.entries[1].engineering_titles == ["多 Agent 编排", "会话压缩"]
    assert result.entries[1].issue_summary_brief == "Issue 主要集中在会话恢复失败"
    assert index_path.exists()

    loaded = load_daily_history_index(index_path)
    assert loaded.total_reports == 2
    assert loaded.entries[0].summary_brief == "11 日摘要"
