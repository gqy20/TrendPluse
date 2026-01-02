"""数据模型单元测试"""
import pytest
from pydantic import ValidationError

from trendpluse.models.signal import DailyReport, Signal


class TestSignal:
    """测试 Signal 模型"""

    def test_valid_signal_minimal(self):
        """测试：创建有效的最小信号"""
        # Arrange & Act
        signal = Signal(
            id="test-signal-1",
            title="Test Signal",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="This is a test signal",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        # Assert
        assert signal.id == "test-signal-1"
        assert signal.title == "Test Signal"
        assert signal.type == "capability"
        assert signal.category == "engineering"
        assert signal.impact_score == 5

    def test_signal_invalid_impact_score_too_low(self):
        """测试：impact_score < 1 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="engineering",
                impact_score=0,  # 无效
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "impact_score" in str(exc_info.value)

    def test_signal_invalid_impact_score_too_high(self):
        """测试：impact_score > 5 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="engineering",
                impact_score=6,  # 无效
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "impact_score" in str(exc_info.value)

    def test_signal_invalid_type(self):
        """测试：无效的 type 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="invalid_type",  # 无效
                category="engineering",
                impact_score=3,
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "type" in str(exc_info.value)

    def test_signal_invalid_category(self):
        """测试：无效的 category 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="invalid_category",  # 无效
                impact_score=3,
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "category" in str(exc_info.value)


class TestDailyReport:
    """测试 DailyReport 模型"""

    def test_valid_daily_report_minimal(self):
        """测试：创建有效的最小日报"""
        # Arrange & Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test summary",
            engineering_signals=[],
            research_signals=[],
        )

        # Assert
        assert report.date == "2026-01-02"
        assert report.summary_brief == "Test summary"
        assert len(report.engineering_signals) == 0
        assert len(report.research_signals) == 0

    def test_daily_report_with_signals(self):
        """测试：包含信号的日报"""
        # Arrange
        signal = Signal(
            id="test-1",
            title="Test Signal",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="Test",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        # Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test summary",
            engineering_signals=[signal],
            research_signals=[],
        )

        # Assert
        assert len(report.engineering_signals) == 1
        assert report.engineering_signals[0].id == "test-1"

    def test_daily_report_default_stats(self):
        """测试：stats 应该有默认值"""
        # Arrange & Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
        )

        # Assert
        assert report.stats["total_prs_analyzed"] == 0
        assert report.stats["total_releases"] == 0
        assert report.stats["high_impact_signals"] == 0
