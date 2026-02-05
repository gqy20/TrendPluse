"""异步 LLM 分析器测试"""

import pytest

from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
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
