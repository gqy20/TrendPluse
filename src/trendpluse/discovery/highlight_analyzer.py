"""项目亮点分析数据模型和分析器"""

from pydantic import BaseModel, Field

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.config import DEFAULT_ANTHROPIC_BASE_URL, DEFAULT_ANTHROPIC_MODEL
from trendpluse.logger import get_logger
from trendpluse.utils.retry import create_anthropic_retry_decorator

logger = get_logger(__name__)

# 创建重试装饰器
_llm_retry = create_anthropic_retry_decorator()


class ProjectHighlight(BaseModel):
    """项目亮点分析结果

    Attributes:
        recommendation_reason: 推荐理由（为什么推荐这个项目）
        technical_highlights: 技术亮点列表（3-5个bullet points）
        use_cases: 适用场景列表
    """

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
        """格式化为 Markdown 格式

        Returns:
            Markdown 格式的亮点分析
        """
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
        """生成降级版本的亮点分析

        当 AI 分析失败时使用，基于项目基本信息生成。

        Args:
            project_info: 项目基本信息字典

        Returns:
            基础版本的 ProjectHighlight
        """
        repo = project_info.get("repo", "")
        stars = project_info.get("stars", 0)
        description = project_info.get("description", "")
        language = project_info.get("language", "")

        # 构建推荐理由（避免行过长）
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


class ProjectHighlightAnalyzer(BaseLLMAnalyzer):
    """项目亮点分析器

    使用 AI 分析项目，生成推荐理由、技术亮点和适用场景。
    """

    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_ANTHROPIC_MODEL,
        base_url: str = DEFAULT_ANTHROPIC_BASE_URL,
    ):
        """初始化分析器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL
        """
        # 使用 instructor 模式（与 TrendAnalyzer 保持一致）
        super().__init__(
            api_key=api_key, model=model, base_url=base_url, use_instructor=True
        )

    def _build_analysis_prompt(self, project) -> str:
        """构建分析提示词

        Args:
            project: 项目对象

        Returns:
            分析提示词
        """
        topics_str = ", ".join(project.topics) if project.topics else "N/A"
        license_str = project.license or "N/A"

        return f"""分析这个 GitHub 项目并生成项目亮点分析。

项目信息：
- 仓库名: {project.repo}
- 描述: {project.description}
- 编程语言: {project.language}
- Stars: {project.stars:,}
- Topics: {topics_str}
- 许可证: {license_str}

请分析并返回 ProjectHighlight，包含以下字段：
1. recommendation_reason: 推荐理由（1-2句话，说明为什么推荐这个项目及其独特价值）
2. technical_highlights: 技术亮点列表（3-5个bullet points，突出技术特色）
3. use_cases: 适用场景列表（必须包含 1-3个bullet points，说明适合什么场景使用）

注意：
- 推荐理由要具体，避免空泛
- 技术亮点要基于项目描述和Topics推断
- **适用场景必须至少提供 1 个**，考虑企业/个人开发者场景
- 用中文回复
"""

    @_llm_retry
    def analyze(self, project) -> ProjectHighlight:
        """分析项目亮点

        Args:
            project: 项目对象

        Returns:
            项目亮点分析结果
        """
        prompt = self._build_analysis_prompt(project)

        try:
            highlight = self.client.chat.completions.create(
                model=self.model,
                response_model=ProjectHighlight,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
            )
            return highlight  # type: ignore[no-any-return]

        except Exception as e:
            logger.warning(f"AI 分析项目 {project.repo} 失败: {e}，使用降级方案")

            # 降级：基于基本信息生成
            return ProjectHighlight.fallback(
                {
                    "repo": project.repo,
                    "stars": project.stars,
                    "description": project.description,
                    "language": project.language,
                }
            )

    def analyze_batch(
        self, projects: list, max_workers: int = 5
    ) -> dict[str, ProjectHighlight]:
        """批量分析项目亮点

        Args:
            projects: 项目列表
            max_workers: 并发分析数量

        Returns:
            {repo: ProjectHighlight} 字典
        """
        results = {}

        for project in projects:
            try:
                highlight = self.analyze(project)
                results[project.repo] = highlight
                logger.info(f"✓ 已分析: {project.repo}")
            except Exception as e:
                logger.error(f"✗ 分析失败 {project.repo}: {e}")
                # 使用降级方案
                results[project.repo] = ProjectHighlight.fallback(
                    {
                        "repo": project.repo,
                        "stars": getattr(project, "stars", 0),
                        "description": getattr(project, "description", ""),
                        "language": getattr(project, "language", ""),
                    }
                )

        return results
