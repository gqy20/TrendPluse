"""SDK PR 分析器测试（全量文件模式 + 引用校验）。"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest

from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.sdk_pr_analyzer import (
    PRSignalItem,
    PRSignalsResult,
    SDKPRAnalyzer,
)
from trendpluse.models.source import AnalysisMaterial


def _material(repo: str, number: int, body: str = "feat: X") -> AnalysisMaterial:
    return AnalysisMaterial.from_pr_details(
        {
            "repo_name": repo,
            "number": number,
            "title": f"PR #{number}",
            "body": body,
            "author": "alice",
            "state": "closed",
            "merged": True,
            "additions": 100,
            "deletions": 10,
            "changed_files": 5,
        }
    )


@pytest.fixture
def log_capture(caplog):
    import logging as _logging

    root = _logging.getLogger("trendpluse")
    original = root.propagate
    root.propagate = True
    yield caplog
    root.propagate = original


class TestSDKPRAnalyzer:
    def test_split_batches_no_upper_bound(self):
        analyzer = SDKPRAnalyzer(batch_size=40)
        prs = [{"repo": "a/b", "number": i} for i in range(500)]
        batches = analyzer._split_batches(prs)
        # 500 个候选 → 13 批，无截断
        assert [len(b) for b in batches] == [40] * 12 + [20]

    def test_write_prs_file_full_body(self, tmp_path):
        analyzer = SDKPRAnalyzer()
        prs = [
            {
                "repo": "owner/repo",
                "number": 42,
                "title": "Important change",
                "body": "L" * 50_000,  # 超长 body 也全量入文件
                "author": "alice",
                "state": "closed",
                "merged": True,
                "changed_files": 12,
                "additions": 1000,
                "deletions": 100,
                "labels": ["feature"],
                "url": "https://github.com/owner/repo/pull/42",
            }
        ]
        path = analyzer._write_prs_file(tmp_path, prs, suffix="-batch-1")
        content = open(path, encoding="utf-8").read()
        assert "L" * 50_000 in content  # 全量 body，零截断
        assert "**Number:** 42" in content

    @pytest.mark.asyncio
    async def test_batch_analysis_logs_and_filters_hallucinated(
        self, tmp_path, log_capture
    ):
        caplog = log_capture
        analyzer = SDKPRAnalyzer(batch_size=10)
        batch = [
            {"repo": "owner/repo", "number": 1, "url": "u1"},
            {"repo": "owner/repo", "number": 2, "url": "u2"},
        ]
        batch_file = analyzer._write_prs_file(tmp_path, batch, suffix="-batch-1")

        fake_output = PRSignalsResult(
            signals=[
                PRSignalItem(
                    pr_number=1,
                    repo="owner/repo",
                    title="真实信号",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="w",
                ),
                PRSignalItem(
                    pr_number=999,  # 幻觉引用
                    repo="owner/repo",
                    title="幻觉信号",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="w",
                ),
            ]
        )
        fake_result = SimpleNamespace(output=fake_output, metrics=None)

        with patch.object(
            analyzer.query_engine,
            "query_async",
            new=AsyncMock(return_value=fake_result),
        ):
            signals = await analyzer._analyze_batch(
                batch, batch_file, batch_index=1, total_batches=1
            )

        assert len(signals) == 1  # 幻觉被确定性过滤
        assert "PR batch 1/1 done" in caplog.text
        assert "prs=2" in caplog.text
        assert "matched=1" in caplog.text
        assert "ref_mismatch=1" in caplog.text

    @pytest.mark.asyncio
    async def test_materials_flow_through_shared_batches(self, tmp_path):
        """materials 入口全量分批，白名单随批切换。"""
        analyzer = SDKPRAnalyzer(batch_size=2)
        materials = [_material("o/r", i) for i in range(5)]

        seen_whitelists = []
        empty = PRSignalsResult(signals=[])

        async def fake_query(prompt):
            assert analyzer.query_engine.file_whitelist is not None
            seen_whitelists.append(set(analyzer.query_engine.file_whitelist))
            return SimpleNamespace(output=empty, metrics=None)

        with patch.object(analyzer.query_engine, "query_async", new=fake_query):
            result = await analyzer.analyze_materials_async(materials)

        assert result == []
        assert len(seen_whitelists) == 3  # 5 materials → 3 批
        assert analyzer.query_engine.file_whitelist is None  # 运行后还原
        # 各批白名单文件互不相同
        assert len({frozenset(w) for w in seen_whitelists}) == 3


class TestClipChangelog:
    def test_short_body_kept_full(self):
        assert ReleaseSummarizer.clip_changelog("abc") == "abc"

    def test_empty_body(self):
        assert ReleaseSummarizer.clip_changelog("") == ""
        assert ReleaseSummarizer.clip_changelog(None) == ""

    def test_extreme_body_head_tail_with_marker(self):
        body = "H" * 40_000 + "MIDDLE" + "T" * 10_000
        clipped = ReleaseSummarizer.clip_changelog(body)
        assert len(clipped) < len(body)
        assert clipped.startswith("H" * ReleaseSummarizer.CHANGELOG_HEAD)
        assert clipped.endswith("T" * ReleaseSummarizer.CHANGELOG_TAIL)
        assert "中间省略" in clipped  # AI 知道信息不完整


class TestBulkChangelogsFile:
    def test_full_changelogs_written(self, tmp_path):
        group = [
            {
                "repo": "vercel/ai",
                "tag_name": f"@pkg{i}@1.0.{i}",
                "body": f"full changelog {i} " + "x" * 5000,
                "html_url": f"https://github.com/vercel/ai/releases/tag/@pkg{i}",
            }
            for i in range(3)
        ]
        path = ReleaseSummarizer._write_bulk_changelogs_file(
            str(tmp_path), "vercel/ai", group
        )
        content = open(path, encoding="utf-8").read()
        # 全量 changelog 入文件（对比旧实现每包 200 字符截断）
        for i in range(3):
            assert f"full changelog {i} " + "x" * 5000 in content
        assert "## @pkg0@1.0.0" in content


class TestPRNumberTypeNormalization:
    @pytest.mark.asyncio
    async def test_string_external_id_matches_int_output(self, tmp_path):
        """material 的 external_id 为 str，LLM 输出 int——归一后必须匹配。

        回归背景: SourceRef.external_id=str("93400") 与 LLM 的 int 93400
        曾因类型不等被整体误杀（matched=0）。
        """
        analyzer = SDKPRAnalyzer(batch_size=10)
        # 材料路径: external_id 是字符串
        materials = [_material("owner/repo", 42)]
        prs = [analyzer._material_to_pr(m) for m in materials]
        assert prs[0]["number"] == 42  # _material_to_pr 已归一为 int

        batch_file = analyzer._write_prs_file(tmp_path, prs, suffix="-batch-1")
        fake_output = PRSignalsResult(
            signals=[
                PRSignalItem(
                    pr_number=42,  # LLM 输出 int
                    repo="owner/repo",
                    title="信号",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="w",
                )
            ]
        )
        fake_result = SimpleNamespace(output=fake_output, metrics=None)
        with patch.object(
            analyzer.query_engine,
            "query_async",
            new=AsyncMock(return_value=fake_result),
        ):
            signals = await analyzer._analyze_batch(
                prs, batch_file, batch_index=1, total_batches=1
            )
        assert len(signals) == 1

        # 批次 key 为 str 的场景（防御批数据来自 JSON 等 str 来源）
        str_batch = [{"repo": "owner/repo", "number": "42", "url": "u"}]
        str_file = analyzer._write_prs_file(tmp_path, str_batch, suffix="-batch-2")
        with patch.object(
            analyzer.query_engine,
            "query_async",
            new=AsyncMock(return_value=fake_result),
        ):
            signals = await analyzer._analyze_batch(
                str_batch, str_file, batch_index=1, total_batches=1
            )
        assert len(signals) == 1
