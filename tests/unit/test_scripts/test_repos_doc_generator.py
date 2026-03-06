"""仓库文档生成器测试

测试从 config 生成监控仓库列表的 Markdown 文档。
"""

from pathlib import Path

from trendpluse.automation.repos_doc_generator import (
    RepoCategory,
    generate_repos_markdown,
    parse_repos_from_config,
)
from trendpluse.models.repository import MonitoredRepo


class TestRepoCategory:
    """测试 RepoCategory 数据类"""

    def test_repo_category_creation(self) -> None:
        """测试创建仓库分类"""
        category = RepoCategory(
            name="Anthropic 核心产品",
            repos=[
                MonitoredRepo(
                    repo="anthropics/claude-code",
                    url="https://github.com/anthropics/claude-code",
                    description="Claude Code",
                ),
                MonitoredRepo(
                    repo="anthropics/skills",
                    url="https://github.com/anthropics/skills",
                    description="Skills",
                ),
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
            MonitoredRepo(
                repo="anthropics/claude-code",
                url="https://github.com/anthropics/claude-code",
                description="Claude Code",
            ),
            MonitoredRepo(
                repo="anthropics/skills",
                url="https://github.com/anthropics/skills",
                description="Skills",
            ),
            MonitoredRepo(
                repo="anthropics/claude-cookbooks",
                url="https://github.com/anthropics/claude-cookbooks",
                description="Cookbooks",
            ),
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
            MonitoredRepo(
                repo="anthropics/claude-agent-sdk-python",
                url="https://github.com/anthropics/claude-agent-sdk-python",
                description="SDK Python",
            ),
            MonitoredRepo(
                repo="anthropics/anthropic-sdk-python",
                url="https://github.com/anthropics/anthropic-sdk-python",
                description="Anthropic SDK Python",
            ),
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
            MonitoredRepo(
                repo="cline/cline",
                url="https://github.com/cline/cline",
                description="Cline",
            ),
            MonitoredRepo(
                repo="paul-gauthier/aider",
                url="https://github.com/paul-gauthier/aider",
                description="Aider",
            ),
            MonitoredRepo(
                repo="continuedev/continue",
                url="https://github.com/continuedev/continue",
                description="Continue",
            ),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 AI 编程助手分类
        ai_assistant = next((c for c in categories if c.name == "AI 编程助手"), None)
        assert ai_assistant is not None
        assert "cline/cline" in [repo.repo for repo in ai_assistant.repos]

    def test_parse_agent_framework_repos(self) -> None:
        """测试解析 Agent 框架仓库"""
        repos = [
            MonitoredRepo(
                repo="langchain-ai/langchain",
                url="https://github.com/langchain-ai/langchain",
                description="LangChain",
            ),
            MonitoredRepo(
                repo="langgenius/dify",
                url="https://github.com/langgenius/dify",
                description="Dify",
            ),
            MonitoredRepo(
                repo="run-llama/llama_index",
                url="https://github.com/run-llama/llama_index",
                description="LlamaIndex",
            ),
        ]

        categories = parse_repos_from_config(repos)

        # 验证存在 Agent 框架分类
        agent_framework = next((c for c in categories if c.name == "Agent 框架"), None)
        assert agent_framework is not None
        assert "langchain-ai/langchain" in [repo.repo for repo in agent_framework.repos]

    def test_parse_unknown_repo_returns_empty_category(self) -> None:
        """测试解析未知仓库时返回空分类而不是抛出异常"""
        repos = [
            MonitoredRepo(
                repo="unknown/user/repo",
                url="https://github.com/unknown/user",
                description="Unknown",
            ),
            MonitoredRepo(
                repo="invalid-format",
                url="https://github.com/invalid-format",
                description="Invalid",
            ),
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
                repos=[
                    MonitoredRepo(
                        repo="anthropics/claude-code",
                        url="https://github.com/anthropics/claude-code",
                        description="Claude Code",
                    )
                ],
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
                    MonitoredRepo(
                        repo="anthropics/claude-code",
                        url="https://github.com/anthropics/claude-code",
                        description="Claude Code",
                    ),
                    MonitoredRepo(
                        repo="anthropics/skills",
                        url="https://github.com/anthropics/skills",
                        description="Skills",
                    ),
                ],
            )
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含分类标题
        assert "#### Anthropic 核心产品" in markdown
        # 验证包含仓库链接
        assert (
            "[anthropics/claude-code](https://github.com/anthropics/claude-code)"
            in markdown
        )
        assert "[anthropics/skills](https://github.com/anthropics/skills)" in markdown

    def test_generate_markdown_with_multiple_categories(self) -> None:
        """测试生成多个分类的 Markdown"""
        categories = [
            RepoCategory(
                name="分类 A",
                repos=[
                    MonitoredRepo(
                        repo="user/repo1",
                        url="https://github.com/user/repo1",
                        description="Repo 1",
                    )
                ],
            ),
            RepoCategory(
                name="分类 B",
                repos=[
                    MonitoredRepo(
                        repo="user/repo2",
                        url="https://github.com/user/repo2",
                        description="Repo 2",
                    )
                ],
            ),
        ]

        markdown = generate_repos_markdown(categories)

        # 验证包含所有分类
        assert "#### 分类 A" in markdown
        assert "#### 分类 B" in markdown
        # 验证包含所有仓库
        assert "[user/repo1](https://github.com/user/repo1)" in markdown
        assert "[user/repo2](https://github.com/user/repo2)" in markdown

    def test_generate_markdown_repo_count(self) -> None:
        """测试生成 Markdown 时统计仓库数量"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[
                    MonitoredRepo(
                        repo="user/repo1",
                        url="https://github.com/user/repo1",
                        description="Repo 1",
                    ),
                    MonitoredRepo(
                        repo="user/repo2",
                        url="https://github.com/user/repo2",
                        description="Repo 2",
                    ),
                    MonitoredRepo(
                        repo="user/repo3",
                        url="https://github.com/user/repo3",
                        description="Repo 3",
                    ),
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
                repos=[
                    MonitoredRepo(
                        repo="run-llama/llama_index",
                        url="https://github.com/run-llama/llama_index",
                        description="LlamaIndex",
                    )
                ],
            )
        ]

        markdown = generate_repos_markdown(categories)

        # 验证下划线被正确转义
        assert "llama\\_index" in markdown
        assert (
            "[run-llama/llama\\_index](https://github.com/run-llama/llama_index)"
            in markdown
        )

    def test_generate_markdown_includes_description(self) -> None:
        """测试生成 Markdown 时包含仓库简介。"""
        categories = [
            RepoCategory(
                name="测试分类",
                repos=[
                    MonitoredRepo(
                        repo="anthropics/claude-code",
                        url="https://github.com/anthropics/claude-code",
                        description="Anthropic 的 CLI 编码代理工具。",
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
            MonitoredRepo(
                repo="anthropics/claude-code",
                url="https://github.com/anthropics/claude-code",
                description="Claude Code",
            ),
            MonitoredRepo(
                repo="anthropics/skills",
                url="https://github.com/anthropics/skills",
                description="Skills",
            ),
            MonitoredRepo(
                repo="cline/cline",
                url="https://github.com/cline/cline",
                description="Cline",
            ),
            MonitoredRepo(
                repo="langchain-ai/langchain",
                url="https://github.com/langchain-ai/langchain",
                description="LangChain",
            ),
        ]

        # Act: 执行解析和生成
        categories = parse_repos_from_config(repos)
        markdown = generate_repos_markdown(categories)

        # Assert: 验证生成的 Markdown
        assert "### 📋 监控项目" in markdown
        assert "4 个" in markdown
        assert (
            "[anthropics/claude-code](https://github.com/anthropics/claude-code)"
            in markdown
        )
        assert "[cline/cline](https://github.com/cline/cline)" in markdown
