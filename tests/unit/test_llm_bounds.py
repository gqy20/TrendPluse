"""LLM 结构化输出容忍处理测试：越界/非法值降级而非抛异常。"""

import pytest

from trendpluse.models.daily_summary import DailySummaryResult
from trendpluse.models.signal import ReleaseSummary, Signal
from trendpluse.utils.llm_bounds import clamp_int, clamp_unit_float, normalize_literal


class TestClampInt:
    def test_out_of_range_high_clamped(self):
        assert clamp_int(934, 1, 5, 3, "f") == 5

    def test_out_of_range_low_clamped(self):
        assert clamp_int(0, 1, 5, 3, "f") == 1

    def test_in_range_unchanged(self):
        assert clamp_int(3, 1, 5, 3, "f") == 3

    def test_numeric_string_coerced(self):
        assert clamp_int("4", 1, 5, 3, "f") == 4

    def test_unparseable_falls_back_to_default(self):
        assert clamp_int("abc", 1, 5, 3, "f") == 3

    def test_none_falls_back_to_default(self):
        assert clamp_int(None, 1, 5, 3, "f") == 3


class TestClampUnitFloat:
    def test_percent_scale_converted(self):
        assert clamp_unit_float(93, "f") == pytest.approx(0.93)

    def test_percent_over_100_clamped(self):
        assert clamp_unit_float(150, "f") == 1.0

    def test_in_range_unchanged(self):
        assert clamp_unit_float(0.85, "f") == pytest.approx(0.85)

    def test_negative_clamped(self):
        assert clamp_unit_float(-2, "f") == 0.0

    def test_none_passthrough(self):
        assert clamp_unit_float(None, "f") is None

    def test_unparseable_returns_none(self):
        assert clamp_unit_float("x", "f") is None


class TestNormalizeLiteral:
    def test_case_insensitive_match(self):
        got = normalize_literal("Feature", ("feature", "fix"), "other", "f")
        assert got == "feature"

    def test_illegal_falls_back(self):
        assert normalize_literal("docs", ("feature", "fix"), "other", "f") == "other"


class TestModelLevelDegradation:
    """9/24 事故回归：单字段越界不得杀死整条日报。"""

    def test_signal_impact_score_934_clamped(self):
        signal = Signal.model_validate(
            {
                "id": "s1",
                "title": "t",
                "type": "capability",
                "category": "engineering",
                "impact_score": 934,
                "why_it_matters": "w",
                "sources": [],
                "related_repos": [],
            }
        )
        assert signal.impact_score == 5

    def test_signal_illegal_enum_degraded(self):
        signal = Signal.model_validate(
            {
                "id": "s1",
                "title": "t",
                "type": "docs",
                "category": "Research",
                "impact_score": 3,
                "why_it_matters": "w",
                "sources": [],
                "related_repos": [],
            }
        )
        assert signal.type == "capability"
        assert signal.category == "research"

    def test_release_summary_degraded(self):
        summary = ReleaseSummary.model_validate(
            {
                "change_type": "docs",
                "key_changes": [],
                "summary_cn": "s",
                "impact_level": 0,
            }
        )
        assert summary.change_type == "other"
        assert summary.impact_level == 1

    def test_daily_summary_result_degraded(self):
        result = DailySummaryResult.model_validate(
            {"summary_brief": "s", "trend_status": "unknown", "confidence": 93}
        )
        assert result.trend_status == "mixed"
        assert result.confidence == pytest.approx(0.93)
