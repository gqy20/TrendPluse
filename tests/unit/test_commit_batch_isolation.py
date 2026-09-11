"""Commit 批次独立文件 + 文件白名单 hook + 批次可见性测试。"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest

from trendpluse.analyzers.sdk_commit_analyzer import (
    CommitSignalItem,
    CommitSignalsResult,
    SDKCommitAnalyzer,
)
from trendpluse.analyzers.structured_query import StructuredQuery
from trendpluse.models.source import AnalysisMaterial


def _commit_material(sha: str, repo: str = "owner/repo") -> AnalysisMaterial:
    return AnalysisMaterial.from_commit_details(
        {"repo": repo, "sha": sha, "message": f"commit {sha[:6]}", "author": "a"}
    )


class TestWhitelistHook:
    def _make_engine(self, whitelist: set[str]):
        engine = StructuredQuery[CommitSignalsResult](
            output_model=CommitSignalsResult, file_whitelist=whitelist
        )
        denials: list[str] = []
        hook = engine._build_whitelist_hook(whitelist, denials)
        return hook, denials

    @pytest.mark.asyncio
    async def test_in_whitelist_allows(self, tmp_path):
        target = tmp_path / "commits-batch-1.md"
        target.write_text("x")
        hook, _ = self._make_engine({str(target)})
        result = await hook(
            {"tool_name": "Read", "tool_input": {"file_path": str(target)}},
            "id-1",
            {},
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow"

    @pytest.mark.asyncio
    async def test_outside_whitelist_denied_with_reason(self, tmp_path):
        allowed = tmp_path / "allowed.md"
        allowed.write_text("x")
        secret = tmp_path / "secret.env"
        secret.write_text("x")
        hook, denials = self._make_engine({str(allowed)})
        result = await hook(
            {"tool_name": "Read", "tool_input": {"file_path": str(secret)}},
            "id-1",
            {},
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
        assert "白名单" in result["hookSpecificOutput"]["permissionDecisionReason"]
        assert len(denials) == 1

    @pytest.mark.asyncio
    async def test_malformed_input_fails_open(self):
        """hook 输入畸形时 fail-open（SDK 对 hook 异常放行，不可崩溃）。"""
        hook, _ = self._make_engine({"/tmp/x.md"})
        result = await hook({}, "id-1", {})  # 缺 tool_name/tool_input
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow"

    @pytest.mark.asyncio
    async def test_non_file_tools_untouched(self):
        """非 Read/Grep/Glob 工具（如 Bash）不由本 hook 拦截。"""
        hook, _ = self._make_engine({"/tmp/x.md"})
        result = await hook(
            {"tool_name": "Bash", "tool_input": {"command": "cat /etc/passwd"}},
            "id-1",
            {},
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow"


@pytest.fixture
def log_capture(caplog):
    """trendpluse 根 logger propagate=False，临时开启让 caplog 可捕获。"""
    import logging as _logging

    root = _logging.getLogger("trendpluse")
    original = root.propagate
    root.propagate = True
    yield caplog
    root.propagate = original


class TestBatchIsolation:
    def test_write_commits_file_suffix(self, tmp_path):
        analyzer = SDKCommitAnalyzer(batch_size=2)
        commits = [
            {"sha": f"sha{i}", "repo": "o/r", "message": "m", "author": "a"}
            for i in range(2)
        ]
        p1 = analyzer._write_commits_file(tmp_path, commits, suffix="-batch-1")
        assert p1.endswith("commits-batch-1.md")

    @pytest.mark.asyncio
    async def test_each_batch_gets_own_file_and_whitelist(self, tmp_path):
        """每批独立文件，且白名单随批切换（mock query_async 层验证）。"""
        analyzer = SDKCommitAnalyzer(batch_size=2)
        materials = [_commit_material(f"sha{i}000000") for i in range(4)]

        seen: list[tuple[str, frozenset[str]]] = []
        empty_output = CommitSignalsResult(signals=[])

        async def fake_query_async(prompt):
            # prompt 中含本批文件路径；白名单此刻应已切换为本批
            assert analyzer.query_engine.file_whitelist is not None
            seen.append((prompt, frozenset(analyzer.query_engine.file_whitelist)))
            return SimpleNamespace(output=empty_output, metrics=None)

        with patch.object(analyzer.query_engine, "query_async", new=fake_query_async):
            result = await analyzer.analyze_materials_async(materials)

        assert result == []
        assert len(seen) == 2
        for prompt, wl in seen:
            assert len(wl) == 1
            # prompt 引用的文件必须就是白名单里的文件
            batch_file = next(iter(wl))
            assert batch_file in prompt
        # 两批的白名单是不同文件
        assert seen[0][1] != seen[1][1]
        # 运行后白名单还原为初始（None）
        assert analyzer.query_engine.file_whitelist is None

    @pytest.mark.asyncio
    async def test_batch_logging_reports_match_and_hallucination(
        self, tmp_path, log_capture
    ):
        """批次日志必须报告 raw/matched/mismatch，消除"成功但零产出"盲区。"""
        caplog = log_capture
        analyzer = SDKCommitAnalyzer(batch_size=10)
        batch = [
            {"sha": "real1", "repo": "o/r", "message": "m", "author": "a"},
            {"sha": "real2", "repo": "o/r", "message": "m", "author": "a"},
        ]
        batch_file = analyzer._write_commits_file(tmp_path, batch, suffix="-batch-1")

        fake_output = CommitSignalsResult(
            signals=[
                CommitSignalItem(
                    title="真信号",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="w",
                    commit_sha="real1",
                ),
                CommitSignalItem(
                    title="幻觉信号",
                    type="capability",
                    category="engineering",
                    impact_score=3,
                    why_it_matters="w",
                    commit_sha="ffffffff",
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

        # 幻觉 SHA 被过滤，只留真实信号
        assert len(signals) == 1
        assert "Commit batch 1/1 done" in caplog.text
        assert "raw_signals=2" in caplog.text
        assert "matched=1" in caplog.text
        assert "sha_mismatch=1" in caplog.text

    @pytest.mark.asyncio
    async def test_batch_failure_logged_with_context(self, tmp_path, log_capture):
        """批次失败日志必须含批次号/规模/错误摘要。"""
        caplog = log_capture
        analyzer = SDKCommitAnalyzer()
        batch = [{"sha": "x", "repo": "o/r", "message": "m", "author": "a"}]
        batch_file = analyzer._write_commits_file(tmp_path, batch)

        with patch.object(
            analyzer.query_engine,
            "query_async",
            new=AsyncMock(side_effect=RuntimeError("structured output failed")),
        ):
            signals = await analyzer._analyze_batch(
                batch, batch_file, batch_index=2, total_batches=3
            )

        assert signals == []
        assert "batch 2/3" in caplog.text
        assert "commits=1" in caplog.text
        assert "structured output failed" in caplog.text
