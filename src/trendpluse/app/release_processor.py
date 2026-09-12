"""Release 编排处理。"""

from __future__ import annotations

from dataclasses import dataclass
from re import match
from typing import Any, cast

from trendpluse.logger import get_logger
from trendpluse.models.signal import (
    BulkReleaseAnalysis,
    NotablePackage,
    ReleasesData,
    ReleaseSummary,
    Signal,
)

logger = get_logger(__name__)

# 同仓库同窗口 release 数达到阈值即判定为 monorepo 批量发版
# （changesets/lerna 模式：一次给几十个子包同步发版本）。
# 正常仓库单日 1-3 个 release 不会触发。
BULK_RELEASE_THRESHOLD = 10


@dataclass
class ReleaseWorkflowResult:
    """Release 编排结果。"""

    releases_data: ReleasesData
    detailed_releases: list[dict[str, Any]]
    release_signals: list[Signal]
    breaking_changes: list[Any]


class ReleaseProcessor:
    """负责 release summary、signal 与 breaking change 的编排。

    monorepo 批量发版整批分析：同仓库 release 数达到
    ``BULK_RELEASE_THRESHOLD`` 时判定为批量发版组（如 vercel/ai 的
    changesets 一次 169 个子包），组内不再逐个调用 LLM——而是把全部
    子包整合成一份材料（每包一行要点）交给 AI **一次整批分析**：
    整体性质、值得单列的子包（major/breaking/新能力）、breaking 判断
    均由 AI 基于完整信息得出，而非模板预设或随机采样。
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
                "Monorepo 批量发版整批分析: %s",
                ", ".join(f"{repo}×{len(g)}" for repo, g in bulk_groups.items()),
            )
        return normal, bulk_groups

    def _analyze_bulk_group(
        self, repo: str, group: list[dict[str, Any]]
    ) -> BulkReleaseAnalysis:
        """整批分析一个批量发版组（sync 包装）。"""
        analyze = getattr(self.release_summarizer, "summarize_bulk_group", None)
        if callable(analyze):
            return cast(BulkReleaseAnalysis, analyze(repo, group))
        return self._fallback_bulk_analysis(repo, group)

    async def _analyze_bulk_group_async(
        self, repo: str, group: list[dict[str, Any]]
    ) -> BulkReleaseAnalysis:
        """整批分析一个批量发版组（优先 async 入口，异常降级语义判断）。"""
        analyze_async = getattr(
            self.release_summarizer, "summarize_bulk_group_async", None
        )
        if callable(analyze_async):
            try:
                return cast(BulkReleaseAnalysis, await analyze_async(repo, group))
            except Exception as exc:
                logger.warning(
                    "批量发版整批分析失败(%s, %d 包)，编排层降级: %s",
                    repo,
                    len(group),
                    exc,
                )
        return self._fallback_bulk_analysis(repo, group)

    @staticmethod
    def _fallback_bulk_analysis(
        repo: str, group: list[dict[str, Any]]
    ) -> BulkReleaseAnalysis:
        """无 summarizer 支持或 LLM 失败时的保守降级：按版本语义识别 major。"""
        notable = []
        has_breaking = False
        for release in group:
            name = str(release.get("tag_name") or release.get("name") or "")
            version_info = release.get("version_info") or {}
            major = int(version_info.get("major", 0) or 0) if version_info else 0
            if major >= 1:
                notable.append(
                    NotablePackage(
                        package=name,
                        reason=f"major 版本线 v{major}（降级语义标记）",
                        change_type="other",
                        impact_level=3,
                    )
                )
                has_breaking = has_breaking or major >= 2
        return BulkReleaseAnalysis(
            summary_cn=(
                f"{repo} monorepo 当日批量发版 {len(group)} 个子包"
                "（整批分析降级，按版本语义识别 major 跳跃）。"
            ),
            key_changes=[],
            notable_packages=notable[:10],
            has_breaking_changes=has_breaking,
            impact_level=3 if notable else 2,
        )

    @staticmethod
    def _apply_bulk_analysis_summaries(
        releases_data: ReleasesData,
        repo: str,
        group: list[dict[str, Any]],
        analysis: BulkReleaseAnalysis,
    ) -> None:
        """把 AI 整批分析结论回填为组内每个 release 的 summary。"""
        group_versions = {
            str(r.get("tag_name") or r.get("name") or "").strip() for r in group
        }
        notable_names = {p.package for p in analysis.notable_packages}
        for release in releases_data.releases:
            if release.repo == repo and release.version in group_versions:
                release.ai_summary = ReleaseSummary(
                    change_type="other",
                    key_changes=analysis.key_changes,
                    summary_cn=(
                        analysis.summary_cn
                        + (
                            f" 本包为值得单独关注的子包：{release.version}"
                            if release.version in notable_names
                            else ""
                        )
                    ),
                    impact_level=analysis.impact_level,
                )

    @staticmethod
    def _build_bulk_signals(
        repo: str,
        group: list[dict[str, Any]],
        analysis: BulkReleaseAnalysis,
    ) -> list[Signal]:
        """基于 AI 整批分析构建信号：1 条整批 + notable 子包单列。"""
        signals: list[Signal] = []

        sources = [
            str(r.get("html_url", "")).strip()
            for r in group
            if str(r.get("html_url", "")).strip()
        ][:3]
        notable_count = len(analysis.notable_packages)
        signals.append(
            Signal(
                id=f"release-bulk-{repo.replace('/', '-')}",
                title=(
                    f"{repo} 批量发版 {len(group)} 个子包"
                    + (f"（{notable_count} 个值得注意）" if notable_count else "")
                ),
                type="release",
                category="engineering",
                impact_score=analysis.impact_level,
                why_it_matters=analysis.summary_cn,
                sources=list(sources),
                related_repos=[repo],
            )
        )

        # AI 判定值得单独关注的子包 → 独立信号（major/breaking/新能力）
        by_version = {
            str(r.get("tag_name") or r.get("name") or "").strip(): r for r in group
        }
        for pkg in analysis.notable_packages:
            release = by_version.get(pkg.package)
            signal_sources = (
                [str(release.get("html_url", "")).strip()]
                if release and release.get("html_url")
                else list(sources)
            )
            signals.append(
                Signal(
                    id=(
                        f"release-bulk-notable-{repo.replace('/', '-')}"
                        f"-{pkg.package[:40]}"
                    ),
                    title=f"{repo} {pkg.package}",
                    type="release",
                    category="engineering",
                    impact_score=pkg.impact_level,
                    why_it_matters=pkg.reason,
                    sources=signal_sources,
                    related_repos=[repo],
                )
            )
        return signals

    @staticmethod
    def _bulk_breaking_entries(
        repo: str,
        analysis: BulkReleaseAnalysis,
    ) -> list[dict[str, Any]]:
        """从 AI 整批分析提取 breaking changes 条目（替代采样送检）。"""
        if not analysis.has_breaking_changes:
            return []
        breaking_pkgs = [
            p for p in analysis.notable_packages if p.change_type == "breaking"
        ]
        if not breaking_pkgs:
            return [
                {
                    "repo": repo,
                    "tag_name": "bulk",
                    "has_breaking": True,
                    "changes": [
                        {
                            "description": analysis.summary_cn,
                            "impact": "medium",
                            "category": "Behavior",
                        }
                    ],
                }
            ]
        return [
            {
                "repo": repo,
                "tag_name": pkg.package,
                "has_breaking": True,
                "changes": [
                    {"description": pkg.reason, "impact": "high", "category": "API"}
                ],
            }
            for pkg in breaking_pkgs
        ]

    async def run_async(
        self,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
    ) -> ReleaseWorkflowResult:
        """异步执行 release 编排。"""
        normal, bulk_groups = self._split_bulk_releases(detailed_releases)
        summary_result = await self.summarize_async(normal)
        self.apply_summary_result(releases_data, normal, summary_result)

        bulk_analyses: dict[str, BulkReleaseAnalysis] = {}
        release_signals = await self.analyze_signals_async(normal)
        for repo, group in bulk_groups.items():
            analysis = await self._analyze_bulk_group_async(repo, group)
            bulk_analyses[repo] = analysis
            self._apply_bulk_analysis_summaries(releases_data, repo, group, analysis)
            release_signals.extend(self._build_bulk_signals(repo, group, analysis))

        breaking_changes = await self.detect_breaking_changes_async(normal)
        for repo, analysis in bulk_analyses.items():
            breaking_changes.extend(self._bulk_breaking_entries(repo, analysis))
        return ReleaseWorkflowResult(
            releases_data=releases_data,
            detailed_releases=detailed_releases,
            release_signals=release_signals,
            breaking_changes=breaking_changes,
        )

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
        if not release_signals:
            logger.warning(
                "release 信号分析零产出（normal=%d）——失败可见，不再模板伪造",
                len(normal_releases),
            )
        else:
            self._log_category_distribution("release", release_signals)
        return release_signals

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
