"""LLM usage 记录与汇总测试（P1-1 / P1-2）。"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.agent_usage import AgentMetricsSummary, AgentRunMetrics
from trendpluse.models.signal import Signal


def _raw_response(
    input_tokens: int = 100, output_tokens: int = 20, model: str = "glm-4.7"
) -> SimpleNamespace:
    """构造带 usage 的 Anthropic 原始响应。"""
    return SimpleNamespace(
        model=model,
        usage=SimpleNamespace(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
            model_dump=lambda: {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            },
        ),
    )


class TestFromAnthropicResponse:
    def test_extracts_usage_and_model(self):
        metrics = AgentRunMetrics.from_anthropic_response(_raw_response(300, 50))
        assert metrics is not None
        assert metrics.model == "glm-4.7"
        assert metrics.usage.input_tokens == 300
        assert metrics.usage.output_tokens == 50
        assert metrics.usage.total_tokens == 350

    def test_none_when_no_usage(self):
        assert (
            AgentRunMetrics.from_anthropic_response(SimpleNamespace(usage=None)) is None
        )

    def test_model_falls_back_to_configured(self):
        response = SimpleNamespace(model=None, usage=_raw_response().usage)
        metrics = AgentRunMetrics.from_anthropic_response(
            response, model="configured-model"
        )
        assert metrics is not None
        assert metrics.model == "configured-model"


class TestFromSdkResultModelUsage:
    """P1-2：model=None 时从 model_usage 提取实际生效模型。"""

    def test_model_from_model_usage(self):
        metrics = AgentRunMetrics.from_sdk_result(
            model=None,
            session_id="s1",
            num_turns=3,
            duration_ms=1000,
            duration_api_ms=800,
            total_cost_usd=0.5,
            usage={"input_tokens": 10, "output_tokens": 5},
            model_usage={"deepseek-v4-flash": {"input_tokens": 10}},
        )
        assert metrics.model == "deepseek-v4-flash"
        assert metrics.usage.total_tokens == 15

    def test_explicit_model_wins(self):
        metrics = AgentRunMetrics.from_sdk_result(
            model="explicit",
            session_id="s1",
            num_turns=1,
            duration_ms=1,
            duration_api_ms=1,
            total_cost_usd=0.0,
            usage=None,
            model_usage={"other-model": {}},
        )
        assert metrics.model == "explicit"

    def test_no_model_info_stays_none(self):
        metrics = AgentRunMetrics.from_sdk_result(
            model=None,
            session_id=None,
            num_turns=0,
            duration_ms=0,
            duration_api_ms=0,
            total_cost_usd=0,
            usage=None,
            model_usage=None,
        )
        assert metrics.model is None


class TestBaseAnalyzerUsageRecording:
    def test_structured_create_records_usage(self):
        """_structured_create 应从 create_with_completion 的原始响应记录 usage。"""

        class _Analyzer(BaseLLMAnalyzer):
            def _unused(self):  # pragma: no cover - 仅实例化
                pass

        analyzer = _Analyzer(api_key="test", model="glm-4.7", use_instructor=True)
        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_create.return_value = (
                Signal(
                    id="s1",
                    title="t",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="w",
                    sources=[],
                    related_repos=[],
                ),
                _raw_response(500, 80),
            )
            result = analyzer._structured_create(
                response_model=Signal,
                messages=[{"role": "user", "content": "p"}],
                max_tokens=100,
            )
        assert result.id == "s1"
        summary = analyzer.get_llm_metrics_summary()
        assert summary is not None
        assert summary.run_count == 1
        assert summary.usage.input_tokens == 500
        assert summary.usage.total_tokens == 580

    def test_anthropic_mode_response_recorded(self):
        """Anthropic 模式的响应 usage 也要被记录。"""

        class _Analyzer(BaseLLMAnalyzer):
            def _unused(self):  # pragma: no cover - 仅实例化
                pass

        analyzer = _Analyzer(api_key="test", model="glm-4.7", use_instructor=False)
        analyzer._record_llm_usage(_raw_response(200, 40))
        analyzer._record_llm_usage(_raw_response(100, 10))
        summary = analyzer.get_llm_metrics_summary()
        assert summary is not None
        assert summary.run_count == 2
        assert summary.usage.total_tokens == 350

    def test_summary_none_when_no_runs(self):
        analyzer = ReleaseSummarizer(api_key="test")
        assert analyzer.get_llm_metrics_summary() is None


class TestStructuredQueryMetrics:
    def test_query_result_metrics_built_from_result_message(self):
        """QueryResult.metrics 应从 ResultMessage 构建（含 model_usage 回落）。"""
        from trendpluse.analyzers.structured_query import StructuredQuery
        from trendpluse.models.daily_summary import DailySummaryResult

        engine = StructuredQuery[DailySummaryResult](
            output_model=DailySummaryResult,
            model=None,
        )
        result_message = SimpleNamespace(
            session_id="sess-1",
            num_turns=5,
            duration_ms=12345,
            duration_api_ms=9000,
            total_cost_usd=1.25,
            usage={"input_tokens": 1000, "output_tokens": 200},
            structured_output='{"summary_brief": "x"}',
            model_usage={"kimi-k3": {"input_tokens": 1000}},
        )
        metrics = AgentRunMetrics.from_sdk_result(
            model=engine.model,
            session_id=result_message.session_id,
            num_turns=result_message.num_turns,
            duration_ms=result_message.duration_ms,
            duration_api_ms=result_message.duration_api_ms,
            total_cost_usd=result_message.total_cost_usd,
            usage=result_message.usage,
            model_usage=result_message.model_usage,
        )
        assert metrics.model == "kimi-k3"
        assert metrics.usage.total_tokens == 1200
        assert metrics.total_cost_usd == 1.25


class TestDailyLlmUsageAggregation:
    """app/daily.py 的 _collect_daily_llm_usage 汇总与预算告警。"""

    def _make_app(self, settings):
        from trendpluse.app.daily import DailyPipelineApp

        analyzer = TrendAnalyzer(api_key="test")
        analyzer._record_llm_usage(_raw_response(1000, 200))
        commit_analyzer = MagicMock()
        commit_analyzer.get_llm_metrics_summary.return_value = (
            AgentMetricsSummary.from_runs(
                [AgentRunMetrics(model="deepseek", total_cost_usd=0.5)]
            )
        )
        release_workflow = SimpleNamespace(
            release_summarizer=MagicMock(
                get_llm_metrics_summary=MagicMock(return_value=None)
            ),
            release_analyzer=MagicMock(
                get_llm_metrics_summary=MagicMock(return_value=None)
            ),
            breaking_changes_detector=MagicMock(
                get_llm_metrics_summary=MagicMock(return_value=None)
            ),
        )
        return DailyPipelineApp(
            settings=settings,
            activity_collector=MagicMock(),
            release_collector=MagicMock(),
            issue_workflow=MagicMock(),
            release_workflow=release_workflow,
            commit_material_builder=MagicMock(),
            commit_analyzer=commit_analyzer,
            collector=MagicMock(),
            event_filter=MagicMock(),
            pr_reader=MagicMock(),
            analyzer=analyzer,
            deduplicator=MagicMock(),
            daily_report_finalizer=MagicMock(),
        )

    def test_collects_usage_from_all_components(self):
        from trendpluse.models.signal import DailyReport

        app = self._make_app(settings=MagicMock(daily_token_budget=0))
        report = DailyReport(date="2026-01-01", summary_brief="x")
        app._collect_daily_llm_usage(report)
        assert report.daily_llm_usage is not None
        assert report.daily_llm_usage.run_count == 2
        assert report.daily_llm_usage.usage.total_tokens == 1200

    def test_budget_exceeded_warns(self, caplog):
        from trendpluse.models.signal import DailyReport

        app = self._make_app(settings=MagicMock(daily_token_budget=100))
        report = DailyReport(date="2026-01-01", summary_brief="x")
        app._collect_daily_llm_usage(report)
        assert report.daily_llm_usage is not None
        assert report.daily_llm_usage.usage.total_tokens > 100


class TestFinalizerAggregatesDailyUsage:
    def test_agent_metrics_summary_includes_daily_llm_usage(self):
        from trendpluse.app.report_finalizer import DailyReportFinalizer
        from trendpluse.models.signal import DailyReport

        report = DailyReport(date="2026-01-01", summary_brief="x")
        report.daily_llm_usage = AgentMetricsSummary.from_runs(
            [AgentRunMetrics(model="glm", total_cost_usd=1.0)]
        )
        DailyReportFinalizer._refresh_agent_metrics(report)
        assert report.agent_metrics_summary is not None
        assert report.agent_metrics_summary.run_count == 1
        assert report.agent_metrics_summary.total_cost_usd == 1.0
