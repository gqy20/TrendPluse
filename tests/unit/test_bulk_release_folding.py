"""Monorepo 批量发版折叠测试。"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from trendpluse.app.release_processor import (
    BULK_RELEASE_THRESHOLD,
    ReleaseProcessor,
)
from trendpluse.models.signal import ReleasesData


def _release(repo: str, version: str) -> dict:
    return {
        "repo": repo,
        "tag_name": version,
        "name": version,
        "body": "changelog",
        "html_url": f"https://github.com/{repo}/releases/tag/{version}",
    }


def _make_processor() -> tuple[ReleaseProcessor, dict[str, MagicMock]]:
    """构造组件全 mock 的 processor，返回各组件便于断言。"""
    components = {
        "release_material_builder": MagicMock(),
        "release_summarizer": MagicMock(),
        "release_analyzer": MagicMock(),
        "breaking_changes_detector": MagicMock(),
    }
    processor = ReleaseProcessor(**components)
    return processor, components


def _releases_data(releases: list[dict]) -> ReleasesData:
    from trendpluse.models.signal import ReleaseInfo

    return ReleasesData(
        total_count=len(releases),
        unique_repos_count=len({r["repo"] for r in releases}),
        releases=[
            ReleaseInfo(
                repo=r["repo"],
                version=r["tag_name"],
                author="x",
                date="2026-09-12",
                summary="s",
                assets_count=0,
                url=r["html_url"],
            )
            for r in releases
        ],
    )


class TestSplitBulkReleases:
    def test_bulk_group_detected(self):
        releases = [
            _release("vercel/ai", f"ai@5.0.{i}") for i in range(BULK_RELEASE_THRESHOLD)
        ] + [_release("anthropics/claude-code", "v2.1.269")]
        normal, bulk = ReleaseProcessor._split_bulk_releases(releases)
        assert len(normal) == 1
        assert "vercel/ai" in bulk
        assert len(bulk["vercel/ai"]) == BULK_RELEASE_THRESHOLD

    def test_normal_volume_not_folded(self):
        releases = (
            [_release("a/repo", f"v1.{i}") for i in range(3)]
            + [_release("b/repo", f"v2.{i}") for i in range(5)]
            + [_release("c/repo", "v9.0.0")]
        )
        normal, bulk = ReleaseProcessor._split_bulk_releases(releases)
        assert len(normal) == len(releases)
        assert bulk == {}


class TestBulkSignal:
    def test_folded_signal_structure(self):
        group = [_release("vercel/ai", f"@ai-sdk/p{i}@2.0.{i}") for i in range(12)]
        signal = ReleaseProcessor._build_bulk_signal("vercel/ai", group)
        assert signal.title == "vercel/ai 批量发版 12 个子包"
        assert signal.type == "release"
        assert signal.category == "engineering"
        assert signal.impact_score == 3
        assert signal.related_repos == ["vercel/ai"]
        assert len(signal.sources) == 3
        assert "批量发版" in signal.why_it_matters


class TestRunAsyncFolding:
    @pytest.mark.asyncio
    async def test_bulk_releases_skip_per_release_llm(self):
        """批量组不进 summarizer/analyzer 的逐个 LLM 调用。"""
        processor, comps = _make_processor()
        bulk = [_release("vercel/ai", f"@pkg{i}@1.0.{i}") for i in range(20)]
        normal = [_release("anthropics/claude-code", "v2.1.269")]
        releases_data = _releases_data(normal + bulk)

        # summarizer 只应收到 normal 组的材料
        comps["release_material_builder"].build.return_value = ["mat-1"]
        comps["release_summarizer"].summarize_materials_async = AsyncMock(
            return_value={"anthropics/claude-code@v2.1.269": MagicMock()}
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(
            return_value=[
                MagicMock(
                    category="engineering",
                    sources=["u"],
                    related_repos=["anthropics/claude-code"],
                )
            ]
        )
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        result = await processor.run_async(releases_data, normal + bulk)

        # 逐个 LLM 调用只发生 1 次（normal），而非 21 次
        built = comps["release_material_builder"].build.call_args_list
        assert all(len(c.args[0]) <= 1 for c in built)

        # 信号 = normal 1 条 + bulk 折叠 1 条
        assert len(result.release_signals) == 2
        bulk_signals = [
            s
            for s in result.release_signals
            if "批量发版" in str(getattr(s, "title", ""))
        ]
        assert len(bulk_signals) == 1

        # breaking 检测收到 normal + 批量组采样（5 个）
        detect_input = comps[
            "breaking_changes_detector"
        ].detect_breaking_changes_async.call_args.args[0]
        assert len(detect_input["detailed_releases"]) == 1 + 5

        # 落盘数据保持完整（21 条），批量组 ai_summary 为共享模板
        assert len(result.detailed_releases) == 21
        vercel = [r for r in releases_data.releases if r.repo == "vercel/ai"]
        assert len(vercel) == 20
        for r in vercel:
            assert r.ai_summary is not None
            assert "批量发版" in r.ai_summary.summary_cn

    @pytest.mark.asyncio
    async def test_no_bulk_all_normal_path(self):
        """无批量组时行为与原路径一致（全部逐个处理）。"""
        processor, comps = _make_processor()
        releases = [_release("a/repo", "v1.0.0"), _release("b/repo", "v2.0.0")]
        releases_data = _releases_data(releases)

        comps["release_material_builder"].build.return_value = ["m1", "m2"]
        comps["release_summarizer"].summarize_materials_async = AsyncMock(
            return_value={}
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(return_value=[])
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        result = await processor.run_async(releases_data, releases)

        assert len(result.release_signals) == 2  # fallback 路径逐个生成
        detect_input = comps[
            "breaking_changes_detector"
        ].detect_breaking_changes_async.call_args.args[0]
        assert len(detect_input["detailed_releases"]) == 2

    @pytest.mark.asyncio
    async def test_category_distribution_logged(self, caplog):
        processor, comps = _make_processor()
        releases = [_release("a/repo", "v1.0.0")]
        releases_data = _releases_data(releases)

        comps["release_material_builder"].build.return_value = ["m1"]
        comps["release_summarizer"].summarize_materials_async = AsyncMock(
            return_value={}
        )
        fake_signal = MagicMock(
            category="research", sources=["u"], related_repos=["a/repo"]
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(
            return_value=[fake_signal]
        )
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        import logging as _logging

        root = _logging.getLogger("trendpluse")
        original = root.propagate
        root.propagate = True
        try:
            with caplog.at_level(_logging.INFO):
                await processor.run_async(releases_data, releases)
        finally:
            root.propagate = original

        assert "release 信号 category 分布" in caplog.text
        assert "research=1" in caplog.text
