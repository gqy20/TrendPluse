"""Issue 文件读写工具"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from trendpluse.collectors.issue_ranker import score_issue
from trendpluse.models.issue import IssueInfo


def _safe_repo_filename(repo: str) -> str:
    return repo.replace("/", "__")


def dump_issues_to_jsonl(
    issues: list[IssueInfo],
    base_dir: str,
    snapshot_date: str,
) -> dict[str, Path]:
    """将 issues 按仓库落盘。

    每仓库写三件文件(双文件设计,实测验证):
    - ``{repo}.jsonl``        原始单行 JSONL(快照/调试兼容,不再供 agent 阅读)
    - ``{repo}__index.jsonl`` 轻量索引:每行一条 issue 摘要 + 全量文件行号范围
    - ``{repo}__full.md``     分节全量:每 issue 一节,含完整 body 原文

    agent 首轮只读索引,按需用行号深读原文——旧 JSONL 单行超 2000 字符会被
    Claude CLI Read 工具静默截断(实测 60 条样本中 10 条 body 不完整),
    markdown 分行格式天然免疫。

    Returns:
        {repo: 原始 jsonl 路径} 映射。
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
        safe_name = _safe_repo_filename(repo)

        raw_path = base_path / f"{safe_name}.jsonl"
        with raw_path.open("w", encoding="utf-8") as f:
            for issue in repo_issues:
                payload = _serialize_raw_issue(issue)
                f.write(json.dumps(payload, ensure_ascii=False) + "\n")

        _dump_dual_files(base_path, safe_name, repo, repo_issues)
        outputs[repo] = raw_path

    return outputs


def _serialize_raw_issue(issue: IssueInfo) -> dict[str, object]:
    """序列化原始 JSONL 行(与旧格式保持一致)。"""
    return {
        "repo": issue.repo,
        "issue_id": issue.issue_id,
        "title": issue.title,
        "body": issue.body,
        "state": issue.state,
        "author": issue.author,
        "created_at": issue.created_at.isoformat(),
        "updated_at": issue.updated_at.isoformat(),
        "closed_at": issue.closed_at.isoformat() if issue.closed_at else None,
        "comments": issue.comments,
        "labels": issue.labels,
        "url": issue.url,
        "last_comment_days": issue.last_comment_days,
        "is_recently_active": issue.is_recently_active,
    }


def _dump_dual_files(
    base_path: Path, safe_name: str, repo: str, repo_issues: list[IssueInfo]
) -> None:
    """写索引 + 分节全量双文件。

    索引行字段(短键,与实测 A/B 验证格式一致):
    n=编号 t=标题 c=评论数 st=状态 s=评分 r=命中原因 ln=[全量文件起止行]
    """
    index_lines: list[str] = []
    full_lines: list[str] = [f"# {repo} Issue Full Content", ""]

    for issue in repo_issues:
        score, reasons = score_issue(issue)
        start = len(full_lines) + 1
        full_lines.append(f"## #{issue.issue_id} {issue.title}")
        labels = ",".join(issue.labels or []) or "-"
        full_lines.append(
            f"- state: {issue.state} | created: "
            f"{issue.created_at.date().isoformat()} | comments: "
            f"{issue.comments or 0} | labels: {labels}"
        )
        full_lines.append(f"- url: {issue.url}")
        full_lines.append("")
        body = (issue.body or "").strip() or "(empty body)"
        full_lines.extend(body.split("\n"))
        full_lines.append("")
        end = len(full_lines)

        index_lines.append(
            json.dumps(
                {
                    "n": issue.issue_id,
                    "t": issue.title,
                    "c": issue.comments or 0,
                    "st": issue.state,
                    "s": score,
                    "r": reasons,
                    "ln": [start, end],
                },
                ensure_ascii=False,
            )
        )

    index_path = base_path / f"{safe_name}__index.jsonl"
    full_path = base_path / f"{safe_name}__full.md"
    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    full_path.write_text("\n".join(full_lines) + "\n", encoding="utf-8")


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
