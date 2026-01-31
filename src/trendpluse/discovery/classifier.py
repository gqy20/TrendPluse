"""项目分类器

基于项目 Topics 自动将项目分类到不同技术栈类别。
"""

from collections import Counter

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)


class ProjectClassifier:
    """项目分类器

    基于 GitHub Topics 自动将项目分类到不同的技术栈/应用场景类别。

    一个项目可以同时属于多个分类（如既是 AI Agent 又是 RAG/检索）。
    """

    # 分类规则（基于 Topics 关键词匹配）
    CATEGORIES = {
        "AI Agents": [
            "agent",
            "multi-agent",
            "autonomous",
            "ai-agents",
            "agentic",
            "agent-framework",
            "mcp",  # Model Context Protocol
        ],
        "RAG/检索": [
            "rag",
            "retrieval",
            "vector",
            "embeddings",
            "semantic-search",
            "graphrag",
            "knowledge-base",
        ],
        "LLM 界面": [
            "llm-ui",
            "webui",
            "chatbot",
            "chatgpt",
            "openai",
            "claude",
            "ollama",
            "open-webui",
        ],
        "开发工具": [
            "developer-tools",
            "ide",
            "editor",
            "cli",
            "sdk",
            "api",
        ],
        "数据/基础设施": [
            "database",
            "vector-database",
            "data-pipeline",
            "infrastructure",
            "deployment",
            "monitoring",
        ],
        "学习资源": [
            "awesome-list",
            "tutorial",
            "prompts",
            "prompt-engineering",
            "documentation",
        ],
    }

    def classify(self, project: DiscoveredProject) -> list[str]:
        """分类单个项目

        Args:
            project: 项目对象

        Returns:
            分类列表，可能包含多个分类（如果项目匹配多个类别）
        """
        # 转换 topics 为小写集合用于匹配
        project_topics = {t.lower() for t in project.topics}

        categories = []

        # 检查每个分类规则
        for category_name, keywords in self.CATEGORIES.items():
            # 检查是否有任何关键词匹配
            if any(kw in project_topics for kw in keywords):
                categories.append(category_name)

        # 如果没有匹配到任何分类，返回"其他"
        return categories or ["其他"]

    def classify_batch(self, projects: list[DiscoveredProject]) -> dict[str, list[str]]:
        """批量分类项目

        Args:
            projects: 项目列表

        Returns:
            {repo: [categories]} 字典
        """
        result = {}
        for project in projects:
            result[project.repo] = self.classify(project)

        logger.info(f"项目分类完成: {len(projects)} 个项目")
        return result

    def get_category_stats(self, classified: dict[str, list[str]]) -> dict[str, int]:
        """获取分类统计

        Args:
            classified: classify_batch 返回的分类结果

        Returns:
            {category_name: count} 统计字典
        """
        # 统计每个分类的出现次数
        counter: Counter[str] = Counter()
        for categories in classified.values():
            for category in categories:
                counter[category] += 1

        return dict(counter)

    def group_by_category(
        self, projects: list[DiscoveredProject]
    ) -> dict[str, list[DiscoveredProject]]:
        """按分类分组项目

        Args:
            projects: 项目列表

        Returns:
            {category: [projects]} 字典
        """
        # 先分类所有项目
        classified = self.classify_batch(projects)

        # 按分类分组
        groups: dict[str, list[DiscoveredProject]] = {}
        for project in projects:
            categories = classified[project.repo]
            for category in categories:
                if category not in groups:
                    groups[category] = []
                groups[category].append(project)

        return groups
