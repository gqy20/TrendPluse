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

    # 需要过滤的无用 topics
    FILTER_TOPICS = {
        # 活动标签
        "hacktoberfest",
        "hacktoberfest2024",
        "hactoberfest",
        # 语言标签（已有 language 字段）
        "javascript",
        "python",
        "typescript",
        "java",
        "go",
        "golang",
        "rust",
        "c",
        "c++",
        "csharp",
        "ruby",
        "php",
        "swift",
        "kotlin",
        "dart",
        "julia",
        "scala",
        "r",
        "matlab",
        "html",
        "css",
        "shell",
        "bash",
    }

    # Topics 规范化映射（变体 → 标准形式）
    TOPIC_NORMALIZATION = {
        "llms": "llm",
        "ai-agents": "agent",
        "agents": "agent",
        "multi-agents": "multi-agent",
        "large-language-models": "llm",
        "large-language-model": "llm",
        "chatbots": "chatbot",
        "openais": "openai",
        "claudes": "claude",
        "ollamas": "ollama",
        "retrievals": "retrieval",
        "vectors": "vector",
        "embeddings": "embedding",
    }

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
        ],
        "学习资源": [
            "awesome-list",
            "tutorial",
            "prompts",
            "prompt-engineering",
            "documentation",
        ],
        # 新增分类
        "机器学习框架": [
            "deep-learning",
            "machine-learning",
            "ml",
            "nlp",
            "natural-language-processing",
            "pytorch",
            "tensorflow",
            "jax",
            "keras",
            "pretrained-models",
            "model-hub",
            "transformer",
            "computer-vision",
            "cv",
        ],
        "监控/观测": [
            "monitoring",
            "monitor",
            "metrics",
            "observability",
            "logging",
            "tracing",
            "alerting",
            "dashboard",
            "prometheus",
            "grafana",
        ],
        "DevOps/基础设施": [
            "devops",
            "infrastructure",
            "deployment",
            "automation",
            "configuration",
            "ci-cd",
            "cicd",
            "container",
            "kubernetes",
            "k8s",
            "docker",
            "orchestration",
        ],
        "Web 框架": [
            "web-framework",
            "backend",
            "api",
            "server",
            "http",
            "rest",
            "graphql",
            "framework",
        ],
    }

    def _clean_topics(self, topics: list[str]) -> list[str]:
        """清洗和规范化 topics

        - 过滤无用 topics（活动标签、语言标签等）
        - 规范化变体（llms → llm, ai-agents → agent）
        - 转换为小写
        - 去重

        Args:
            topics: 原始 topics 列表

        Returns:
            清洗后的 topics 列表
        """
        cleaned = []
        seen = set()

        for topic in topics:
            # 转小写
            topic_lower = topic.lower()

            # 过滤无用 topics
            if topic_lower in self.FILTER_TOPICS:
                continue

            # 规范化
            normalized = self.TOPIC_NORMALIZATION.get(topic_lower, topic_lower)

            # 去重
            if normalized not in seen:
                seen.add(normalized)
                cleaned.append(normalized)

        return cleaned

    def classify(self, project: DiscoveredProject) -> list[str]:
        """分类单个项目

        Args:
            project: 项目对象

        Returns:
            分类列表，可能包含多个分类（如果项目匹配多个类别）
        """
        # 先清洗 topics
        cleaned_topics = self._clean_topics(project.topics)

        # 转换为集合用于匹配
        project_topics = set(cleaned_topics)

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
