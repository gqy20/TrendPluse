"""Prompt golden 测试：锁定所有发给 LLM 的提示词字节级内容。

迁移 YAML 前用 ``UPDATE_GOLDEN=1`` 生成基线；之后任何 prompt 变更
（包括 YAML 迁移本身）都必须保持字节级一致，除非显式更新 golden。

用法::

    UPDATE_GOLDEN=1 uv run pytest tests/unit/test_prompt_golden.py   # 生成/更新
    uv run pytest tests/unit/test_prompt_golden.py                   # 校验
"""

from __future__ import annotations

import asyncio
import os
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from trendpluse.analyzers.breaking_changes_detector import BreakingChangesDetector
from trendpluse.analyzers.daily_summary_agent import DailySummaryAgent
from trendpluse.analyzers.issue_agent_runner import IssueAgentRunner
from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer
from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.analyzers.weekly_aggregator import WeeklyAggregator
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial

GOLDEN_DIR = Path(__file__).parents[1] / "fixtures" / "prompts"
DATE = "2026-01-01"


def _assert_golden(name: str, content: str) -> None:
    """与 golden 文件字节级比对（UPDATE_GOLDEN=1 时写入）。"""
    path = GOLDEN_DIR / f"{name}.txt"
    if os.environ.get("UPDATE_GOLDEN"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    assert path.exists(), f"缺少 golden 文件: {path}（先运行 UPDATE_GOLDEN=1）"
    expected = path.read_text(encoding="utf-8")
    assert content == expected, f"prompt 与 golden 不一致: {name}"


def _signal(idx: int, *, category: str = "engineering") -> Signal:
    return Signal(
        id=f"sig-{idx}",
        title=f"示例信号标题 {idx}",
        type="capability",
        category=category,
        impact_score=4,
        why_it_matters=f"示例重要性说明 {idx}",
        sources=[f"https://github.com/owner/repo/pull/{idx}"],
        related_repos=["owner/repo"],
    )


def _material() -> AnalysisMaterial:
    return AnalysisMaterial.from_pr_details(
        {
            "repo_name": "owner/repo",
            "number": 42,
            "title": "示例 PR 标题",
            "body": "示例 PR 描述内容",
            "author": "alice",
            "html_url": "https://github.com/owner/repo/pull/42",
        }
    )


def _release_dict() -> dict:
    return {
        "repo": "owner/repo",
        "tag_name": "v1.2.3",
        "name": "Release v1.2.3",
        "body": "示例 release notes 正文内容",
        "html_url": "https://github.com/owner/repo/releases/tag/v1.2.3",
        "published_at": "2026-01-01T00:00:00Z",
        "author": "bob",
    }


def _mock_report_response() -> MagicMock:
    response = MagicMock()
    response.date = DATE
    response.summary_brief = "总览"
    response.engineering_signals = []
    response.research_signals = []
    response.commit_signals = []
    response.stats = {}
    return response


# ── trend_analyzer ───────────────────────────────────────────────────


class TestTrendAnalyzerGoldens:
    def test_pr_signal_extraction(self):
        analyzer = TrendAnalyzer(api_key="test")
        _assert_golden(
            "trend_analyzer.pr_signal_extraction",
            analyzer._build_material_prompt(_material()),
        )

    def test_aggregation_sync(self):
        analyzer = TrendAnalyzer(api_key="test")
        with patch.object(analyzer.client.chat.completions, "create") as mock_create:
            mock_create.return_value = _mock_report_response()
            analyzer.aggregate_and_generate_report(
                pr_signals=[_signal(1)],
                commit_signals=[_signal(2)],
                release_signals=[_signal(3)],
                date=DATE,
            )
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("trend_analyzer.aggregation_sync", prompt)

    def test_aggregation_async(self):
        analyzer = TrendAnalyzer(api_key="test")
        assert analyzer.async_instructor_client is not None
        with patch.object(
            analyzer.async_instructor_client.chat.completions, "create"
        ) as mock_create:
            mock_create.return_value = _mock_report_response()

            async def _run():
                return await analyzer.aggregate_and_generate_report_async(
                    pr_signals=[_signal(1)],
                    commit_signals=[_signal(2)],
                    release_signals=[_signal(3)],
                    date=DATE,
                )

            asyncio.run(_run())
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("trend_analyzer.aggregation_async", prompt)

    def test_aggregation_sync_empty(self):
        analyzer = TrendAnalyzer(api_key="test")
        with patch.object(analyzer.client.chat.completions, "create") as mock_create:
            mock_create.return_value = _mock_report_response()
            analyzer.aggregate_and_generate_report(
                pr_signals=[],
                commit_signals=[],
                release_signals=[],
                date=DATE,
            )
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("trend_analyzer.aggregation_sync_empty", prompt)

    def test_generate_report_sync(self):
        analyzer = TrendAnalyzer(api_key="test")
        with patch.object(analyzer.client.chat.completions, "create") as mock_create:
            mock_create.return_value = _mock_report_response()
            analyzer.generate_report(
                [_signal(1), _signal(2, category="research")], DATE
            )
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("trend_analyzer.generate_report_sync", prompt)

    def test_generate_report_async(self):
        analyzer = TrendAnalyzer(api_key="test")
        assert analyzer.async_instructor_client is not None
        with patch.object(
            analyzer.async_instructor_client.chat.completions, "create"
        ) as mock_create:
            mock_create.return_value = _mock_report_response()

            async def _run():
                return await analyzer.generate_report_async(
                    [_signal(1), _signal(2, category="research")], DATE
                )

            asyncio.run(_run())
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("trend_analyzer.generate_report_async", prompt)


# ── release_analyzer ─────────────────────────────────────────────────


class TestReleaseAnalyzerGoldens:
    def test_analysis(self):
        analyzer = ReleaseAnalyzer(api_key="test")
        _assert_golden(
            "release_analyzer.analysis",
            analyzer._build_prompt([_release_dict()]),
        )


# ── release_summarizer ───────────────────────────────────────────────


class TestReleaseSummarizerGoldens:
    def test_system_and_user_sync(self):
        summarizer = ReleaseSummarizer(api_key="test")
        with patch.object(summarizer.client.chat.completions, "create") as mock_create:
            mock_create.return_value = MagicMock()
            summarizer._summarize_single_release(_release_dict())
            messages = mock_create.call_args.kwargs["messages"]
        _assert_golden("release_summarizer.system", messages[0]["content"])
        _assert_golden("release_summarizer.single_release", messages[1]["content"])

    def test_system_and_user_async(self):
        summarizer = ReleaseSummarizer(api_key="test")
        assert summarizer.async_instructor_client is not None
        with patch.object(
            summarizer.async_instructor_client.chat.completions, "create"
        ) as mock_create:
            mock_create.return_value = MagicMock()

            async def _run():
                return await summarizer._summarize_single_release_async(_release_dict())

            asyncio.run(_run())
            messages = mock_create.call_args.kwargs["messages"]
        _assert_golden(
            "release_summarizer.single_release_async", messages[1]["content"]
        )


# ── breaking_changes_detector ────────────────────────────────────────


class TestBreakingChangesDetectorGoldens:
    def test_analysis(self):
        detector = BreakingChangesDetector(api_key="test")
        _assert_golden(
            "breaking_changes_detector.analysis",
            detector._build_prompt([_release_dict()]),
        )


# ── sdk_commit_analyzer ──────────────────────────────────────────────


class TestSDKCommitAnalyzerGoldens:
    def test_commit_analysis(self):
        analyzer = SDKCommitAnalyzer()
        _assert_golden(
            "sdk_commit_analyzer.commit_analysis",
            analyzer._build_prompt("/tmp/golden/commits.md", 3),
        )


# ── issue_agent_runner ───────────────────────────────────────────────


class TestIssueAgentRunnerGoldens:
    def test_analysis(self):
        runner = IssueAgentRunner()
        _assert_golden(
            "issue_agent_runner.analysis",
            runner._build_analysis_prompt(Path("/tmp/golden/issues.jsonl")),
        )


# ── daily_summary_agent ──────────────────────────────────────────────


class TestDailySummaryAgentGoldens:
    def test_enhance(self):
        agent = DailySummaryAgent(
            reports_dir="/tmp/golden/reports",
            history_index_path="/tmp/golden/daily-report-index.json",
        )
        _assert_golden(
            "daily_summary_agent.enhance",
            agent._build_prompt(Path("/tmp/golden/current_report.json")),
        )


# ── weekly_aggregator ────────────────────────────────────────────────


class TestWeeklyAggregatorGoldens:
    def test_aggregate_sync(self):
        aggregator = WeeklyAggregator(api_key="test")
        with patch.object(aggregator._client.messages, "create") as mock_create:
            mock_create.return_value = SimpleNamespace(
                content=[
                    SimpleNamespace(text='{"core_trends": [], "summary_brief": "概览"}')
                ]
            )
            aggregator.aggregate([_signal(1), _signal(2)])
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("weekly_aggregator.aggregate_sync", prompt)

    def test_aggregate_async(self):
        aggregator = WeeklyAggregator(api_key="test")
        with patch.object(
            aggregator._async_client.messages,
            "create",
            new=AsyncMock(
                return_value=SimpleNamespace(
                    content=[
                        SimpleNamespace(
                            text='{"core_trends": [], "summary_brief": "概览"}'
                        )
                    ]
                )
            ),
        ) as mock_create:

            async def _run():
                return await aggregator.aggregate_async([_signal(1), _signal(2)])

            asyncio.run(_run())
            prompt = mock_create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("weekly_aggregator.aggregate_async", prompt)


# ── signal_deduplicator ──────────────────────────────────────────────


class TestSignalDeduplicatorGoldens:
    def test_duplicate_check(self, tmp_path):
        llm_client = MagicMock()
        llm_client.messages.create.return_value = SimpleNamespace(
            content=[SimpleNamespace(text="UNIQUE")]
        )
        deduplicator = SignalDeduplicator(
            llm_client=llm_client,
            history_path=str(tmp_path / "signal_history.json"),
        )
        deduplicator._llm_check_duplicate(_signal(1), [_signal(2), _signal(3)])
        prompt = llm_client.messages.create.call_args.kwargs["messages"][0]["content"]
        _assert_golden("signal_deduplicator.duplicate_check", prompt)


@pytest.mark.parametrize(
    "name",
    sorted(p.stem for p in (GOLDEN_DIR).glob("*.txt")) if GOLDEN_DIR.exists() else [],
)
def test_no_orphan_golden_files(name: str):
    """golden 文件必须与测试一一对应，防止改名后留下孤儿文件。"""
    test_source = Path(__file__).read_text(encoding="utf-8")
    assert f'"{name}"' in test_source, f"孤儿 golden 文件: {name}"
