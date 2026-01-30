"""周报 AI 聚合器

使用 LLM 对一周的信号进行整合分析，识别核心趋势。
"""

from anthropic import Anthropic
from pydantic import BaseModel, Field


class CoreTrend(BaseModel):
    """核心趋势

    AI 识别出的本周核心技术趋势，包含相关信号。
    """

    title: str = Field(description="趋势标题")
    theme: str = Field(description="主题分类，如 architecture, tooling, research 等")
    description: str = Field(description="趋势描述")
    signal_ids: list[str] = Field(
        description="组成此趋势的信号 ID 列表", default_factory=list
    )
    impact_level: int = Field(description="影响级别 1-5", ge=1, le=5, default=3)


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

    与机械聚合不同，AI 聚合器可以：
    - 识别语义相关的信号（即使关键词不同）
    - 将多个相关信号整合为一个趋势
    - 生成有意义的趋势描述
    - 提供周报级别的智能摘要
    """

    def __init__(self, api_key: str, base_url: str | None = None, use_llm: bool = True):
        """初始化聚合器

        Args:
            api_key: Anthropic API 密钥
            base_url: API 基础 URL（可选）
            use_llm: 是否使用 LLM，False 时降级到机械聚合
        """
        self._client = Anthropic(api_key=api_key, base_url=base_url)
        self._use_llm = use_llm

    def aggregate(self, signals: list) -> WeeklyAggregationResult:
        """聚合信号列表

        Args:
            signals: 信号列表

        Returns:
            聚合结果
        """
        if not signals:
            return WeeklyAggregationResult(
                core_trends=[],
                summary_brief="本周暂无信号",
                total_signals=0,
            )

        if self._use_llm:
            return self._aggregate_with_llm(signals)
        else:
            return self._aggregate_fallback(signals)

    def _aggregate_with_llm(self, signals: list) -> WeeklyAggregationResult:
        """使用 LLM 聚合

        Args:
            signals: 信号列表

        Returns:
            AI 聚合结果
        """
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

        try:
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

            # 提取响应
            result_text = response.content[0].text
            result = WeeklyAggregationResult.model_validate_json(result_text)
            result.total_signals = len(signals)
            return result

        except Exception as e:
            from trendpluse.logger import get_logger

            logger = get_logger(__name__)
            logger.warning(f"LLM 聚合失败: {e}，降级到机械聚合")
            return self._aggregate_fallback(signals)

    def _aggregate_fallback(self, signals: list) -> WeeklyAggregationResult:
        """降级到机械聚合

        当 LLM 不可用时，使用简单的排序策略。

        Args:
            signals: 信号列表

        Returns:
            机械聚合结果
        """
        from trendpluse.models.signal import Signal

        # 按 impact_score 降序排序
        sorted_signals = sorted(
            signals,
            key=lambda s: s.impact_score if isinstance(s, Signal) else 0,
            reverse=True,
        )

        # 取 Top 5 作为核心趋势
        core_trends = []
        for sig in sorted_signals[:5]:
            if isinstance(sig, Signal):
                # 推断主题
                theme = self._infer_theme(sig.type, sig.category)

                trend = CoreTrend(
                    title=sig.title,
                    theme=theme,
                    description=sig.why_it_matters,
                    signal_ids=[sig.id],
                    impact_level=sig.impact_score,
                )
                core_trends.append(trend)

        summary_brief = (
            f"本周共发现 {len(signals)} 个信号，{len(core_trends)} 个高影响趋势"
        )

        return WeeklyAggregationResult(
            core_trends=core_trends,
            summary_brief=summary_brief,
            total_signals=len(signals),
        )

    def _infer_theme(self, signal_type: str, category: str) -> str:
        """推断主题分类

        Args:
            signal_type: 信号类型
            category: 信号分类

        Returns:
            主题分类
        """
        # 研究类信号
        if category == "research":
            return "research"

        # 工程类信号根据类型推断
        type_theme_map = {
            "capability": "tooling",
            "abstraction": "architecture",
            "workflow": "workflow",
            "performance": "performance",
            "safety": "safety",
            "eval": "research",
        }
        return type_theme_map.get(signal_type, "ecosystem")
