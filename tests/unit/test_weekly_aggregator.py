"""WeeklyAggregator AI 聚合器测试

测试 WeeklyAggregator 的 AI 整合分析功能。
"""

from types import SimpleNamespace
from typing import Any, cast
from unittest.mock import patch

import pytest
from anthropic.types import TextBlock, ThinkingBlock

from trendpluse.analyzers.weekly_aggregator import (
    WeeklyAggregationResult,
    WeeklyAggregator,
)
from trendpluse.models.signal import CoreTrend, Signal


@pytest.fixture
def sample_signals():
    """创建示例信号"""
    return [
        Signal(
            id="sig-1",
            title="项目 A 新增异步支持",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="采用异步架构提升性能",
            sources=["https://github.com/test/a"],
            related_repos=["test/a"],
        ),
        Signal(
            id="sig-2",
            title="项目 B 重构为异步架构",
            type="abstraction",
            category="engineering",
            impact_score=4,
            why_it_matters="从同步迁移到异步",
            sources=["https://github.com/test/b"],
            related_repos=["test/b"],
        ),
        Signal(
            id="sig-3",
            title="项目 C 新增异步工具",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="提供异步开发工具",
            sources=["https://github.com/test/c"],
            related_repos=["test/c"],
        ),
        Signal(
            id="sig-4",
            title="新型模型架构研究",
            type="eval",
            category="research",
            impact_score=5,
            why_it_matters="提出新的模型架构",
            sources=["https://github.com/test/d"],
            related_repos=["test/d"],
        ),
    ]


class TestWeeklyAggregationResult:
    """测试周报聚合结果模型"""

    def test_create_minimal_result(self):
        """测试创建最小聚合结果"""
        # Arrange & Act
        result = WeeklyAggregationResult(
            core_trends=[],
            summary_brief="测试周报",
        )

        # Assert
        assert result.core_trends == []
        assert result.summary_brief == "测试周报"
        assert result.total_signals == 0

    def test_create_full_result(self):
        """测试创建完整聚合结果"""
        # Arrange
        trend = CoreTrend(
            title="AI 工具链爆发",
            theme="tooling",
            description="本周多个 AI 工具链项目发布重要更新",
            signal_ids=["sig-1", "sig-2"],
            impact_level=5,
        )

        # Act
        result = WeeklyAggregationResult(
            core_trends=[trend],
            summary_brief="本周共发现 10 个信号，形成 1 个核心趋势",
            total_signals=10,
        )

        # Assert
        assert len(result.core_trends) == 1
        assert result.core_trends[0].title == "AI 工具链爆发"
        assert result.total_signals == 10


class TestCoreTrend:
    """测试核心趋势模型"""

    def test_create_trend(self):
        """测试创建趋势"""
        # Arrange & Act
        trend = CoreTrend(
            title="异步架构普及",
            theme="architecture",
            description="多个项目采用异步架构",
            signal_ids=["sig-1", "sig-2", "sig-3"],
            impact_level=4,
        )

        # Assert
        assert trend.title == "异步架构普及"
        assert trend.theme == "architecture"
        assert len(trend.signal_ids) == 3
        assert trend.impact_level == 4


class TestWeeklyAggregator:
    """测试周报聚合器"""

    def test_aggregate_empty_signals(self):
        """测试聚合空信号列表"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        # Act
        result = aggregator.aggregate([])

        # Assert
        assert result.core_trends == []
        assert result.total_signals == 0

    @patch.object(
        WeeklyAggregator,
        "aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[
                CoreTrend(
                    title="异步架构成为本周主流",
                    theme="architecture",
                    description="多个项目采用或新增异步支持，形成明显趋势",
                    signal_ids=["sig-1", "sig-2", "sig-3"],
                    impact_level=5,
                ),
                CoreTrend(
                    title="模型架构创新",
                    theme="research",
                    description="新型模型架构提出研究突破",
                    signal_ids=["sig-4"],
                    impact_level=5,
                ),
            ],
            summary_brief=(
                "本周共分析 4 个信号，识别出 2 个核心趋势：异步架构普及、模型架构创新"
            ),
            total_signals=4,
        ),
    )
    def test_aggregate_with_llm(self, mock_aggregate, sample_signals):
        """测试使用 LLM 聚合"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        # Act
        result = aggregator.aggregate(sample_signals)

        # Assert
        assert len(result.core_trends) == 2
        assert result.core_trends[0].title == "异步架构成为本周主流"
        assert result.core_trends[0].theme == "architecture"
        assert "sig-1" in result.core_trends[0].signal_ids
        assert result.total_signals == 4

    @patch.object(
        WeeklyAggregator,
        "aggregate",
        return_value=WeeklyAggregationResult(
            core_trends=[
                CoreTrend(
                    title="异步架构成为本周主流",
                    theme="architecture",
                    description="多个项目采用或新增异步支持，形成明显趋势",
                    signal_ids=["sig-1", "sig-2", "sig-3"],
                    impact_level=5,
                ),
                CoreTrend(
                    title="模型架构创新",
                    theme="research",
                    description="新型模型架构提出研究突破",
                    signal_ids=["sig-4"],
                    impact_level=5,
                ),
            ],
            summary_brief=(
                "本周共分析 4 个信号，识别出 2 个核心趋势：异步架构普及、模型架构创新"
            ),
            total_signals=4,
        ),
    )
    def test_aggregate_signal_deduplication_by_theme(
        self, mock_aggregate, sample_signals
    ):
        """测试按主题去重和分组"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        # Act
        result = aggregator.aggregate(sample_signals)

        # Assert - 验证信号被正确分组
        architecture_trend = next(
            (t for t in result.core_trends if t.theme == "architecture"), None
        )
        assert architecture_trend is not None
        assert len(architecture_trend.signal_ids) == 3

    def test_aggregate_skips_thinking_block_and_reads_text_block(self, sample_signals):
        """同步聚合应跳过 thinking block 并读取后续文本块。"""
        aggregator = WeeklyAggregator(api_key="test-key")
        response = SimpleNamespace(
            content=[
                ThinkingBlock(signature="sig", thinking="先思考", type="thinking"),
                TextBlock(
                    text=(
                        '{"core_trends":[{"title":"异步架构成为本周主流",'
                        '"theme":"architecture","description":"多个项目拥抱异步",'
                        '"signal_ids":["sig-1","sig-2"],"impact_level":5}],'
                        '"summary_brief":"本周聚焦异步架构演进"}'
                    ),
                    type="text",
                ),
            ]
        )
        aggregator._client.messages.create = lambda *args, **kwargs: response
        aggregator._llm_retry = lambda func: func

        result = aggregator.aggregate(sample_signals)

        assert result.summary_brief == "本周聚焦异步架构演进"
        assert result.core_trends[0].title == "异步架构成为本周主流"
        assert result.total_signals == len(sample_signals)

    def test_aggregate_retries_when_llm_returns_invalid_json(self, sample_signals):
        """同步聚合在首次返回非法 JSON 时应自动重试。"""
        aggregator = WeeklyAggregator(api_key="test-key", retry_max_attempts=2)
        responses = iter(
            [
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"未闭合"',
                            type="text",
                        )
                    ]
                ),
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text=(
                                '{"core_trends":[{"title":"异步架构成为本周主流",'
                                '"theme":"architecture","description":"多个项目拥抱异步",'
                                '"signal_ids":["sig-1","sig-2"],"impact_level":5}],'
                                '"summary_brief":"本周聚焦异步架构演进"}'
                            ),
                            type="text",
                        )
                    ]
                ),
            ]
        )
        aggregator._client.messages.create = lambda *args, **kwargs: next(responses)
        aggregator._llm_retry = lambda func: func

        result = aggregator.aggregate(sample_signals)

        assert result.summary_brief == "本周聚焦异步架构演进"
        assert result.core_trends[0].title == "异步架构成为本周主流"
        assert result.total_signals == len(sample_signals)

    def test_aggregate_raises_after_repeated_invalid_json(self, sample_signals):
        """同步聚合多次失败应抛异常（失败可见，不模板降级）。"""
        aggregator = WeeklyAggregator(api_key="test-key", retry_max_attempts=2)
        responses = iter(
            [
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"未闭合"',
                            type="text",
                        )
                    ]
                ),
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"仍未闭合"',
                            type="text",
                        )
                    ]
                ),
            ]
        )
        aggregator._client.messages.create = lambda *args, **kwargs: next(responses)
        aggregator._llm_retry = lambda func: func

        with pytest.raises(RuntimeError, match="周报聚合连续失败"):
            aggregator.aggregate(sample_signals)

    @pytest.mark.asyncio
    async def test_aggregate_async_skips_thinking_block_and_reads_text_block(
        self, sample_signals
    ):
        """异步聚合应跳过 thinking block 并读取后续文本块。"""
        aggregator = WeeklyAggregator(api_key="test-key")
        response = SimpleNamespace(
            content=[
                ThinkingBlock(signature="sig", thinking="先思考", type="thinking"),
                TextBlock(
                    text=(
                        '{"core_trends":[{"title":"模型架构创新",'
                        '"theme":"research","description":"研究信号形成主趋势",'
                        '"signal_ids":["sig-4"],"impact_level":5}],'
                        '"summary_brief":"本周研究创新活跃"}'
                    ),
                    type="text",
                ),
            ]
        )

        async def _fake_retry(_func):
            return response

        cast(Any, aggregator)._run_with_llm_retry_async = _fake_retry

        result = await aggregator.aggregate_async(sample_signals)

        assert result.summary_brief == "本周研究创新活跃"
        assert result.core_trends[0].title == "模型架构创新"
        assert result.total_signals == len(sample_signals)

    @pytest.mark.asyncio
    async def test_aggregate_async_retries_when_llm_returns_invalid_json(
        self, sample_signals
    ):
        """异步聚合在首次返回非法 JSON 时应自动重试。"""
        aggregator = WeeklyAggregator(api_key="test-key", retry_max_attempts=2)
        responses = iter(
            [
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"未闭合"',
                            type="text",
                        )
                    ]
                ),
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text=(
                                '{"core_trends":[{"title":"模型架构创新",'
                                '"theme":"research","description":"研究信号形成主趋势",'
                                '"signal_ids":["sig-4"],"impact_level":5}],'
                                '"summary_brief":"本周研究创新活跃"}'
                            ),
                            type="text",
                        )
                    ]
                ),
            ]
        )

        async def _fake_retry(_func):
            return next(responses)

        cast(Any, aggregator)._run_with_llm_retry_async = _fake_retry

        result = await aggregator.aggregate_async(sample_signals)

        assert result.summary_brief == "本周研究创新活跃"
        assert result.core_trends[0].title == "模型架构创新"
        assert result.total_signals == len(sample_signals)

    @pytest.mark.asyncio
    async def test_aggregate_async_raises_after_repeated_invalid_json(
        self, sample_signals
    ):
        """异步聚合多次失败应抛异常（失败可见，不模板降级）。"""
        aggregator = WeeklyAggregator(api_key="test-key", retry_max_attempts=2)
        responses = iter(
            [
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"未闭合"',
                            type="text",
                        )
                    ]
                ),
                SimpleNamespace(
                    content=[
                        TextBlock(
                            text='{"core_trends":[{"title":"仍未闭合"',
                            type="text",
                        )
                    ]
                ),
            ]
        )

        async def _fake_retry(_func):
            return next(responses)

        cast(Any, aggregator)._run_with_llm_retry_async = _fake_retry

        with pytest.raises(RuntimeError, match="周报聚合连续失败"):
            await aggregator.aggregate_async(sample_signals)


class TestWeeklyAggregatorModelWiring:
    """模型配置接线测试。

    回归背景：模型曾被硬编码为 "glm-4.7"，切换到第三方网关后该模型不存在
    （503 model_not_found），会导致每周一的周报 AI 聚合必然失败。
    """

    def _ok_response(self) -> SimpleNamespace:
        return SimpleNamespace(
            content=[
                TextBlock(
                    text=(
                        '{"core_trends":[{"title":"模型可配置",'
                        '"theme":"architecture","description":"模型跟随配置",'
                        '"signal_ids":["sig-1"],"impact_level":4}],'
                        '"summary_brief":"本周模型配置生效"}'
                    ),
                    type="text",
                )
            ]
        )

    def test_sync_call_uses_configured_model(self, sample_signals):
        """同步聚合应把配置的模型传给 API，而不是硬编码值。"""
        aggregator = WeeklyAggregator(api_key="test-key", model="my-gateway-model")
        captured: dict[str, Any] = {}

        def _fake_create(*args, **kwargs):
            captured.update(kwargs)
            return self._ok_response()

        aggregator._client.messages.create = _fake_create
        aggregator._llm_retry = lambda func: func

        aggregator.aggregate(sample_signals)

        assert captured["model"] == "my-gateway-model"

    def test_model_defaults_to_config_default(self):
        """未显式传 model 时应回落到配置里的默认模型。"""
        from trendpluse.config import DEFAULT_ANTHROPIC_MODEL

        aggregator = WeeklyAggregator(api_key="test-key")

        assert aggregator._model == DEFAULT_ANTHROPIC_MODEL

    def test_hardcoded_glm_model_is_gone(self):
        """源码中不应再残留硬编码的 glm-4.7。"""
        from pathlib import Path

        source = (
            Path(__file__).resolve().parents[2]
            / "src"
            / "trendpluse"
            / "analyzers"
            / "weekly_aggregator.py"
        ).read_text(encoding="utf-8")

        assert 'model="glm-4.7"' not in source

    @pytest.mark.asyncio
    async def test_async_call_awaits_async_client(self, sample_signals):
        """异步聚合必须走 AsyncAnthropic 客户端。

        回归背景：此前 `aggregate_async` 对同步 client 的返回值做 `await`，
        运行时会抛 TypeError；因测试替换了 `_run_with_llm_retry_async`
        而长期未被发现。这里不替换重试包装，直接跑真实 await 路径。
        """
        aggregator = WeeklyAggregator(api_key="test-key", model="my-gateway-model")
        captured: dict[str, Any] = {}

        async def _fake_create(*args, **kwargs):
            captured.update(kwargs)
            return self._ok_response()

        aggregator._async_client.messages.create = _fake_create

        result = await aggregator.aggregate_async(sample_signals)

        assert captured["model"] == "my-gateway-model"
        assert result.summary_brief == "本周模型配置生效"
