"""周报 AI 聚合器

使用 LLM 对一周的信号进行整合分析，识别核心趋势。
"""

import asyncio
import json
from collections.abc import Sequence
from json import JSONDecodeError

import anthropic
from anthropic import Anthropic
from anthropic.types import TextBlock
from pydantic import BaseModel, Field

from trendpluse.logger import get_logger
from trendpluse.models.signal import CoreTrend
from trendpluse.utils.retry import create_anthropic_retry_decorator

logger = get_logger(__name__)


class WeeklyAggregationResult(BaseModel):
    """周报聚合结果

    AI 对一周信号进行整合分析后的结果。
    """

    core_trends: list[CoreTrend] = Field(
        description="核心趋势列表，AI 整合分析后识别的 3-5 个主要趋势",
        default_factory=list,
    )
    summary_brief: str = Field(description="周报摘要")
    total_signals: int = Field(description="总信号数", default=0)


class WeeklyAggregator:
    """周报聚合器

    使用 LLM 对一周信号进行 AI 整合分析，识别核心技术趋势。

    功能：
    - 识别语义相关的信号（即使关键词不同）
    - 将多个相关信号整合为一个趋势
    - 生成有意义的趋势描述
    - 提供周报级别的智能摘要
    """

    def __init__(
        self,
        api_key: str,
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        """初始化聚合器

        Args:
            api_key: Anthropic API 密钥
            base_url: API 基础 URL（可选）
        """
        self._client = Anthropic(api_key=api_key, base_url=base_url)
        self._retry_max_attempts = retry_max_attempts
        self._retry_wait_min = retry_wait_min
        self._retry_wait_max = retry_wait_max
        self._llm_retry = create_anthropic_retry_decorator(
            max_attempts=retry_max_attempts,
            wait_min=retry_wait_min,
            wait_max=retry_wait_max,
        )

    @staticmethod
    def _extract_text_from_response(response) -> str:
        """从 Anthropic 响应中提取首个文本块内容。"""
        content: Sequence[object] = getattr(response, "content", [])

        for block in content:
            if isinstance(block, TextBlock):
                return block.text

            text = getattr(block, "text", None)
            if isinstance(text, str) and text.strip():
                return text

        block_types = [
            str(getattr(block, "type", type(block).__name__)) for block in content
        ]
        raise ValueError(
            f"LLM 响应未包含文本块，实际内容块类型: {block_types or ['<empty>']}"
        )

    def _parse_result_text(self, result_text: str) -> WeeklyAggregationResult:
        """解析 LLM 返回的聚合 JSON。"""
        cleaned_text = self._extract_json_from_markdown(result_text)

        try:
            return WeeklyAggregationResult.model_validate_json(cleaned_text)
        except Exception:
            try:
                data = json.loads(cleaned_text)
            except JSONDecodeError:
                normalized = cleaned_text.strip()
                if normalized.startswith("{") and normalized.endswith("}"):
                    normalized = normalized.replace("True", "true").replace(
                        "False", "false"
                    )
                    normalized = normalized.replace("'", '"')
                    data = json.loads(normalized)
                else:
                    raise

            return WeeklyAggregationResult.model_validate(data)

    async def _run_with_llm_retry_async(self, func):
        retryable_errors = (anthropic.APITimeoutError, anthropic.RateLimitError)
        attempts = self._retry_max_attempts
        wait_min = self._retry_wait_min
        wait_max = self._retry_wait_max

        for attempt in range(1, attempts + 1):
            try:
                return await func()
            except retryable_errors:
                if attempt >= attempts:
                    raise
                backoff = wait_min * (2 ** (attempt - 1))
                await asyncio.sleep(min(wait_max, backoff))

    def aggregate(self, signals: list) -> WeeklyAggregationResult:
        """聚合信号列表

        Args:
            signals: 信号列表

        Returns:
            聚合结果

        Raises:
            Exception: LLM 调用失败时抛出异常
        """
        if not signals:
            return WeeklyAggregationResult(
                core_trends=[],
                summary_brief="本周暂无信号",
                total_signals=0,
            )

        from trendpluse.models.signal import Signal

        # 构建提示词
        signal_summaries = []
        for sig in signals:
            if isinstance(sig, Signal):
                signal_summaries.append(
                    f"- [{sig.id}] {sig.title}\n"
                    f"  类型: {sig.type} | 影响: {sig.impact_score}/5\n"
                    f"  说明: {sig.why_it_matters}\n"
                    f"  仓库: {', '.join(sig.related_repos)}"
                )

        prompt = f"""你是一个技术趋势分析专家。请分析以下 {len(signals)} 个信号，
识别出本周的核心技术趋势（3-5 个）。

## 信号列表

{chr(10).join(signal_summaries)}

## 分析要求

1. **趋势识别**：将语义相关的信号整合为一个趋势
   - 例如：3 个关于"异步架构"的信号 → "异步架构普及"趋势
   - 不同类型的信号可以归为同一趋势（如 capability + abstraction）

2. **趋势命名**：为每个趋势生成简洁有力的标题

3. **主题分类**：使用以下主题之一
   - architecture: 架构模式
   - tooling: 工具链/框架
   - performance: 性能优化
   - safety: 安全性
   - research: 研究创新
   - workflow: 工作流
   - ecosystem: 生态发展

4. **趋势描述**：说明为什么这是本周的核心趋势

5. **周报摘要**：生成 1-2 句话的本周总览

## 返回格式要求

请直接返回 JSON 格式（不要使用 markdown 代码块）。

返回示例（请严格遵循此格式）:
{{"core_trends":[{{"title":"趋势标题","theme":"architecture","description":"趋势描述","signal_ids":["sig-1","sig-2"],"impact_level":5}}],"summary_brief":"本周总览"}}

**重要**：
- 必须是完整的 JSON 对象（以 {{ 开头，}} 结尾）
- 不要使用 markdown 代码块（```json）
- core_trends 和 summary_brief 都是必需字段
"""

        def _call():
            return self._client.messages.create(
                model="glm-4.7",
                max_tokens=2000,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

        last_error: Exception | None = None

        for attempt in range(1, self._retry_max_attempts + 1):
            response = self._llm_retry(_call)()
            result_text = self._extract_text_from_response(response)

            try:
                result = self._parse_result_text(result_text)
            except Exception as exc:
                last_error = exc
                logger.warning(
                    "周报聚合结果解析失败，第 %s/%s 次重试: %s",
                    attempt,
                    self._retry_max_attempts,
                    exc,
                )
                if attempt >= self._retry_max_attempts:
                    raise
                continue

            result.total_signals = len(signals)
            return result

        if last_error is not None:
            raise last_error
        raise RuntimeError("周报聚合未返回结果")

    async def aggregate_async(self, signals: list) -> WeeklyAggregationResult:
        if not signals:
            return WeeklyAggregationResult(
                core_trends=[],
                summary_brief="本周暂无信号",
                total_signals=0,
            )

        from trendpluse.models.signal import Signal

        signal_summaries = []
        for sig in signals:
            if isinstance(sig, Signal):
                signal_summaries.append(
                    f"- [{sig.id}] {sig.title}\n"
                    f"  类型: {sig.type} | 影响: {sig.impact_score}/5\n"
                    f"  说明: {sig.why_it_matters}\n"
                    f"  仓库: {', '.join(sig.related_repos)}"
                )

        prompt = f"""你是一个技术趋势分析专家。请分析以下 {len(signals)} 个信号，
识别出本周的核心技术趋势（3-5 个）。

## 信号列表

{chr(10).join(signal_summaries)}

## 分析要求

1. **趋势识别**：将语义相关的信号整合为一个趋势
   - 例如：3 个关于"异步架构"的信号 → "异步架构普及"趋势
   - 不同类型的信号可以归为同一趋势（如 capability + abstraction）

2. **趋势命名**：为每个趋势生成简洁有力的标题

3. **主题分类**：使用以下主题之一
   - architecture: 架构模式
   - tooling: 工具链/框架
   - performance: 性能优化
   - safety: 安全性
   - research: 研究创新
   - workflow: 工作流
   - ecosystem: 生态发展

4. **趋势描述**：说明为什么这是本周的核心趋势

5. **周报摘要**：生成 1-2 句话的本周总览

## 返回格式要求

请直接返回 JSON 格式（不要使用 markdown 代码块）。

返回示例（请严格遵循此格式）:
{{"core_trends":[{{"title":"趋势标题","theme":"architecture","description":"趋势描述","signal_ids":["sig-1","sig-2"],"impact_level":5}}],"summary_brief":"本周总览"}}

**重要**：
- 必须是完整的 JSON 对象（以 {{ 开头，}} 结尾）
- 不要使用 markdown 代码块（```json）
- core_trends 和 summary_brief 都是必需字段
"""

        async def _call():
            return await self._client.messages.create(
                model="glm-4.7",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )

        last_error: Exception | None = None

        for attempt in range(1, self._retry_max_attempts + 1):
            response = await self._run_with_llm_retry_async(_call)
            result_text = self._extract_text_from_response(response)

            try:
                result = self._parse_result_text(result_text)
            except Exception as exc:
                last_error = exc
                logger.warning(
                    "异步周报聚合结果解析失败，第 %s/%s 次重试: %s",
                    attempt,
                    self._retry_max_attempts,
                    exc,
                )
                if attempt >= self._retry_max_attempts:
                    raise
                continue

            result.total_signals = len(signals)
            return result

        if last_error is not None:
            raise last_error
        raise RuntimeError("异步周报聚合未返回结果")

    def _extract_json_from_markdown(self, response: str) -> str:
        """从 markdown 代码块中提取 JSON

        Args:
            response: LLM 返回的响应文本

        Returns:
            清理后的 JSON 字符串
        """
        # 移除可能的 markdown 代码块标记
        text = response.strip()
        if text.startswith("```json"):
            text = text[7:]  # 移除 ```json
        elif text.startswith("```"):
            text = text[3:]  # 移除 ```
        if text.endswith("```"):
            text = text[:-3]  # 移除结尾的 ```
        return text.strip()
