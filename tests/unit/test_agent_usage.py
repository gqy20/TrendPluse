"""Agent usage 聚合测试。"""

from unittest.mock import Mock

from trendpluse.models.agent_usage import (
    AgentMetricsSummary,
    AgentRunMetrics,
)


def test_agent_metrics_summary_ignores_non_metrics_objects() -> None:
    """聚合时应忽略 Mock 等非 AgentRunMetrics 对象。"""
    result = AgentMetricsSummary.from_runs(
        [
            Mock(),
            AgentRunMetrics(
                model="sonnet",
                session_id="s1",
                num_turns=2,
                duration_ms=100,
                duration_api_ms=80,
                total_cost_usd=0.12,
                usage={"total_tokens": 50, "tool_uses": 1, "duration_ms": 100},
                raw_usage={"total_tokens": 50, "tool_uses": 1, "duration_ms": 100},
            ),
            None,
        ]
    )

    assert result is not None
    assert result.run_count == 1
    assert result.total_turns == 2
    assert result.total_cost_usd == 0.12
    assert result.usage.total_tokens == 50


def test_agent_metrics_summary_combine_ignores_non_summary_objects() -> None:
    """合并时应忽略非 AgentMetricsSummary 对象。"""
    result = AgentMetricsSummary.combine(
        runs=[],
        summaries=[
            Mock(),
            AgentMetricsSummary(
                run_count=2,
                models=["sonnet"],
                total_turns=4,
                total_duration_ms=200,
                total_api_duration_ms=150,
                total_cost_usd=0.3,
                usage={"total_tokens": 120, "tool_uses": 2, "duration_ms": 200},
            ),
        ],
    )

    assert result is not None
    assert result.run_count == 2
    assert result.total_turns == 4
    assert result.total_cost_usd == 0.3
    assert result.usage.total_tokens == 120
