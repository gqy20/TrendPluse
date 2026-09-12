"""Release 编排处理。"""

from __future__ import annotations

from dataclasses import dataclass
from re import match
from typing import Any, cast

from trendpluse.logger import get_logger
from trendpluse.models.signal import ReleasesData, ReleaseSummary, Signal

logger = get_logger(__name__)

# 同仓库同窗口 release 数达到阈值即判定为 monorepo 批量发版
# （changesets/lerna 模式：一次给几十个子包同步发版本）。
# 正常仓库单日 1-3 个 release 不会触发。
BULK_RELEASE_THRESHOLD = 10

# 批量发版组送入 breaking changes 检测的代表数量
# （changesets 子包 changelog 高度同构，代表性采样足够）
BULK_BREAKING_SAMPLE_SIZE = 5


@dataclass
class ReleaseWorkflowResult:
    """Release 编排结果。"""

    releases_data: ReleasesData
    detailed_releases: list[dict[str, Any]]
    release_signals: list[Signal]
    breaking_changes: list[Any]


class ReleaseProcessor:
    """负责 release summary、signal 与 breaking change 的编排。

    monorepo 批量发版折叠：同仓库 release 数达到 ``BULK_RELEASE_THRESHOLD``
    时判定为批量发版组（如 vercel/ai 的 changesets 一次 169 个子包），
    组内不再逐个调用 LLM——summary 共享模板、信号折叠为 1 条、
    breaking 检测仅采样，避免噪音淹没重要发布与 token 浪费。
    """

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

    @staticmethod
    def _split_bulk_releases(
        detailed_releases: list[dict[str, Any]],
    ) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
        """按仓库分组拆分正常与批量发版 release。

        Returns:
            (normal_releases, bulk_groups) 元组：正常 release 列表与
            按仓库名索引的批量发版组。
        """
        by_repo: dict[str, list[dict[str, Any]]] = {}
        for release in detailed_releases:
            repo = str(release.get("repo", "")).strip()
            if repo:
                by_repo.setdefault(repo, []).append(release)

        normal: list[dict[str, Any]] = []
        bulk_groups: dict[str, list[dict[str, Any]]] = {}
        for repo, group in by_repo.items():
            if len(group) >= BULK_RELEASE_THRESHOLD:
                bulk_groups[repo] = group
            else:
                normal.extend(group)

        if bulk_groups:
            logger.info(
                "Monorepo 批量发版折叠: %s",
                ", ".join(f"{repo}×{len(g)}" for repo, g in bulk_groups.items()),
            )
        return normal, bulk_groups

    @staticmethod
    def _bulk_summary(
        repo: str, release: dict[str, Any], group_size: int
    ) -> ReleaseSummary:
        """为批量发版组内的 release 构造共享模板 summary（不调 LLM）。"""
        version = str(release.get("tag_name") or release.get("name") or "")
        return ReleaseSummary(
            change_type="other",
            key_changes=[f"{repo} monorepo 当日批量发版 {group_size} 个子包"],
            summary_cn=(
                f"{version} 属于 {repo} 的 monorepo 批量发版"
                f"（当日共 {group_size} 个包），多为 changesets 版本同步升级，"
                "无单独重大变更。"
            ),
            impact_level=2,
        )

    @staticmethod
    def _build_bulk_signal(repo: str, group: list[dict[str, Any]]) -> Signal:
        """将批量发版组折叠为单条合成信号。"""
        versions = [
            str(r.get("tag_name") or r.get("name") or "").strip() for r in group
        ]
        sample_versions = [v for v in versions if v][:5]
        sources = [str(r.get("html_url", "")).strip() for r in group[:3]]
        return Signal(
            id=f"release-bulk-{repo.replace('/', '-')}",
            title=f"{repo} 批量发版 {len(group)} 个子包",
            type="release",
            category="engineering",
            impact_score=3,
            why_it_matters=(
                f"monorepo 批量发版（changesets 模式），当日同步发布 "
                f"{len(group)} 个子包（如 {', '.join(sample_versions[:3])}），"
                "多为版本同步升级；如依赖该仓库请关注主包版本。"
            ),
            sources=[s for s in sources if s],
            related_repos=[repo],
        )

    def run(
        self,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
    ) -> ReleaseWorkflowResult:
        """同步执行 release 编排。"""
        normal, bulk_groups = self._split_bulk_releases(detailed_releases)
        self.apply_summaries(releases_data, normal)
        self._apply_bulk_summaries(releases_data, bulk_groups)
        release_signals = self.analyze_signals(normal)
        release_signals.extend(
            self._build_bulk_signal(repo, group) for repo, group in bulk_groups.items()
        )
        breaking_changes = self.detect_breaking_changes(
            self._breaking_detection_view(normal, bulk_groups)
        )
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
        """异步执行 release 编排。"""
        normal, bulk_groups = self._split_bulk_releases(detailed_releases)
        summary_result = await self.summarize_async(normal)
        self.apply_summary_result(releases_data, normal, summary_result)
        self._apply_bulk_summaries(releases_data, bulk_groups)
        release_signals = await self.analyze_signals_async(normal)
        release_signals.extend(
            self._build_bulk_signal(repo, group) for repo, group in bulk_groups.items()
        )
        breaking_changes = await self.detect_breaking_changes_async(
            self._breaking_detection_view(normal, bulk_groups)
        )
        return ReleaseWorkflowResult(
            releases_data=releases_data,
            detailed_releases=detailed_releases,
            release_signals=release_signals,
            breaking_changes=breaking_changes,
        )

    @staticmethod
    def _breaking_detection_view(
        normal: list[dict[str, Any]],
        bulk_groups: dict[str, list[dict[str, Any]]],
    ) -> list[dict[str, Any]]:
        """breaking 检测输入视图：正常全量 + 批量组代表采样。"""
        view = list(normal)
        for group in bulk_groups.values():
            view.extend(group[:BULK_BREAKING_SAMPLE_SIZE])
        return view

    @staticmethod
    def _apply_bulk_summaries(
        releases_data: ReleasesData,
        bulk_groups: dict[str, list[dict[str, Any]]],
    ) -> None:
        """为批量发版组回填共享模板 summary（零 LLM 调用）。"""
        bulk_versions: dict[str, list[str]] = {}
        for repo, group in bulk_groups.items():
            bulk_versions[repo] = [
                str(r.get("tag_name") or r.get("name") or "").strip() for r in group
            ]
        for release in releases_data.releases:
            repo = release.repo
            versions = bulk_versions.get(repo)
            if not versions or release.version not in versions:
                continue
            release.ai_summary = ReleaseProcessor._bulk_summary(
                repo, {"tag_name": release.version}, len(versions)
            )

    def apply_summaries(
        self, releases_data: ReleasesData, normal_releases: list[dict[str, Any]]
    ) -> None:
        """为 release 数据附加 AI 总结。"""
        if not normal_releases:
            return
        release_materials = self.release_material_builder.build(normal_releases)
        summaries = self.release_summarizer.summarize_materials(release_materials)
        self.apply_summary_result(releases_data, normal_releases, summaries)

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
        normal_releases: list[dict[str, Any]],
        summaries: dict[str, Any],
    ) -> None:
        """将 release summary 结果回填到 release 数据。

        仅回填正常 release（批量发版组由 _apply_bulk_summaries 处理）。
        """
        if not normal_releases or not isinstance(summaries, dict):
            return
        for release in releases_data.releases:
            key = f"{release.repo}@{release.version}"
            if key in summaries:
                release.ai_summary = summaries[key]

    def analyze_signals(self, normal_releases: list[dict[str, Any]]) -> list[Signal]:
        """分析 release 信号。"""
        if not normal_releases:
            return []
        release_materials = self.release_material_builder.build(normal_releases)
        release_signals = cast(
            list[Signal],
            self.release_analyzer.analyze_materials(release_materials),
        )
        if release_signals:
            self._log_category_distribution("release", release_signals)
            return release_signals
        return self.build_fallback_signals(normal_releases)

    async def analyze_signals_async(
        self, normal_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """异步分析 release 信号。"""
        if not normal_releases:
            return []
        release_materials = self.release_material_builder.build(normal_releases)
        release_signals = cast(
            list[Signal],
            await self.release_analyzer.analyze_materials_async(release_materials),
        )
        if release_signals:
            self._log_category_distribution("release", release_signals)
            return release_signals
        return self.build_fallback_signals(normal_releases)

    @staticmethod
    def _log_category_distribution(source: str, signals: list[Signal]) -> None:
        """打印上游信号 category 分布（research 分类触发的可观测性）。"""
        counts: dict[str, int] = {}
        for signal in signals:
            counts[signal.category] = counts.get(signal.category, 0) + 1
        distribution = " ".join(
            f"{category}={count}" for category, count in sorted(counts.items())
        )
        logger.info(
            "%s 信号 category 分布: %s (total=%d)", source, distribution, len(signals)
        )

    def detect_breaking_changes(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """检测 breaking changes。"""
        if not detailed_releases:
            return []
        breaking_changes = self.breaking_changes_detector.detect_breaking_changes(
            {"detailed_releases": detailed_releases}
        )
        return cast(list[Any], self.deduplicate_breaking_changes(breaking_changes))

    async def detect_breaking_changes_async(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """异步检测 breaking changes。"""
        if not detailed_releases:
            return []
        payload = {"detailed_releases": detailed_releases}
        detector = self.breaking_changes_detector
        breaking_changes = await detector.detect_breaking_changes_async(payload)
        return cast(list[Any], self.deduplicate_breaking_changes(breaking_changes))

    def deduplicate_breaking_changes(
        self, breaking_changes: Any
    ) -> list[dict[str, Any]]:
        """按 repo 和变更指纹去重，优先保留具体版本 tag。"""
        if not isinstance(breaking_changes, list):
            return []

        deduplicated: dict[tuple[str, tuple[str, ...]], dict[str, Any]] = {}
        for entry in breaking_changes:
            if not isinstance(entry, dict):
                continue

            fingerprint = self._breaking_change_fingerprint(entry)
            if fingerprint is None:
                continue

            existing = deduplicated.get(fingerprint)
            if existing is None or self._prefer_breaking_change(entry, existing):
                deduplicated[fingerprint] = entry

        return list(deduplicated.values())

    def _breaking_change_fingerprint(
        self, entry: dict[str, Any]
    ) -> tuple[str, tuple[str, ...]] | None:
        """构建 breaking changes 去重指纹。"""
        repo = str(entry.get("repo", "")).strip()
        changes = entry.get("changes")
        if not repo or not isinstance(changes, list):
            tag_name = str(entry.get("tag_name", "")).strip()
            fallback_key = (
                tag_name or str(entry.get("version", "")).strip() or "unknown"
            )
            return repo, (fallback_key,)

        normalized_changes = []
        for change in changes:
            if not isinstance(change, dict):
                continue
            description = str(change.get("description", "")).strip().lower()
            category = str(change.get("category", "")).strip().lower()
            impact = str(change.get("impact", "")).strip().lower()
            if description:
                normalized_changes.append(f"{category}|{impact}|{description}")

        if not normalized_changes:
            tag_name = str(entry.get("tag_name", "")).strip()
            fallback_key = (
                tag_name or str(entry.get("version", "")).strip() or "unknown"
            )
            return repo, (fallback_key,)
        return repo, tuple(sorted(normalized_changes))

    def _prefer_breaking_change(
        self, candidate: dict[str, Any], existing: dict[str, Any]
    ) -> bool:
        """判断 candidate 是否比 existing 更适合作为保留项。"""
        candidate_tag = str(candidate.get("tag_name", "")).strip()
        existing_tag = str(existing.get("tag_name", "")).strip()

        candidate_is_floating = self._is_floating_major_tag(candidate_tag)
        existing_is_floating = self._is_floating_major_tag(existing_tag)

        if candidate_is_floating != existing_is_floating:
            return not candidate_is_floating

        if len(candidate_tag) != len(existing_tag):
            return len(candidate_tag) > len(existing_tag)

        return candidate_tag > existing_tag

    def _is_floating_major_tag(self, tag_name: str) -> bool:
        """判断 tag 是否为浮动主版本别名。"""
        normalized = tag_name.lstrip("v")
        return bool(match(r"^\d+$", normalized))

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
