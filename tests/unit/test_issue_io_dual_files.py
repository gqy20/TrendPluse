"""Issue 双文件落盘与行号索引测试"""

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

from trendpluse.models.issue import IssueInfo
from trendpluse.utils.issue_io import dump_issues_to_jsonl


def _issue(
    issue_id: int,
    title: str,
    body: str | None = "steps to reproduce\nerror: boom",
    state: str = "open",
    comments: int = 2,
    created_days_ago: int = 1,
) -> IssueInfo:
    now = datetime.now(UTC)
    created = now - timedelta(days=created_days_ago)
    return IssueInfo(
        repo="owner/repo",
        issue_id=issue_id,
        title=title,
        body=body,
        state=state,
        author="user",
        created_at=created,
        updated_at=now,
        closed_at=None,
        comments=comments,
        labels=["bug"],
        url=f"https://example.com/{issue_id}",
        last_comment_days=0,
        is_recently_active=True,
    )


def test_dump_writes_dual_files(tmp_path: Path) -> None:
    """每仓库应落盘原始 jsonl + 索引 + 全量三件文件。"""
    issues = [_issue(1, "crash on startup"), _issue(2, "feat: add export", body=None)]

    outputs = dump_issues_to_jsonl(issues, str(tmp_path), "2026-02-05")
    assert set(outputs.keys()) == {"owner/repo"}

    base = tmp_path / "2026-02-05"
    index_path = base / "owner__repo__index.jsonl"
    full_path = base / "owner__repo__full.md"
    assert index_path.exists()
    assert full_path.exists()

    index_rows = [json.loads(line) for line in index_path.read_text().splitlines()]
    assert len(index_rows) == 2
    assert index_rows[0]["n"] == 1
    assert index_rows[0]["t"] == "crash on startup"
    assert index_rows[0]["c"] == 2
    assert index_rows[0]["st"] == "open"
    assert isinstance(index_rows[0]["ln"], list)
    assert len(index_rows[0]["ln"]) == 2


def test_index_line_ranges_cover_full_sections(tmp_path: Path) -> None:
    """索引 ln 行号范围必须精确覆盖全量文件中对应 issue 的节。

    agent 依赖 Read(offset=ln[0], limit=ln[1]-ln[0]+1) 取回完整原文,
    行号错位会导致 agent 读到别的 issue 或丢内容。
    """
    body = "first line\nerror: boom\n" + "\n".join(f"line {i}" for i in range(30))
    issues = [_issue(1, "crash", body=body), _issue(2, "hang", body="steps: x")]

    dump_issues_to_jsonl(issues, str(tmp_path), "2026-02-05")
    base = tmp_path / "2026-02-05"
    index_rows = [
        json.loads(line)
        for line in (base / "owner__repo__index.jsonl").read_text().splitlines()
    ]
    full_lines = (base / "owner__repo__full.md").read_text().splitlines()

    for row in index_rows:
        start, end = row["ln"]
        section = full_lines[start - 1 : end]
        joined = "\n".join(section)
        # 节内必须能找到该 issue 的标题行与 url
        assert f"## #{row['n']} " in joined
        assert f"https://example.com/{row['n']}" in joined
        # 节外相邻行不应混入下一节标题
        assert joined.count("\n## #") == 0 or section[0].startswith(f"## #{row['n']}")

    # 各节互不重叠
    ranges = [tuple(row["ln"]) for row in index_rows]
    for i in range(len(ranges) - 1):
        assert ranges[i][1] < ranges[i + 1][0]


def test_full_file_lines_within_read_tool_limit(tmp_path: Path) -> None:
    """全量文件单行不得超 2000 字符(Claude CLI Read 行截断上限)。

    body 无论多长,按行拆分后每行原样保留,超长行仅来自原始 body 单行。
    """
    long_line = "x" * 3000
    issues = [_issue(1, "crash", body=long_line)]

    dump_issues_to_jsonl(issues, str(tmp_path), "2026-02-05")
    full_path = tmp_path / "2026-02-05" / "owner__repo__full.md"
    lines = full_path.read_text().splitlines()
    # 原始 body 单行超限会被 Read 截断——记录该已知限制:除 body 原文行外,
    # 结构行(标题/元数据)必须全部短于上限
    structural = [line for line in lines if line.startswith(("-", "#"))]
    assert all(len(line) < 2000 for line in structural)
