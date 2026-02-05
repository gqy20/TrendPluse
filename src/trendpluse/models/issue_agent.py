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
