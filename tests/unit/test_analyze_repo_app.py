"""单仓库分析应用测试。"""

from trendpluse.app.analyze_repo import generate_markdown_report, parse_github_url


def test_parse_github_url_supports_https_and_short_form() -> None:
    """应支持 HTTPS 和 owner/repo 两种形式。"""
    assert parse_github_url("https://github.com/openai/openai-python") == (
        "openai",
        "openai-python",
    )
    assert parse_github_url("openai/openai-python") == (
        "openai",
        "openai-python",
    )


def test_parse_github_url_supports_ssh_git_suffix() -> None:
    """应支持 SSH 和 .git 后缀。"""
    assert parse_github_url("git@github.com:openai/openai-python.git") == (
        "openai",
        "openai-python",
    )


def test_generate_markdown_report_contains_core_sections() -> None:
    """生成的 Markdown 应包含关键分节。"""
    report = generate_markdown_report(
        {
            "repo": "openai/openai-python",
            "repo_url": "https://github.com/openai/openai-python",
            "analysis_date": "2026-03-06T10:00:00+00:00",
            "days_back": 7,
            "ai_summary": "最近更新集中在 SDK 体验改进。",
            "activity": {"commits": 12, "top_contributors": ["alice", "bob"]},
            "releases": {
                "count": 1,
                "all": [
                    {
                        "version": "v1.2.3",
                        "url": "https://github.com/openai/openai-python/releases/v1.2.3",
                        "date": "2026-03-05",
                        "author": "alice",
                        "summary": "Bug fixes",
                    }
                ],
            },
            "pr_events": {"count": 2, "titles": ["Fix bug", "Add feature"]},
        }
    )

    assert "## 📊 仓库分析报告" in report
    assert "### 🤖 AI 分析摘要" in report
    assert "### 📈 活跃度统计" in report
    assert "### 🚀 发布动态" in report
    assert "### 🔀 PR 活动" in report
