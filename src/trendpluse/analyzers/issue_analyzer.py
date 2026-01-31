"""Issue 分析器

使用 AI 对 Issue 进行分类、情绪分析和痛点提取。
"""

from typing import Literal

from pydantic import BaseModel, Field

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.logger import get_logger
from trendpluse.models.issue import IssueInfo
from trendpluse.models.signal import Signal
from trendpluse.utils.retry import create_anthropic_retry_decorator

logger = get_logger(__name__)

_llm_retry = create_anthropic_retry_decorator()


class IssueAnalysis(BaseModel):
    """Issue 分析结果

    AI 对 Issue 进行分类和情绪分析的结果。
    """

    # 基础分类
    category: Literal["bug_report", "feature_request", "question", "discussion"] = (
        Field(description="Issue 分类")
    )

    # 情绪分析
    sentiment: Literal["positive", "neutral", "negative"] = Field(
        description="情绪倾向"
    )
    sentiment_score: float = Field(ge=-1.0, le=1.0, description="情绪分数 -1到1")

    # 痛点提取（Bug Report）
    pain_point: str | None = Field(default=None, description="用户痛点描述")
    affected_area: str | None = Field(default=None, description="影响的功能区域")

    # 需求提取（Feature Request）
    feature_description: str | None = Field(default=None, description="功能需求描述")
    priority: Literal["low", "medium", "high", "critical"] = Field(
        default="medium", description="优先级"
    )

    # 技术标签
    tech_tags: list[str] = Field(default_factory=list, description="技术标签")


class IssueAnalyzer(BaseLLMAnalyzer):
    """Issue 分析器

    使用 AI 对 Issue 进行分类、情绪分析和痛点提取。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str | None = None,
    ):
        """初始化分析器

        Args:
            api_key: API Key
            model: 模型名称
            base_url: API Base URL
        """
        super().__init__(api_key, model, base_url, use_instructor=True)

    def analyze(self, issue: IssueInfo) -> IssueAnalysis:
        """分析单个 Issue

        Args:
            issue: Issue 信息

        Returns:
            分析结果
        """
        # 构建 Prompt
        prompt = f"""分析以下 GitHub Issue，提取关键信息。

Issue 标题: {issue.title}
Issue 内容: {issue.body or "(无内容)"}
仓库: {issue.repo}
状态: {issue.state}
标签: {", ".join(issue.labels)}
评论数: {issue.comments}
链接: {issue.url}

请分析并返回结构化数据，包括：
1. 分类: bug_report / feature_request / question / discussion
2. 情绪: positive / neutral / negative
3. 痛点: 用户遇到的问题（如果适用）
4. 功能需求: 用户想要的功能（如果是 feature_request）
5. 优先级: low / medium / high / critical
6. 技术标签: 相关技术栈关键词
"""

        analysis = self._call_llm_for_analysis(prompt)
        return analysis

    @_llm_retry
    def _call_llm_for_analysis(self, prompt: str) -> IssueAnalysis:  # type: ignore[no-any-return]
        """调用 LLM 分析 Issue

        Args:
            prompt: 分析提示词

        Returns:
            分析结果
        """
        analysis = self.client.chat.completions.create(
            model=self.model,
            response_model=IssueAnalysis,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
        )
        return analysis

    def analyze_batch(
        self,
        issues: list[IssueInfo],
        max_workers: int = 3,
    ) -> dict[str, IssueAnalysis]:
        """批量分析 Issues

        Args:
            issues: Issue 列表
            max_workers: 最大并行数

        Returns:
            {issue_key: 分析结果} 字典，格式为 "repo#issue_id"
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        results = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_issue = {
                executor.submit(self.analyze, issue): issue for issue in issues
            }

            for future in as_completed(future_to_issue):
                issue = future_to_issue[future]
                try:
                    analysis = future.result()
                    key = f"{issue.repo}#{issue.issue_id}"
                    results[key] = analysis
                except Exception as e:
                    logger.debug(f"分析 Issue {issue.repo}#{issue.issue_id} 失败: {e}")

        return results

    def extract_signals(
        self,
        issues: list[IssueInfo],
        analyses: dict[str, IssueAnalysis],
    ) -> list[Signal]:
        """从 Issue 分析结果中提取趋势信号

        Args:
            issues: Issue 列表
            analyses: 分析结果字典

        Returns:
            信号列表
        """
        signals = []

        for issue in issues:
            key = f"{issue.repo}#{issue.issue_id}"
            analysis = analyses.get(key)

            if not analysis:
                continue

            # 只将高价值的 Issue 转换为信号
            if not self._is_high_value_issue(issue, analysis):
                continue

            signal = self._create_signal(issue, analysis)
            if signal:
                signals.append(signal)

        return signals

    def _is_high_value_issue(self, issue: IssueInfo, analysis: IssueAnalysis) -> bool:
        """判断是否为高价值 Issue

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            True 如果是高价值 Issue
        """
        # 高优先级功能请求
        if analysis.category == "feature_request" and analysis.priority in (
            "high",
            "critical",
        ):
            return True

        # 有讨论价值的（评论数 >= 5）
        if issue.comments >= 5:
            return True

        # 负面情绪的 Bug（用户痛点）
        if analysis.category == "bug_report" and analysis.sentiment == "negative":
            return True

        return False

    def _create_signal(
        self, issue: IssueInfo, analysis: IssueAnalysis
    ) -> Signal | None:  # type: ignore[no-any-return]
        """创建信号对象

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            信号对象，如果不适合则返回 None
        """
        # 确定信号类型
        signal_type: Literal[
            "capability",
            "abstraction",
            "workflow",
            "eval",
            "safety",
            "performance",
            "commit",
            "release",
        ] = {
            "bug_report": "workflow",
            "feature_request": "capability",
            "question": "abstraction",
            "discussion": "abstraction",
        }.get(analysis.category, "workflow")  # type: ignore[assignment]

        # 构建描述
        if analysis.pain_point:
            description = f"用户痛点: {analysis.pain_point}"
        elif analysis.feature_description:
            description = f"功能需求: {analysis.feature_description}"
        else:
            description = issue.title

        return Signal(
            id=f"issue-{issue.repo.replace('/', '-')}-{issue.issue_id}",
            title=issue.title,
            type=signal_type,
            category="engineering",  # Issue 主要反映工程问题
            impact_score=self._calculate_impact_score(issue, analysis),
            why_it_matters=description,
            sources=[issue.url],
            related_repos=[issue.repo],
        )

    def _calculate_impact_score(self, issue: IssueInfo, analysis: IssueAnalysis) -> int:
        """计算影响评分 (1-5)

        评分规则：
        - 特殊规则：critical + comments>=10 = 5（最高分）
        - 基础分：0 评论=1，有评论=2
        - 评论数加分：>=20:+1, >=10:+0.5, >=5:+0, <5:0
        - 优先级加分：critical:+2, high:+1, medium:+0.5, low:0
        - 负面情绪加分：low:+0.5
        - 四舍五入，限制在 1-5

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            影响评分 1-5
        """
        # 特殊规则：critical + 高评论数 = 最高分
        if analysis.priority == "critical" and issue.comments >= 10:
            return 5

        # 基础分：有评论的至少 2 分
        score = 2.0 if issue.comments > 0 else 1.0

        # 评论数加分（额外）
        if issue.comments >= 20:
            score += 1
        elif issue.comments >= 10:
            score += 0.5

        # 优先级加分
        priority_score = {
            "low": 0,
            "medium": 0.5,
            "high": 1,
            "critical": 2,
        }
        score += priority_score.get(analysis.priority, 0)

        # 负面情绪加分（仅 low）
        if analysis.sentiment == "negative" and analysis.priority == "low":
            score += 0.5

        # 四舍五入并限制范围
        rounded = int(score + 0.5)
        return max(1, min(5, rounded))
