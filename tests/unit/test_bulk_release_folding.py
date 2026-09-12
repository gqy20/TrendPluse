"""Monorepo 批量发版整批分析测试。"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from trendpluse.app.release_processor import (
    BULK_RELEASE_THRESHOLD,
    ReleaseProcessor,
)
from trendpluse.models.signal import (
    BulkReleaseAnalysis,
    NotablePackage,
    ReleasesData,
)


def _release(repo: str, version: str, body: str = "changelog") -> dict:
    return {
        "repo": repo,
        "tag_name": version,
        "name": version,
        "body": body,
        "html_url": f"https://github.com/{repo}/releases/tag/{version}",
    }


def _analysis(
    summary: str = "纯 changesets 版本同步升级，无重大变更。",
    notable: list[NotablePackage] | None = None,
    has_breaking: bool = False,
    impact: int = 2,
) -> BulkReleaseAnalysis:
    return BulkReleaseAnalysis(
        summary_cn=summary,
        key_changes=["版本同步"],
        notable_packages=notable or [],
        has_breaking_changes=has_breaking,
        impact_level=impact,
    )


def _make_processor() -> tuple[ReleaseProcessor, dict[str, MagicMock]]:
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


class TestBulkSignalsFromAnalysis:
    def test_pure_sync_batch(self):
        group = [_release("vercel/ai", f"@pkg{i}@2.0.{i}") for i in range(20)]
        signals = ReleaseProcessor._build_bulk_signals("vercel/ai", group, _analysis())
        assert len(signals) == 1  # 纯同步：仅 1 条整批信号
        assert "批量发版 20 个子包" in signals[0].title
        assert signals[0].impact_score == 2
        assert signals[0].why_it_matters == "纯 changesets 版本同步升级，无重大变更。"

    def test_notable_packages_get_own_signals(self):
        group = [_release("vercel/ai", f"@pkg{i}@2.0.{i}") for i in range(12)]
        notable = [
            NotablePackage(
                package="@gateway@3.0.0",
                reason="major 版本跳跃，网关 API 重构",
                change_type="breaking",
                impact_level=4,
            ),
            NotablePackage(
                package="@react@2.1.0",
                reason="新增服务端流式渲染能力",
                change_type="feature",
                impact_level=3,
            ),
        ]
        signals = ReleaseProcessor._build_bulk_signals(
            "vercel/ai", group, _analysis(notable=notable, impact=3)
        )
        assert len(signals) == 3  # 1 整批 + 2 notable
        assert "2 个值得注意" in signals[0].title
        notable_titles = [s.title for s in signals[1:]]
        assert "vercel/ai @gateway@3.0.0" in notable_titles
        gateway = next(s for s in signals if "@gateway" in s.title)
        assert gateway.impact_score == 4
        assert gateway.why_it_matters == "major 版本跳跃，网关 API 重构"

    def test_bulk_breaking_entries_from_ai(self):
        notable = [
            NotablePackage(
                package="@gateway@3.0.0",
                reason="API 不兼容重构",
                change_type="breaking",
                impact_level=4,
            )
        ]
        entries = ReleaseProcessor._bulk_breaking_entries(
            "vercel/ai", _analysis(notable=notable, has_breaking=True, impact=4)
        )
        assert len(entries) == 1
        assert entries[0]["tag_name"] == "@gateway@3.0.0"
        assert entries[0]["changes"][0]["impact"] == "high"

    def test_no_breaking_no_entries(self):
        assert ReleaseProcessor._bulk_breaking_entries("r", _analysis()) == []


class TestRunAsyncIntegration:
    @pytest.mark.asyncio
    async def test_bulk_group_analyzed_once_with_full_material(self):
        """批量组走整批分析：AI 收到含全部子包的材料，非逐包调用。"""
        processor, comps = _make_processor()
        bulk = [
            _release("vercel/ai", f"@pkg{i}@2.0.{i}", body=f"fix: issue {i}")
            for i in range(15)
        ]
        normal = [_release("anthropics/claude-code", "v2.1.269")]
        releases_data = _releases_data(normal + bulk)

        comps["release_material_builder"].build.return_value = ["mat-1"]
        comps["release_summarizer"].summarize_materials_async = AsyncMock(
            return_value={}
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(return_value=[])
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        captured: dict = {}

        async def fake_bulk_async(repo, group):
            captured["repo"] = repo
            captured["group"] = group
            return _analysis()

        comps["release_summarizer"].summarize_bulk_group_async = fake_bulk_async

        result = await processor.run_async(releases_data, normal + bulk)

        # 整批分析被调用一次，收到完整 15 包材料
        assert captured["repo"] == "vercel/ai"
        assert len(captured["group"]) == 15

        # summarizer 的逐包路径只收到 normal（1 个）
        summarize_call = comps["release_summarizer"].summarize_materials_async.call_args
        assert len(summarize_materials_arg(summarize_call)) == 1

        # 信号 = 批量整批 1（normal analyzer 空产出不再模板伪造）
        assert len(result.release_signals) == 1

        # 落盘数据完整（16 条），批量组 ai_summary 为 AI 分析结论
        assert len(result.detailed_releases) == 16
        vercel = [r for r in releases_data.releases if r.repo == "vercel/ai"]
        assert len(vercel) == 15
        for r in vercel:
            assert r.ai_summary is not None
            assert "changesets" in r.ai_summary.summary_cn

    @pytest.mark.asyncio
    async def test_bulk_notable_flow_through(self):
        """AI 判定的 notable 子包贯通到信号与 breaking。"""
        processor, comps = _make_processor()
        bulk = [_release("vercel/ai", f"@pkg{i}@2.0.{i}") for i in range(12)]
        releases_data = _releases_data(bulk)

        comps["release_summarizer"].summarize_bulk_group_async = AsyncMock(
            return_value=_analysis(
                notable=[
                    NotablePackage(
                        package="@pkg5@2.0.5",
                        reason="新增重要能力 X",
                        change_type="feature",
                        impact_level=4,
                    )
                ],
                has_breaking=False,
                impact=3,
            )
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(return_value=[])
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        result = await processor.run_async(releases_data, bulk)

        assert len(result.release_signals) == 2  # 整批 + notable
        notable_signal = next(s for s in result.release_signals if "pkg5" in s.title)
        assert notable_signal.impact_score == 4
        # notable 包的落盘 summary 额外标注
        pkg5 = next(r for r in releases_data.releases if r.version == "@pkg5@2.0.5")
        assert pkg5.ai_summary is not None
        assert "值得单独关注" in pkg5.ai_summary.summary_cn

    @pytest.mark.asyncio
    async def test_bulk_llm_failure_falls_back_to_semantic(self):
        """整批分析 LLM 失败时降级为版本语义判断（major 仍标出）。"""
        processor, comps = _make_processor()
        bulk = [
            _release("vercel/ai", f"@pkg{i}@2.0.{i}", body="sync") for i in range(11)
        ] + [
            _release("vercel/ai", "@gateway@3.0.0", body=""),
        ]
        bulk[-1]["version_info"] = {"major": 3}
        releases_data = _releases_data(bulk)

        comps["release_summarizer"].summarize_bulk_group_async = AsyncMock(
            side_effect=RuntimeError("LLM down")
        )
        comps["release_analyzer"].analyze_materials_async = AsyncMock(return_value=[])
        comps["breaking_changes_detector"].detect_breaking_changes_async = AsyncMock(
            return_value=[]
        )

        result = await processor.run_async(releases_data, bulk)

        # 降级路径：整批 1 + major 包 notable 1
        assert len(result.release_signals) == 2
        assert any("@gateway@3.0.0" in s.title for s in result.release_signals)


def summarize_materials_arg(call) -> list:
    """从 summarize_materials_async 调用参数中提取 release 材料。"""
    materials: list = call.args[0] if call.args else call.kwargs.get("materials", [])
    return materials
