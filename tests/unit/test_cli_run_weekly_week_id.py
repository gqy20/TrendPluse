"""`trendpluse-run-weekly` 周标识解析测试。"""

from datetime import datetime

import pytest

from trendpluse.cli.run_weekly import resolve_weekly_reference_date


def test_resolve_weekly_reference_date_uses_input_week_id() -> None:
    """指定周标识时应映射到下一周周一参考时间。"""
    result = resolve_weekly_reference_date("2026-W09")

    assert result == datetime(2026, 3, 2)


def test_resolve_weekly_reference_date_falls_back_to_now(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """未指定周标识时应回退到当前时间。"""

    class FrozenDateTime(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 3, 7, 8, 9, 10, tzinfo=tz)

    monkeypatch.setattr("trendpluse.cli.run_weekly.datetime", FrozenDateTime)

    result = resolve_weekly_reference_date("")

    assert result == FrozenDateTime(2026, 3, 7, 8, 9, 10)


def test_resolve_weekly_reference_date_rejects_invalid_value() -> None:
    """非法周标识应抛出明确异常。"""
    with pytest.raises(ValueError, match="WEEK_ID 格式错误"):
        resolve_weekly_reference_date("2026/09")
