"""TrendAnalyzer 重试机制测试

使用 TDD 方法测试 AI 调用失败后的自动重试功能。
"""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial


def _signal() -> Signal:
    return Signal(
        id="test-1",
        title="测试 PR",
        type="capability",
        category="engineering",
        impact_score=4,
        why_it_matters="测试",
        sources=["https://github.com/test/repo/pull/1"],
        related_repos=["test/repo"],
    )


def _material() -> AnalysisMaterial:
    return AnalysisMaterial.from_pr_details(
        {
            "repo_name": "test/repo",
            "number": 1,
            "title": "Test PR",
            "body": "Test body",
            "author": "user1",
        }
    )


def _mock_client_with_side_effect(side_effect) -> MagicMock:
    """构造 async 路径可用的 mock client（side_effect 为 async 函数）。"""
    mock_client = MagicMock()
    mock_client.chat.completions.create_with_completion = AsyncMock(
        side_effect=side_effect
    )
    return mock_client


class TestTrendAnalyzerRetry:
    """TrendAnalyzer 重试机制测试类"""

    @pytest.mark.asyncio
    async def test_retry_on_transient_failure(self):
        """测试：临时失败时应重试并最终成功"""
        signal = _signal()
        call_count = [0]

        async def fails_then_succeeds(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] < 3:
                from anthropic import APITimeoutError

                raise APITimeoutError("模拟 API 超时")
            return (signal, SimpleNamespace(usage=None, model=None))

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.async_instructor_client = _mock_client_with_side_effect(
            fails_then_succeeds
        )

        signal_out = await analyzer.analyze_material_async(_material())

        assert call_count[0] == 3
        assert signal_out.id == "test-1"

    @pytest.mark.asyncio
    async def test_retry_exhausted_raises_error(self):
        """测试：重试耗尽后应抛出异常"""
        call_count = [0]

        async def always_fails(*args, **kwargs):
            call_count[0] += 1
            from anthropic import APITimeoutError

            raise APITimeoutError("模拟 API 持续超时")

        analyzer = TrendAnalyzer(
            api_key="test-key",
            retry_max_attempts=3,
            retry_wait_min=0,
            retry_wait_max=0,
        )
        analyzer.async_instructor_client = _mock_client_with_side_effect(always_fails)

        with pytest.raises(Exception):  # noqa: B017 - tenacity reraise 原始异常
            await analyzer.analyze_material_async(_material())
        assert call_count[0] == 3

    @pytest.mark.asyncio
    async def test_no_retry_on_permanent_error(self):
        """测试：永久错误（如认证失败）不应重试"""
        call_count = [0]

        async def auth_error(*args, **kwargs):
            call_count[0] += 1
            from anthropic import AuthenticationError

            raise AuthenticationError("invalid api key")

        analyzer = TrendAnalyzer(
            api_key="test-key",
            retry_max_attempts=3,
            retry_wait_min=0,
            retry_wait_max=0,
        )
        analyzer.async_instructor_client = _mock_client_with_side_effect(auth_error)

        with pytest.raises(Exception):  # noqa: B017
            await analyzer.analyze_material_async(_material())
        # 永久错误只调用一次，不重试
        assert call_count[0] == 1
