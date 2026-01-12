"""TrendAnalyzer 重试机制测试

使用 TDD 方法测试 AI 调用失败后的自动重试功能。
"""

from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import Signal


class TestTrendAnalyzerRetry:
    """TrendAnalyzer 重试机制测试类"""

    @pytest.fixture
    def mock_signal(self):
        """Mock API 响应"""
        return Signal(
            id="test-1",
            title="测试 PR",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="这是一个测试 PR",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

    def test_retry_on_transient_failure(self, mock_signal):
        """测试：临时失败时应重试并最终成功"""
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_fails_then_succeeds(*args, **kwargs):
            call_count[0] += 1
            # 前两次失败，第三次成功
            if call_count[0] < 3:
                from anthropic import APITimeoutError

                raise APITimeoutError("模拟 API 超时")
            return mock_signal

        mock_client.chat.completions.create.side_effect = (
            mock_create_fails_then_succeeds
        )

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        pr = {
            "repo_name": "test/repo",
            "number": 1,
            "title": "Test PR",
            "body": "Test body",
            "author": "user1",
            "url": "https://github.com/test/repo/pull/1",
        }

        # 应该在重试后成功
        signal = analyzer.analyze_pr(pr)

        # 验证调用了 3 次（初始调用 + 2 次重试）
        assert call_count[0] == 3
        assert signal.title == "测试 PR"

    def test_retry_exhausted_raises_error(self):
        """测试：超过最大重试次数后应抛出异常"""
        mock_client = MagicMock()

        def mock_create_always_fails(*args, **kwargs):
            from anthropic import APITimeoutError

            raise APITimeoutError("持续 API 超时")

        mock_client.chat.completions.create.side_effect = mock_create_always_fails

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        pr = {
            "repo_name": "test/repo",
            "number": 1,
            "title": "Test PR",
            "body": "Test body",
            "author": "user1",
            "url": "https://github.com/test/repo/pull/1",
        }

        # 应该在重试耗尽后抛出异常
        with pytest.raises(Exception):
            analyzer.analyze_pr(pr)

    def test_no_retry_on_permanent_error(self):
        """测试：永久性错误不应重试（如认证错误）"""
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_auth_error(*args, **kwargs):
            call_count[0] += 1
            from anthropic import AuthenticationError

            raise AuthenticationError("无效的 API 密钥")

        mock_client.chat.completions.create.side_effect = mock_create_auth_error

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        pr = {
            "repo_name": "test/repo",
            "number": 1,
            "title": "Test PR",
            "body": "Test body",
            "author": "user1",
            "url": "https://github.com/test/repo/pull/1",
        }

        # 认证错误应该快速失败
        try:
            analyzer.analyze_pr(pr)
        except Exception:
            pass

        # 验证只调用了一次（没有重试）
        assert call_count[0] == 1
