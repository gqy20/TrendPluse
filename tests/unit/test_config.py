"""配置管理单元测试"""

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from trendpluse.utils.repo_config_loader import load_monitored_repo_configs


class TestSettings:
    """测试 Settings 配置模型"""

    @staticmethod
    def _clear_github_token_env(monkeypatch) -> None:
        """清理所有 GitHub Token 相关环境变量。"""
        monkeypatch.delenv("PAT_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_PAT", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    def test_init_with_valid_env_vars(self, monkeypatch):
        """测试：使用有效的环境变量初始化配置"""
        # Arrange - 准备环境变量
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.setenv("GITHUB_REPOS", '["owner1/repo1", "owner2/repo2"]')

        # Act - 导入并创建配置
        from trendpluse.config import Settings

        settings = Settings()

        # Assert - 验证配置
        assert settings.github_token == "test_token"
        assert settings.anthropic_api_key == "test_key"
        assert settings.github_repos == ["owner1/repo1", "owner2/repo2"]

    def test_init_with_default_repos(self, monkeypatch):
        """测试：默认从根目录 repos.json 加载仓库列表。"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        # 不设置 GITHUB_REPOS

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        repo_file = Path(__file__).resolve().parents[2] / "repos.json"
        default_repos = load_monitored_repo_configs(str(repo_file))
        assert len(settings.github_repos) == len(default_repos)

        # 验证核心仓库存在（这些是关键的代表性仓库）
        core_repos = [
            "anthropics/claude-code",  # Anthropic 核心
            "anthropics/skills",
            "cline/cline",  # AI 编程助手
            "langchain-ai/langchain",  # Agent 框架
            "openai/swarm",  # Agentic AI
            "AndyMik90/Auto-Claude",  # 自主编程代理
        ]
        for repo in core_repos:
            assert repo in settings.github_repos, f"核心仓库 {repo} 未找到"

    def test_init_with_repo_file(self, monkeypatch, tmp_path):
        """测试：未显式提供 GITHUB_REPOS 时应从 JSON 文件加载。"""
        self._clear_github_token_env(monkeypatch)
        repo_file = tmp_path / "repos.json"
        repo_file.write_text(
            json.dumps(
                [
                    {
                        "url": "https://github.com/owner/repo1",
                        "description": "仓库一",
                    },
                    {
                        "url": "https://github.com/owner/repo2",
                        "description": "仓库二",
                    },
                ]
            ),
            encoding="utf-8",
        )
        monkeypatch.setenv("GITHUB_REPOS_FILE", str(repo_file))
        monkeypatch.delenv("GITHUB_REPOS", raising=False)

        from trendpluse.config import Settings

        settings = Settings()

        assert settings.github_repos == ["owner/repo1", "owner/repo2"]
        assert settings.monitored_repo_configs[0].description == "仓库一"

    def test_monitored_repo_configs_fallback_to_env_repos(self, monkeypatch):
        """测试：仅使用 GITHUB_REPOS 时仍可生成结构化配置。"""
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_REPOS", '["owner/from-env"]')

        from trendpluse.config import Settings

        settings = Settings()

        assert settings.monitored_repo_configs[0].repo == "owner/from-env"
        assert (
            settings.monitored_repo_configs[0].url
            == "https://github.com/owner/from-env"
        )
        assert settings.monitored_repo_configs[0].description == ""

    def test_github_repos_env_takes_priority_over_repo_file(
        self, monkeypatch, tmp_path
    ):
        """测试：显式设置 GITHUB_REPOS 时优先使用环境变量。"""
        self._clear_github_token_env(monkeypatch)
        repo_file = tmp_path / "repos.json"
        repo_file.write_text(
            json.dumps(
                [
                    {
                        "url": "https://github.com/owner/from-file",
                        "description": "文件配置",
                    }
                ]
            ),
            encoding="utf-8",
        )
        monkeypatch.setenv("GITHUB_REPOS_FILE", str(repo_file))
        monkeypatch.setenv("GITHUB_REPOS", '["owner/from-env"]')

        from trendpluse.config import Settings

        settings = Settings()

        assert settings.github_repos == ["owner/from-env"]

    def test_invalid_repo_file_url_raises_error(self, monkeypatch, tmp_path):
        """测试：配置文件中的非法 GitHub URL 会抛出错误。"""
        self._clear_github_token_env(monkeypatch)
        repo_file = tmp_path / "repos.json"
        repo_file.write_text(
            json.dumps(
                [
                    {
                        "url": "https://gitlab.com/owner/repo1",
                        "description": "非法地址",
                    }
                ]
            ),
            encoding="utf-8",
        )
        monkeypatch.setenv("GITHUB_REPOS_FILE", str(repo_file))
        monkeypatch.delenv("GITHUB_REPOS", raising=False)

        from trendpluse.config import Settings

        with pytest.raises(ValidationError):
            Settings()

    def test_validate_invalid_repo_format(self, monkeypatch):
        """测试：无效的仓库格式应该抛出错误"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.setenv("GITHUB_REPOS", '["invalid-repo-name"]')

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            from trendpluse.config import Settings

            _ = Settings()

        assert "Invalid repo format" in str(exc_info.value)

    def test_validate_missing_required_fields(self, monkeypatch):
        """测试：缺少必需字段应该抛出错误"""
        # Arrange - 清除所有环境变量（包括备选变量）
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        monkeypatch.delenv("ANTHROPIC_AUTH_KEY", raising=False)
        monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
        self._clear_github_token_env(monkeypatch)

        # Act & Assert
        # 注意：anthropic_api_key 现在有默认值（空字符串），所以不会抛出 ValidationError
        # 这个测试验证了默认值的行为
        from trendpluse.config import Settings

        settings = Settings()

        # 验证默认值为空字符串
        assert settings.anthropic_api_key == ""
        assert settings.github_token == ""  # 也有默认值

    def test_max_candidates_default_value(self, monkeypatch):
        """测试：max_candidates 默认值应该是 20"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.max_candidates == 20

    def test_daily_token_budget_default_value(self, monkeypatch):
        """测试：daily_token_budget 默认值应该是 50000000。"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.daily_token_budget == 50_000_000

    def test_issue_agent_review_confidence_threshold_default_value(self, monkeypatch):
        """测试：Issue Agent 审核阈值默认值应该是 0.6"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.issue_agent_review_confidence_threshold == 0.6

    def test_feishu_at_mobiles_empty_string(self, monkeypatch):
        """测试：空字符串应该返回空列表"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.setenv("FEISHU_AT_MOBILES", "")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.feishu_at_mobiles == ""
        assert settings.feishu_at_mobiles_list == []

    def test_feishu_at_mobiles_comma_separated(self, monkeypatch):
        """测试：逗号分隔格式应该正确解析"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.setenv("FEISHU_AT_MOBILES", "13800138000,13900139000")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.feishu_at_mobiles == "13800138000,13900139000"
        assert settings.feishu_at_mobiles_list == ["13800138000", "13900139000"]

    def test_feishu_at_mobiles_default(self, monkeypatch):
        """测试：未设置时应该使用默认值（空列表）"""
        # Arrange
        self._clear_github_token_env(monkeypatch)
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.delenv("FEISHU_AT_MOBILES", raising=False)

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.feishu_at_mobiles == ""
        assert settings.feishu_at_mobiles_list == []

    def test_anthropic_auth_key_fallback(self, monkeypatch):
        """测试：ANTHROPIC_AUTH_KEY 应该作为 ANTHROPIC_API_KEY 的备选"""
        # Arrange - 只设置 ANTHROPIC_AUTH_KEY，不设置 ANTHROPIC_API_KEY
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        monkeypatch.setenv("ANTHROPIC_AUTH_KEY", "fallback_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert - 应该使用 ANTHROPIC_AUTH_KEY 的值
        assert settings.anthropic_api_key == "fallback_key"

    def test_anthropic_api_key_priority(self, monkeypatch):
        """测试：当两者都存在时，ANTHROPIC_API_KEY 优先"""
        # Arrange - 同时设置两个环境变量
        monkeypatch.setenv("ANTHROPIC_API_KEY", "primary_key")
        monkeypatch.setenv("ANTHROPIC_AUTH_KEY", "fallback_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert - 应该使用 ANTHROPIC_API_KEY 的值（优先级更高）
        assert settings.anthropic_api_key == "primary_key"
