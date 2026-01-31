"""项目分类器测试

测试 ProjectClassifier 的功能。
"""

import pytest

from trendpluse.discovery.classifier import ProjectClassifier
from trendpluse.models.discovery import DiscoveredProject


class TestProjectClassifier:
    """项目分类器测试"""

    @pytest.fixture
    def sample_projects(self):
        """创建不同类别的示例项目"""
        projects = []

        # AI Agent 项目
        projects.append(
            DiscoveredProject(
                repo="test/agent-1",
                name="agent-1",
                description="Multi-agent AI system",
                stars=1000,
                language="Python",
                topics=["agent", "multi-agent", "autonomous", "ai-agents"],
                license="MIT",
                open_issues=10,
                forks=100,
                watchers=1000,
                last_commit_at=None,
                discovery_source="trending",
                discovery_reason="AI agent project",
            )
        )

        # RAG 项目
        projects.append(
            DiscoveredProject(
                repo="test/rag-1",
                name="rag-1",
                description="RAG retrieval system",
                stars=2000,
                language="Python",
                topics=["rag", "retrieval", "vector", "embeddings"],
                license="Apache-2.0",
                open_issues=20,
                forks=200,
                watchers=2000,
                last_commit_at=None,
                discovery_source="keyword",
                discovery_reason="RAG system",
            )
        )

        # LLM 界面项目
        projects.append(
            DiscoveredProject(
                repo="test/llm-ui-1",
                name="llm-ui-1",
                description="LLM chat interface",
                stars=5000,
                language="TypeScript",
                topics=["llm-ui", "webui", "chatbot", "openai", "ollama"],
                license="MIT",
                open_issues=30,
                forks=500,
                watchers=5000,
                last_commit_at=None,
                discovery_source="trending",
                discovery_reason="LLM UI",
            )
        )

        # 开发工具项目
        projects.append(
            DiscoveredProject(
                repo="test/devtools-1",
                name="devtools-1",
                description="Developer CLI tool",
                stars=1500,
                language="Go",
                topics=["developer-tools", "cli", "sdk"],
                license="MIT",
                open_issues=15,
                forks=150,
                watchers=1500,
                last_commit_at=None,
                discovery_source="keyword",
                discovery_reason="Dev tool",
            )
        )

        # 学习资源项目
        projects.append(
            DiscoveredProject(
                repo="test/awesome-1",
                name="awesome-1",
                description="Awesome list of AI tools",
                stars=3000,
                language="",
                topics=["awesome-list", "prompt-engineering", "prompts"],
                license="CC0-1.0",
                open_issues=5,
                forks=300,
                watchers=3000,
                last_commit_at=None,
                discovery_source="keyword",
                discovery_reason="Awesome list",
            )
        )

        # 无明确分类的项目
        projects.append(
            DiscoveredProject(
                repo="test/other-1",
                name="other-1",
                description="Random web project",
                stars=500,
                language="JavaScript",
                topics=["web", "frontend"],
                license="MIT",
                open_issues=25,
                forks=50,
                watchers=500,
                last_commit_at=None,
                discovery_source="keyword",
                discovery_reason="Web project",
            )
        )

        # 同时属于多个分类的项目
        projects.append(
            DiscoveredProject(
                repo="test/multi-1",
                name="multi-1",
                description="AI agent framework with RAG",
                stars=4000,
                language="Python",
                topics=["agent", "multi-agent", "rag", "llm"],
                license="MIT",
                open_issues=40,
                forks=400,
                watchers=4000,
                last_commit_at=None,
                discovery_source="trending",
                discovery_reason="Multi-category",
            )
        )

        return projects

    def test_classify_ai_agent_project(self, sample_projects):
        """测试 AI Agent 项目分类"""
        classifier = ProjectClassifier()
        project = sample_projects[0]  # agent-1

        categories = classifier.classify(project)

        assert "AI Agents" in categories

    def test_classify_rag_project(self, sample_projects):
        """测试 RAG 项目分类"""
        classifier = ProjectClassifier()
        project = sample_projects[1]  # rag-1

        categories = classifier.classify(project)

        assert "RAG/检索" in categories

    def test_classify_llm_ui_project(self, sample_projects):
        """测试 LLM 界面项目分类"""
        classifier = ProjectClassifier()
        project = sample_projects[2]  # llm-ui-1

        categories = classifier.classify(project)

        assert "LLM 界面" in categories

    def test_classify_devtools_project(self, sample_projects):
        """测试开发工具项目分类"""
        classifier = ProjectClassifier()
        project = sample_projects[3]  # devtools-1

        categories = classifier.classify(project)

        assert "开发工具" in categories

    def test_classify_learning_resource_project(self, sample_projects):
        """测试学习资源项目分类"""
        classifier = ProjectClassifier()
        project = sample_projects[4]  # awesome-1

        categories = classifier.classify(project)

        assert "学习资源" in categories

    def test_classify_other_project(self, sample_projects):
        """测试无明确分类的项目"""
        classifier = ProjectClassifier()
        project = sample_projects[5]  # other-1

        categories = classifier.classify(project)

        # 应该至少有一个分类（默认的"其他"）
        assert len(categories) >= 1
        assert "其他" in categories

    def test_classify_multi_category_project(self, sample_projects):
        """测试多分类项目"""
        classifier = ProjectClassifier()
        project = sample_projects[6]  # multi-1

        categories = classifier.classify(project)

        # 应该同时属于 AI Agents 和 RAG/检索
        assert "AI Agents" in categories
        assert "RAG/检索" in categories
        assert len(categories) >= 2

    def test_classify_batch_returns_dict(self, sample_projects):
        """测试批量分类"""
        classifier = ProjectClassifier()

        result = classifier.classify_batch(sample_projects)

        # 验证返回字典
        assert isinstance(result, dict)
        assert len(result) == len(sample_projects)

        # 验证每个项目都有分类
        for project in sample_projects:
            assert project.repo in result
            assert isinstance(result[project.repo], list)
            assert len(result[project.repo]) >= 1

    def test_get_category_stats(self, sample_projects):
        """测试获取分类统计"""
        classifier = ProjectClassifier()
        classified = classifier.classify_batch(sample_projects)

        stats = classifier.get_category_stats(classified)

        # 验证统计数据
        assert isinstance(stats, dict)
        assert "AI Agents" in stats
        assert "RAG/检索" in stats

        # 验证计数正确
        agent_count = sum(1 for cats in classified.values() if "AI Agents" in cats)
        assert stats["AI Agents"] == agent_count

    def test_empty_topics_returns_other(self):
        """测试空 topics 返回默认分类"""
        classifier = ProjectClassifier()
        project = DiscoveredProject(
            repo="test/no-topics",
            name="no-topics",
            description="No topics project",
            stars=100,
            language="Python",
            topics=[],
            license="MIT",
            open_issues=5,
            forks=10,
            watchers=100,
            last_commit_at=None,
            discovery_source="keyword",
            discovery_reason="No topics",
        )

        categories = classifier.classify(project)

        assert "其他" in categories
