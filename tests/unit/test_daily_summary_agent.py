"""日报总结 Agent 测试。"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest
from claude_agent_sdk.types import ResultMessage
from pydantic import ValidationError

from trendpluse.analyzers.daily_summary_agent import DailySummaryAgent
from trendpluse.models.signal import DailyReport, ReportStats


def _build_report() -> DailyReport:
    return DailyReport(
        date="2026-03-18",
        summary_brief="旧摘要",
        engineering_signals=[],
        research_signals=[],
        commit_signals=[],
        release_signals=[],
        stats=ReportStats(),
    )


@pytest.mark.asyncio
async def test_daily_summary_agent_query_uses_broader_tools_and_limits(
    tmp_path: Path,
) -> None:
    """日报总结 Agent 应向 SDK 透传更宽的只读分析权限和轮数限制。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
        model="sonnet",
        max_turns=33,
        max_budget_usd=7.5,
    )

    async def fake_query(*, prompt, options=None, transport=None):
        assert options is not None
        assert options.allowed_tools == ["Read", "Glob", "LS", "Grep"]
        assert options.max_turns == 33
        assert options.max_budget_usd == 7.5
        assert options.output_format is not None
        yield ResultMessage(
            subtype="success",
            duration_ms=1,
            duration_api_ms=1,
            is_error=False,
            num_turns=3,
            session_id="s1",
            total_cost_usd=0.123,
            usage={"input_tokens": 11, "output_tokens": 7},
            structured_output={
                "summary_brief": "今天的趋势在历史上属于延续中的新推进。",
                "trend_status": "continuing",
                "trend_delta": "较昨日新增了落地动作。",
                "historical_basis_dates": ["2026-03-16", "2026-03-17"],
                "historical_comparison": "今天不是重复昨天，而是在同一趋势上继续推进。",
                "top_new_trends": ["落地部署"],
                "top_continuing_trends": ["多 Agent 协作"],
                "confidence": 0.86,
            },
        )

    with patch("claude_agent_sdk.query", fake_query):
        result = await agent._run_agent_query_async(tmp_path / "today.json")

    parsed = json.loads(result)
    assert parsed["trend_status"] == "continuing"
    assert parsed["confidence"] == 0.86
    metrics = agent.get_last_run_metrics()
    assert metrics is not None
    assert metrics.total_cost_usd == 0.123
    assert metrics.usage.input_tokens == 11
    assert metrics.usage.output_tokens == 7
    assert metrics.usage.total_tokens == 18


@pytest.mark.asyncio
async def test_daily_summary_agent_query_registers_stderr_callback(
    tmp_path: Path,
) -> None:
    """日报总结 Agent 应接收并记录 SDK CLI 的 stderr 输出。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
    )

    async def fake_query(*, prompt, options=None, transport=None):
        assert options is not None
        assert callable(options.stderr)
        options.stderr("cli boom")
        yield ResultMessage(
            subtype="success",
            duration_ms=1,
            duration_api_ms=1,
            is_error=False,
            num_turns=1,
            session_id="s2",
            structured_output={
                "summary_brief": "有结果",
                "trend_status": "new",
                "trend_delta": "新增趋势",
                "historical_basis_dates": [],
                "historical_comparison": "首日报，无历史对比。",
                "top_new_trends": ["模型分层化"],
                "top_continuing_trends": [],
                "confidence": None,
            },
        )

    with (
        patch("claude_agent_sdk.query", fake_query),
        patch("trendpluse.analyzers.daily_summary_agent.logger.warning") as warning,
    ):
        await agent._run_agent_query_async(tmp_path / "today.json")

    warning.assert_called_with("DailySummaryAgent CLI stderr: %s", "cli boom")
    assert list(agent._recent_cli_stderr) == ["cli boom"]


def test_daily_summary_agent_prompt_mentions_candidate_history_paths(
    tmp_path: Path,
) -> None:
    """Prompt 应明确告知索引、今日草稿和全量历史目录，并让 Agent 自主回读。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
    )

    prompt = agent._build_prompt(current_report_path=tmp_path / "today.json")

    assert "先读取历史日报索引" in prompt
    assert "再读取今天的日报草稿" in prompt
    assert "历史日报原文目录" in prompt
    assert "自行决定需要回读哪些历史日报原文" in prompt
    assert "不要只局限于最近几天" in prompt


def test_daily_summary_agent_enhance_updates_report_fields(tmp_path: Path) -> None:
    """增强结果应回写到日报对象。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
    )
    report = _build_report()

    with (
        patch.object(agent, "refresh_history_index"),
        patch.object(
            agent,
            "_run_with_report_context",
            return_value=agent._result_model(
                summary_brief="新的总结",
                trend_status="continuing",
                trend_delta="新增部署动作",
                historical_basis_dates=["2026-03-16"],
                historical_comparison="是延续，不是重复",
                top_new_trends=["部署"],
                top_continuing_trends=["多 Agent"],
                confidence=0.92,
            ),
        ),
    ):
        agent.enhance(report=report, date=None)

    assert report.summary_brief == "新的总结"
    assert report.trend_status == "continuing"
    assert report.historical_basis_dates == ["2026-03-16"]


@pytest.mark.asyncio
async def test_daily_summary_agent_enhance_async_updates_report_fields(
    tmp_path: Path,
) -> None:
    """异步增强结果应回写到日报对象，且可在 running loop 中使用。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
    )
    report = _build_report()

    with (
        patch.object(agent, "refresh_history_index"),
        patch.object(
            agent,
            "_run_with_report_context_async",
            return_value=agent._result_model(
                summary_brief="异步新的总结",
                trend_status="continuing",
                trend_delta="异步新增部署动作",
                historical_basis_dates=["2026-03-17"],
                historical_comparison="异步链路也能完成增强",
                top_new_trends=["部署"],
                top_continuing_trends=["多 Agent"],
                confidence=0.95,
            ),
        ),
    ):
        await agent.enhance_async(report=report, date=None)

    assert report.summary_brief == "异步新的总结"
    assert report.trend_status == "continuing"
    assert report.historical_basis_dates == ["2026-03-17"]


def test_daily_summary_agent_retries_after_validation_failure(tmp_path: Path) -> None:
    """结构化结果校验失败后应重试，并在后续成功时返回结果。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
        retry_max_attempts=2,
        retry_wait_seconds=0.0,
    )
    report = _build_report()
    call_count = {"value": 0}

    def fake_run(current_report_path: Path) -> str:
        call_count["value"] += 1
        if call_count["value"] == 1:
            return '{"summary_brief":"bad"}'
        return json.dumps(
            {
                "summary_brief": "新的总结",
                "trend_status": "continuing",
                "trend_delta": "新增推进",
                "historical_basis_dates": ["2026-03-17"],
                "historical_comparison": "相对历史有新动作",
                "top_new_trends": ["部署"],
                "top_continuing_trends": ["多 Agent"],
                "confidence": 0.8,
            },
            ensure_ascii=False,
        )

    with patch.object(agent, "_run_agent_query", side_effect=fake_run):
        result = agent._run_with_report_context(report)

    assert call_count["value"] == 2
    assert result.summary_brief == "新的总结"


def test_daily_summary_agent_raises_after_retry_exhausted(tmp_path: Path) -> None:
    """当重试耗尽时，应抛出最后一次失败异常。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
        retry_max_attempts=2,
        retry_wait_seconds=0.0,
    )
    report = _build_report()

    with (
        patch.object(agent, "_run_agent_query", return_value='{"summary_brief":"bad"}'),
        pytest.raises(ValidationError),
    ):
        agent._run_with_report_context(report)


@pytest.mark.asyncio
async def test_daily_summary_agent_async_retries_after_sdk_process_error(
    tmp_path: Path,
) -> None:
    """SDK 进程错误应进入重试，并在后续成功时返回结果。"""
    agent = DailySummaryAgent(
        reports_dir=str(tmp_path / "reports" / "daily"),
        history_index_path=str(
            tmp_path / "data" / "history" / "daily-report-index.json"
        ),
        retry_max_attempts=2,
        retry_wait_seconds=0.0,
    )
    report = _build_report()
    call_count = {"value": 0}

    from claude_agent_sdk import ProcessError

    async def fake_run(current_report_path: Path) -> str:
        call_count["value"] += 1
        if call_count["value"] == 1:
            raise ProcessError("cli failed", exit_code=1, stderr="boom")
        return json.dumps(
            {
                "summary_brief": "新的总结",
                "trend_status": "continuing",
                "trend_delta": "新增推进",
                "historical_basis_dates": ["2026-03-17"],
                "historical_comparison": "相对历史有新动作",
                "top_new_trends": ["部署"],
                "top_continuing_trends": ["多 Agent"],
                "confidence": 0.8,
            },
            ensure_ascii=False,
        )

    with patch.object(agent, "_run_agent_query_async", side_effect=fake_run):
        result = await agent._run_with_report_context_async(report)

    assert call_count["value"] == 2
    assert result.summary_brief == "新的总结"
