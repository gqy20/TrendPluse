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
