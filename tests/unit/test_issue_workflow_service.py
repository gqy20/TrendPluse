"""Issue 工作流服务测试。"""

from __future__ import annotations

from pathlib import Path

import pytest

from trendpluse.workflows.issue_workflow import IssueWorkflowService


class DummyIssueCollector:
    """测试用 IssueCollector。"""

    def __init__(self, issues):
        self.issues = issues
        self.calls = []

    def fetch_issues(
        self,
        *,
        repos,
        snapshot_date,
        max_workers,
        max_issues_per_repo,
    ):
        self.calls.append(
            {
                "repos": repos,
                "snapshot_date": snapshot_date,
                "max_workers": max_workers,
                "max_issues_per_repo": max_issues_per_repo,
            }
        )
        return self.issues, {"total": len(self.issues)}


class DummyIssueRunner:
    """测试用 IssueAgentRunner。"""

    def __init__(self, model=None, retry_max_attempts=3, retry_wait_seconds=1.0):
        self.model = model
        self.retry_max_attempts = retry_max_attempts
        self.retry_wait_seconds = retry_wait_seconds
        self.calls = []

    async def analyze_directory(self, input_dir: Path, output_dir: Path):
        self.calls.append((input_dir, output_dir))
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "repo.analysis.json").write_text(
            '{"top_pain_points": []}', encoding="utf-8"
        )
        return 1


def test_collect_and_analyze_dumps_issue_files(tmp_path, monkeypatch) -> None:
    """测试同步流程会抓取并落盘 issue。"""
    dumped = {}

    def fake_dump(issues, base_dir, snapshot_date):
        dumped["issues"] = issues
        dumped["base_dir"] = base_dir
        dumped["snapshot_date"] = snapshot_date
        issue_dir = Path(base_dir) / snapshot_date
        issue_dir.mkdir(parents=True, exist_ok=True)
        (issue_dir / "owner__repo.jsonl").write_text("{}", encoding="utf-8")
        return {"owner/repo": issue_dir / "owner__repo.jsonl"}

    monkeypatch.setattr(
        "trendpluse.workflows.issue_workflow.dump_issues_to_jsonl", fake_dump
    )

    service = IssueWorkflowService(
        issue_collector=DummyIssueCollector([{"repo": "owner/repo"}]),
        issue_dump_dir=str(tmp_path),
        enable_issue_agent_analysis=False,
        anthropic_api_key="",
        max_parallel_workers=4,
        max_issues_per_repo=20,
    )

    service.collect_and_analyze(["owner/repo"], "2026-03-06")

    assert dumped["snapshot_date"] == "2026-03-06"
    assert dumped["base_dir"] == str(tmp_path)


@pytest.mark.asyncio
async def test_collect_and_analyze_async_runs_issue_agent(
    tmp_path, monkeypatch
) -> None:
    """测试异步流程会触发 issue agent 分析。"""
    runner = DummyIssueRunner()

    def fake_runner_factory(**kwargs):
        return runner

    def fake_dump(issues, base_dir, snapshot_date):
        issue_dir = Path(base_dir) / snapshot_date
        issue_dir.mkdir(parents=True, exist_ok=True)
        (issue_dir / "owner__repo.jsonl").write_text("{}", encoding="utf-8")
        return {"owner/repo": issue_dir / "owner__repo.jsonl"}

    monkeypatch.setattr(
        "trendpluse.workflows.issue_workflow.dump_issues_to_jsonl", fake_dump
    )

    service = IssueWorkflowService(
        issue_collector=DummyIssueCollector([{"repo": "owner/repo"}]),
        issue_dump_dir=str(tmp_path),
        enable_issue_agent_analysis=True,
        anthropic_api_key="test-key",
        max_parallel_workers=4,
        max_issues_per_repo=20,
        issue_agent_model=None,
        issue_agent_retry_max_attempts=2,
        issue_agent_retry_wait_seconds=0.0,
        runner_factory=fake_runner_factory,
    )

    await service.collect_and_analyze_async(["owner/repo"], "2026-03-06")

    assert len(runner.calls) == 1
    input_dir, output_dir = runner.calls[0]
    assert input_dir == tmp_path / "2026-03-06"
    assert output_dir == tmp_path / "2026-03-06" / "analysis"


def test_load_insights_delegates_to_loader(tmp_path, monkeypatch) -> None:
    """测试读取 issue 洞察委托给 loader。"""
    loaded = {}

    def fake_loader(base_dir, snapshot_date):
        loaded["base_dir"] = base_dir
        loaded["snapshot_date"] = snapshot_date
        return {"ok": True}

    monkeypatch.setattr(
        "trendpluse.workflows.issue_workflow.load_issue_agent_report",
        fake_loader,
    )

    service = IssueWorkflowService(
        issue_collector=DummyIssueCollector([]),
        issue_dump_dir=str(tmp_path),
        enable_issue_agent_analysis=False,
        anthropic_api_key="",
        max_parallel_workers=4,
        max_issues_per_repo=20,
    )

    result = service.load_insights("2026-03-06")

    assert result == {"ok": True}
    assert loaded == {"base_dir": str(tmp_path), "snapshot_date": "2026-03-06"}
