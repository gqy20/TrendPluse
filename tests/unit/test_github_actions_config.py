"""GitHub Actions 配置测试"""
import os

import pytest


class TestGitHubActionsConfig:
    """测试 GitHub Actions 环境配置"""

    def test_anthropic_api_key_required(self, monkeypatch):
        """测试：ANTHROPIC_API_KEY 是必需的"""
        # Arrange - 移除环境变量
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            from trendpluse.config import Settings
            _ = Settings()

        assert "anthropic_api_key" in str(exc_info.value).lower()

    def test_github_token_optional(self, monkeypatch):
        """测试：GITHUB_TOKEN 是可选的"""
        # Arrange
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)

        # Act & Assert - 不应该抛出错误
        from trendpluse.config import Settings
        settings = Settings()

        assert settings.github_token == ""

    def test_anthropic_base_url_default(self, monkeypatch):
        """测试：ANTHROPIC_BASE_URL 有默认值"""
        # Arrange
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
        monkeypatch.delenv("ANTHROPIC_BASE_URL", raising=False)

        # Act
        from trendpluse.config import Settings
        settings = Settings()

        # Assert
        assert settings.anthropic_base_url == "https://open.bigmodel.cn/api/anthropic"
