"""Issue Agent 协调器集成测试"""

from __future__ import annotations

from pathlib import Path

from trendpluse.app.issue_agent import IssueWorkflowCoordinator
from trendpluse.models.issue_agent import IssueAgentBatchResult


class _StubIssueAgentRunner:
    called = False

    def __init__(
        self,
        model=None,
        retry_max_attempts: int = 3,
        retry_wait_seconds: float = 1.0,
        review_confidence_threshold: float = 0.6,
        total_timeout_seconds: float = 600.0,
        attempt_timeout_seconds: float = 120.0,
        **kwargs,  # 接受其他参数
    ):
        self.model = model
        self.retry_max_attempts = retry_max_attempts
        self.retry_wait_seconds = retry_wait_seconds
        self.review_confidence_threshold = review_confidence_threshold
        self.total_timeout_seconds = total_timeout_seconds
        self.attempt_timeout_seconds = attempt_timeout_seconds

    async def analyze_directory(
        self, input_dir: Path, output_dir: Path
    ) -> IssueAgentBatchResult:
        _StubIssueAgentRunner.called = True
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "repo.analysis.json").write_text(
            '{"top_pain_points": []}', encoding="utf-8"
        )
        return IssueAgentBatchResult(
            expected_files=1,
            succeeded_files=1,
            failed_files=0,
            failed_samples=[],
        )


def test_pipeline_runs_issue_agent_when_enabled(tmp_path, monkeypatch):
    """启用开关且存在 JSONL 输入时，应触发 Issue Agent 分析。"""
    date = "2026-02-06"
    issue_dir = tmp_path / date
    issue_dir.mkdir(parents=True)
    (issue_dir / "owner__repo.jsonl").write_text(
        '{"repo":"owner/repo","issue_id":1}\n', encoding="utf-8"
    )

    coordinator = IssueWorkflowCoordinator(
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

    coordinator.run_issue_agent_analysis(date)

    assert _StubIssueAgentRunner.called is True
    assert (issue_dir / "analysis" / "repo.analysis.json").exists()
