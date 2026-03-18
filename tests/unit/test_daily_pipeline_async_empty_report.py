"""异步日报空报告分支测试。"""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace
from typing import Any, cast
from unittest.mock import AsyncMock, Mock

import pytest

from trendpluse.app.daily import DailyPipelineApp


@pytest.mark.asyncio
async def test_run_daily_async_uses_async_empty_report_finalizer() -> None:
    """异步日报在无 PR 信号时应走异步空报告收尾。"""
    final_report = object()
    app = DailyPipelineApp(
        settings=SimpleNamespace(github_repos=[]),
        activity_collector=Mock(),
        release_collector=Mock(),
        issue_workflow=Mock(),
        release_workflow=Mock(),
        commit_material_builder=Mock(),
        commit_analyzer=Mock(),
        collector=Mock(),
        event_filter=Mock(),
        pr_reader=Mock(),
        analyzer=Mock(),
        deduplicator=Mock(),
        daily_report_finalizer=SimpleNamespace(
            handle_empty_report_async=AsyncMock(return_value=final_report),
            handle_empty_report=Mock(
                side_effect=AssertionError("不应调用同步空报告收尾")
            ),
        ),
    )
    cast(Any, app)._collect_daily_inputs_async = AsyncMock(
        return_value=SimpleNamespace(
            activity_data=None,
            commit_signals=[],
            releases_data=None,
        )
    )
    cast(Any, app)._collect_pr_signals_async = AsyncMock(return_value=[])

    result = await app.run_daily_async(datetime(2026, 3, 18))

    app.daily_report_finalizer.handle_empty_report_async.assert_awaited_once()
    assert result is final_report
