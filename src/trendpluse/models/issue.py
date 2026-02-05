"""Issue 相关数据模型

定义 Issue 分析相关的数据结构。
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

from trendpluse.utils.text import sanitize_optional_text


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

    @field_validator("pain_point", "affected_area", "feature_description")
    @classmethod
    def _sanitize_optional_text(cls, value: str | None) -> str | None:
        """清洗可选文本字段。

        将无效占位符或空文本转为 None，避免污染聚合结果。
        """
        return sanitize_optional_text(value)


class IssueInfo(BaseModel):
    """单个 Issue 信息

    从 GitHub API 获取的 Issue 数据。
    """

    repo: str = Field(description="仓库名称 owner/repo")
    issue_id: int = Field(description="Issue 编号")
    title: str = Field(description="Issue 标题")
    body: str | None = Field(default=None, description="Issue 内容")
    state: str = Field(description="状态: open/closed")
    author: str = Field(description="创建者")
    created_at: datetime = Field(description="创建时间")
    updated_at: datetime = Field(description="更新时间")
    closed_at: datetime | None = Field(default=None, description="关闭时间")
    comments: int = Field(description="评论数", ge=0)
    labels: list[str] = Field(default_factory=list, description="标签列表")
    url: str = Field(description="Issue 链接")

    # 活跃度指标
    last_comment_days: int = Field(default=0, description="最后评论距今天数", ge=0)
    is_recently_active: bool = Field(default=False, description="最近活跃")


class UserPainPoint(BaseModel):
    """用户痛点

    从多个 Issues 中聚合出的用户痛点。
    """

    topic: str = Field(description="痛点主题")
    count: int = Field(description="提及次数", ge=1)
    avg_sentiment: float = Field(description="平均情绪分数 -1到1", ge=-1.0, le=1.0)
    affected_repos: list[str] = Field(description="受影响仓库")
    sample_urls: list[str] = Field(description="示例 Issue 链接")


class IssueData(BaseModel):
    """Issue 汇总数据

    用于报告的 Issue 分析汇总数据。
    """

    total_count: int = Field(description="总 Issue 数", ge=0)
    bug_reports: int = Field(description="Bug 报告数", ge=0)
    feature_requests: int = Field(description="功能请求数", ge=0)
    questions: int = Field(description="问题数", ge=0)
    discussions: int = Field(description="讨论数", ge=0)

    # 情绪统计
    sentiment_distribution: dict[str, int] = Field(
        default_factory=dict,
        description="情绪分布 {positive: x, neutral: y, negative: z}",
    )

    # 痛点排行
    top_pain_points: list[UserPainPoint] = Field(default_factory=list)


class IssueQualityDecision(BaseModel):
    """Issue 质量判定结果（用于过滤与主题补全）"""

    include: bool = Field(description="是否保留该 Issue")
    reason: str | None = Field(default=None, description="排除/保留原因")
    normalized_topic: str | None = Field(default=None, description="归一化后的中文主题")


class BatchIssueAnalysis(BaseModel):
    """批量 Issue 分析结果

    用于批量分析多个 Issues 时返回的聚合结果。
    """

    # 固定长度的结果数组，索引对应输入 Issues 的顺序
    results: list[IssueAnalysis | None] = Field(
        description="分析结果数组，null 表示该位置分析失败"
    )

    # 统计信息
    success_count: int = Field(default=0, ge=0, description="成功的数量")
    failure_count: int = Field(default=0, ge=0, description="失败的数量")

    # 失败详情（用于重试）
    failed_indices: list[int] = Field(
        default_factory=list, description="失败的索引位置"
    )
    errors: list[str | None] = Field(
        default_factory=list, description="每个位置的错误信息"
    )
