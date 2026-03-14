"""TrendAnalyzer 验证错误重试测试

测试当 LLM 返回的数据格式不正确导致 Pydantic 验证失败时，
系统应该能够自动重试并最终成功。
"""

from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import DailyReport, ReportStats, Signal


def create_validation_error():
    """创建模拟的 ValidationError 用于测试"""
    # 使用更简单的方式：尝试用错误的类型创建模型来触发 ValidationError
    try:
        # 尝试用字符串代替 ReportStats 对象，应该触发 ValidationError
        DailyReport(
            date="2026-03-10",
            summary_brief="test",
            stats="invalid_string",  # 错误：应该是 ReportStats 对象
        )
    except ValidationError as e:
        return e
    raise AssertionError("Should have raised ValidationError")


class TestValidationErrorRetry:
    """测试验证错误重试机制"""

    def test_retry_on_validation_error(self):
        """测试：当 stats 字段返回字符串而非对象时，应该重试并最终成功"""
        mock_client = MagicMock()

        call_count = [0]
        validation_error = create_validation_error()

        def mock_create_fails_then_succeeds(*args, **kwargs):
            call_count[0] += 1
            # 前两次抛出 ValidationError，第三次返回正确的对象
            if call_count[0] < 3:
                raise validation_error
            # 第三次返回正确格式的报告
            return DailyReport(
                date="2026-03-10",
                summary_brief="Test summary",
                stats=ReportStats(
                    total_signals=10,
                    total_prs_analyzed=5,
                    total_commits_analyzed=3,
                    total_releases=2,
                    high_impact_signals=2,
                ),
            )

        mock_client.chat.completions.create.side_effect = (
            mock_create_fails_then_succeeds
        )

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        # 使用同步方法测试
        signals = [
            Signal(
                id="test-1",
                title="Test Signal",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test",
                sources=[],
                related_repos=[],
            )
        ]

        # 调用 generate_report，验证重试逻辑
        report = analyzer.generate_report(signals, "2026-03-10")

        # 验证调用了 3 次（初始调用 + 2 次重试）
        assert call_count[0] == 3
        assert report.date == "2026-03-10"

    def test_retry_exhausted_on_validation_error(self):
        """测试：持续验证失败时应该抛出异常"""
        mock_client = MagicMock()

        validation_error = create_validation_error()

        def mock_create_always_fails(*args, **kwargs):
            # 始终抛出 ValidationError
            raise validation_error

        mock_client.chat.completions.create.side_effect = mock_create_always_fails

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        signals = [
            Signal(
                id="test-1",
                title="Test Signal",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="Test",
                sources=[],
                related_repos=[],
            )
        ]

        # 超过最大重试次数后应该抛出 ValidationError
        with pytest.raises(ValidationError):
            analyzer.generate_report(signals, "2026-03-10")
