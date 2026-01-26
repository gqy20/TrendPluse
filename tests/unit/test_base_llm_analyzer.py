"""LLM 分析器基类测试"""

from trendpluse.analyzers.base import BaseLLMAnalyzer


class TestExtractJsonFromMarkdown:
    """测试从 Markdown 中提取 JSON"""

    def test_removes_json_code_block(self):
        """应该移除 ```json 代码块标记"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        response = '```json\n{"key": "value"}\n```'
        result = analyzer._extract_json_from_markdown(response)
        assert result == '{"key": "value"}'

    def test_removes_generic_code_block(self):
        """应该移除 ``` 代码块标记"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        response = '```\n{"key": "value"}\n```'
        result = analyzer._extract_json_from_markdown(response)
        assert result == '{"key": "value"}'

    def test_removes_only_leading_markers(self):
        """应该只移除开头的标记"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        response = '```json\n{"key": "value"}'
        result = analyzer._extract_json_from_markdown(response)
        assert result == '{"key": "value"}'

    def test_returns_clean_json_when_no_markers(self):
        """没有代码块标记时应该返回原始内容"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        response = '{"key": "value"}'
        result = analyzer._extract_json_from_markdown(response)
        assert result == '{"key": "value"}'

    def test_strips_whitespace(self):
        """应该去除首尾空白"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        response = '  \n  ```json\n{"key": "value"}\n```\n  \n'
        result = analyzer._extract_json_from_markdown(response)
        assert result == '{"key": "value"}'


class TestValidateAndCreateSignal:
    """测试使用 Pydantic 验证创建 Signal（推荐方法）"""

    def test_creates_signal_with_required_fields(self):
        """应该创建包含必需字段的 Signal"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        item = {
            "title": "Test Signal",
            "type": "capability",
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "Test description",
        }
        sources = ["https://example.com/pr/1"]
        related_repos = ["anthropics/claude-code"]

        signal = analyzer._validate_and_create_signal(
            item=item,
            index=0,
            sources=sources,
            related_repos=related_repos,
        )

        assert signal is not None
        assert signal.id == "signal-0"
        assert signal.title == "Test Signal"
        assert signal.type == "capability"
        assert signal.sources == sources
        assert signal.related_repos == related_repos

    def test_uses_default_sources_when_not_provided(self):
        """未提供 sources 时应该使用空列表"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        item = {
            "title": "Test Signal",
            "type": "workflow",
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "Test description",
        }

        signal = analyzer._validate_and_create_signal(
            item=item,
            index=0,
            sources=[],
            related_repos=[],
        )

        assert signal is not None
        assert signal.sources == []

    def test_merges_related_repos(self):
        """应该合并提供的 related_repos"""
        analyzer = BaseLLMAnalyzer(api_key="test", model="test")
        item = {
            "title": "Test Signal",
            "type": "capability",
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "Test description",
            "related_repos": ["repo1", "repo2"],
        }

        signal = analyzer._validate_and_create_signal(
            item=item,
            index=0,
            sources=[],
            related_repos=["repo3"],
        )

        # 应该去重并合并
        assert signal is not None
        assert set(signal.related_repos) == {"repo1", "repo2", "repo3"}
