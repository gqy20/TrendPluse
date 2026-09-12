"""Breaking Changes 检测器

使用 AI 分析 release notes，检测 breaking changes 和不兼容更新。
"""

import json
from typing import Any

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.config import DEFAULT_ANTHROPIC_MODEL
from trendpluse.logger import get_logger
from trendpluse.prompts import render_prompt

logger = get_logger(__name__)


class BreakingChangesDetector(BaseLLMAnalyzer):
    """Breaking Changes 检测器

    分析 release notes，检测 breaking changes 和不兼容更新。
    使用 Anthropic 模式（手动解析 JSON），因为需要处理多个 release 的批量分析。
    """

    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_ANTHROPIC_MODEL,
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        """初始化检测器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL（可选）
        """
        # 使用 Anthropic 模式（手动解析 JSON）
        super().__init__(
            api_key=api_key,
            model=model,
            base_url=base_url,
            use_instructor=False,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    async def detect_breaking_changes_async(
        self, releases: dict[str, Any]
    ) -> list[dict]:
        detailed_releases = releases.get("detailed_releases", [])
        if not detailed_releases:
            logger.debug("BreakingChangesDetector: 收到空 release 列表")
            return []

        logger.debug(
            "BreakingChangesDetector: 开始分析 "
            f"{len(detailed_releases)} 个 releases（异步）"
        )
        try:
            llm_response = await self._call_llm_async(detailed_releases)
            breaking_changes = self._parse_response(llm_response)
            return breaking_changes
        except Exception as e:
            logger.debug(
                f"BreakingChangesDetector: 异步检测失败 - {type(e).__name__}: {e}"
            )
            return []

    async def _call_llm_async(self, releases: list[dict[str, Any]]) -> str:
        prompt = self._build_prompt(releases)

        async def _call():
            return await self.async_client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}],
            )

        message = await self._run_with_llm_retry_async(_call)
        self._record_llm_usage(message)
        return self._extract_text_from_response(message)

    def _build_prompt(self, releases: list[dict[str, Any]]) -> str:
        """构建分析 prompt

        Args:
            releases: release 数据列表

        Returns:
            prompt 文本
        """
        releases_text = json.dumps(releases, ensure_ascii=False, indent=2)
        return render_prompt(
            "breaking_changes_detector.analysis", releases_text=releases_text
        )

    def _parse_response(self, llm_response: str) -> list[dict]:
        """解析 LLM 响应

        Args:
            llm_response: LLM 响应文本

        Returns:
            breaking changes 列表
        """
        try:
            # 移除可能的 markdown 代码块标记
            response_text = llm_response.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:]  # 移除 ```json
            elif response_text.startswith("```"):
                response_text = response_text[3:]  # 移除 ```
            if response_text.endswith("```"):
                response_text = response_text[:-3]  # 移除结尾的 ```
            response_text = response_text.strip()

            # 解析 JSON
            data = json.loads(response_text)

            # 处理空数组
            if not data:
                return []

            # 验证返回的是列表
            if not isinstance(data, list):
                return []

            return data

        except (json.JSONDecodeError, TypeError, ValueError):
            # 解析失败时返回空列表
            return []
