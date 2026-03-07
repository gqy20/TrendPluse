"""迁移旧版 Issue Agent 分析文件到新版 signals 结构。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def infer_repo_from_path(path: Path) -> str:
    """根据文件名推断仓库名。"""
    stem = path.stem.removesuffix(".analysis")
    return stem.replace("__", "/")


def infer_snapshot_date(path: Path) -> str:
    """根据目录结构推断快照日期。"""
    analysis_dir = path.parent
    snapshot_dir = analysis_dir.parent
    return snapshot_dir.name


def build_source_issues(
    *,
    repo: str,
    sample_urls: list[str],
) -> list[dict[str, Any]]:
    """根据旧字段构造来源 Issue 列表。"""
    return [
        {
            "repo": repo,
            "issue_number": None,
            "title": "",
            "url": url,
            "labels": [],
            "evidence": None,
        }
        for url in sample_urls
    ]


def migrate_payload(payload: dict[str, Any], path: Path) -> dict[str, Any]:
    """将旧版 top_pain_points 结构迁移为新版 signals 结构。"""
    if "signals" in payload:
        return payload

    repo = infer_repo_from_path(path)
    snapshot_date = infer_snapshot_date(path)
    legacy_points = payload.get("top_pain_points", [])
    signals: list[dict[str, Any]] = []

    for index, item in enumerate(legacy_points, start=1):
        if not isinstance(item, dict):
            continue
        topic = str(item.get("topic", "")).strip()
        if not topic:
            continue

        sample_urls = [
            str(url) for url in item.get("sample_urls", []) if isinstance(url, str)
        ]
        affected_repos = [
            str(value)
            for value in item.get("affected_repos", [])
            if isinstance(value, str)
        ]
        signal = {
            "id": str(item.get("id") or f"{path.stem}-{index}"),
            "repo": str(item.get("repo") or repo),
            "topic": topic,
            "summary": str(item.get("summary") or item.get("review_reason") or topic),
            "category": item.get("category"),
            "count": item.get("count", 1),
            "affected_repos": affected_repos,
            "sample_urls": sample_urls,
            "aliases": [
                str(value)
                for value in item.get("aliases", [])
                if isinstance(value, str)
            ],
            "confidence": item.get("confidence"),
            "priority": item.get("priority"),
            "review_reason": item.get("review_reason"),
            "source_issues": item.get("source_issues")
            or build_source_issues(repo=repo, sample_urls=sample_urls),
            "source_signal_ids": item.get("source_signal_ids") or [],
        }
        signals.append(signal)

    return {
        "repo": repo,
        "snapshot_date": snapshot_date,
        "signals": signals,
        "expected_issue_count": payload.get("expected_issue_count", 0),
        "analyzed_issue_count": payload.get("analyzed_issue_count", len(signals)),
        "quality_score": payload.get("quality_score", 0.0),
        "quality_status": payload.get("quality_status", "poor"),
        "errors": payload.get("errors") or payload.get("failed_samples") or [],
    }


def migrate_file(path: Path, *, dry_run: bool) -> bool:
    """迁移单个文件。"""
    raw = json.loads(path.read_text(encoding="utf-8"))
    migrated = migrate_payload(raw, path)
    changed = migrated != raw
    if changed and not dry_run:
        path.write_text(
            json.dumps(migrated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return bool(changed)


def iter_analysis_files(target: Path) -> list[Path]:
    """遍历待迁移的分析文件。"""
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.analysis.json"))


def main() -> None:
    """命令入口。"""
    parser = argparse.ArgumentParser(description="迁移旧版 Issue Agent 分析文件")
    parser.add_argument(
        "target",
        nargs="?",
        default="data/issues",
        help="待迁移的文件或目录（默认: data/issues）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅显示会变更的文件，不写回",
    )
    args = parser.parse_args()

    target = Path(args.target)
    files = iter_analysis_files(target)
    changed_files: list[Path] = []

    for path in files:
        try:
            if migrate_file(path, dry_run=args.dry_run):
                changed_files.append(path)
        except Exception as exc:
            print(f"[ERROR] {path}: {exc}")

    mode = "DRY-RUN" if args.dry_run else "APPLY"
    print(f"[{mode}] scanned={len(files)} changed={len(changed_files)}")
    for path in changed_files:
        print(path)


if __name__ == "__main__":
    main()
