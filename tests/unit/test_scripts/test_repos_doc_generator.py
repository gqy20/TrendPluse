"""仓库文档生成器测试

测试从 config 生成监控仓库列表的 Markdown 文档。
"""

from pathlib import Path

from trendpluse.app.repos_doc_generator import (
    RepoCategory,
    generate_repos_markdown,
    parse_repos_from_config,
)
from trendpluse.models.repository import MonitoredRepo


def _build_repo(
    repo: str,
    description: str,
    url: str | None = None,
) -> MonitoredRepo:
    """构造测试用监控仓库。"""
    return MonitoredRepo(
        repo=repo,
        url=url or f"https://github.com/{repo}",
        description=description,
    )


class TestRepoCategory:
    """测试 RepoCategory 数据类"""

    def test_repo_category_creation(self) -> None:
        """测试创建仓库分类"""
        category = RepoCategory(
            name="Anthropic 核心产品",
            repos=[
                _build_repo("anthropics/claude-code", "Claude Code"),
                _build_repo("anthropics/skills", "Skills"),
            ],
        )

        assert category.name == "Anthropic 核心产品"
        assert [repo.repo for repo in category.repos] == [
            "anthropics/claude-code",
            "anthropics/skills",
        ]

    def test_repo_category_empty_repos(self) -> None:
        """测试空仓库列表的分类"""
        category = RepoCategory(name="测试分类", repos=[])

        assert category.repos == []


class TestParseReposFromConfig:
    """测试从配置解析仓库列表"""

    def test_parse_anthropic_core_products(self) -> None:
        """测试解析 Anthropic 核心产品"""
        repos = [
            _build_repo("anthropics/claude-code", "Claude Code"),
            _build_repo("anthropics/skills", "Skills"),
            _build_repo("anthropics/claude-cookbooks", "Cookbooks"),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 Anthropic 核心产品分类
        anthropic_core = next(
            (c for c in categories if c.name == "Anthropic 核心产品"), None
        )
        assert anthropic_core is not None
        assert "anthropics/claude-code" in [repo.repo for repo in anthropic_core.repos]

    def test_parse_sdk_repos(self) -> None:
        """测试解析 SDK 仓库"""
        repos = [
            _build_repo("anthropics/claude-agent-sdk-python", "SDK Python"),
            _build_repo("anthropics/anthropic-sdk-python", "Anthropic SDK Python"),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 Anthropic SDK & Agent 分类
        sdk_category = next(
            (c for c in categories if c.name == "Anthropic SDK & Agent"), None
        )
        assert sdk_category is not None
        assert "anthropics/claude-agent-sdk-python" in [
            repo.repo for repo in sdk_category.repos
        ]

    def test_parse_ai_assistant_repos(self) -> None:
        """测试解析 AI 编程助手仓库"""
        repos = [
            _build_repo("cline/cline", "Cline"),
            _build_repo("paul-gauthier/aider", "Aider"),
            _build_repo("continuedev/continue", "Continue"),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 AI 编程助手分类
        ai_assistant = next((c for c in categories if c.name == "AI 编程助手"), None)
        assert ai_assistant is not None
        assert "cline/cline" in [repo.repo for repo in ai_assistant.repos]

    def test_parse_agent_framework_repos(self) -> None:
        """测试解析 Agent 框架仓库"""
        repos = [
            _build_repo("langchain-ai/langchain", "LangChain"),
            _build_repo("langgenius/dify", "Dify"),
            _build_repo("run-llama/llama_index", "LlamaIndex"),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 Agent 框架分类
        agent_framework = next((c for c in categories if c.name == "Agent 框架"), None)
        assert agent_framework is not None
        assert "langchain-ai/langchain" in [repo.repo for repo in agent_framework.repos]

    def test_parse_unknown_repo_returns_empty_category(self) -> None:
        """测试解析未知仓库时返回空分类而不是抛出异常"""
        repos = [
            _build_repo(
                "unknown/user/repo", "Unknown", "https://github.com/unknown/user"
            ),
            _build_repo("invalid-format", "Invalid"),
        ]

        # 应该不抛出异常，但返回空或默认分类
        categories = parse_repos_from_config(repos)

        # 未知仓库应该被分配到某个分类中或被忽略
        # 这里我们验证不会抛出异常
        assert isinstance(categories, list)

    def test_parse_empty_repos_list(self) -> None:
        """测试解析空仓库列表"""
        repos: list[MonitoredRepo] = []

        categories = parse_repos_from_config(repos)

        assert categories == []


class TestGenerateReposMarkdown:
    """测试生成仓库列表 Markdown"""

    def test_generate_markdown_header(self) -> None:
        """测试生成 Markdown 头部"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[_build_repo("anthropics/claude-code", "Claude Code")],
            )
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含正确的标题
        assert "### 📋 监控项目" in markdown
        assert "我们监控以下" in markdown

    def test_generate_markdown_with_single_category(self) -> None:
        """测试生成单个分类的 Markdown"""
        categories = [
            RepoCategory(
                name="Anthropic 核心产品",
                repos=[
                    _build_repo("anthropics/claude-code", "Claude Code"),
                    _build_repo("anthropics/skills", "Skills"),
                ],
            )
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含分类标题
        assert "#### Anthropic 核心产品" in markdown
        assert '<div class="tp-entry-grid">' in markdown
        assert (
            'class="tp-entry-card" href="https://github.com/anthropics/claude-code"'
            in markdown
        )
        assert (
            'class="tp-entry-card" href="https://github.com/anthropics/skills"'
            in markdown
        )

    def test_generate_markdown_with_multiple_categories(self) -> None:
        """测试生成多个分类的 Markdown"""
        categories = [
            RepoCategory(
                name="分类 A",
                repos=[_build_repo("user/repo1", "Repo 1")],
            ),
            RepoCategory(
                name="分类 B",
                repos=[_build_repo("user/repo2", "Repo 2")],
            ),
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含所有分类
        assert "#### 分类 A" in markdown
        assert "#### 分类 B" in markdown
        assert 'href="https://github.com/user/repo1"' in markdown
        assert 'href="https://github.com/user/repo2"' in markdown

    def test_generate_markdown_repo_count(self) -> None:
        """测试生成 Markdown 时统计仓库数量"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[
                    _build_repo("user/repo1", "Repo 1"),
                    _build_repo("user/repo2", "Repo 2"),
                    _build_repo("user/repo3", "Repo 3"),
                ],
            )
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含正确的仓库总数
        assert "3 个" in markdown

    def test_generate_markdown_underscore_escaping(self) -> None:
        """测试 Markdown 中的下划线转义"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[_build_repo("run-llama/llama_index", "LlamaIndex")],
            )
        ]

        markdown = generate_repos_markdown(categories)

        assert "run-llama/llama_index" in markdown
        assert 'href="https://github.com/run-llama/llama_index"' in markdown

    def test_generate_markdown_includes_description(self) -> None:
        """测试生成 Markdown 时包含仓库简介。"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[
                    _build_repo(
                        "anthropics/claude-code",
                        "Anthropic 的 CLI 编码代理工具。",
                    )
                ],
            )
        ]

        markdown = generate_repos_markdown(categories)

        assert "Anthropic 的 CLI 编码代理工具" in markdown


class TestIntegration:
    """集成测试"""

    def test_full_workflow_from_config_to_markdown(self, tmp_path: Path) -> None:
        """测试完整工作流：从配置到 Markdown 生成"""
        # Arrange: 准备测试数据
        repos = [
            _build_repo("anthropics/claude-code", "Claude Code"),
            _build_repo("anthropics/skills", "Skills"),
            _build_repo("cline/cline", "Cline"),
            _build_repo("langchain-ai/langchain", "LangChain"),
        ]

        # Act: 执行解析和生成
        categories = parse_repos_from_config(repos)
        markdown = generate_repos_markdown(categories)

        # Assert: 验证生成的 Markdown
        assert "### 📋 监控项目" in markdown
        assert "4 个" in markdown
        assert 'href="https://github.com/anthropics/claude-code"' in markdown
        assert 'href="https://github.com/cline/cline"' in markdown
