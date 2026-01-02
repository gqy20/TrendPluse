"""配置管理单元测试"""

import pytest
from pydantic import ValidationError


class TestSettings:
    """测试 Settings 配置模型"""

    def test_init_with_valid_env_vars(self, monkeypatch):
        """测试：使用有效的环境变量初始化配置"""
        # Arrange - 准备环境变量
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
        """测试：使用默认仓库列表"""
        # Arrange
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        # 不设置 GITHUB_REPOS

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert - 应该使用默认的 19 个仓库
        assert len(settings.github_repos) == 19
        assert "anthropics/skills" in settings.github_repos
        assert "anthropics/claude-quickstarts" in settings.github_repos
        assert "cline/cline" in settings.github_repos
        assert "continuedev/continue" in settings.github_repos

    def test_validate_invalid_repo_format(self, monkeypatch):
        """测试：无效的仓库格式应该抛出错误"""
        # Arrange
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
        # Arrange - 清除环境变量
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            from trendpluse.config import Settings

            _ = Settings()

        # 应该提示缺少必需字段（只有 anthropic_api_key）
        errors = exc_info.value.errors()
        error_fields = {e["loc"][0] for e in errors}
        assert "anthropic_api_key" in error_fields

    def test_max_candidates_default_value(self, monkeypatch):
        """测试：max_candidates 默认值应该是 20"""
        # Arrange
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.max_candidates == 20

    def test_daily_token_budget_default_value(self, monkeypatch):
        """测试：daily_token_budget 默认值应该是 100000"""
        # Arrange
        monkeypatch.setenv("GITHUB_TOKEN", "test_token")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")

        # Act
        from trendpluse.config import Settings

        settings = Settings()

        # Assert
        assert settings.daily_token_budget == 100_000
