"""Issue 洞察 Markdown 渲染测试。"""

from trendpluse.markdown_reporter import MarkdownReporter
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
    )

    content = MarkdownReporter()._render_issue_insights(report)

    assert "### 全局摘要" in content
    assert "### 跨仓库问题" in content
    assert "### 仓库级信号" in content
    assert "owner/repo1" in content
    assert "Login expires after upgrade" in content
