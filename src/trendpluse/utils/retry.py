"""重试装饰器工厂函数

统一管理 LLM 和 GitHub API 的重试策略，避免重复的 @retry 装饰器配置。
所有重试在等待前打 WARNING 日志（含失败原因与等待时长），重试过程不再静默。
"""

import ssl
from collections.abc import Callable

import anthropic
import httpx
from github import GithubException
from pydantic import ValidationError
from tenacity import (
    RetryCallState,
    retry,
    retry_if_exception,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from trendpluse.logger import get_logger

logger = get_logger(__name__)


def _log_retry_attempt(retry_state: RetryCallState) -> None:
    """tenacity before_sleep 回调：重试等待前记录失败原因。"""

    if retry_state.outcome is None or not retry_state.outcome.failed:
        logger.warning(
            "调用重试（第 %d 次尝试后）",
            retry_state.attempt_number,
        )
        return

    wait_seconds = retry_state.next_action.sleep if retry_state.next_action else 0.0
    exc = retry_state.outcome.exception()
    if isinstance(exc, ValidationError):
        # Pydantic 验证失败日志很长，只记第一个错误
        detail = f"ValidationError: {exc.errors()[:1]}"
    elif exc is not None:
        text = str(exc)[:200]
        detail = f"{type(exc).__name__}: {text}" if text else type(exc).__name__
    else:
        detail = "未知错误"
    logger.warning(
        "第 %d 次尝试失败: %s，%.1fs 后重试",
        retry_state.attempt_number,
        detail[:300],
        wait_seconds,
    )


def create_anthropic_retry_decorator(
    max_attempts: int = 3,
    wait_min: int = 1,
    wait_max: int = 10,
    retry_validation_error: bool = True,
) -> Callable:
    """创建 Anthropic API 重试装饰器

    用于 LLM 调用的自动重试，处理临时网络错误和速率限制。

    Args:
        max_attempts: 最大重试次数（默认 3）
        wait_min: 最小等待时间（秒，默认 1）
        wait_max: 最大等待时间（秒，默认 10）
        retry_validation_error: 是否重试 Pydantic 验证错误（默认 True）

    Returns:
        重试装饰器

    Example:
        >>> retry_decorator = create_anthropic_retry_decorator()
        >>>
        >>> @retry_decorator
        >>> def call_llm():
        >>>     ...

    可重试的错误类型:
        - anthropic.APITimeoutError: API 超时
        - anthropic.RateLimitError: 速率限制
        - ValidationError: Pydantic 验证错误（如 LLM 返回格式不正确）

    重试策略:
        - 指数退避：1s → 2s → 4s → ... → wait_max
        - 超过最大次数后重新抛出异常
    """
    # 可重试的临时错误类型
    _retryable_errors: tuple[type, ...] = (
        anthropic.APITimeoutError,
        anthropic.RateLimitError,
    )

    # 添加 Pydantic 验证错误（LLM 返回格式不正确时的重试）
    if retry_validation_error:
        _retryable_errors = _retryable_errors + (ValidationError,)

    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=wait_min, max=wait_max),
        retry=retry_if_exception_type(_retryable_errors),
        before_sleep=_log_retry_attempt,
        reraise=True,
    )


def create_github_retry_decorator(
    max_attempts: int = 3,
    wait_min: int = 4,
    wait_max: int = 60,
) -> Callable:
    """创建 GitHub API 重试装饰器

    用于 GitHub API 调用的自动重试，处理临时网络错误和速率限制。

    Args:
        max_attempts: 最大重试次数（默认 3）
        wait_min: 最小等待时间（秒，默认 4）
        wait_max: 最大等待时间（秒，默认 60）

    Returns:
        重试装饰器

    Example:
        >>> retry_decorator = create_github_retry_decorator()
        >>>
        >>> @retry_decorator
        >>> def fetch_github_data():
        >>>     ...

    可重试的错误类型:
        - GithubException: 速率限制（429）与 5xx 服务端错误
        - ssl.SSLError / httpx.TransportError: 瞬时网络中断
          （如 GraphQL 查询的 UNEXPECTED_EOF_WHILE_READING）
        - 4xx 永久错误不重试

    重试策略:
        - 指数退避：4s → 8s → 16s → ... → wait_max
        - 超过最大次数后重新抛出异常

    Note:
        GitHub API 速率限制建议更长的等待时间（默认最小 4 秒）
    """

    def _retryable(exc: BaseException) -> bool:
        """只重试可恢复错误（速率限制 429 + 5xx + 瞬时网络错误）。"""
        if isinstance(exc, GithubException):
            status = getattr(exc, "status", 0) or 0
            return status == 429 or status >= 500
        return isinstance(exc, (ssl.SSLError, httpx.TransportError, ConnectionError))

    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=wait_min, max=wait_max),
        retry=retry_if_exception(_retryable),
        before_sleep=_log_retry_attempt,
        reraise=True,
    )
