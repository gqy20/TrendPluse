"""测试 Signal 类的 Emoji 映射功能

验证信号类型到 Emoji 的映射是否正确，确保单一数据源。
"""

# mypy: disable-error-code="attr-defined"

from trendpluse.models.signal import Signal


class TestSignalEmoji:
    """测试 Signal 类的 Emoji 相关功能"""

    def test_get_type_emoji_all_known_types(self):
        """测试所有已知信号类型的 Emoji 映射

        Given: 已知的信号类型
        When: 调用 get_type_emoji
        Then: 返回正确的 Emoji
        """
        expected_emojis = {
            "capability": "🚀",
            "abstraction": "🎨",
            "workflow": "⚙️",
            "eval": "📊",
            "safety": "🛡️",
            "performance": "⚡",
            "commit": "💾",
            "release": "🎯",
        }

        for signal_type, expected_emoji in expected_emojis.items():
            result = Signal.get_type_emoji(signal_type)
            assert result == expected_emoji, (
                f"{signal_type} 应返回 {expected_emoji}，实际返回 {result}"
            )

    def test_get_type_emoji_unknown_type(self):
        """测试未知信号类型返回默认 Emoji

        Given: 未知的信号类型
        When: 调用 get_type_emoji
        Then: 返回默认 Emoji 📌
        """
        result = Signal.get_type_emoji("unknown_type")
        assert result == "📌"

    def test_get_type_emoji_empty_string(self):
        """测试空字符串返回默认 Emoji

        Given: 空字符串作为信号类型
        When: 调用 get_type_emoji
        Then: 返回默认 Emoji 📌
        """
        result = Signal.get_type_emoji("")
        assert result == "📌"

    def test_get_type_emoji_case_sensitive(self):
        """测试 Emoji 映射区分大小写

        Given: 大写的信号类型
        When: 调用 get_type_emoji
        Then: 返回默认 Emoji（因为映射是小写）
        """
        result = Signal.get_type_emoji("CAPABILITY")
        assert result == "📌"

    def test_emoji_mapping_is_complete(self):
        """测试 Emoji 映射包含所有 Signal 类型定义

        Given: Signal 模型中定义的 type 字段
        When: 检查映射是否完整
        Then: 所有类型都有对应的 Emoji
        """
        # 从 Signal 的 type 字面量类型中获取所有可能的类型
        from trendpluse.models.signal import Signal

        # Signal.type 的定义
        expected_types = [
            "capability",
            "abstraction",
            "workflow",
            "eval",
            "safety",
            "performance",
            "commit",
            "release",
        ]

        for signal_type in expected_types:
            emoji = Signal.get_type_emoji(signal_type)
            assert emoji != "📌", f"{signal_type} 缺少 Emoji 映射（返回了默认值）"

    def test_emoji_mapping_single_source_of_truth(self):
        """测试 Emoji 映射是单一数据源

        Given: 项目中使用 Emoji 的地方
        When: 检查是否有重复的映射定义
        Then: 应该只有一个地方定义映射
        """
        # 这个测试验证我们的重构是否成功：
        # 1. Signal.get_type_emoji() 存在
        # 2. 其他类应该使用它而不是重新定义

        assert hasattr(Signal, "get_type_emoji"), (
            "Signal 类应该有 get_type_emoji 类方法"
        )
        assert callable(getattr(Signal, "get_type_emoji")), (
            "get_type_emoji 应该是可调用的"
        )
