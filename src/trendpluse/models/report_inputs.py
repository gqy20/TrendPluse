"""报告流程中间数据模型。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from trendpluse.models.signal import ActivityData, ReleasesData


@dataclass
class DailyPipelineInputs:
    """日报流程所需的基础输入与中间结果。"""

    activity_data: ActivityData
    detailed_commits: list[dict[str, Any]]
    releases_data: ReleasesData
    detailed_releases: list[dict[str, Any]]
    commit_signals: list[Any]
    release_signals: list[Any]
    breaking_changes: list[Any]
