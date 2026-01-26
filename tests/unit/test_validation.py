"""测试 Pydantic 验证功能

演示新的 _validate_and_create_signal 方法的验证能力。
"""

from trendpluse.analyzers.base import BaseLLMAnalyzer


class TestSignalValidation:
    """测试 Signal 的 Pydantic 验证"""

    def test_validate_and_create_signal_with_valid_data(self):
        """测试：使用有效数据创建信号"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        valid_item = {
            "title": "新特性",
            "type": "capability",
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "这是一个重要的新功能",
        }

        signal = analyzer._validate_and_create_signal(
            item=valid_item,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],
        )

        assert signal is not None
        assert signal.id == "signal-0"
        assert signal.title == "新特性"
        assert signal.type == "capability"
        assert signal.category == "engineering"
        assert signal.impact_score == 4
        assert signal.why_it_matters == "这是一个重要的新功能"
        assert signal.sources == ["https://github.com/test/repo/commit/abc123"]
        assert signal.related_repos == ["test/repo"]

    def test_validate_and_create_signal_with_missing_required_field(self):
        """测试：缺少必需字段时返回 None"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        # 缺少必需字段 title
        invalid_item = {
            "type": "capability",
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "这是一个重要的新功能",
        }

        signal = analyzer._validate_and_create_signal(
            item=invalid_item,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],
        )

        assert signal is None

    def test_validate_and_create_signal_with_invalid_type(self):
        """测试：type 字段值无效时返回 None"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        # type 不是有效的枚举值
        invalid_item = {
            "title": "新特性",
            "type": "invalid_type",  # ❌ 不是有效的枚举值
            "category": "engineering",
            "impact_score": 4,
            "why_it_matters": "这是一个重要的新功能",
        }

        signal = analyzer._validate_and_create_signal(
            item=invalid_item,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],
        )

        assert signal is None

    def test_validate_and_create_signal_with_invalid_impact_score_range(self):
        """测试：impact_score 超出范围时返回 None"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        # impact_score 超出 1-5 范围
        invalid_item = {
            "title": "新特性",
            "type": "capability",
            "category": "engineering",
            "impact_score": 10,  # ❌ 超出 1-5 范围
            "why_it_matters": "这是一个重要的新功能",
        }

        signal = analyzer._validate_and_create_signal(
            item=invalid_item,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],
        )

        assert signal is None

    def test_validate_and_create_signal_with_wrong_field_type(self):
        """测试：字段类型错误时返回 None"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        # impact_score 应该是 int，但提供了 str
        invalid_item = {
            "title": "新特性",
            "type": "capability",
            "category": "engineering",
            "impact_score": "high",  # ❌ 应该是 int，不是 str
            "why_it_matters": "这是一个重要的新功能",
        }

        signal = analyzer._validate_and_create_signal(
            item=invalid_item,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],
        )

        assert signal is None

    def test_validate_and_create_signal_merges_related_repos(self):
        """测试：正确合并 related_repos"""
        analyzer = BaseLLMAnalyzer(
            api_key="test-key",
            model="glm-4.7",
            use_instructor=False,
        )

        item_with_related_repos = {
            "title": "跨项目特性",
            "type": "capability",
            "category": "engineering",
            "impact_score": 5,
            "why_it_matters": "影响多个项目",
            "related_repos": ["other/repo1", "other/repo2"],
        }

        signal = analyzer._validate_and_create_signal(
            item=item_with_related_repos,
            index=0,
            sources=["https://github.com/test/repo/commit/abc123"],
            related_repos=["test/repo"],  # 外部传入的
        )

        assert signal is not None
        # 应该包含 LLM 返回的 + 外部传入的（去重）
        assert set(signal.related_repos) == {
            "test/repo",
            "other/repo1",
            "other/repo2",
        }
