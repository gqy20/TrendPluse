"""飞书 Issue 洞察格式测试。"""

from trendpluse.models.issue_agent import (
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)
from trendpluse.notifiers.feishu_formatter import FeishuFormatter


def test_generate_issue_insights_content_uses_new_structure() -> None:
    formatter = FeishuFormatter()
    report = IssueAgentReport(
        summary_brief="Issue Agent 汇总了 2 个仓库，识别出 1 个跨仓库问题。",
        global_highlights=["登录失效：影响 2 个仓库，累计 3 个 issue"],
        top_pain_points=[
            IssueAgentPainPoint(
                topic="登录失效",
                count=3,
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
                        summary="升级后频繁掉登录态",
                        count=2,
                        affected_repos=["owner/repo1"],
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
            )
        ],
        expected_files=1,
        generated_files=1,
        parsed_files=1,
        failed_files=0,
        quality_score=1.0,
        quality_status="good",
    )

    content = formatter._generate_issue_insights_content(report)

    assert "全局摘要" in content
    assert "全局亮点" in content
    assert "仓库级信号" in content
    assert "Login expires after upgrade" in content
