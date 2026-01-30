"""信号数据模型

定义趋势信号和日报的数据结构。
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

# 信号类型到 Emoji 的映射常量
SIGNAL_TYPE_EMOJIS: dict[str, str] = {
    "capability": "🚀",
    "abstraction": "🎨",
    "workflow": "⚙️",
    "eval": "📊",
    "safety": "🛡️",
    "performance": "⚡",
    "commit": "💾",
    "release": "🎯",
}

DEFAULT_EMOJI: str = "📌"

# Release 变更类型到 Emoji 的映射常量
RELEASE_CHANGE_TYPE_EMOJIS: dict[str, str] = {
    "feature": "🆕",
    "fix": "🔧",
    "improvement": "✨",
    "breaking": "💥",
    "other": "📦",
}


class ReleaseSummary(BaseModel):
    """Release 总结（AI 生成）

    由 ReleaseSummarizer 生成的 Release 变更总结。
    """

    change_type: Literal["feature", "fix", "improvement", "breaking", "other"] = Field(
        description="变更类型"
    )
    key_changes: list[str] = Field(description="关键变更点列表（简洁的中文描述）")
    summary_cn: str = Field(description="中文总结（2-3 句话）")
    impact_level: int = Field(ge=1, le=5, description="影响级别 1-5")

    @classmethod
    def get_change_type_emoji(cls, change_type: str) -> str:
        """获取变更类型的表情

        Args:
            change_type: 变更类型

        Returns:
            类型表情，未知类型返回默认值 📌
        """
        return RELEASE_CHANGE_TYPE_EMOJIS.get(change_type, DEFAULT_EMOJI)


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

    # 聚合信号引用字段（仅用于 engineering_signals）
    source_signal_ids: list[str] = Field(
        default_factory=list,
        description=("支持此聚合信号的原始信号 ID 列表 (仅用于聚合信号，由 LLM 填充)"),
    )

    @classmethod
    def get_type_emoji(cls, signal_type: str) -> str:
        """获取信号类型的表情

        Args:
            signal_type: 信号类型

        Returns:
            类型表情，未知类型返回默认值 📌
        """
        return SIGNAL_TYPE_EMOJIS.get(signal_type, DEFAULT_EMOJI)


class RepoActivity(BaseModel):
    """单个仓库的活跃度数据"""

    repo: str = Field(description="仓库名称 owner/repo")
    commits: int = Field(description="Commit 数量", ge=0)
    top_contributors: list[str] = Field(
        description="Top 贡献者列表", default_factory=list
    )


class ActivityData(BaseModel):
    """仓库活跃度汇总数据"""

    total_commits: int = Field(description="总 Commit 数", ge=0)
    active_repos_count: int = Field(description="活跃仓库数量", ge=0)
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
    ai_summary: ReleaseSummary | None = Field(
        default=None, description="AI 生成的变更总结（可选）"
    )


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


class WeeklyActivity(BaseModel):
    """周活跃度汇总数据"""

    total_commits: int = Field(description="总 Commit 数", ge=0)
    active_repos_count: int = Field(description="活跃仓库数量", ge=0)
    top_repos: list[RepoActivity] = Field(description="TOP 活跃仓库列表")


class WeeklyReport(BaseModel):
    """周报数据模型"""

    week_id: str = Field(description="周标识，如 2026-W05")
    start_date: str = Field(description="开始日期 YYYY-MM-DD")
    end_date: str = Field(description="结束日期 YYYY-MM-DD")
    summary_brief: str = Field(description="本周总览（2-3 句话）")

    # 聚合信号
    engineering_signals: list[Signal] = Field(default_factory=list)
    research_signals: list[Signal] = Field(default_factory=list)

    # 统计数据
    daily_reports_count: int = Field(default=0, description="包含的日报数量", ge=0)
    total_prs_analyzed: int = Field(default=0, description="总分析 PR 数", ge=0)
    high_impact_signals: int = Field(default=0, description="高影响信号数", ge=0)
    total_commits: int = Field(default=0, description="总 Commit 数", ge=0)
    total_releases: int = Field(default=0, description="总 Release 数", ge=0)

    # 活跃度数据（聚合）
    weekly_activity: WeeklyActivity | None = Field(default=None)

    @classmethod
    def get_week_id(cls, date: datetime) -> str:
        """获取周标识，如 2026-W05

        使用 ISO 8601 标准：
        - 周一为一周的第一天
        - 第一周包含该年 1 月 4 日

        Args:
            date: 日期对象

        Returns:
            周标识，如 "2026-W05"
        """
        year, week, _ = date.isocalendar()
        return f"{year}-W{week:02d}"
