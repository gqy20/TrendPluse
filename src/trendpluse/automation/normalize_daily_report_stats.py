"""归一化每日报告 JSON 的 stats 字段。

将历史 reports/daily/report-*.json 中不稳定的 stats key
统一为固定口径，便于跨天可比分析。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REQUIRED_KEYS = [
    "total_signals",
    "pr_count",
    "commit_count",
    "release_count",
    "unique_repos",
    "total_prs_analyzed",
    "total_commits_analyzed",
    "total_releases",
    "total_releases_analyzed",
    "high_impact_signals",
    "total_breaking_changes",
]


def as_int(value: Any, default: int = 0) -> int:
    """将值转换为 int，失败时返回默认值。"""
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def compute_high_impact(report: dict[str, Any]) -> int:
    """计算高影响信号数量（impact_score >= 4）。"""
    total = 0
    for section in (
        "engineering_signals",
        "research_signals",
        "commit_signals",
        "release_signals",
    ):
        signals = report.get(section) or []
        if not isinstance(signals, list):
            continue
        for signal in signals:
            if not isinstance(signal, dict):
                continue
            if as_int(signal.get("impact_score"), 0) >= 4:
                total += 1
    return total


def compute_unique_repos(report: dict[str, Any]) -> int:
    """计算去重后仓库数（统一小写）。"""
    repos: set[str] = set()
    for section in (
        "engineering_signals",
        "research_signals",
        "commit_signals",
        "release_signals",
    ):
        signals = report.get(section) or []
        if not isinstance(signals, list):
            continue
        for signal in signals:
            if not isinstance(signal, dict):
                continue
            related = signal.get("related_repos") or []
            if not isinstance(related, list):
                continue
            for repo in related:
                if isinstance(repo, str) and repo.strip():
                    repos.add(repo.strip().lower())

    releases = (report.get("releases") or {}).get("releases") or []
    if isinstance(releases, list):
        for rel in releases:
            if not isinstance(rel, dict):
                continue
            repo = rel.get("repo")
            if isinstance(repo, str) and repo.strip():
                repos.add(repo.strip().lower())

    return len(repos)


def normalize_stats(report: dict[str, Any]) -> dict[str, int]:
    """按固定口径构建 stats。"""
    stats = report.get("stats") or {}
    if not isinstance(stats, dict):
        stats = {}

    pr_count = as_int(stats.get("pr_count"), as_int(stats.get("total_pr_signals"), 0))
    if pr_count == 0:
        pr_count = as_int(stats.get("total_prs_analyzed"), 0)

    commit_count = as_int(
        stats.get("commit_count"),
        as_int(stats.get("total_commit_signals"), 0),
    )
    if commit_count == 0:
        commit_count = as_int(stats.get("commit_signals_count"), 0)
    if commit_count == 0:
        commit_count = len(report.get("commit_signals") or [])

    release_count = as_int(
        stats.get("release_count"),
        as_int(stats.get("total_release_signals"), 0),
    )
    if release_count == 0:
        release_count = as_int(stats.get("release_signals_count"), 0)
    if release_count == 0:
        release_count = len(report.get("release_signals") or [])

    total_releases = as_int(stats.get("total_releases"), 0)
    if total_releases == 0:
        total_releases = as_int((report.get("releases") or {}).get("total_count"), 0)

    total_releases_analyzed = as_int(stats.get("total_releases_analyzed"), 0)
    if total_releases_analyzed == 0:
        total_releases_analyzed = total_releases

    total_commits_analyzed = as_int(stats.get("total_commits_analyzed"), 0)
    if total_commits_analyzed == 0:
        total_commits_analyzed = as_int(
            (report.get("activity") or {}).get("total_commits"),
            0,
        )

    high_impact = as_int(stats.get("high_impact_signals"), 0)
    if high_impact == 0:
        high_impact = compute_high_impact(report)

    total_breaking_changes = as_int(stats.get("total_breaking_changes"), 0)
    if total_breaking_changes == 0:
        bc = report.get("breaking_changes") or []
        if isinstance(bc, list):
            total_breaking_changes = len(bc)

    unique_repos = as_int(stats.get("unique_repos"), 0)
    if unique_repos == 0:
        unique_repos = compute_unique_repos(report)

    total_signals = as_int(stats.get("total_signals"), 0)
    if total_signals == 0:
        total_signals = pr_count + commit_count + release_count

    normalized = {
        "total_signals": total_signals,
        "pr_count": pr_count,
        "commit_count": commit_count,
        "release_count": release_count,
        "unique_repos": unique_repos,
        "total_prs_analyzed": as_int(stats.get("total_prs_analyzed"), pr_count),
        "total_commits_analyzed": total_commits_analyzed,
        "total_releases": total_releases,
        "total_releases_analyzed": total_releases_analyzed,
        "high_impact_signals": high_impact,
        "total_breaking_changes": total_breaking_changes,
    }
    return normalized


def normalize_file(path: Path, apply: bool) -> tuple[bool, dict[str, int] | None]:
    """归一化单个文件。"""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return False, None

    original_stats = raw.get("stats") or {}
    normalized = normalize_stats(raw)
    changed = original_stats != normalized
    if changed and apply:
        raw["stats"] = normalized
        path.write_text(
            json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return changed, normalized


def run_normalize_daily_report_stats(
    reports_dir: str = "reports/daily", *, apply: bool = False
) -> None:
    """执行日报 stats 归一化。"""
    report_dir = Path(reports_dir)
    files = sorted(report_dir.glob("report-*.json"))
    if not files:
        print(f"未找到文件: {report_dir}")
        return

    changed_count = 0
    sample: list[str] = []
    for path in files:
        changed, normalized = normalize_file(path, apply=apply)
        if changed:
            changed_count += 1
            if len(sample) < 5 and normalized:
                sample.append(
                    f"{path.name}: total={normalized['total_signals']}, "
                    f"pr={normalized['pr_count']}, "
                    f"commit={normalized['commit_count']}, "
                    f"release={normalized['release_count']}"
                )

    mode = "已修复" if apply else "可修复"
    print(f"{mode}: {changed_count}/{len(files)}")
    for line in sample:
        print(f"- {line}")
    if not apply:
        print("提示: 添加 --apply 执行写入")
