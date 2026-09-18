"""Issue 痛点信号评分器。

在进入 LLM 分析前对候选 issue 做"痛点概率"排序,替代旧的 created-desc 先到先得。
评分只用于排序,不做硬截断——实测(comments>=3 硬过滤会砍掉约半数真痛点)证明
互动/关键词只能作为排序信号,不能作为过滤条件。

权重经 5 月真实数据校准(141 条 agent 判定的 P0/P1 痛点 vs 670 条候选池):
- title 关键词: 金标命中 59%,池内仅 7-55% → +3
- comments 阶梯: 金标 76% >=2 评论 → +1~+3
- 长寿悬置(open 且创建超 7 天): 金标 62% 是活跃老 issue → +2
"""

from __future__ import annotations

import re
from datetime import UTC, datetime

from trendpluse.models.issue import IssueInfo

_TITLE_KW = re.compile(
    r"\b(fail|fails|failed|failure|error|bug|broken|breaks|crash|cannot|"
    r"can'?t|not working|doesn'?t|does not|regression|stopped working|"
    r"silently|undefined|exception|timeout|hang|stuck)\b",
    re.IGNORECASE,
)
_TRACE_KW = re.compile(
    r"(traceback|exception|panic|stack trace|errno|segfault|error:)",
    re.IGNORECASE,
)
_REPRO_KW = re.compile(
    r"(steps to reproduce|reproduce|reproduc|minimal repro)", re.IGNORECASE
)
_BAD_LABEL = re.compile(
    r"(question|discussion|documentation|announcement|duplicate|wontfix|invalid)",
    re.IGNORECASE,
)


def score_issue(issue: IssueInfo, now: datetime | None = None) -> tuple[int, list[str]]:
    """对单条 issue 打痛点信号分。

    Args:
        issue: 候选 issue
        now: 评估基准时间(默认当前),决定"悬置时长"计算

    Returns:
        (分数, 命中原因列表),分数越高越可能是有分析价值的用户痛点。
    """
    now = now or datetime.now(UTC)
    score = 0
    reasons: list[str] = []

    title = issue.title or ""
    body = issue.body or ""

    if _TITLE_KW.search(title):
        score += 3
        reasons.append("title_kw")

    if _TRACE_KW.search(body):
        score += 2
        reasons.append("stacktrace")

    if _REPRO_KW.search(body):
        score += 1
        reasons.append("repro")

    comments = issue.comments or 0
    if comments >= 5:
        score += 3
        reasons.append("comments5")
    elif comments >= 3:
        score += 2
        reasons.append("comments3")
    elif comments == 2:
        score += 1
        reasons.append("comments2")

    created = issue.created_at
    age_days = (now - created).days if created <= now else 0
    if 7 < age_days <= 30 and issue.state == "open":
        score += 2
        reasons.append("open_lingering")

    if len(title) < 30 and comments == 0:
        score -= 2
        reasons.append("thin")

    if _BAD_LABEL.search(" ".join(issue.labels or [])):
        score -= 2
        reasons.append("bad_label")

    return score, reasons


def rank_issues(
    issues: list[IssueInfo], now: datetime | None = None
) -> list[IssueInfo]:
    """按痛点评分降序排序(稳定排序,同分保持原顺序)。

    Args:
        issues: 候选 issue 列表
        now: 评估基准时间

    Returns:
        排序后的列表(新列表,不修改入参)。
    """
    now = now or datetime.now(UTC)
    return sorted(issues, key=lambda issue: score_issue(issue, now)[0], reverse=True)
