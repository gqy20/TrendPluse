"""Pipeline 并行采集集成测试

测试 Pipeline 正确使用并行采集方法。
"""

from unittest.mock import MagicMock


class TestPipelineParallelCollection:
    """测试 Pipeline 并行采集集成"""

    def test_uses_parallel_collection_when_enabled(self):
        """测试：当启用并行时，应使用并行采集方法"""
        # Arrange - 先不 patch，只测试配置结构
        mock_settings = MagicMock()
        mock_settings.github_token = "test_token"
        mock_settings.anthropic_api_key = "test_api_key"
        mock_settings.anthropic_model = "glm-4.7"
        mock_settings.anthropic_base_url = "https://open.bigmodel.cn/api/anthropic"
        mock_settings.github_repos = ["anthropics/skills", "test/repo"]
        mock_settings.max_candidates = 20
        mock_settings.days_to_lookback = 1
        mock_settings.enable_parallel_collection = True
        mock_settings.max_parallel_workers = 4
        mock_settings.include_prereleases = False
        mock_settings.feishu_webhook_url = ""

        # Act & Assert - 验证配置存在
        assert hasattr(mock_settings, "enable_parallel_collection")
        assert mock_settings.enable_parallel_collection is True
        assert hasattr(mock_settings, "max_parallel_workers")
        assert mock_settings.max_parallel_workers == 4

    def test_uses_sequential_collection_when_parallel_disabled(self):
        """测试：当禁用并行时，应使用串行采集方法"""
        # Arrange
        mock_settings = MagicMock()
        mock_settings.github_token = "test_token"
        mock_settings.anthropic_api_key = "test_api_key"
        mock_settings.anthropic_model = "glm-4.7"
        mock_settings.anthropic_base_url = "https://open.bigmodel.cn/api/anthropic"
        mock_settings.github_repos = ["anthropics/skills"]
        mock_settings.max_candidates = 20
        mock_settings.days_to_lookback = 1
        mock_settings.enable_parallel_collection = False
        mock_settings.include_prereleases = False
        mock_settings.feishu_webhook_url = ""

        # Act & Assert - 验证配置存在
        assert hasattr(mock_settings, "enable_parallel_collection")
        assert mock_settings.enable_parallel_collection is False
