"""项目分类器测试

测试 ProjectClassifier 的功能。
"""

import pytest

from trendpluse.discovery.classifier import ProjectClassifier
from trendpluse.models.discovery import DiscoveredProject


def _build_project(**overrides) -> DiscoveredProject:
    """构造测试用项目。"""
    defaults = {
        "repo": "test/project",
        "name": "project",
        "description": "Test project",
        "stars": 1000,
        "language": "Python",
        "topics": ["ai"],
        "license": "MIT",
        "open_issues": 10,
        "forks": 100,
        "watchers": 1000,
        "last_commit_at": None,
        "discovery_source": "trending",
        "discovery_reason": "Test project",
    }
    defaults.update(overrides)
    return DiscoveredProject(**defaults)


class TestProjectClassifier:
    """项目分类器测试"""

    @pytest.fixture
    def sample_projects(self):
        """创建不同类别的示例项目"""
        projects = []

        # AI Agent 项目
        projects.append(
            _build_project(
                repo="test/agent-1",
                name="agent-1",
                description="Multi-agent AI system",
                topics=["agent", "multi-agent", "autonomous", "ai-agents"],
                discovery_reason="AI agent project",
            )
        )

        # RAG 项目
        projects.append(
            _build_project(
                repo="test/rag-1",
                name="rag-1",
                description="RAG retrieval system",
                stars=2000,
                topics=["rag", "retrieval", "vector", "embeddings"],
                license="Apache-2.0",
                open_issues=20,
                forks=200,
                watchers=2000,
                discovery_source="keyword",
                discovery_reason="RAG system",
            )
        )

        # LLM 界面项目
        projects.append(
            _build_project(
                repo="test/llm-ui-1",
                name="llm-ui-1",
                description="LLM chat interface",
                stars=5000,
                language="TypeScript",
                topics=["llm-ui", "webui", "chatbot", "openai", "ollama"],
                open_issues=30,
                forks=500,
                watchers=5000,
                discovery_reason="LLM UI",
            )
        )

        # 开发工具项目
        projects.append(
            _build_project(
                repo="test/devtools-1",
                name="devtools-1",
                description="Developer CLI tool",
                stars=1500,
                language="Go",
                topics=["developer-tools", "cli", "sdk"],
                open_issues=15,
                forks=150,
                watchers=1500,
                discovery_source="keyword",
                discovery_reason="Dev tool",
            )
        )

        # 学习资源项目
        projects.append(
            _build_project(
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
                discovery_source="keyword",
                discovery_reason="Awesome list",
            )
        )

        # 无明确分类的项目
        projects.append(
            _build_project(
                repo="test/other-1",
                name="other-1",
                description="Random web project",
                stars=500,
                language="JavaScript",
                topics=["web", "frontend"],
                open_issues=25,
                forks=50,
                watchers=500,
                discovery_source="keyword",
                discovery_reason="Web project",
            )
        )

        # 同时属于多个分类的项目
        projects.append(
            _build_project(
                repo="test/multi-1",
                name="multi-1",
                description="AI agent framework with RAG",
                stars=4000,
                topics=["agent", "multi-agent", "rag", "llm"],
                open_issues=40,
                forks=400,
                watchers=4000,
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
        project = _build_project(
            repo="test/no-topics",
            name="no-topics",
            description="No topics project",
            stars=100,
            topics=[],
            open_issues=5,
            forks=10,
            watchers=100,
            discovery_source="keyword",
            discovery_reason="No topics",
        )

        categories = classifier.classify(project)

        assert "其他" in categories


class TestTopicCleaning:
    """Topics 清洗功能测试"""

    def test_clean_topics_filters_activity_tags(self):
        """测试过滤活动标签（如 hacktoberfest）"""
        classifier = ProjectClassifier()

        dirty = ["ai", "llm", "hacktoberfest", "rag"]
        cleaned = classifier._clean_topics(dirty)

        assert "hacktoberfest" not in cleaned
        assert "ai" in cleaned
        assert "llm" in cleaned
        assert "rag" in cleaned

    def test_clean_topics_normalizes_variants(self):
        """测试规范化 topics 变体"""
        classifier = ProjectClassifier()

        dirty = ["llms", "ai-agents", "large-language-models"]
        cleaned = classifier._clean_topics(dirty)

        assert "llm" in cleaned
        assert "llms" not in cleaned
        assert "agent" in cleaned
        assert "ai-agents" not in cleaned
        assert "llm" in cleaned  # large-language-models → llm

    def test_clean_topics_converts_to_lowercase(self):
        """测试转换为小写"""
        classifier = ProjectClassifier()

        dirty = ["AI", "LLM", "RAG", "DeepLearning"]
        cleaned = classifier._clean_topics(dirty)

        assert "ai" in cleaned
        assert "llm" in cleaned
        assert "rag" in cleaned
        assert "deeplearning" in cleaned
        assert "AI" not in cleaned
        assert "LLM" not in cleaned

    def test_clean_topics_filters_language_tags(self):
        """测试过滤语言标签（可选功能）"""
        classifier = ProjectClassifier()

        # 语言标签应该被过滤，因为已有 language 字段
        dirty = ["ai", "javascript", "python", "llm", "golang"]
        cleaned = classifier._clean_topics(dirty)

        # 验证语言标签被过滤
        assert "javascript" not in cleaned
        assert "python" not in cleaned
        assert "golang" not in cleaned
        # 技术主题保留
        assert "ai" in cleaned
        assert "llm" in cleaned

    def test_clean_topics_empty_list(self):
        """测试空列表处理"""
        classifier = ProjectClassifier()

        cleaned = classifier._clean_topics([])

        assert cleaned == []

    def test_clean_topics_removes_duplicates(self):
        """测试去重"""
        classifier = ProjectClassifier()

        dirty = ["ai", "AI", "llm", "llm", "rag"]
        cleaned = classifier._clean_topics(dirty)

        assert cleaned.count("ai") == 1
        assert cleaned.count("llm") == 1
        assert cleaned.count("rag") == 1

    def test_classify_uses_cleaned_topics(self):
        """测试分类使用清洗后的 topics"""
        classifier = ProjectClassifier()

        # 使用未规范化的 topics
        project = _build_project(
            repo="test/test-agent",
            name="test-agent",
            description="Test",
            topics=["AI-Agents", "Multi-Agent", "hacktoberfest"],  # 未规范化
            discovery_reason="Test",
        )

        categories = classifier.classify(project)

        # 应该能正确匹配到 AI Agents（使用清洗后的 topics）
        assert "AI Agents" in categories


class TestExtendedCategories:
    """扩展分类功能测试"""

    def test_classify_ml_framework_project(self):
        """测试机器学习框架项目分类"""
        classifier = ProjectClassifier()

        # Transformers 类项目
        project = _build_project(
            repo="huggingface/transformers",
            name="transformers",
            description="ML framework",
            stars=100000,
            topics=[
                "deep-learning",
                "machine-learning",
                "nlp",
                "pytorch",
                "pretrained-models",
                "transformer",
            ],
            license="Apache-2.0",
            open_issues=100,
            forks=10000,
            watchers=100000,
            discovery_reason="ML framework",
        )

        categories = classifier.classify(project)

        assert "机器学习框架" in categories

    def test_classify_monitoring_project(self):
        """测试监控工具项目分类"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="prometheus/prometheus",
            name="prometheus",
            description="Monitoring system",
            stars=50000,
            language="Go",
            topics=["monitoring", "metrics", "observability", "alerting"],
            license="Apache-2.0",
            open_issues=50,
            forks=5000,
            watchers=50000,
            discovery_reason="Monitoring tool",
        )

        categories = classifier.classify(project)

        assert "监控/观测" in categories

    def test_classify_devops_project(self):
        """测试 DevOps/基础设施项目分类"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="ansible/ansible",
            name="ansible",
            description="Automation tool",
            stars=60000,
            topics=[
                "devops",
                "automation",
                "configuration",
                "deployment",
                "infrastructure",
            ],
            license="GPL-3.0",
            open_issues=80,
            forks=10000,
            watchers=60000,
            discovery_reason="DevOps tool",
        )

        categories = classifier.classify(project)

        assert "DevOps/基础设施" in categories

    def test_classify_web_framework_project(self):
        """测试 Web 框架项目分类"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="example/fastapi",
            name="fastapi",
            description="Web framework",
            stars=70000,
            topics=["api", "backend", "http", "rest", "web-framework"],
            open_issues=30,
            forks=5000,
            watchers=70000,
            discovery_reason="Web framework",
        )

        categories = classifier.classify(project)

        assert "Web 框架" in categories

    def test_kubernetes_classified_as_devops(self):
        """测试 Kubernetes 被分类为 DevOps"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="kubernetes/kubernetes",
            name="kubernetes",
            description="Container orchestrator",
            stars=100000,
            language="Go",
            topics=["kubernetes", "container", "orchestration", "deployment"],
            license="Apache-2.0",
            open_issues=200,
            forks=30000,
            watchers=100000,
            discovery_reason="Kubernetes",
        )

        categories = classifier.classify(project)

        # kubernetes 关键词应该匹配到 DevOps/基础设施
        assert "DevOps/基础设施" in categories

    def test_tensorflow_classified_as_ml_framework(self):
        """测试 TensorFlow 被分类为机器学习框架"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="tensorflow/tensorflow",
            name="tensorflow",
            description="ML framework",
            stars=180000,
            topics=[
                "machine-learning",
                "deep-learning",
                "tensorflow",
                "keras",
            ],
            license="Apache-2.0",
            open_issues=150,
            forks=90000,
            watchers=180000,
            discovery_reason="ML framework",
        )

        categories = classifier.classify(project)

        assert "机器学习框架" in categories

    def test_grafana_classified_as_monitoring(self):
        """测试 Grafana 被分类为监控工具"""
        classifier = ProjectClassifier()

        project = _build_project(
            repo="grafana/grafana",
            name="grafana",
            description="Dashboard",
            stars=60000,
            language="TypeScript",
            topics=["monitoring", "metrics", "dashboard", "observability"],
            license="AGPL-3.0",
            open_issues=70,
            forks=12000,
            watchers=60000,
            discovery_reason="Monitoring",
        )

        categories = classifier.classify(project)

        assert "监控/观测" in categories
