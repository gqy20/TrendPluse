"""`trendpluse-run` 日期解析测试。"""

from datetime import datetime

import pytest

from trendpluse.cli.run import resolve_report_datetime


def test_resolve_report_datetime_uses_env_value() -> None:
    """传入固定日期时应返回对应日期。"""
    result = resolve_report_datetime("2026-03-06")

    assert result == datetime(2026, 3, 6)


def test_resolve_report_datetime_falls_back_to_now(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """未传日期时应回退到当前时间。"""

    class FrozenDateTime(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 3, 7, 8, 9, 10, tzinfo=tz)

    monkeypatch.setattr("trendpluse.cli.run.datetime", FrozenDateTime)

    result = resolve_report_datetime(None)

    assert result == FrozenDateTime(2026, 3, 7, 8, 9, 10)


def test_resolve_report_datetime_rejects_invalid_value() -> None:
    """非法日期格式应抛出明确异常。"""
    with pytest.raises(ValueError, match="REPORT_DATE 格式错误"):
        resolve_report_datetime("2026/03/06")
