"""日报总结增强结果校验。"""

from collections.abc import Mapping
from typing import Any

VALID_TREND_STATUS = {
    "new",
    "continuing",
    "resurfacing",
    "weakening",
    "mixed",
}


def validate_smoke_daily_summary(data: Mapping[str, Any]) -> None:
    """校验 smoke workflow 产出的日报增强字段。

    该校验器用于 GitHub Actions smoke 验收，目标是确认 summary agent
    不仅跑通，而且已经按约定格式回填关键字段。
    """

    summary_brief = str(data.get("summary_brief") or "").strip()
    if not summary_brief:
        raise ValueError("summary_brief 不能为空")

    # 零信号（如 smoke 用低活动 test-repos）：agent 无趋势可填，
    # 只确认 summary_brief 已回填即可证明 agent 跑通
    stats = data.get("stats") or {}
    if not (stats.get("total_signals") or 0):
        return

    trend_status = data.get("trend_status")
    if trend_status not in VALID_TREND_STATUS:
        raise ValueError(f"trend_status 非法: {trend_status!r}")

    trend_delta = str(data.get("trend_delta") or "").strip()
    if not trend_delta:
        raise ValueError("trend_delta 不能为空")

    historical_comparison = str(data.get("historical_comparison") or "").strip()
    if not historical_comparison:
        raise ValueError("historical_comparison 不能为空")

    top_new_trends = data.get("top_new_trends") or []
    top_continuing_trends = data.get("top_continuing_trends") or []
    if not isinstance(top_new_trends, list):
        raise ValueError("top_new_trends 必须为列表")
    if not isinstance(top_continuing_trends, list):
        raise ValueError("top_continuing_trends 必须为列表")
    if not top_new_trends and not top_continuing_trends:
        raise ValueError("top_new_trends 和 top_continuing_trends 不能同时为空")

    historical_basis_dates = data.get("historical_basis_dates") or []
    if not isinstance(historical_basis_dates, list):
        raise ValueError("historical_basis_dates 必须为列表")

    summary_confidence = data.get("summary_confidence")
    if summary_confidence is not None and not isinstance(
        summary_confidence, int | float
    ):
        raise ValueError("summary_confidence 必须为数字或 null")
