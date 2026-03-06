"""项目亮点分析数据模型。"""

from pydantic import BaseModel, Field


class ProjectHighlight(BaseModel):
    """项目亮点分析结果。"""

    recommendation_reason: str = Field(
        description="为什么推荐这个项目",
        min_length=10,
        max_length=500,
    )
    technical_highlights: list[str] = Field(
        description="技术亮点列表",
        min_length=1,
        max_length=5,
    )
    use_cases: list[str] = Field(
        description="适用场景列表",
        min_length=1,
        max_length=5,
    )

    def format_as_markdown(self) -> str:
        """格式化为 Markdown 格式。"""
        lines = [
            f"{self.recommendation_reason}\n",
            "\n",
            "**技术亮点**:\n",
        ]

        for highlight in self.technical_highlights:
            lines.append(f"- {highlight}\n")

        if self.use_cases:
            lines.extend(["\n", "**适用场景**:\n"])
            for use_case in self.use_cases:
                lines.append(f"- {use_case}\n")

        return "".join(lines)

    @classmethod
    def fallback(cls, project_info: dict) -> "ProjectHighlight":
        """生成降级版本的亮点分析。"""
        repo = project_info.get("repo", "")
        stars = project_info.get("stars", 0)
        description = project_info.get("description", "")
        language = project_info.get("language", "")

        desc_preview = description[:100] if description else ""
        recommendation = (
            f"{repo} 是一个{language}项目，拥有 {stars:,} Stars。{desc_preview}..."
        )

        return cls(
            recommendation_reason=recommendation,
            technical_highlights=[
                f"活跃的开源社区 ({stars:,} Stars)",
                f"使用 {language} 开发",
            ],
            use_cases=[f"{language} 开发项目"],
        )
