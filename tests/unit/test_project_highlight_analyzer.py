"""项目亮点分析器测试

测试 ProjectHighlightAnalyzer 的功能。
"""

from unittest.mock import MagicMock, patch

from trendpluse.discovery.highlight_analyzer import (
    ProjectHighlight,
    ProjectHighlightAnalyzer,
)


class MockProject:
    """模拟项目对象"""

    def __init__(
        self,
        repo: str = "open-webui/open-webui",
        description: str = "User-friendly AI Interface",
        language: str = "Python",
        stars: int = 122000,
        topics: list[str] | None = None,
        license: str | None = "MIT",
    ):
        self.repo = repo
        self.description = description
        self.language = language
        self.stars = stars
        self.topics = topics or ["ai", "llm"]
        self.license = license


class TestProjectHighlightAnalyzer:
    """项目亮点分析器测试"""

    def test_project_highlight_model(self):
        """测试 ProjectHighlight 数据模型"""
        highlight = ProjectHighlight(
            recommendation_reason="这是一个优秀的开源项目",
            technical_highlights=["亮点1", "亮点2"],
            use_cases=["场景1", "场景2"],
        )

        assert highlight.recommendation_reason == "这是一个优秀的开源项目"
        assert len(highlight.technical_highlights) == 2
        assert len(highlight.use_cases) == 2

    def test_format_as_markdown(self):
        """测试 Markdown 格式化"""
        highlight = ProjectHighlight(
            recommendation_reason="这是一个优秀的开源项目",
            technical_highlights=["亮点1", "亮点2"],
            use_cases=["场景1"],
        )

        markdown = highlight.format_as_markdown()

        assert "这是一个优秀的开源项目" in markdown
        assert "**技术亮点**:" in markdown
        assert "- 亮点1" in markdown
        assert "**适用场景**:" in markdown

    def test_fallback_method(self):
        """测试降级方法"""
        project_info = {
            "repo": "test/repo",
            "stars": 10000,
            "description": "Test project",
            "language": "Python",
        }

        highlight = ProjectHighlight.fallback(project_info)

        assert "test/repo" in highlight.recommendation_reason
        assert "10,000 Stars" in highlight.technical_highlights[0]
        assert "Python" in highlight.technical_highlights[1]

    @patch("trendpluse.analyzers.base.Anthropic")
    def test_analyze_project_success(self, mock_anthropic, mock_env_vars):
        """测试成功分析项目"""
        # 模拟 LLM 响应
        json_response = """```json
{
    "recommendation_reason": "这是一个优秀的AI界面项目",
    "technical_highlights": [
        "支持多种AI模型后端",
        "提供直观的Web界面",
        "开源可自部署"
    ],
    "use_cases": [
        "企业内部AI助手部署",
        "个人AI工具开发"
    ]
}
```"""

        mock_message = MagicMock()
        mock_message.content = [MagicMock(type="text", text=json_response)]

        mock_anthropic.return_value.messages.create.return_value = mock_message

        analyzer = ProjectHighlightAnalyzer(
            api_key="test_key",
            model="test-model",
            base_url="http://test",
            use_instructor=False,
        )
        result = analyzer.analyze(MockProject())

        assert result.recommendation_reason == "这是一个优秀的AI界面项目"
        assert len(result.technical_highlights) == 3
        assert "支持多种AI模型后端" in result.technical_highlights
        assert len(result.use_cases) == 2

    @patch("trendpluse.analyzers.base.Anthropic")
    def test_analyze_project_with_empty_response(self, mock_anthropic, mock_env_vars):
        """测试 LLM 返回空响应时的降级处理"""
        mock_message = MagicMock()
        mock_message.content = [MagicMock(type="text", text="")]

        mock_anthropic.return_value.messages.create.return_value = mock_message

        analyzer = ProjectHighlightAnalyzer(
            api_key="test_key",
            model="test-model",
            base_url="http://test",
            use_instructor=False,
        )
        result = analyzer.analyze(MockProject())

        # 应该返回降级结果
        assert result.recommendation_reason != ""
        assert len(result.technical_highlights) > 0

    @patch("trendpluse.analyzers.base.Anthropic")
    def test_analyze_with_timeout(self, mock_anthropic, mock_env_vars):
        """测试超时处理"""
        import anthropic

        mock_anthropic.return_value.messages.create.side_effect = (
            anthropic.APITimeoutError("Request timeout")
        )

        analyzer = ProjectHighlightAnalyzer(
            api_key="test_key",
            model="test-model",
            base_url="http://test",
            use_instructor=False,
        )
        result = analyzer.analyze(MockProject())

        # 超时时应该返回降级结果
        assert result is not None
        assert result.recommendation_reason != ""
