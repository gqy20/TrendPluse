"""WeeklyAggregator AI 聚合器测试

测试 WeeklyAggregator 的 AI 整合分析功能。
"""

from unittest.mock import MagicMock, patch

import pytest
from trendpluse.analyzers.weekly_aggregator import (  # type: ignore
    CoreTrend,
    WeeklyAggregationResult,
    WeeklyAggregator,
)

from trendpluse.models.signal import Signal


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

    @pytest.fixture
    def sample_signals(self):
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

    @pytest.fixture
    def mock_llm_response(self):
        """Mock LLM 响应"""
        return WeeklyAggregationResult(
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
        )

    def test_aggregate_empty_signals(self, sample_signals):
        """测试聚合空信号列表"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        # Act
        result = aggregator.aggregate([])

        # Assert
        assert result.core_trends == []
        assert result.total_signals == 0

    @patch("trendpluse.analyzers.base.anthropic")
    def test_aggregate_with_llm(
        self, mock_anthropic, sample_signals, mock_llm_response
    ):
        """测试使用 LLM 聚合"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        # Mock LLM 响应
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text=mock_llm_response.model_dump_json())]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.Anthropic.return_value = mock_client

        # Act
        result = aggregator.aggregate(sample_signals)

        # Assert
        assert len(result.core_trends) == 2
        assert result.core_trends[0].title == "异步架构成为本周主流"
        assert result.core_trends[0].theme == "architecture"
        assert "sig-1" in result.core_trends[0].signal_ids
        assert result.total_signals == 4

    @patch("trendpluse.analyzers.base.anthropic")
    def test_aggregate_signal_deduplication_by_theme(
        self, mock_anthropic, sample_signals, mock_llm_response
    ):
        """测试按主题去重和分组"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key")

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text=mock_llm_response.model_dump_json())]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.Anthropic.return_value = mock_client

        # Act
        result = aggregator.aggregate(sample_signals)

        # Assert - 验证信号被正确分组
        architecture_trend = next(
            (t for t in result.core_trends if t.theme == "architecture"), None
        )
        assert architecture_trend is not None
        assert len(architecture_trend.signal_ids) == 3

    def test_aggregate_fallback_without_llm(self, sample_signals):
        """测试无 LLM 时的降级处理"""
        # Arrange
        aggregator = WeeklyAggregator(api_key="test-key", use_llm=False)

        # Act
        result = aggregator.aggregate(sample_signals)

        # Assert - 降级到简单聚合（按 impact_score 排序取 Top 5）
        assert len(result.core_trends) > 0
        # 验证是按分数排序的
        if len(result.core_trends) > 1:
            assert (
                result.core_trends[0].impact_level >= result.core_trends[1].impact_level
            )
