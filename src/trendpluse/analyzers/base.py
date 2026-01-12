"""LLM 分析器基类

提供 Anthropic 客户端初始化和响应文本提取的共享功能。
"""

from abc import ABC
from typing import Any

from anthropic import Anthropic
from anthropic.types import TextBlock

from trendpluse.models.signal import Signal


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

    def _create_signal_from_dict(
        self,
        item: dict[str, Any],
        index: int,
        sources: list[str],
        related_repos: list[str],
    ) -> Signal:
        """从字典创建 Signal 对象

        Args:
            item: LLM 返回的信号字典
            index: 信号索引（用于生成 ID）
            sources: 来源链接列表
            related_repos: 相关仓库列表

        Returns:
            Signal 对象

        Raises:
            KeyError: 如果缺少必需字段
        """
        # 合并 related_repos（LLM 返回的 + 外部传入的）
        ai_related_repos = item.get("related_repos", [])
        merged_repos = list(set(related_repos + ai_related_repos))

        return Signal(
            id=f"signal-{index}",
            title=item["title"],
            type=item["type"],
            category=item["category"],
            impact_score=item["impact_score"],
            why_it_matters=item["why_it_matters"],
            sources=sources,
            related_repos=merged_repos,
        )
