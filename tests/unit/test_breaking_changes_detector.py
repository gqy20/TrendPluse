"""Breaking Changes 检测器单元测试"""

from unittest.mock import MagicMock, patch

from trendpluse.analyzers.breaking_changes_detector import (
    BreakingChangesDetector,
)


class TestBreakingChangesDetector:
    """测试 Breaking Changes 检测器"""

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_init_with_required_params(self, mock_anthropic):
        """测试：正确初始化检测器"""
        # Arrange & Act
        detector = BreakingChangesDetector(
            api_key="test_key",
            model="glm-4.7",
            base_url="https://api.test.com",
        )

        # Assert
        assert detector.api_key == "test_key"
        assert detector.model == "glm-4.7"
        assert detector.base_url == "https://api.test.com"
        mock_anthropic.assert_called_once()

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_breaking_changes_returns_list(self, mock_anthropic):
        """测试：检测应返回 breaking changes 列表"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        mock_message.content = [
            MagicMock(
                text='[{"repo": "test/repo", "tag_name": "v2.0.0", '
                '"has_breaking": true, '
                '"changes": [{"description": "API 移除", '
                '"impact": "high", "category": "API"}]}]'
            )
        ]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        detector = BreakingChangesDetector(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v2.0.0",
                    "name": "Major Release",
                    "body": "BREAKING CHANGE: Removed old API",
                }
            ]
        }

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert
        assert len(results) == 1
        assert results[0]["repo"] == "test/repo"
        assert results[0]["tag_name"] == "v2.0.0"
        assert results[0]["has_breaking"] is True
        assert len(results[0]["changes"]) == 1

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_with_empty_releases(self, mock_anthropic):
        """测试：空 releases 应返回空列表"""
        # Arrange
        mock_anthropic.return_value = MagicMock()
        detector = BreakingChangesDetector(api_key="test_key")
        releases = {"detailed_releases": []}

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert
        assert results == []

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_parses_markdown_code_blocks(self, mock_anthropic):
        """测试：应正确解析 markdown 代码块"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        response_text = (
            '```json\n[{"repo": "test/repo", "tag_name": "v2.0.0", '
            '"has_breaking": false, "changes": []}]\n```'
        )
        mock_message.content = [MagicMock(text=response_text)]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        detector = BreakingChangesDetector(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v2.0.0",
                    "body": "No breaking changes",
                }
            ]
        }

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert
        assert len(results) == 1
        assert results[0]["has_breaking"] is False

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_handles_llm_error_gracefully(self, mock_anthropic):
        """测试：LLM 错误应优雅处理"""
        # Arrange
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("API Error")
        mock_anthropic.return_value = mock_client

        detector = BreakingChangesDetector(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v2.0.0",
                    "body": "Test",
                }
            ]
        }

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert - 应返回空列表
        assert results == []

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_identifies_multiple_breaking_changes(self, mock_anthropic):
        """测试：应识别多个 breaking changes"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        response_json = (
            '[{"repo": "test/repo", "tag_name": "v2.0.0", '
            '"has_breaking": true, '
            '"changes": ['
            '{"description": "API 移除", "impact": "high", "category": "API"}, '
            '{"description": "配置变更", "impact": "medium", "category": "Config"}'
            "]}]"
        )
        mock_message.content = [MagicMock(text=response_json)]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        detector = BreakingChangesDetector(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v2.0.0",
                    "body": "Multiple breaking changes",
                }
            ]
        }

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert
        assert len(results) == 1
        assert results[0]["has_breaking"] is True
        assert len(results[0]["changes"]) == 2

    @patch("trendpluse.analyzers.breaking_changes_detector.Anthropic")
    def test_detect_filters_non_breaking_releases(self, mock_anthropic):
        """测试：应过滤非 breaking changes 的版本"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        # AI 返回空数组表示没有 breaking changes
        mock_message.content = [MagicMock(text="[]")]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        detector = BreakingChangesDetector(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v1.0.1",
                    "body": "Bug fixes only",
                }
            ]
        }

        # Act
        results = detector.detect_breaking_changes(releases)

        # Assert
        assert results == []
