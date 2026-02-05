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

    def analyze_releases(self, releases: dict[str, Any]) -> list[Signal]:
        """分析 release 列表

        Args:
            releases: release 数据字典

        Returns:
            信号列表
        """
        # 获取详细的 release 列表
        detailed_releases = releases.get("detailed_releases", [])

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

    async def analyze_releases_async(self, releases: dict[str, Any]) -> list[Signal]:
        detailed_releases = releases.get("detailed_releases", [])
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
        return self._extract_text_from_response(message)

    def _build_prompt(self, releases: list[dict[str, Any]]) -> str:
        """构建分析 prompt

        Args:
            releases: release 数据列表

        Returns:
            prompt 文本
        """
        releases_text = json.dumps(releases, ensure_ascii=False, indent=2)

        prompt = """\
你是一个技术趋势分析专家。请分析以下 GitHub Releases，提取有价值的\
版本升级趋势和重要特性信息。

## Release 数据

{releases_text}

## 分析要求

请识别以下内容：

1. **重大版本升级**：
   - 主版本升级（major version bump）
   - Breaking changes
   - 重大架构变更

2. **重要新特性**：
   - 新功能发布（capability）
   - 抽象层改进（abstraction）
   - 工作流优化（workflow）
   - 安全性增强（safety）
   - 性能优化（performance）

3. **评估标准**：
   - 优先关注主版本升级（如 v1.0.0 → v2.0.0）
   - 关注重要的次版本更新（如包含 breaking changes）
   - **过滤掉纯 bug 修复的补丁版本**（如 v1.0.0 → v1.0.1）
   - 关注影响范围广的特性
   - 关注技术创新点

## 输出格式

请以 JSON 数组格式返回，每个元素包含：

```json
[
  {{
    "title": "简短标题（5-10字）",
    "type": "信号类型（capability/abstraction/workflow/eval/safety/performance）",
    "category": "分类（engineering/research）",
    "impact_score": 影响评分（1-5）,
    "why_it_matters": "为什么重要（1-2句话）",
    "related_repos": ["相关仓库名"],
    "sources": ["release链接"]
  }}
]
```

注意：
- **所有文本内容必须使用中文**（title、why_it_matters 等）
- **只返回真正有价值的重大更新**
- **忽略纯 bug 修复的补丁版本**
- **如果没有重要更新，返回空数组 []**
- impact_score 基于影响范围和重要性（主版本升级通常 4-5 分）
"""

        return prompt.format(releases_text=releases_text)

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
