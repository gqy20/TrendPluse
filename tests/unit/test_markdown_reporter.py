"""MarkdownReporter 单元测试

测试 Markdown 报告生成器的核心功能。
"""

import pytest

from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import Signal


class TestMarkdownReporter:
    """MarkdownReporter 测试类"""

    @pytest.fixture
    def reporter(self):
        """创建 MarkdownReporter 实例"""
        return MarkdownReporter()

    @pytest.fixture
    def sample_signal(self):
        """示例信号数据"""
        return Signal(
            id="test-1",
            title="测试信号",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="这是一个测试信号",
            sources=[
                "https://github.com/anthropics/claude-code-action/commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370"
            ],
            related_repos=["anthropics/claude-code-action"],
        )

    def test_render_signal_includes_commit_sha(self, reporter, sample_signal):
        """测试渲染信号 - commit 链接应包含短 SHA"""
        # Act
        rendered = reporter.render_signal(sample_signal)

        # Assert - 应包含仓库名和短 SHA
        assert "@b17b541" in rendered
        assert "anthropics/claude-code-action" in rendered

    def test_render_signal_with_multiple_sources(self, reporter):
        """测试渲染信号 - 多个来源应正确格式化"""
        # Arrange
        signal = Signal(
            id="test-2",
            title="多来源测试",
            type="capability",
            category="engineering",
            impact_score=3,
            why_it_matters="测试多个来源",
            sources=[
                "https://github.com/anthropics/claude-code-action/commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370",
                "https://github.com/cline/cline/pull/456",
                "https://github.com/continuedev/continue",
            ],
            related_repos=[
                "anthropics/claude-code-action",
                "cline/cline",
            ],
        )

        # Act
        rendered = reporter.render_signal(signal)

        # Assert - 应包含各种格式的来源
        assert "@b17b541" in rendered  # commit 格式
        assert "#456" in rendered  # PR 格式
        assert "continuedev/continue" in rendered  # 仓库格式

    def test_render_signal_uses_markdown_sections(self, reporter, sample_signal):
        """测试渲染信号使用当前 Markdown 结构。"""
        rendered = reporter.render_signal(sample_signal)

        assert "### 🚀 测试信号" in rendered
        assert "**类型**: `capability`" in rendered
        assert "**影响**: ⭐⭐⭐⭐ (4/5)" in rendered
        assert "**来源**:" in rendered
        assert "这是一个测试信号" in rendered
        assert "anthropics/claude-code-action" in rendered

    def test_render_signal_medium_impact(self, reporter):
        """测试渲染信号 - 中等影响评分应输出正确星级。"""
        # Arrange
        signal = Signal(
            id="test-3",
            title="中等影响信号",
            type="workflow",
            category="engineering",
            impact_score=3,
            why_it_matters="这是一个中等影响的信号",
            sources=["https://github.com/test/repo/pull/123"],
            related_repos=["test/repo"],
        )

        # Act
        rendered = reporter.render_signal(signal)

        assert "⭐⭐⭐ (3/5)" in rendered
        assert "中等影响信号" in rendered

    def test_render_signal_low_impact(self, reporter):
        """测试渲染信号 - 低影响评分应输出正确星级。"""
        # Arrange
        signal = Signal(
            id="test-4",
            title="低影响信号",
            type="eval",
            category="research",
            impact_score=2,
            why_it_matters="这是一个低影响的信号",
            sources=["https://github.com/test/repo/pull/456"],
            related_repos=["test/repo"],
        )

        # Act
        rendered = reporter.render_signal(signal)

        assert "⭐⭐ (2/5)" in rendered
