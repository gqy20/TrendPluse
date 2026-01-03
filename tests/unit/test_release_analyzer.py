"""Release 分析器单元测试"""

from unittest.mock import MagicMock, patch

from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer


class TestReleaseAnalyzer:
    """测试 Release 分析器"""

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_init_with_required_params(self, mock_anthropic):
        """测试：正确初始化分析器"""
        # Arrange & Act
        analyzer = ReleaseAnalyzer(
            api_key="test_key",
            model="glm-4.7",
            base_url="https://api.test.com",
        )

        # Assert
        assert analyzer.api_key == "test_key"
        assert analyzer.model == "glm-4.7"
        assert analyzer.base_url == "https://api.test.com"
        mock_anthropic.assert_called_once()

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_init_with_default_model(self, mock_anthropic):
        """测试：使用默认模型初始化"""
        # Arrange & Act
        analyzer = ReleaseAnalyzer(api_key="test_key")

        # Assert
        assert analyzer.model == "glm-4.7"

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_returns_signals(self, mock_anthropic):
        """测试：分析 releases 应返回信号列表"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        response_json = (
            '[{"title": "新版本发布", "type": "capability", '
            '"category": "engineering", "impact_score": 4, '
            '"why_it_matters": "重要功能更新", '
            '"related_repos": ["test/repo"], '
            '"sources": ["https://github.com/test/repo/releases/v1.0.0"]}]'
        )
        mock_message.content = [MagicMock(text=response_json)]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v1.0.0",
                    "name": "First Release",
                    "body": "Initial release",
                    "created_at": "2025-01-01T00:00:00Z",
                }
            ]
        }

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert len(signals) == 1
        assert signals[0].title == "新版本发布"
        assert signals[0].type == "capability"
        assert signals[0].category == "engineering"
        assert signals[0].impact_score == 4

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_with_empty_list(self, mock_anthropic):
        """测试：空 releases 应返回空列表"""
        # Arrange
        mock_anthropic.return_value = MagicMock()
        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {"detailed_releases": []}

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert signals == []

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_with_missing_detailed_releases(self, mock_anthropic):
        """测试：缺少 detailed_releases 字段应返回空列表"""
        # Arrange
        mock_anthropic.return_value = MagicMock()
        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {}

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert signals == []

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_handles_llm_error_gracefully(self, mock_anthropic):
        """测试：LLM API 错误应优雅处理并返回空列表"""
        # Arrange
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("API Error")
        mock_anthropic.return_value = mock_client

        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v1.0.0",
                    "name": "Test Release",
                }
            ]
        }

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert - 应返回空列表而不是抛出异常
        assert signals == []

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_parses_markdown_code_blocks(self, mock_anthropic):
        """测试：应正确解析 markdown 代码块包裹的 JSON"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        response_text = (
            '```json\n[{"title": "测试", "type": "capability", '
            '"category": "engineering", "impact_score": 3, '
            '"why_it_matters": "测试", '
            '"related_repos": ["test/repo"], '
            '"sources": ["https://github.com/test/repo/releases/v1.0.0"]}]\n```'
        )
        mock_message.content = [MagicMock(text=response_text)]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v1.0.0",
                    "name": "Test Release",
                }
            ]
        }

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert len(signals) == 1
        assert signals[0].title == "测试"

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_filters_minor_releases(self, mock_anthropic):
        """测试：应过滤掉不重要的版本更新"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        # 返回空数组表示没有重要信号
        mock_message.content = [MagicMock(text="[]")]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v1.0.1",
                    "name": "Patch Release",
                    "body": "Bug fixes",
                }
            ]
        }

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert signals == []

    @patch("trendpluse.analyzers.release_analyzer.Anthropic")
    def test_analyze_releases_identifies_major_version_upgrade(
        self, mock_anthropic
    ):
        """测试：应识别主版本升级"""
        # Arrange
        mock_client = MagicMock()
        mock_message = MagicMock()
        response_json = (
            '[{"title": "重大版本升级 2.0", "type": "capability", '
            '"category": "engineering", "impact_score": 5, '
            '"why_it_matters": "重大架构改进", '
            '"related_repos": ["test/repo"], '
            '"sources": ["https://github.com/test/repo/releases/v2.0.0"]}]'
        )
        mock_message.content = [MagicMock(text=response_json)]
        mock_client.messages.create.return_value = mock_message
        mock_anthropic.return_value = mock_client

        analyzer = ReleaseAnalyzer(api_key="test_key")
        releases = {
            "detailed_releases": [
                {
                    "repo": "test/repo",
                    "tag_name": "v2.0.0",
                    "name": "Major Release",
                    "version_info": {"major": 2, "minor": 0, "patch": 0},
                }
            ]
        }

        # Act
        signals = analyzer.analyze_releases(releases)

        # Assert
        assert len(signals) == 1
        assert signals[0].impact_score == 5
        assert "2.0" in signals[0].title
