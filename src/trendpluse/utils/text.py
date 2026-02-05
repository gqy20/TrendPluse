"""文本清洗工具函数。"""

from __future__ import annotations


def sanitize_optional_text(value: str | None) -> str | None:
    """清洗可选文本字段。

    将无效占位符或空文本转为 None。
    """
    if value is None:
        return None

    cleaned = value.strip()
    if not cleaned:
        return None

    stripped = cleaned.strip("\"'").strip()
    lower = stripped.lower()

    invalid_tokens = {
        "null",
        "none",
        "n/a",
        "na",
        "nil",
        "undefined",
        "unknown",
        "无",
        "暂无",
        "无内容",
        "不适用",
        "未知",
    }

    if lower in invalid_tokens:
        return None

    return cleaned
