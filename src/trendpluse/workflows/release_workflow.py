"""Release 工作流服务。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast

from trendpluse.models.signal import ReleasesData, Signal


@dataclass
class ReleaseWorkflowResult:
    """Release 工作流结果。"""

    releases_data: ReleasesData
    detailed_releases: list[dict[str, Any]]
    release_signals: list[Signal]
    breaking_changes: list[Any]


class ReleaseWorkflowService:
    """负责 release summary、signal 与 breaking change 的编排。"""

    def __init__(
        self,
        *,
        release_material_builder: Any,
        release_summarizer: Any,
        release_analyzer: Any,
        breaking_changes_detector: Any,
    ) -> None:
        self.release_material_builder = release_material_builder
        self.release_summarizer = release_summarizer
        self.release_analyzer = release_analyzer
        self.breaking_changes_detector = breaking_changes_detector

    def run(
        self,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
    ) -> ReleaseWorkflowResult:
        """同步执行 release 工作流。"""
        self.apply_summaries(releases_data, detailed_releases)
        release_signals = self.analyze_signals(detailed_releases)
        breaking_changes = self.detect_breaking_changes(detailed_releases)
        return ReleaseWorkflowResult(
            releases_data=releases_data,
            detailed_releases=detailed_releases,
            release_signals=release_signals,
            breaking_changes=breaking_changes,
        )

    async def run_async(
        self,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
    ) -> ReleaseWorkflowResult:
        """异步执行 release 工作流。"""
        summary_result = await self.summarize_async(detailed_releases)
        self.apply_summary_result(releases_data, detailed_releases, summary_result)
        release_signals = await self.analyze_signals_async(detailed_releases)
        breaking_changes = await self.detect_breaking_changes_async(detailed_releases)
        return ReleaseWorkflowResult(
            releases_data=releases_data,
            detailed_releases=detailed_releases,
            release_signals=release_signals,
            breaking_changes=breaking_changes,
        )

    def apply_summaries(
        self, releases_data: ReleasesData, detailed_releases: list[dict[str, Any]]
    ) -> None:
        """为 release 数据附加 AI 总结。"""
        if not detailed_releases:
            return
        release_materials = self.release_material_builder.build(detailed_releases)
        summaries = self.release_summarizer.summarize_materials(release_materials)
        self.apply_summary_result(releases_data, detailed_releases, summaries)

    async def summarize_async(
        self, detailed_releases: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """异步生成 release summaries。"""
        if not detailed_releases:
            return {}
        release_materials = self.release_material_builder.build(detailed_releases)
        summaries = await self.release_summarizer.summarize_materials_async(
            release_materials
        )
        return cast(dict[str, Any], summaries)

    def apply_summary_result(
        self,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
        summaries: dict[str, Any],
    ) -> None:
        """将 release summary 结果回填到 release 数据。"""
        if not detailed_releases or not isinstance(summaries, dict):
            return
        for release in releases_data.releases:
            key = f"{release.repo}@{release.version}"
            if key in summaries:
                release.ai_summary = summaries[key]

    def analyze_signals(self, detailed_releases: list[dict[str, Any]]) -> list[Signal]:
        """分析 release 信号。"""
        if not detailed_releases:
            return []
        release_materials = self.release_material_builder.build(detailed_releases)
        release_signals = cast(
            list[Signal],
            self.release_analyzer.analyze_materials(release_materials),
        )
        if release_signals:
            return release_signals
        return self.build_fallback_signals(detailed_releases)

    async def analyze_signals_async(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """异步分析 release 信号。"""
        if not detailed_releases:
            return []
        release_materials = self.release_material_builder.build(detailed_releases)
        release_signals = cast(
            list[Signal],
            await self.release_analyzer.analyze_materials_async(release_materials),
        )
        if release_signals:
            return release_signals
        return self.build_fallback_signals(detailed_releases)

    def detect_breaking_changes(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """检测 breaking changes。"""
        if not detailed_releases:
            return []
        breaking_changes = self.breaking_changes_detector.detect_breaking_changes(
            {"detailed_releases": detailed_releases}
        )
        return cast(list[Any], breaking_changes)

    async def detect_breaking_changes_async(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """异步检测 breaking changes。"""
        if not detailed_releases:
            return []
        payload = {"detailed_releases": detailed_releases}
        detector = self.breaking_changes_detector
        breaking_changes = await detector.detect_breaking_changes_async(payload)
        return cast(list[Any], breaking_changes)

    def build_fallback_signals(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """构建 release 信号兜底结果。"""
        signals: list[Signal] = []
        for idx, release in enumerate(detailed_releases):
            repo = str(release.get("repo", "")).strip()
            tag_name = str(
                release.get("tag_name") or release.get("name") or f"unknown-{idx + 1}"
            ).strip()
            source_url = str(release.get("html_url", "")).strip()
            version_info = release.get("version_info") or {}
            major = int(version_info.get("major", 0)) if version_info else 0
            is_prerelease = bool(version_info.get("is_prerelease", False))

            impact_score = 4 if major >= 1 and not is_prerelease else 3
            title = f"{repo} 发布 {tag_name}" if repo else f"版本发布 {tag_name}"
            why_it_matters = (
                f"{repo} 发布新版本 {tag_name}，建议评估变更影响与兼容性。"
                if repo
                else f"检测到新版本 {tag_name}，建议评估变更影响与兼容性。"
            )

            signals.append(
                Signal(
                    id=f"release-fallback-{idx}",
                    title=title,
                    type="release",
                    category="engineering",
                    impact_score=impact_score,
                    why_it_matters=why_it_matters,
                    sources=[source_url] if source_url else [],
                    related_repos=[repo] if repo else [],
                )
            )
        return signals
