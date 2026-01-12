"""重试工具函数测试"""

import anthropic
from github import GithubException
from pytest import raises

from trendpluse.utils.retry import (
    create_anthropic_retry_decorator,
    create_github_retry_decorator,
)


class TestCreateAnthropicRetryDecorator:
    """测试 Anthropic 重试装饰器工厂"""

    def test_returns_callable(self):
        """应该返回可调用的装饰器"""
        decorator = create_anthropic_retry_decorator()
        assert callable(decorator)

    def test_decorator_returns_wrapper(self):
        """装饰器应该返回包装后的函数"""
        decorator = create_anthropic_retry_decorator()

        @decorator
        def dummy_func():
            return "success"

        assert callable(dummy_func)
        assert dummy_func() == "success"

    def test_retries_on_timeout_error(self):
        """应该重试 APITimeoutError"""
        decorator = create_anthropic_retry_decorator(max_attempts=2)

        call_count = 0

        @decorator
        def failing_func():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise anthropic.APITimeoutError("Timeout")
            return "success"

        result = failing_func()
        assert result == "success"
        assert call_count == 2

    def test_retries_on_rate_limit_error(self):
        """应该重试 RateLimitError"""
        decorator = create_anthropic_retry_decorator(max_attempts=2)

        call_count = 0

        # 创建模拟的 response 对象
        class MockRequest:
            pass

        class MockResponse:
            status_code = 429
            request = MockRequest()
            headers = {}

        @decorator
        def failing_func():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise anthropic.RateLimitError(
                    "Rate limit", response=MockResponse(), body={}
                )
            return "success"

        result = failing_func()
        assert result == "success"
        assert call_count == 2

    def test_reraises_after_max_attempts(self):
        """超过最大重试次数后应该重新抛出异常"""
        decorator = create_anthropic_retry_decorator(max_attempts=2)

        @decorator
        def always_failing_func():
            raise anthropic.APITimeoutError("Always timeout")

        with raises(anthropic.APITimeoutError):
            always_failing_func()

    def test_custom_max_attempts(self):
        """应该支持自定义最大重试次数"""
        decorator = create_anthropic_retry_decorator(max_attempts=5)

        call_count = 0

        @decorator
        def failing_func():
            nonlocal call_count
            call_count += 1
            if call_count < 4:
                raise anthropic.APITimeoutError("Timeout")
            return "success"

        result = failing_func()
        assert result == "success"
        assert call_count == 4

    def test_custom_wait_parameters(self):
        """应该支持自定义等待参数"""
        decorator = create_anthropic_retry_decorator(
            max_attempts=3,
            wait_min=2,
            wait_max=5,
        )

        @decorator
        def dummy_func():
            return "success"

        assert dummy_func() == "success"


class TestCreateGithubRetryDecorator:
    """测试 GitHub 重试装饰器工厂"""

    def test_returns_callable(self):
        """应该返回可调用的装饰器"""
        decorator = create_github_retry_decorator()
        assert callable(decorator)

    def test_decorator_returns_wrapper(self):
        """装饰器应该返回包装后的函数"""
        decorator = create_github_retry_decorator()

        @decorator
        def dummy_func():
            return "success"

        assert callable(dummy_func)
        assert dummy_func() == "success"

    def test_retries_on_github_exception(self):
        """应该重试 GithubException"""
        decorator = create_github_retry_decorator(max_attempts=2)

        call_count = 0

        @decorator
        def failing_func():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise GithubException(403, {"message": "Rate limit"})
            return "success"

        result = failing_func()
        assert result == "success"
        assert call_count == 2

    def test_reraises_after_max_attempts(self):
        """超过最大重试次数后应该重新抛出异常"""
        decorator = create_github_retry_decorator(max_attempts=2)

        @decorator
        def always_failing_func():
            raise GithubException(403, {"message": "Always error"})

        with raises(GithubException):
            always_failing_func()

    def test_custom_wait_parameters(self):
        """应该支持自定义等待参数"""
        decorator = create_github_retry_decorator(
            max_attempts=3,
            wait_min=4,
            wait_max=60,
        )

        @decorator
        def dummy_func():
            return "success"

        assert dummy_func() == "success"


class TestRetryDecoratorConsistency:
    """测试重试装饰器的一致性"""

    def test_anthropic_default_params(self):
        """Anthropic 装饰器应该有默认参数"""
        decorator = create_anthropic_retry_decorator()
        # 应该能正常工作，使用默认参数
        assert callable(decorator)

    def test_github_default_params(self):
        """GitHub 装饰器应该有默认参数"""
        decorator = create_github_retry_decorator()
        # 应该能正常工作，使用默认参数
        assert callable(decorator)
