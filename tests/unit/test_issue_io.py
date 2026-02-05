"""Issue IO 工具测试"""

from datetime import UTC, datetime
from pathlib import Path

from trendpluse.models.issue import IssueInfo
from trendpluse.utils.issue_io import dump_issues_to_jsonl, read_issues_jsonl


def test_dump_issues_to_jsonl_groups_by_repo(tmp_path: Path) -> None:
    now = datetime.now(UTC)
    issues = [
        IssueInfo(
            repo="owner/repo1",
            issue_id=1,
            title="A",
            body="Body",
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=["bug"],
            url="https://example.com/1",
            last_comment_days=0,
            is_recently_active=True,
        ),
        IssueInfo(
            repo="owner/repo2",
            issue_id=2,
            title="B",
            body=None,
            state="closed",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=1,
            labels=[],
            url="https://example.com/2",
            last_comment_days=1,
            is_recently_active=False,
        ),
    ]

    outputs = dump_issues_to_jsonl(issues, str(tmp_path), "2026-02-05")
    assert set(outputs.keys()) == {"owner/repo1", "owner/repo2"}

    for repo, path in outputs.items():
        items = read_issues_jsonl(path)
        assert len(items) == 1
        assert items[0]["repo"] == repo
