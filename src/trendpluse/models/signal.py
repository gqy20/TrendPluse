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
    activity: dict | None = Field(
        default=None,
        description="仓库活跃度数据（可选）",
    )
    releases: dict | None = Field(
        default=None,
        description="Release 发布数据（可选）",
    )
    breaking_changes: list[dict] | None = Field(
        default=None,
        description="Breaking Changes 列表（可选）",
    )
