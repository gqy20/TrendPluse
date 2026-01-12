"""LLM 分析器基类

提供 Anthropic 客户端初始化和响应文本提取的共享功能。
"""

from abc import ABC

from anthropic import Anthropic
from anthropic.types import TextBlock


class BaseLLMAnalyzer(ABC):
    """LLM 分析器基类"""

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str | None = None,
    ):
        """初始化分析器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL（可选）
        """
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

        # 初始化 Anthropic 客户端
        if base_url:
            self.client = Anthropic(api_key=api_key, base_url=base_url)
        else:
            self.client = Anthropic(api_key=api_key)

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
