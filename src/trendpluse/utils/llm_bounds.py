"""LLM 结构化输出的容忍处理。

原则：LLM 返回的单个字段越界/不可解析/枚举非法时，只做降级
（钳制到边界 / 回落默认值 / 归一到兜底枚举）并记录 warning 日志，
绝不抛 ValidationError 杀死整条管道的产出。
降级事件会进入运行日志与 Actions 输出，保证问题可见、可追溯。
"""

from __future__ import annotations

from typing import Any

from trendpluse.logger import get_logger

logger = get_logger(__name__)


def clamp_int(value: Any, low: int, high: int, default: int, field: str) -> int:
    """将 LLM 整数评分钳制到 [low, high]，不可解析时回落 default。"""
    try:
        num = int(value)
    except (TypeError, ValueError):
        logger.warning(
            "LLM 字段 %s=%r 不可解析，降级为默认值 %d", field, value, default
        )
        return default
    if num < low or num > high:
        clamped = min(max(num, low), high)
        logger.warning(
            "LLM 字段 %s=%d 越界 [%d, %d]，钳制为 %d", field, num, low, high, clamped
        )
        return clamped
    return num


def clamp_unit_float(value: Any, field: str) -> float | None:
    """将 LLM 的 0-1 比例钳制到 [0, 1]；>1 视为百分制先除 100；不可解析返回 None。"""
    if value is None:
        return None
    try:
        num = float(value)
    except (TypeError, ValueError):
        logger.warning("LLM 字段 %s=%r 不可解析，降级为 None", field, value)
        return None
    if num > 1.0:
        num /= 100.0
        logger.warning("LLM 字段 %s 疑似百分制，换算为 %.2f", field, num)
    if num < 0.0 or num > 1.0:
        clamped = min(max(num, 0.0), 1.0)
        logger.warning("LLM 字段 %s 越界 [0, 1]，钳制为 %.2f", field, clamped)
        return clamped
    return num


def normalize_literal(
    value: Any, allowed: tuple[str, ...], fallback: str, field: str
) -> str:
    """LLM 枚举值非法时归一到 fallback（大小写不敏感匹配优先）。"""
    if isinstance(value, str):
        lowered = value.strip().lower()
        for item in allowed:
            if lowered == item.lower():
                return item
    logger.warning(
        "LLM 字段 %s=%r 不在允许值 %s 内，降级为 %s", field, value, allowed, fallback
    )
    return fallback
