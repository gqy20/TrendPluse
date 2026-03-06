"""Issue Agent 与 Pipeline 集成测试"""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import trendpluse.pipeline as pipeline_module
from trendpluse.services.issue_workflow_service import IssueWorkflowService


class _StubIssueAgentRunner:
    called = False

    def __init__(
        self,
        model=None,
        retry_max_attempts: int = 3,
        retry_wait_seconds: float = 1.0,
    ):
        self.model = model
        self.retry_max_attempts = retry_max_attempts
        self.retry_wait_seconds = retry_wait_seconds

    async def analyze_directory(self, input_dir: Path, output_dir: Path) -> int:
        _StubIssueAgentRunner.called = True
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "repo.analysis.json").write_text(
            '{"top_pain_points": []}', encoding="utf-8"
        )
        return 1


def test_pipeline_runs_issue_agent_when_enabled(tmp_path, monkeypatch):
    """启用开关且存在 JSONL 输入时，应触发 Issue Agent 分析。"""
    date = "2026-02-06"
    issue_dir = tmp_path / date
    issue_dir.mkdir(parents=True)
    (issue_dir / "owner__repo.jsonl").write_text(
        '{"repo":"owner/repo","issue_id":1}\n', encoding="utf-8"
    )

    pipeline = object.__new__(pipeline_module.TrendPulsePipeline)
    pipeline.settings = cast(
        Any,
        SimpleNamespace(
            enable_issue_agent_analysis=True,
            anthropic_api_key="test-key",
            issue_dump_dir=str(tmp_path),
            issue_agent_model=None,
            issue_agent_retry_max_attempts=2,
            issue_agent_retry_wait_seconds=0.0,
        ),
    )
    pipeline.issue_workflow = IssueWorkflowService(
        issue_collector=None,
        issue_dump_dir=str(tmp_path),
        enable_issue_agent_analysis=True,
        anthropic_api_key="test-key",
        max_parallel_workers=4,
        max_issues_per_repo=20,
        issue_agent_model=None,
        issue_agent_retry_max_attempts=2,
        issue_agent_retry_wait_seconds=0.0,
        runner_factory=_StubIssueAgentRunner,
    )

    pipeline._run_issue_agent_analysis(date)

    assert _StubIssueAgentRunner.called is True
    assert (issue_dir / "analysis" / "repo.analysis.json").exists()
