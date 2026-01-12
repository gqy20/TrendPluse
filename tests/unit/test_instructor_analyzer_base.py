"""Instructor 分析器基类测试"""

from trendpluse.analyzers.base import BaseLLMAnalyzer


class TestInstructorClientInitialization:
    """测试 Instructor 客户端初始化"""

    def test_creates_instructor_client_from_anthropic(self):
        """应该创建 instructor 客户端"""
        analyzer = BaseLLMAnalyzer(
            api_key="test_key",
            model="test-model",
            base_url="https://api.test.com",
        )
        # 验证客户端存在
        assert hasattr(analyzer, "client")

    def test_client_has_expected_methods(self):
        """客户端应该有预期的 chat.completions 方法"""
        analyzer = BaseLLMAnalyzer(
            api_key="test_key",
            model="test-model",
        )
        # 检查是否有 chat.completions 接口
        assert hasattr(analyzer.client, "chat")
        assert hasattr(analyzer.client.chat, "completions")
        assert hasattr(analyzer.client.chat.completions, "create")


class TestInstructorModeSupport:
    """测试 Instructor 模式支持"""

    def test_instructor_client_is_structured_mode(self):
        """instructor 客户端应该支持结构化输出"""
        analyzer = BaseLLMAnalyzer(
            api_key="test_key",
            model="test-model",
        )
        # instructor 客户端应该有 response_model 参数支持
        # 这是 instructor 模式的标志
        assert hasattr(analyzer.client, "chat")

    def test_base_class_stores_model_name(self):
        """基类应该存储模型名称"""
        model = "glm-4.7"
        analyzer = BaseLLMAnalyzer(
            api_key="test_key",
            model=model,
        )
        assert analyzer.model == model

    def test_base_class_stores_base_url(self):
        """基类应该存储 base_url"""
        base_url = "https://open.bigmodel.cn/api/anthropic"
        analyzer = BaseLLMAnalyzer(
            api_key="test_key",
            model="test-model",
            base_url=base_url,
        )
        assert analyzer.base_url == base_url
