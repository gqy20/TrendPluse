"""Issue 相关数据模型

定义 Issue 分析相关的数据结构。
"""

from datetime import datetime

from pydantic import BaseModel, Field


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
