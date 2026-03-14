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

    def test_render_signal_card_html(self, reporter, sample_signal):
        """测试渲染信号卡片 - HTML 格式应包含正确的类和结构"""
        # Act
        rendered = reporter.render_signal_card(sample_signal)

        # Assert - 验证 HTML 卡片结构
        assert '<div class="signal-card signal-high-impact">' in rendered
        assert '<div class="signal-header">' in rendered
        assert '<div class="signal-icon">' in rendered
        assert '<h4 class="signal-title">测试信号</h4>' in rendered
        assert '<span class="signal-type-badge capability">' in rendered
        assert '<span class="signal-stars">⭐⭐⭐⭐</span>' in rendered
        assert '<div class="signal-body">' in rendered
        assert '<div class="signal-footer">' in rendered
        assert "这是一个测试信号" in rendered
        assert "anthropics/claude-code-action" in rendered

    def test_render_signal_card_medium_impact(self, reporter):
        """测试渲染信号卡片 - 中等影响评分应使用正确的样式"""
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
        rendered = reporter.render_signal_card(signal)

        # Assert - 中等影响应使用 medium 样式
        assert '<div class="signal-card signal-medium-impact">' in rendered
        assert '<span class="signal-stars">⭐⭐⭐</span>' in rendered
        assert "中等影响信号" in rendered

    def test_render_signal_card_low_impact(self, reporter):
        """测试渲染信号卡片 - 低影响评分应使用正确的样式"""
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
        rendered = reporter.render_signal_card(signal)

        # Assert - 低影响应使用 low 样式
        assert '<div class="signal-card signal-low-impact">' in rendered
        assert '<span class="signal-stars">⭐⭐</span>' in rendered

    def test_render_bento_grid(self, reporter, sample_signal):
        """测试渲染 Bento Grid - 应包含正确的容器和卡片"""
        # Arrange
        signals = [sample_signal]

        # Act
        rendered = reporter.render_bento_grid(signals, "工程")

        # Assert - 验证 Bento Grid 结构
        assert '<div class="bento-grid">' in rendered
        assert "<h2>🔧 工程信号</h2>" in rendered
        assert "signal-card" in rendered

    def test_render_signal_grid(self, reporter, sample_signal):
        """测试渲染统一核心信号区块。"""
        rendered = reporter.render_signal_grid([sample_signal])

        assert "<h2>核心信号</h2>" in rendered
        assert '<div class="bento-grid">' in rendered
        assert "signal-card" in rendered
