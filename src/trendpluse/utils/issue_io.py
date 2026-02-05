"""Issue 文件读写工具"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from trendpluse.models.issue import IssueInfo


def _safe_repo_filename(repo: str) -> str:
    return repo.replace("/", "__")


def dump_issues_to_jsonl(
    issues: list[IssueInfo],
    base_dir: str,
    snapshot_date: str,
) -> dict[str, Path]:
    """将 issues 按仓库落盘为 JSONL 文件。

    返回 {repo: file_path} 映射。
    """
    if not issues:
        return {}

    base_path = Path(base_dir) / snapshot_date
    base_path.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, list[IssueInfo]] = defaultdict(list)
    for issue in issues:
        grouped[issue.repo].append(issue)

    outputs: dict[str, Path] = {}
    for repo, repo_issues in grouped.items():
        file_path = base_path / f"{_safe_repo_filename(repo)}.jsonl"
        with file_path.open("w", encoding="utf-8") as f:
            for issue in repo_issues:
                payload = {
                    "repo": issue.repo,
                    "issue_id": issue.issue_id,
                    "title": issue.title,
                    "body": issue.body,
                    "state": issue.state,
                    "author": issue.author,
                    "created_at": issue.created_at.isoformat(),
                    "updated_at": issue.updated_at.isoformat(),
                    "closed_at": issue.closed_at.isoformat()
                    if issue.closed_at
                    else None,
                    "comments": issue.comments,
                    "labels": issue.labels,
                    "url": issue.url,
                    "last_comment_days": issue.last_comment_days,
                    "is_recently_active": issue.is_recently_active,
                }
                f.write(json.dumps(payload, ensure_ascii=False) + "\n")
        outputs[repo] = file_path

    return outputs


def read_issues_jsonl(path: Path) -> list[dict[str, object]]:
    """读取 JSONL Issue 文件（用于测试/调试）"""
    items: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items
