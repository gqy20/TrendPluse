"""日报增强结果校验测试。"""

import pytest

from trendpluse.utils.daily_summary_validation import validate_smoke_daily_summary


def test_validate_smoke_daily_summary_accepts_first_report_shape():
    """首日报场景应满足 smoke 校验。"""
    validate_smoke_daily_summary(
        {
            "summary_brief": "首日报中识别到多项工程信号，并建立了后续对比基准。",
            "trend_status": "new",
            "trend_delta": "作为首份日报，无历史基准可对比，今日所有信号均属新发现。",
            "historical_basis_dates": [],
            "historical_comparison": "无历史日报数据，今天是监控起始日。",
            "top_new_trends": ["视频处理", "模型分层化"],
            "top_continuing_trends": [],
            "summary_confidence": None,
        }
    )


def test_validate_smoke_daily_summary_rejects_missing_key_fields():
    """关键增强字段为空时应报错。"""
    with pytest.raises(ValueError, match="historical_comparison 不能为空"):
        validate_smoke_daily_summary(
            {
                "summary_brief": "有摘要",
                "trend_status": "continuing",
                "trend_delta": "有变化说明",
                "historical_basis_dates": ["2026-03-17"],
                "historical_comparison": "",
                "top_new_trends": ["新趋势"],
                "top_continuing_trends": [],
                "summary_confidence": 0.8,
            }
        )


def test_validate_smoke_daily_summary_rejects_empty_trend_lists():
    """两个趋势列表都为空时应报错。"""
    with pytest.raises(
        ValueError, match="top_new_trends 和 top_continuing_trends 不能同时为空"
    ):
        validate_smoke_daily_summary(
            {
                "summary_brief": "有摘要",
                "trend_status": "mixed",
                "trend_delta": "有变化说明",
                "historical_basis_dates": ["2026-03-17"],
                "historical_comparison": "今天的变化相对历史较为复杂。",
                "top_new_trends": [],
                "top_continuing_trends": [],
                "summary_confidence": 0.5,
            }
        )
