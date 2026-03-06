"""来源引用与分析材料模型。"""

from typing import Any, Literal

from pydantic import BaseModel, Field


class SourceRef(BaseModel):
    """待读取来源的统一引用。"""

    source_type: Literal["pull_request"] = Field(description="来源类型")
    provider: Literal["github"] = Field(description="来源提供方")
    repo: str = Field(description="仓库名称 owner/repo")
    external_id: str = Field(description="外部系统中的对象 ID")
    url: str = Field(description="对象链接")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="附加元数据",
    )

    @classmethod
    def from_pr_candidate(cls, candidate: dict[str, Any]) -> "SourceRef":
        """从 PR 候选事件构建来源引用。"""
        pull_request = candidate.get("payload", {}).get("pull_request", {})
        repo = str(candidate.get("repo", {}).get("name", "")).strip()
        number = pull_request.get("number", "")
        url = str(
            pull_request.get("url")
            or pull_request.get("html_url")
            or f"https://github.com/{repo}/pull/{number}"
        ).strip()

        return cls(
            source_type="pull_request",
            provider="github",
            repo=repo,
            external_id=str(number),
            url=url,
            metadata={
                "state": pull_request.get("state"),
                "merged": pull_request.get("merged"),
                "draft": pull_request.get("draft"),
                "changed_files": pull_request.get("changed_files"),
                "labels": pull_request.get("labels", []),
            },
        )


class AnalysisMaterial(BaseModel):
    """统一的可分析材料。"""

    source_ref: SourceRef = Field(description="来源引用")
    title: str = Field(default="", description="标题")
    body: str = Field(default="", description="正文")
    author: str = Field(default="", description="作者")
    created_at: str | None = Field(default=None, description="创建时间")
    updated_at: str | None = Field(default=None, description="更新时间")
    raw_payload: dict[str, Any] = Field(
        default_factory=dict,
        description="原始读取结果",
    )

    @classmethod
    def from_pr_details(cls, pr_details: dict[str, Any]) -> "AnalysisMaterial":
        """从旧版 PR 详情字典构建分析材料。"""
        repo = str(
            pr_details.get("repo_name")
            or pr_details.get("repo")
            or pr_details.get("repository")
            or "unknown"
        ).strip()
        number = pr_details.get("number", "")
        url = str(
            pr_details.get("url")
            or pr_details.get("html_url")
            or f"https://github.com/{repo}/pull/{number}"
        ).strip()

        return cls(
            source_ref=SourceRef(
                source_type="pull_request",
                provider="github",
                repo=repo,
                external_id=str(number),
                url=url,
                metadata={},
            ),
            title=str(pr_details.get("title", "")),
            body=str(pr_details.get("body", "")),
            author=str(pr_details.get("author", "")),
            created_at=pr_details.get("created_at"),
            updated_at=pr_details.get("updated_at") or pr_details.get("closed_at"),
            raw_payload=dict(pr_details),
        )
