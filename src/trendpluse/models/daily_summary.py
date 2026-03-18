"""日报历史索引与总结增强数据模型。"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class DailyHistoryEntry(BaseModel):
    """单日历史索引摘要。"""

    date: str = Field(description="日报日期 YYYY-MM-DD")
    summary_brief: str = Field(default="", description="日报摘要")
    engineering_titles: list[str] = Field(default_factory=list)
    research_titles: list[str] = Field(default_factory=list)
    release_titles: list[str] = Field(default_factory=list)
    top_repos: list[str] = Field(default_factory=list)
    high_impact_signals: int = Field(default=0, ge=0)
    signal_count: int = Field(default=0, ge=0)
    issue_summary_brief: str | None = Field(default=None)


class DailyHistoryIndex(BaseModel):
    """全量历史日报轻量索引。"""

    total_reports: int = Field(default=0, ge=0)
    entries: list[DailyHistoryEntry] = Field(default_factory=list)


class DailySummaryResult(BaseModel):
    """日报总结增强结果。"""

    summary_brief: str = Field(description="最终日报摘要")
    trend_status: Literal[
        "new",
        "continuing",
        "resurfacing",
        "weakening",
        "mixed",
    ] = Field(description="当天趋势状态")
    trend_delta: str | None = Field(default=None, description="相对历史的变化说明")
    historical_basis_dates: list[str] = Field(default_factory=list)
    historical_comparison: str | None = Field(
        default=None, description="与历史对比后的结论"
    )
    top_new_trends: list[str] = Field(default_factory=list)
    top_continuing_trends: list[str] = Field(default_factory=list)
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)
