"""Issue 洞察 Markdown 渲染测试。"""

from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.agent_usage import AgentMetricsSummary
from trendpluse.models.issue_agent import (
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)


def test_render_issue_insights_includes_global_summary_and_repo_signals() -> None:
    """日报应渲染全局摘要、全局信号和仓库级信号。"""
    report = IssueAgentReport(
        summary_brief="Issue Agent 汇总了 2 个仓库，识别出 1 个跨仓库问题。",
        global_highlights=["登录失效：影响 2 个仓库，累计 3 个 issue"],
        top_pain_points=[
            IssueAgentPainPoint(
                topic="登录失效",
                count=3,
                priority="P0",
                affected_repos=["owner/repo1", "owner/repo2"],
                sample_urls=["https://github.com/owner/repo1/issues/101"],
                source_issues=[
                    IssueAgentSourceIssue(
                        repo="owner/repo1",
                        issue_number=101,
                        title="Login expires after upgrade",
                        url="https://github.com/owner/repo1/issues/101",
                    )
                ],
            )
        ],
        repo_reports=[
            RepoIssueSignalReport(
                repo="owner/repo1",
                snapshot_date="2026-03-07",
                signals=[
                    IssueAgentPainPoint(
                        topic="登录失效",
                        count=2,
                        affected_repos=["owner/repo1"],
                        sample_urls=["https://github.com/owner/repo1/issues/101"],
                    )
                ],
            )
        ],
        expected_files=1,
        generated_files=1,
        parsed_files=1,
        failed_files=0,
        quality_score=1.0,
        quality_status="good",
        cross_repo_item_count=1,
        other_category_count=0,
        category_coverage=1.0,
        agent_metrics_summary=AgentMetricsSummary(
            run_count=2,
            models=["sonnet"],
            total_turns=5,
            total_duration_ms=2500,
            total_api_duration_ms=1900,
            total_cost_usd=0.46,
            usage={"total_tokens": 300, "tool_uses": 3, "duration_ms": 2500},
        ),
    )

    content = MarkdownReporter()._render_issue_insights(report)

    assert "### 全局摘要" in content
    assert "跨仓库项: `1`" in content
    assert "other 分类: `0`" in content
    assert "分类覆盖率: `100.0%`" in content
    assert "调用统计:" in content
    assert "Tokens `300`" in content
    assert "Cost `$0.460000`" in content
    assert "### 跨仓库共性问题" in content
    assert "### 仓库级信号" in content
    assert "owner/repo1" in content
    assert "Login expires after upgrade" in content


def test_render_issue_insights_separates_single_repo_hotspots() -> None:
    """当没有跨仓库项时，不应把单仓热点渲染为跨仓库问题。"""
    report = IssueAgentReport(
        summary_brief="今日未形成明显跨仓库共性，以下为高影响单仓问题。",
        top_pain_points=[
            IssueAgentPainPoint(
                topic="应用启动崩溃",
                count=5,
                priority="P0",
                affected_repos=["owner/repo1"],
                sample_urls=["https://github.com/owner/repo1/issues/101"],
                source_issues=[
                    IssueAgentSourceIssue(
                        repo="owner/repo1",
                        issue_number=101,
                        title="App crashes on startup",
                        url="https://github.com/owner/repo1/issues/101",
                    )
                ],
            )
        ],
        expected_files=1,
        generated_files=1,
        parsed_files=1,
        failed_files=0,
        quality_score=1.0,
        quality_status="good",
    )

    content = MarkdownReporter()._render_issue_insights(report)

    assert "### 跨仓库共性问题" in content
    assert "### 高影响单仓问题" in content
    assert "暂无跨仓库共性问题。" in content
