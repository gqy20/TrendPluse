"""LLM 分析器基类

提供统一的 LLM 客户端初始化，支持 instructor 和 Anthropic 两种模式。
"""

import asyncio
import inspect
from abc import ABC
from typing import Any

import anthropic
import instructor
from anthropic import Anthropic, AsyncAnthropic
from anthropic.types import TextBlock
from pydantic import BaseModel, ValidationError

from trendpluse.logger import get_logger
from trendpluse.models.signal import Signal
from trendpluse.utils.retry import create_anthropic_retry_decorator

logger = get_logger(__name__)

# Instructor 和 Anthropic 客户端的联合类型
LLMClient = instructor.Instructor | Anthropic


class BaseLLMAnalyzer(ABC):
    """LLM 分析器基类

    默认使用 instructor 模式，提供更好的类型安全和结构化输出。
    """

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str | None = None,
        use_instructor: bool = True,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        """初始化分析器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL（可选）
            use_instructor: 是否使用 instructor 模式（默认 True）
        """
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.use_instructor = use_instructor
        self.retry_max_attempts = retry_max_attempts
        self.retry_wait_min = retry_wait_min
        self.retry_wait_max = retry_wait_max

        # 初始化客户端（使用类型忽略以避免类型检查错误）
        if use_instructor:
            # instructor 模式：支持结构化输出（直接返回 Pydantic 模型）
            anthropic_client = Anthropic(api_key=api_key, base_url=base_url)
            self.client = instructor.from_anthropic(anthropic_client)  # type: ignore[assignment]
        else:
            # Anthropic 模式：返回文本需要手动解析（向后兼容）
            if base_url:
                self.client = Anthropic(api_key=api_key, base_url=base_url)  # type: ignore[assignment]
            else:
                self.client = Anthropic(api_key=api_key)  # type: ignore[assignment]

        # 初始化异步客户端（用于 async I/O 并发）
        self.async_client = AsyncAnthropic(api_key=api_key, base_url=base_url)  # type: ignore[assignment]
        self.async_instructor_client = None
        if use_instructor:
            self.async_instructor_client = instructor.from_anthropic(self.async_client)  # type: ignore[assignment]

        logger.info("LLM 初始化: %s model=%s", self.__class__.__name__, self.model)

    def _run_with_llm_retry(self, func):
        """统一封装 LLM 调用重试逻辑（可配置）"""
        decorator = create_anthropic_retry_decorator(
            max_attempts=self.retry_max_attempts,
            wait_min=self.retry_wait_min,
            wait_max=self.retry_wait_max,
        )
        wrapped = decorator(func)
        return wrapped()

    async def _maybe_await(self, value):
        if inspect.isawaitable(value):
            return await value
        return value

    async def _run_with_llm_retry_async(self, func):
        """异步重试封装（与同步重试配置保持一致）

        支持重试的错误类型：
        - APITimeoutError: API 超时
        - RateLimitError: 速率限制
        - ValidationError: Pydantic 验证错误（如 LLM 返回格式不正确）
        """
        retryable_errors = (
            anthropic.APITimeoutError,
            anthropic.RateLimitError,
            ValidationError,
        )
        attempts = self.retry_max_attempts
        wait_min = self.retry_wait_min
        wait_max = self.retry_wait_max

        for attempt in range(1, attempts + 1):
            try:
                return await self._maybe_await(func())
            except retryable_errors:
                if attempt >= attempts:
                    raise
                backoff = wait_min * (2 ** (attempt - 1))
                await asyncio.sleep(min(wait_max, backoff))

    def _extract_text_from_response(self, message) -> str:
        """从 Anthropic 消息响应中提取文本内容

        Args:
            message: Anthropic API 返回的消息对象

        Returns:
            提取的文本内容，如果找不到 TextBlock 则返回空字符串
        """
        for block in message.content:
            if isinstance(block, TextBlock):
                return block.text  # type: ignore[no-any-return]
            # 兼容测试中的 MagicMock 对象
            if hasattr(block, "text"):
                return block.text  # type: ignore[no-any-return]
        # 如果没有找到 TextBlock，返回空字符串
        return ""

    @staticmethod
    def _extract_json_from_markdown(response: str) -> str:
        """从 LLM 响应中提取 JSON 内容

        移除可能的 markdown 代码块标记（```json 或 ```）。

        Args:
            response: LLM 响应文本

        Returns:
            提取的 JSON 字符串

        Example:
            >>> response = '```json\\n{"key": "value"}\\n```'
            >>> BaseLLMAnalyzer._extract_json_from_markdown(response)
            '{"key": "value"}'
        """
        # 移除可能的 markdown 代码块标记
        response_text = response.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]  # 移除 ```json
        elif response_text.startswith("```"):
            response_text = response_text[3:]  # 移除 ```
        if response_text.endswith("```"):
            response_text = response_text[:-3]  # 移除结尾的 ```
        return response_text.strip()

    def _validate_and_create_signal(
        self,
        item: dict[str, Any],
        index: int,
        sources: list[str],
        related_repos: list[str],
        model_class: type[BaseModel] = Signal,
    ) -> Signal | None:
        """使用 Pydantic 验证并创建信号对象

        通过 Pydantic 模型验证 LLM 返回的数据，确保：
        - 所有必需字段都存在
        - 字段类型正确
        - 枚举值有效
        - 数值在有效范围内

        Args:
            item: LLM 返回的信号字典
            index: 信号索引（用于生成 ID）
            sources: 来源链接列表
            related_repos: 相关仓库列表
            model_class: Pydantic 模型类（默认 Signal）

        Returns:
            验证通过的模型对象，验证失败返回 None

        Example:
            >>> signal = analyzer._validate_and_create_signal(
            ...     item={"title": "新特性", "type": "capability", ...},
            ...     index=0,
            ...     sources=["https://github.com/..."],
            ...     related_repos=["owner/repo"]
            ... )
        """
        try:
            # 合并 related_repos（LLM 返回的 + 外部传入的）
            ai_related_repos = item.get("related_repos", [])
            merged_repos = list(set(related_repos + ai_related_repos))

            # 添加系统字段
            validated_item = {
                **item,
                "id": f"signal-{index}",
                "sources": sources,
                "related_repos": merged_repos,
            }

            # 使用 Pydantic 验证并创建对象
            result = model_class(**validated_item)
            # 类型断言：model_class 默认是 Signal，返回 Signal | None
            return result  # type: ignore[return-value]

        except ValidationError:
            # 验证失败时返回 None，让调用者决定如何处理
            # 可以记录验证错误的详细信息
            return None
