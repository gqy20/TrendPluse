"""Release 分析器

使用 AI 分析 release 内容，提取版本升级趋势和重要特性。
"""

import json
from typing import Any

from pydantic import ValidationError

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.config import DEFAULT_ANTHROPIC_MODEL
from trendpluse.logger import get_logger
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial
from trendpluse.prompts import render_prompt

logger = get_logger(__name__)


class ReleaseAnalyzer(BaseLLMAnalyzer):
    """Release 分析器

    分析 release 内容，提取版本升级趋势和重要特性。
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
        """初始化分析器

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

    @staticmethod
    def _material_to_release(material: AnalysisMaterial) -> dict[str, Any]:
        """将分析材料还原为 release 分析所需结构。"""
        raw_payload = dict(material.raw_payload)
        if "repo" not in raw_payload:
            raw_payload["repo"] = material.source_ref.repo
        if "tag_name" not in raw_payload:
            raw_payload["tag_name"] = material.source_ref.external_id
        if "html_url" not in raw_payload:
            raw_payload["html_url"] = material.source_ref.url
        if "body" not in raw_payload:
            raw_payload["body"] = material.body
        if "name" not in raw_payload:
            raw_payload["name"] = material.title
        if "author" not in raw_payload:
            raw_payload["author"] = material.author
        if "created_at" not in raw_payload:
            raw_payload["created_at"] = material.created_at
        if "published_at" not in raw_payload:
            raw_payload["published_at"] = material.updated_at
        if "version_info" not in raw_payload:
            raw_payload["version_info"] = material.source_ref.metadata.get(
                "version_info", {}
            )
        return raw_payload

    def analyze_materials(self, materials: list[AnalysisMaterial]) -> list[Signal]:
        """分析 release 材料列表。"""
        detailed_releases = [
            self._material_to_release(material)
            for material in materials
            if material.source_ref.source_type == "release"
        ]
        return self._analyze_release_payloads(detailed_releases)

    async def analyze_materials_async(
        self, materials: list[AnalysisMaterial]
    ) -> list[Signal]:
        """异步分析 release 材料列表。"""
        detailed_releases = [
            self._material_to_release(material)
            for material in materials
            if material.source_ref.source_type == "release"
        ]
        return await self._analyze_release_payloads_async(detailed_releases)

    def _analyze_release_payloads(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """分析 release 数据列表。"""
        # 处理空列表
        if not detailed_releases:
            logger.debug("ReleaseAnalyzer: 收到空 release 列表")
            return []

        logger.debug(f"ReleaseAnalyzer: 开始分析 {len(detailed_releases)} 个 releases")

        try:
            # 调用 LLM 分析
            logger.debug("ReleaseAnalyzer: 调用 LLM 分析...")
            llm_response = self._call_llm(detailed_releases)
            logger.debug(f"ReleaseAnalyzer: LLM 响应长度: {len(llm_response)} 字符")
            logger.debug(f"ReleaseAnalyzer: LLM 响应预览: {llm_response[:500]}...")

            # 解析响应
            signals = self._parse_signals(llm_response, detailed_releases)
            logger.debug(f"ReleaseAnalyzer: 解析得到 {len(signals)} 个信号")

            return signals

        except Exception as e:
            # 出错时返回空列表
            logger.debug(f"ReleaseAnalyzer: 分析失败 - {type(e).__name__}: {e}")
            return []

    async def _analyze_release_payloads_async(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        if not detailed_releases:
            logger.debug("ReleaseAnalyzer: 收到空 release 列表")
            return []

        logger.debug(
            f"ReleaseAnalyzer: 开始分析 {len(detailed_releases)} 个 releases（异步）"
        )
        try:
            llm_response = await self._call_llm_async(detailed_releases)
            signals = self._parse_signals(llm_response, detailed_releases)
            return signals
        except Exception as e:
            logger.debug(f"ReleaseAnalyzer: 异步分析失败 - {type(e).__name__}: {e}")
            return []

    def _call_llm(self, releases: list[dict[str, Any]]) -> str:
        """调用 LLM 分析 releases

        Args:
            releases: release 数据列表

        Returns:
            LLM 响应文本
        """
        # 构建 prompt
        prompt = self._build_prompt(releases)

        # 调用 API
        def _call():
            return self.client.messages.create(  # type: ignore[call-overload]
                model=self.model,
                max_tokens=4096,
                temperature=0.3,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

        # 使用基类方法提取文本
        message = self._run_with_llm_retry(_call)
        self._record_llm_usage(message)
        return self._extract_text_from_response(message)

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
        return render_prompt("release_analyzer.analysis", releases_text=releases_text)

    def _parse_signals(
        self, llm_response: str, releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """解析 LLM 响应为信号列表

        使用 Pydantic 验证确保数据格式正确：
        - 必需字段完整性
        - 字段类型正确性
        - 枚举值有效性
        - 数值范围检查

        Args:
            llm_response: LLM 响应文本
            releases: 原始 release 数据

        Returns:
            验证通过的信号列表
        """
        try:
            # 1. 使用基类方法提取 JSON（移除 ```json 标记）
            response_text = self._extract_json_from_markdown(llm_response)

            # 2. 解析 JSON
            data = json.loads(response_text)

            # 3. 处理空数组
            if not data:
                return []

            # 4. 转换为 Signal 对象（使用 Pydantic 验证）
            signals = []
            skipped_count = 0

            for idx, item in enumerate(data):
                # 构建来源链接
                if idx < len(releases):
                    repo = releases[idx].get("repo", "")
                    tag_name = releases[idx].get("tag_name", "")
                    release_url = f"https://github.com/{repo}/releases/tag/{tag_name}"
                    sources = [release_url]
                    related_repos = [repo]
                else:
                    sources = item.get("sources", [])
                    related_repos = item.get("related_repos", [])

                # 使用新的验证方法（Pydantic 自动验证）
                signal = self._validate_and_create_signal(
                    item=item,
                    index=idx,
                    sources=sources,
                    related_repos=related_repos,
                )

                if signal is not None:
                    signals.append(signal)
                else:
                    skipped_count += 1

            # 记录跳过的信号数量（用于调试）
            if skipped_count > 0:
                logger.debug(f"ReleaseAnalyzer: 跳过 {skipped_count} 个验证失败的信号")

            return signals

        except (json.JSONDecodeError, ValidationError) as e:
            # JSON 解析失败或验证失败时返回空列表
            logger.debug(f"ReleaseAnalyzer: 解析失败 - {type(e).__name__}: {e}")
            return []
