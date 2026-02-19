"""Issue Agent 结果模型"""

from pydantic import BaseModel, Field


class IssueAgentPainPoint(BaseModel):
    """Agent 汇总的痛点"""

    topic: str = Field(description="痛点主题")
    count: int = Field(description="提及次数", ge=1)
    affected_repos: list[str] = Field(description="受影响仓库")
    sample_urls: list[str] = Field(description="示例 Issue 链接")


class IssueAgentReport(BaseModel):
    """Agent 输出的 Issue 汇总结果"""

    top_pain_points: list[IssueAgentPainPoint] = Field(default_factory=list)
    expected_files: int = Field(default=0, ge=0, description="预期分析文件数")
    generated_files: int = Field(default=0, ge=0, description="实际生成的分析文件数")
    parsed_files: int = Field(default=0, ge=0, description="成功解析的分析文件数")
    failed_files: int = Field(default=0, ge=0, description="解析失败的分析文件数")
    failed_samples: list[str] = Field(
        default_factory=list,
        description="失败文件示例（最多 5 个）",
    )
