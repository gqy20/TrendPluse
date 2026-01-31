"""项目发现数据模型

定义自动发现 GitHub 项目相关的数据结构。
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class DiscoveredProject(BaseModel):
    """发现的热门项目"""

    # 基本信息
    repo: str = Field(description="仓库名称 owner/repo")
    name: str = Field(description="项目名称")
    description: str = Field(description="项目描述")
    stars: int = Field(description="当前 star 数", ge=0)

    # 增长指标
    stars_growth_7d: int = Field(default=0, description="7天增长")
    stars_growth_30d: int = Field(default=0, description="30天增长")

    # 技术信息
    language: str = Field(description="主要语言")
    topics: list[str] = Field(default_factory=list, description="主题标签")
    license: str | None = Field(default=None, description="许可证")

    # 活跃度指标
    open_issues: int = Field(default=0, description="开放 Issue 数")
    forks: int = Field(default=0, description="Fork 数")
    watchers: int = Field(default=0, description="Watchers 数")
    last_commit_at: datetime | None = Field(default=None, description="最后提交时间")

    # 质量评估
    quality_score: float = Field(default=0, ge=0, le=100, description="质量评分 0-100")
    activity_level: Literal["high", "medium", "low"] = Field(default="medium")
    community_score: float = Field(default=0, ge=0, le=100, description="社区活跃度")

    # 发现元数据
    discovery_source: Literal["trending", "keyword", "related"] = Field(
        description="发现来源"
    )
    discovery_time: datetime = Field(default_factory=datetime.now)
    discovery_reason: str = Field(description="发现原因/关键词")

    # 推荐信息
    recommended: bool = Field(default=False, description="是否推荐添加")
    recommendation_priority: Literal["high", "medium", "low"] = Field(default="medium")


class DiscoveryReport(BaseModel):
    """发现报告"""

    date: str = Field(description="报告日期 YYYY-MM-DD")
    total_discovered: int = Field(description="总发现数")
    passed_quality: int = Field(description="通过质量评估数")
    high_priority: int = Field(description="高优先级推荐数")
    candidates: list[DiscoveredProject] = Field(description="候选项目列表")

    # 去重信息
    duplicates_removed: int = Field(default=0, description="去重移除数")
    already_monitored: int = Field(default=0, description="已在监控列表数")

    # 来源统计
    source_breakdown: dict[str, int] = Field(
        default_factory=dict,
        description="各来源发现数量",
    )
