"""信号数据模型

定义趋势信号和日报的数据结构。
"""

from typing import Literal

from pydantic import BaseModel, Field


class Signal(BaseModel):
    """单条趋势信号"""

    id: str = Field(description="唯一标识")
    title: str = Field(description="信号标题")
    type: Literal[
        "capability",
        "abstraction",
        "workflow",
        "eval",
        "safety",
        "performance",
        "commit",
        "release",
    ] = Field(description="信号类型")
    category: Literal["engineering", "research"] = Field(
        description="信号分类：工程或研究"
    )
    impact_score: int = Field(
        ge=1,
        le=5,
        description="影响评分 1-5",
    )
    why_it_matters: str = Field(description="1-2 句话说明重要性")
    sources: list[str] = Field(description="PR/Release 链接")
    related_repos: list[str] = Field(description="相关仓库名称")


class RepoActivity(BaseModel):
    """单个仓库的活跃度数据"""

    repo: str = Field(description="仓库名称 owner/repo")
    commits: int = Field(description="Commit 数量", ge=0)
    new_contributors: int = Field(description="新贡献者数量", ge=0)
    top_contributors: list[str] = Field(
        description="Top 贡献者列表", default_factory=list
    )


class ActivityData(BaseModel):
    """仓库活跃度汇总数据"""

    total_commits: int = Field(description="总 Commit 数", ge=0)
    active_repos_count: int = Field(description="活跃仓库数量", ge=0)
    new_contributors: int = Field(description="新贡献者总数", ge=0)
    top_repos: list[RepoActivity] = Field(description="TOP 活跃仓库列表")


class ReleaseInfo(BaseModel):
    """单个版本发布信息"""

    repo: str = Field(description="仓库名称 owner/repo")
    version: str = Field(description="版本号")
    author: str = Field(description="发布者")
    date: str = Field(description="发布日期 YYYY-MM-DD")
    summary: str = Field(description="发布摘要")
    assets_count: int = Field(description="资产文件数量", ge=0, default=0)
    url: str = Field(description="发布链接 URL")


class ReleasesData(BaseModel):
    """版本发布汇总数据"""

    total_count: int = Field(description="总发布数量", ge=0)
    unique_repos_count: int = Field(description="涉及仓库数量", ge=0)
    releases: list[ReleaseInfo] = Field(description="版本发布列表")


class DailyReport(BaseModel):
    """每日分析报告"""

    date: str
    summary_brief: str = Field(description="当日总览（2-3 句话）")
    engineering_signals: list[Signal] = Field(default_factory=list)
    research_signals: list[Signal] = Field(default_factory=list)
    commit_signals: list[Signal] = Field(default_factory=list)
    release_signals: list[Signal] = Field(default_factory=list)
    stats: dict = Field(
        default_factory=lambda: {
            "total_prs_analyzed": 0,
            "total_releases": 0,
            "high_impact_signals": 0,
            "total_commits_analyzed": 0,
        }
    )
    activity: ActivityData | None = Field(
        default=None,
        description="仓库活跃度数据（可选）",
    )
    releases: ReleasesData | None = Field(
        default=None,
        description="Release 发布数据（可选）",
    )
    breaking_changes: list[dict] | None = Field(
        default=None,
        description="Breaking Changes 列表（可选）",
    )
    monitored_repos: list[str] | None = Field(
        default=None,
        description="监控的仓库列表（可选）",
    )
