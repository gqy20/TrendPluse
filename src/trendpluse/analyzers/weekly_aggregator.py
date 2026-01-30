"""周报 AI 聚合器

使用 LLM 对一周的信号进行整合分析，识别核心趋势。
"""

from anthropic import Anthropic
from anthropic.types import TextBlock
from pydantic import BaseModel, Field

from trendpluse.models.signal import CoreTrend


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

    def __init__(self, api_key: str, base_url: str | None = None):
        """初始化聚合器

        Args:
            api_key: Anthropic API 密钥
            base_url: API 基础 URL（可选）
        """
        self._client = Anthropic(api_key=api_key, base_url=base_url)

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

请以 JSON 格式返回，遵循 WeeklyAggregationResult 模型。
"""

        response = self._client.messages.create(
            model="glm-4.7",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        # 提取响应 - 获取第一个文本块
        text_block: TextBlock = response.content[0]  # type: ignore[assignment]
        result_text = text_block.text

        # 清理可能的 markdown 代码块标记
        result_text = self._extract_json_from_markdown(result_text)

        result = WeeklyAggregationResult.model_validate_json(result_text)
        result.total_signals = len(signals)
        return result

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
