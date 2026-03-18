"""Issue 全局汇总测试。"""

from trendpluse.issue_signal_aggregator import IssueGlobalSummarizer
from trendpluse.models.issue_agent import (
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)


class _StubSummarizer(IssueGlobalSummarizer):
    def __init__(self) -> None:
        super().__init__(api_key="test-key", model="glm-4.7", base_url="")

    def _call_llm_for_summary(self, report: IssueAgentReport):
        return self.response_model(
            summary_brief="Issue Agent 汇总了 2 个仓库，识别出 1 个跨仓库问题。",
            global_highlights=["登录失效：影响 2 个仓库，累计 3 个 issue"],
        )


def _build_report() -> IssueAgentReport:
    return IssueAgentReport(
        repo_reports=[
            RepoIssueSignalReport(
                repo="owner/repo1",
                snapshot_date="2026-03-07",
                signals=[
                    IssueAgentPainPoint(
                        id="sig-1",
                        repo="owner/repo1",
                        topic="登录失效",
                        summary="升级后频繁掉登录态",
                        count=2,
                        priority="P1",
                        confidence=0.8,
                        affected_repos=["owner/repo1"],
                        sample_urls=["u1"],
                        source_issues=[
                            IssueAgentSourceIssue(
                                repo="owner/repo1",
                                issue_number=101,
                                title="Login expires",
                                url="u1",
                            )
                        ],
                    )
                ],
            ),
            RepoIssueSignalReport(
                repo="owner/repo2",
                snapshot_date="2026-03-07",
                signals=[
                    IssueAgentPainPoint(
                        id="sig-2",
                        repo="owner/repo2",
                        topic="OAuth 回调异常",
                        summary="OAuth 回调后会话丢失",
                        count=1,
                        priority="P0",
                        confidence=0.95,
                        affected_repos=["owner/repo2"],
                        sample_urls=["u2"],
                        source_issues=[
                            IssueAgentSourceIssue(
                                repo="owner/repo2",
                                issue_number=9,
                                title="OAuth callback loses session",
                                url="u2",
                            )
                        ],
                    )
                ],
            ),
        ],
        top_pain_points=[
            IssueAgentPainPoint(
                topic="登录失效",
                count=3,
                priority="P0",
                confidence=0.95,
                affected_repos=["owner/repo1", "owner/repo2"],
                sample_urls=["u1", "u2"],
            )
        ],
    )


def test_issue_global_summarizer_builds_summary_and_highlights() -> None:
    """全局汇总器应优先使用 LLM 结果。"""
    summarized = _StubSummarizer().summarize(_build_report())

    assert summarized.summary_brief is not None
    assert "2 个仓库" in summarized.summary_brief
    assert summarized.global_highlights
    assert "登录失效" in summarized.global_highlights[0]


def test_issue_global_summarizer_falls_back_when_llm_fails() -> None:
    """LLM 失败时应退回规则摘要。"""

    class _FailSummarizer(IssueGlobalSummarizer):
        def __init__(self) -> None:
            super().__init__(api_key="test-key", model="glm-4.7", base_url="")

        def _call_llm_for_summary(self, report: IssueAgentReport):
            raise RuntimeError("boom")

    summarized = _FailSummarizer().summarize(_build_report())

    assert summarized.summary_brief is not None
    assert "Issue Agent 汇总了 2 个仓库" in summarized.summary_brief
    assert summarized.global_highlights


def test_issue_global_summarizer_fallback_distinguishes_single_repo_hotspots() -> None:
    """无跨仓库项时，fallback 摘要应明确这是单仓高影响问题。"""

    class _FailSummarizer(IssueGlobalSummarizer):
        def __init__(self) -> None:
            super().__init__(api_key="test-key", model="glm-4.7", base_url="")

        def _call_llm_for_summary(self, report: IssueAgentReport):
            raise RuntimeError("boom")

    report = IssueAgentReport(
        repo_reports=[
            RepoIssueSignalReport(
                repo="owner/repo1",
                snapshot_date="2026-03-07",
                signals=[
                    IssueAgentPainPoint(
                        id="sig-1",
                        repo="owner/repo1",
                        topic="应用启动崩溃",
                        summary="升级后启动即崩溃",
                        count=5,
                        priority="P0",
                        confidence=0.95,
                        affected_repos=["owner/repo1"],
                        sample_urls=["u1"],
                    )
                ],
            )
        ],
        top_pain_points=[
            IssueAgentPainPoint(
                topic="应用启动崩溃",
                count=5,
                priority="P0",
                confidence=0.95,
                affected_repos=["owner/repo1"],
                sample_urls=["u1"],
            )
        ],
    )

    summarized = _FailSummarizer().summarize(report)

    assert summarized.summary_brief is not None
    assert "未形成明显跨仓库共性问题" in summarized.summary_brief
    assert "高影响单仓问题" in summarized.summary_brief
    assert summarized.global_highlights
    assert "owner/repo1" in summarized.global_highlights[0]


def test_issue_global_summarizer_prompt_includes_category_and_split_candidates() -> (
    None
):
    """全局汇总 prompt 应显式带出 category，并区分跨仓库/单仓候选。"""
    summarizer = IssueGlobalSummarizer(
        api_key="test-key",
        model="glm-4.7",
        base_url="",
    )
    report = IssueAgentReport(
        repo_reports=[
            RepoIssueSignalReport(
                repo="owner/repo1",
                snapshot_date="2026-03-07",
                signals=[
                    IssueAgentPainPoint(
                        id="sig-1",
                        repo="owner/repo1",
                        topic="应用启动崩溃",
                        summary="升级后启动即崩溃",
                        category="startup_crash",
                        count=5,
                        priority="P0",
                        confidence=0.95,
                        affected_repos=["owner/repo1"],
                        sample_urls=["u1"],
                    )
                ],
            )
        ],
        top_pain_points=[
            IssueAgentPainPoint(
                topic="认证失效",
                category="auth_permission",
                count=4,
                priority="P0",
                confidence=0.92,
                affected_repos=["owner/repo1", "owner/repo2"],
                sample_urls=["u2", "u3"],
            ),
            IssueAgentPainPoint(
                topic="应用启动崩溃",
                category="startup_crash",
                count=5,
                priority="P0",
                confidence=0.95,
                affected_repos=["owner/repo1"],
                sample_urls=["u1"],
            ),
        ],
        cross_repo_item_count=1,
        other_category_count=0,
        category_coverage=1.0,
    )

    prompt = summarizer._build_prompt(report)

    assert '"category": "startup_crash"' in prompt
    assert '"cross_repo_candidates"' in prompt
    assert '"single_repo_candidates"' in prompt
    assert '"semantic_quality"' in prompt
    assert '"cross_repo_item_count": 1' in prompt
    assert '"category": "auth_permission"' in prompt
