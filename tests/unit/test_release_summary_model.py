"""ReleaseSummary 数据模型单元测试

测试 AI 生成的 Release 总结数据结构。
"""

from typing import Literal

import pytest

from trendpluse.models.signal import ReleaseSummary


class TestReleaseSummary:
    """测试 ReleaseSummary 数据模型"""

    def test_create_release_summary_with_all_fields(self):
        """测试：创建包含所有字段的 ReleaseSummary

        验证模型可以正确创建并包含所有必需字段。
        """
        # Arrange & Act
        summary = ReleaseSummary(
            change_type="feature",
            key_changes=[
                "新增 Codex 内置插件支持",
                "修复 OpenAI Business 连接问题",
                "优化文件追踪功能",
            ],
            summary_cn="本次更新主要新增了 Codex 内置插件支持，"
            "修复了 OpenAI Business 计划的连接问题，"
            "并优化了文件追踪功能。",
            impact_level=3,
        )

        # Assert
        assert summary.change_type == "feature"
        assert len(summary.key_changes) == 3
        assert "Codex" in summary.summary_cn
        assert summary.impact_level == 3

    def test_change_type_must_be_valid(self):
        """测试：change_type 必须是有效值

        验证只有预定义的变更类型才能被接受。
        """
        # Arrange & Act & Assert
        # 有效的变更类型
        valid_types: list[
            Literal["feature", "fix", "improvement", "breaking", "other"]
        ] = [
            "feature",
            "fix",
            "improvement",
            "breaking",
            "other",
        ]
        for change_type in valid_types:
            summary = ReleaseSummary(
                change_type=change_type,
                key_changes=["test"],
                summary_cn="test",
                impact_level=1,
            )
            assert summary.change_type == change_type

    def test_impact_level_must_be_between_1_and_5(self):
        """测试：impact_level 必须在 1-5 之间

        验证影响级别必须符合要求。
        """
        # Arrange & Act & Assert
        for level in [1, 2, 3, 4, 5]:
            summary = ReleaseSummary(
                change_type="feature",
                key_changes=["test"],
                summary_cn="test",
                impact_level=level,
            )
            assert summary.impact_level == level

    def test_impact_level_out_of_range_raises_error(self):
        """测试：超出范围的 impact_level 应该抛出错误

        验证 Pydantic 的验证机制。
        """
        # Arrange & Act & Assert
        with pytest.raises(ValueError):  # Pydantic ValidationError
            ReleaseSummary(
                change_type="feature",
                key_changes=["test"],
                summary_cn="test",
                impact_level=6,  # 超出范围
            )

    def test_get_change_type_emoji(self):
        """测试：获取变更类型的表情

        验证每种变更类型都有对应的表情符号。
        """
        # Arrange & Act & Assert
        assert ReleaseSummary.get_change_type_emoji("feature") == "🆕"
        assert ReleaseSummary.get_change_type_emoji("fix") == "🔧"
        assert ReleaseSummary.get_change_type_emoji("improvement") == "✨"
        assert ReleaseSummary.get_change_type_emoji("breaking") == "💥"
        assert ReleaseSummary.get_change_type_emoji("other") == "📦"
        assert ReleaseSummary.get_change_type_emoji("unknown") == "📌"

    def test_key_changes_can_be_empty(self):
        """测试：key_changes 可以为空列表

        验证模型允许空的变更列表。
        """
        # Arrange & Act
        summary = ReleaseSummary(
            change_type="other",
            key_changes=[],
            summary_cn="无重大变更",
            impact_level=1,
        )

        # Assert
        assert summary.key_changes == []
        assert len(summary.key_changes) == 0

    def test_summary_cn_can_be_empty_string(self):
        """测试：summary_cn 可以为空字符串

        验证模型允许空的总结文本。
        """
        # Arrange & Act
        summary = ReleaseSummary(
            change_type="other",
            key_changes=[],
            summary_cn="",
            impact_level=1,
        )

        # Assert
        assert summary.summary_cn == ""


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
