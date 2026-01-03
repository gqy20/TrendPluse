"""测试添加仓库到配置脚本"""

from pathlib import Path


class TestAddRepo:
    """测试 add_repo.py 脚本功能"""

    def test_add_repo_to_category(self, tmp_path: Path):
        """测试：添加仓库到指定分类"""
        # Arrange - 准备临时配置文件
        config_content = '''"""配置管理模块"""

from pydantic import Field

class Settings:
    github_repos: list[str] = Field(
        default=[
            # Anthropic 核心产品
            "anthropics/claude-code",
            "anthropics/skills",
            # Anthropic SDK & Agent
            "anthropics/anthropic-sdk-python",
            # Agentic AI 核心框架
            "openai/swarm",
            "crewAIInc/crewAI",
            # 自主 AI 编程代理
            "cline/cline",
        ]
    )
'''
        config_file = tmp_path / "config.py"
        config_file.write_text(config_content)

        # Act - 添加新仓库
        from scripts.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="openai/codex",
            category="Agentic AI 核心框架",
        )

        # Assert - 验证添加成功
        assert result is True
        updated_content = config_file.read_text()

        # 检查仓库已添加
        assert (
            '"openai/codex"' in updated_content or "'openai/codex'" in updated_content
        )

        # 检查添加位置正确（在 Agentic AI 核心框架分类下）
        lines = updated_content.split("\n")
        swarm_line = next(i for i, line in enumerate(lines) if "openai/swarm" in line)
        codex_line = next(i for i, line in enumerate(lines) if "openai/codex" in line)
        next_section_line = next(
            i for i, line in enumerate(lines) if "# 自主 AI 编程代理" in line
        )

        # codex 应该在 swarm 之后，下一个分类之前
        assert swarm_line < codex_line < next_section_line

    def test_add_duplicate_repo_returns_false(self, tmp_path: Path):
        """测试：添加已存在的仓库返回 False"""
        # Arrange
        config_content = '''"""配置管理模块"""

class Settings:
    github_repos: list[str] = Field(
        default=[
            "anthropics/claude-code",
        ]
    )
'''
        config_file = tmp_path / "config.py"
        config_file.write_text(config_content)

        # Act
        from scripts.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="anthropics/claude-code",
            category="Anthropic 核心产品",
        )

        # Assert
        assert result is False

    def test_add_repo_invalid_category(self, tmp_path: Path):
        """测试：无效分类返回 False"""
        # Arrange
        config_content = '''"""配置管理模块"""

class Settings:
    github_repos: list[str] = Field(default=[])
'''
        config_file = tmp_path / "config.py"
        config_file.write_text(config_content)

        # Act
        from scripts.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="test/repo",
            category="不存在的分类",
        )

        # Assert
        assert result is False

    def test_validate_repo_format(self):
        """测试：仓库格式验证"""
        from scripts.add_repo import validate_repo_format

        # 有效格式
        assert validate_repo_format("anthropics/claude-code") is True
        assert validate_repo_format("openai/swarm") is True
        assert validate_repo_format("a/b") is True

        # 无效格式
        assert validate_repo_format("anthropics-claude-code") is False
        assert validate_repo_format("anthropics/claude/code") is False
        assert validate_repo_format("/claude-code") is False
        assert validate_repo_format("anthropics/") is False
        assert validate_repo_format("") is False

    def test_parse_issue_body(self):
        """测试：解析 Issue 表单内容"""
        from scripts.add_repo import parse_issue_body

        body = """
        ### GitHub 仓库

        openai/codex

        ### 分类

        Agentic AI 核心框架

        ### 添加理由

        这是一个终端编程代理工具
        """

        # Act
        result = parse_issue_body(body)

        # Assert
        assert result["repo"] == "openai/codex"
        assert result["category"] == "Agentic AI 核心框架"
        assert "终端编程代理" in result["reason"]

    def test_category_to_marker_mapping(self):
        """测试：分类到注释标记的映射"""
        from scripts.add_repo import get_category_markers

        # 测试主要分类
        markers = get_category_markers("Agentic AI 核心框架")
        assert markers is not None
        assert "start" in markers
        assert "end" in markers
        assert "Agentic AI" in markers["start"]

        # 无效分类
        assert get_category_markers("不存在的分类") is None
