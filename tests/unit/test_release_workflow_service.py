"""Release 工作流服务测试。"""

from __future__ import annotations

import pytest

from trendpluse.app.release_processor import ReleaseProcessor
from trendpluse.models.signal import (
    ReleaseInfo,
    ReleasesData,
    ReleaseSummary,
    Signal,
)


class DummyReleaseMaterialBuilder:
    """测试用 ReleaseMaterialBuilder。"""

    def build(self, detailed_releases):
        return detailed_releases


class DummyReleaseSummarizer:
    """测试用 ReleaseSummarizer。"""

    def __init__(self, summaries=None):
        self.summaries = summaries or {}

    def summarize_materials(self, materials):
        return self.summaries

    async def summarize_materials_async(self, materials):
        return self.summaries


class DummyReleaseAnalyzer:
    """测试用 ReleaseAnalyzer。"""

    def __init__(self, signals=None):
        self.signals = signals or []

    def analyze_materials(self, materials):
        return self.signals

    async def analyze_materials_async(self, materials):
        return self.signals


class DummyBreakingChangesDetector:
    """测试用 BreakingChangesDetector。"""

    def __init__(self, changes=None):
        self.changes = changes or []

    def detect_breaking_changes(self, payload):
        return self.changes

    async def detect_breaking_changes_async(self, payload):
        return self.changes


def test_run_applies_summaries_and_returns_signals() -> None:
    """测试同步 workflow 会回填 summary 并返回 signals。"""
    releases_data = ReleasesData(
        total_count=1,
        unique_repos_count=1,
        releases=[
            ReleaseInfo(
                repo="test/repo",
                version="v1.0.0",
                author="alice",
                date="2026-03-06",
                summary="release",
                url="https://github.com/test/repo/releases/tag/v1.0.0",
            )
        ],
    )
    detailed_releases = [
        {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "html_url": "https://github.com/test/repo/releases/tag/v1.0.0",
            "version_info": {"major": 1, "minor": 0, "patch": 0},
        }
    ]
    summary = ReleaseSummary(
        change_type="feature",
        key_changes=["新增功能"],
        summary_cn="新增功能总结",
        impact_level=3,
    )
    signal = Signal(
        id="release-1",
        title="test/repo 发布 v1.0.0",
        type="release",
        category="engineering",
        impact_score=4,
        why_it_matters="重要发布",
        sources=["https://github.com/test/repo/releases/tag/v1.0.0"],
        related_repos=["test/repo"],
    )

    service = ReleaseProcessor(
        release_material_builder=DummyReleaseMaterialBuilder(),
        release_summarizer=DummyReleaseSummarizer({"test/repo@v1.0.0": summary}),
        release_analyzer=DummyReleaseAnalyzer([signal]),
        breaking_changes_detector=DummyBreakingChangesDetector([{"repo": "test/repo"}]),
    )

    result = service.run(releases_data, detailed_releases)

    assert result.release_signals == [signal]
    assert result.breaking_changes == [{"repo": "test/repo"}]
    assert result.releases_data.releases[0].ai_summary == summary


def test_run_falls_back_when_release_analyzer_returns_empty() -> None:
    """测试 analyzer 无结果时使用 deterministic fallback。"""
    releases_data = ReleasesData(
        total_count=1,
        unique_repos_count=1,
        releases=[
            ReleaseInfo(
                repo="test/repo",
                version="v1.0.0",
                author="alice",
                date="2026-03-06",
                summary="release",
                url="https://github.com/test/repo/releases/tag/v1.0.0",
            )
        ],
    )
    detailed_releases = [
        {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "html_url": "https://github.com/test/repo/releases/tag/v1.0.0",
            "version_info": {"major": 1, "minor": 0, "patch": 0},
        }
    ]
    service = ReleaseProcessor(
        release_material_builder=DummyReleaseMaterialBuilder(),
        release_summarizer=DummyReleaseSummarizer(),
        release_analyzer=DummyReleaseAnalyzer([]),
        breaking_changes_detector=DummyBreakingChangesDetector([]),
    )

    result = service.run(releases_data, detailed_releases)

    assert len(result.release_signals) == 1
    assert result.release_signals[0].type == "release"
    assert result.release_signals[0].sources == [
        "https://github.com/test/repo/releases/tag/v1.0.0"
    ]


def test_run_deduplicates_breaking_changes_preferring_specific_tags() -> None:
    """测试 breaking changes 去重时优先保留具体版本 tag。"""
    releases_data = ReleasesData(total_count=0, unique_repos_count=0, releases=[])
    detailed_releases = [
        {
            "repo": "test/repo",
            "tag_name": "v1.0.69",
            "html_url": "https://github.com/test/repo/releases/tag/v1.0.69",
            "version_info": {"major": 1, "minor": 0, "patch": 69},
        }
    ]
    duplicated_changes = [
        {
            "repo": "test/repo",
            "tag_name": "v1",
            "changes": [
                {
                    "description": "统一 prompt 输入",
                    "impact": "high",
                    "category": "Config",
                }
            ],
        },
        {
            "repo": "test/repo",
            "tag_name": "v1.0.69",
            "changes": [
                {
                    "description": "统一 prompt 输入",
                    "impact": "high",
                    "category": "Config",
                }
            ],
        },
    ]

    service = ReleaseProcessor(
        release_material_builder=DummyReleaseMaterialBuilder(),
        release_summarizer=DummyReleaseSummarizer(),
        release_analyzer=DummyReleaseAnalyzer([]),
        breaking_changes_detector=DummyBreakingChangesDetector(duplicated_changes),
    )

    result = service.run(releases_data, detailed_releases)

    assert result.breaking_changes == [
        {
            "repo": "test/repo",
            "tag_name": "v1.0.69",
            "changes": [
                {
                    "description": "统一 prompt 输入",
                    "impact": "high",
                    "category": "Config",
                }
            ],
        }
    ]


@pytest.mark.asyncio
async def test_run_async_uses_same_fallback_behavior() -> None:
    """测试异步 workflow 也会使用相同 fallback。"""
    releases_data = ReleasesData(total_count=0, unique_repos_count=0, releases=[])
    detailed_releases = [
        {
            "repo": "test/repo",
            "tag_name": "v2.0.0",
            "html_url": "https://github.com/test/repo/releases/tag/v2.0.0",
            "version_info": {"major": 2, "minor": 0, "patch": 0},
        }
    ]
    service = ReleaseProcessor(
        release_material_builder=DummyReleaseMaterialBuilder(),
        release_summarizer=DummyReleaseSummarizer(),
        release_analyzer=DummyReleaseAnalyzer([]),
        breaking_changes_detector=DummyBreakingChangesDetector([]),
    )

    result = await service.run_async(releases_data, detailed_releases)

    assert len(result.release_signals) == 1
    assert result.release_signals[0].impact_score == 4
