"""异步 LLM 分析器测试"""

import pytest

from trendpluse.analyzers.issue_analyzer import IssueAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.issue import IssueAnalysis, IssueInfo
from trendpluse.models.signal import ReleaseSummary, Signal


class _AsyncChatStub:
    def __init__(self, result):
        self._result = result

    async def create(self, *args, **kwargs):
        return self._result


class _AsyncInstructorClientStub:
    def __init__(self, result):
        self.chat = type(
            "Chat",
            (),
            {"completions": _AsyncChatStub(result)},
        )()


@pytest.mark.asyncio
async def test_trend_analyzer_analyze_prs_async():
    analyzer = TrendAnalyzer(api_key="test", model="test")
    analyzer.async_instructor_client = _AsyncInstructorClientStub(
        Signal(
            id="pr-1",
            title="测试",
            type="capability",
            category="engineering",
            impact_score=3,
            why_it_matters="测试",
            sources=["https://example.com"],
            related_repos=["repo/a"],
        )
    )

    pr_list = [
        {
            "repo_name": "repo/a",
            "number": 1,
            "title": "Test",
            "body": "Body",
            "author": "alice",
            "url": "https://github.com/repo/a/pull/1",
        }
    ]

    results = await analyzer.analyze_prs_async(pr_list, max_workers=2)
    assert len(results) == 1
    assert results[0].id == "pr-1"


@pytest.mark.asyncio
async def test_issue_analyzer_analyze_batch_async():
    analyzer = IssueAnalyzer(api_key="test", model="test")
    analyzer.async_instructor_client = _AsyncInstructorClientStub(
        IssueAnalysis(
            category="bug_report",
            sentiment="neutral",
            sentiment_score=0,
            pain_point="测试",
            affected_area=None,
            feature_description=None,
            priority="low",
            technical_tags=[],
        )
    )

    issue = IssueInfo(
        repo="repo/a",
        issue_id=1,
        title="Bug",
        body="Body",
        state="open",
        author="alice",
        created_at="2026-01-01T00:00:00Z",
        updated_at="2026-01-01T00:00:00Z",
        closed_at=None,
        comments=0,
        labels=[],
        url="https://github.com/repo/a/issues/1",
        last_comment_days=1,
        is_recently_active=True,
    )

    results = await analyzer.analyze_batch_async([issue], max_workers=2)
    assert "repo/a#1" in results
    assert results["repo/a#1"].category == "bug_report"


@pytest.mark.asyncio
async def test_release_summarizer_summarize_releases_async():
    summarizer = ReleaseSummarizer(api_key="test", model="test")
    summarizer.async_instructor_client = _AsyncInstructorClientStub(
        ReleaseSummary(
            change_type="feature",
            key_changes=["测试变更"],
            summary_cn="测试总结",
            impact_level=3,
        )
    )

    releases = [
        {
            "repo": "repo/a",
            "tag_name": "v1.0.0",
            "body": "Test release notes",
        }
    ]

    results = await summarizer.summarize_releases_async(releases, max_workers=2)
    assert "repo/a@v1.0.0" in results
    assert results["repo/a@v1.0.0"].change_type == "feature"
