"""Issue 痛点信号评分器测试"""

from datetime import UTC, datetime, timedelta

from trendpluse.collectors.issue_ranker import rank_issues, score_issue
from trendpluse.models.issue import IssueInfo


def _issue(
    title: str,
    body: str | None = "",
    comments: int = 0,
    state: str = "open",
    labels: list[str] | None = None,
    created_days_ago: int = 1,
) -> IssueInfo:
    now = datetime.now(UTC)
    return IssueInfo(
        repo="owner/repo",
        issue_id=1,
        title=title,
        body=body,
        state=state,
        author="user",
        created_at=now - timedelta(days=created_days_ago),
        updated_at=now,
        closed_at=None,
        comments=comments,
        labels=labels or [],
        url="https://example.com/1",
        last_comment_days=0,
        is_recently_active=True,
    )


def test_title_keyword_scores_high() -> None:
    score, reasons = score_issue(_issue("Search fails with error on startup"))
    assert score == 3
    assert "title_kw" in reasons


def test_stacktrace_and_repro_add_score() -> None:
    score, reasons = score_issue(
        _issue(
            "how do I change the workspace theme",
            body="steps to reproduce\nTraceback boom",
            comments=2,
        )
    )
    assert "stacktrace" in reasons
    assert "repro" in reasons
    assert score == 4


def test_comments_ladder() -> None:
    assert score_issue(_issue("a sufficiently long title here", comments=5))[0] == 3
    assert score_issue(_issue("a sufficiently long title here", comments=3))[0] == 2
    assert score_issue(_issue("a sufficiently long title here", comments=2))[0] == 1
    assert score_issue(_issue("a sufficiently long title here", comments=0))[0] == 0


def test_open_lingering_scores_high() -> None:
    """open 且创建超 7 天 = 长寿悬置痛点(金标画像 62%)。"""
    issue = _issue(
        "cannot login after upgrading to the latest release",
        state="open",
        created_days_ago=10,
    )
    score, reasons = score_issue(issue)
    assert "open_lingering" in reasons
    assert score == 5


def test_thin_title_penalized() -> None:
    score, reasons = score_issue(_issue("hi", comments=0))
    assert "thin" in reasons
    assert score == -2


def test_bad_label_penalized() -> None:
    score, reasons = score_issue(
        _issue("a sufficiently long title here", labels=["question"])
    )
    assert "bad_label" in reasons
    assert score == -2


def test_rank_orders_descending() -> None:
    """排序后疑似痛点排在噪声前面。"""
    pain = _issue("regression: build broken", comments=4, created_days_ago=9)
    noise = _issue("how to configure theme?", comments=0, labels=["question"])
    ranked = rank_issues([noise, pain])
    assert ranked[0] is pain
    assert ranked[1] is noise


def test_rank_is_stable_for_equal_scores() -> None:
    a = _issue("alpha")
    b = _issue("beta")
    ranked = rank_issues([a, b])
    assert ranked[0] is a
    assert ranked[1] is b
