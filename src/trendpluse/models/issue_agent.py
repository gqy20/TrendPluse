"""Issue Agent 结果模型"""

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, Field

ISSUE_AGENT_CATEGORY_VALUES = (
    "startup_crash",
    "workflow_runtime",
    "auth_permission",
    "session_state",
    "tool_call_protocol",
    "packaging_release",
    "quota_rate_limit",
    "ui_interaction",
    "other",
)
IssueAgentCategory = Literal[
    "startup_crash",
    "workflow_runtime",
    "auth_permission",
    "session_state",
    "tool_call_protocol",
    "packaging_release",
    "quota_rate_limit",
    "ui_interaction",
    "other",
]


@dataclass(slots=True)
class IssueAgentBatchResult:
    """Issue Agent 批量分析统计。"""

    expected_files: int
    succeeded_files: int
    failed_files: int
    failed_samples: list[str]


class IssueAgentPainPoint(BaseModel):
    """Agent 汇总的痛点"""

    id: str | None = Field(default=None, description="信号唯一标识")
    repo: str | None = Field(default=None, description="来源仓库（仓库级信号时使用）")
    topic: str = Field(description="痛点主题")
    summary: str | None = Field(default=None, description="痛点摘要")
    category: IssueAgentCategory | None = Field(default=None, description="痛点分类")
    count: int = Field(description="提及次数", ge=1)
    affected_repos: list[str] = Field(description="受影响仓库")
    sample_urls: list[str] = Field(description="示例 Issue 链接")
    aliases: list[str] = Field(default_factory=list, description="主题别名")
    confidence: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="审稿置信度",
    )
    priority: str | None = Field(
        default=None,
        pattern=r"^P[0-2]$",
        description="优先级标签（P0/P1/P2）",
    )
    review_reason: str | None = Field(
        default=None,
        description="审稿保留/过滤理由",
    )
    source_issues: list["IssueAgentSourceIssue"] = Field(
        default_factory=list,
        description="支撑该信号的原始 Issue 列表",
    )
    source_signal_ids: list[str] = Field(
        default_factory=list,
        description="全局汇总时引用的仓库级 signal 标识",
    )


class IssueAgentSourceIssue(BaseModel):
    """Issue 信号来源。"""

    repo: str = Field(description="仓库名")
    issue_number: int | None = Field(default=None, description="Issue 编号")
    title: str = Field(default="", description="Issue 标题")
    url: str = Field(description="Issue 链接")
    labels: list[str] = Field(default_factory=list, description="Issue 标签")
    evidence: str | None = Field(default=None, description="证据摘录")


class RepoIssueSignalReport(BaseModel):
    """单仓库 Issue Agent 分析结果。"""

    repo: str = Field(description="仓库名")
    snapshot_date: str = Field(description="快照日期")
    signals: list[IssueAgentPainPoint] = Field(default_factory=list)
    expected_issue_count: int = Field(default=0, ge=0)
    analyzed_issue_count: int = Field(default=0, ge=0)
    quality_score: float = Field(default=0.0, ge=0.0, le=1.0)
    quality_status: str = Field(default="poor")
    errors: list[str] = Field(default_factory=list)


class IssueAgentReport(BaseModel):
    """Agent 输出的 Issue 汇总结果"""

    summary_brief: str | None = Field(default=None, description="全局摘要")
    global_highlights: list[str] = Field(default_factory=list, description="全局亮点")
    top_pain_points: list[IssueAgentPainPoint] = Field(default_factory=list)
    repo_reports: list[RepoIssueSignalReport] = Field(default_factory=list)
    expected_files: int = Field(default=0, ge=0, description="预期分析文件数")
    generated_files: int = Field(default=0, ge=0, description="实际生成的分析文件数")
    parsed_files: int = Field(default=0, ge=0, description="成功解析的分析文件数")
    failed_files: int = Field(default=0, ge=0, description="解析失败的分析文件数")
    failed_samples: list[str] = Field(
        default_factory=list,
        description="失败文件示例（最多 5 个）",
    )
    quality_score: float = Field(default=0.0, ge=0.0, le=1.0, description="质量分")
    quality_status: str = Field(
        default="poor",
        description="质量等级：good/warning/poor/no_data",
    )
    cross_repo_item_count: int = Field(
        default=0,
        ge=0,
        description="跨仓库问题数量",
    )
    other_category_count: int = Field(
        default=0,
        ge=0,
        description="other 分类数量",
    )
    category_coverage: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="痛点分类覆盖率",
    )


IssueAgentPainPoint.model_rebuild()
RepoIssueSignalReport.model_rebuild()
IssueAgentReport.model_rebuild()
