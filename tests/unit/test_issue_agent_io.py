"""Issue Agent 聚合读取测试"""

from pathlib import Path

from trendpluse.models.issue_agent import IssueAgentReport
from trendpluse.utils.issue_agent_io import (
    load_issue_agent_report,
    summarize_issue_agent_run_status,
)


def test_load_issue_agent_report_merges_topics(tmp_path: Path) -> None:
    base_dir = tmp_path / "issues"
    snapshot = base_dir / "2026-02-05" / "analysis"
    snapshot.mkdir(parents=True, exist_ok=True)

    (snapshot / "repo1.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-05",
  "signals": [
    {
      "topic": "安装失败",
      "count": 2,
      "affected_repos": ["a/b"],
      "sample_urls": ["u1"],
      "aliases": ["install failure"],
      "confidence": 0.8,
      "priority": "P1",
      "review_reason": "影响首次使用"
    }
  ]
}""",
        encoding="utf-8",
    )
    (snapshot / "repo2.analysis.json").write_text(
        """{
  "repo": "c/d",
  "snapshot_date": "2026-02-05",
  "signals": [
    {
      "topic": "安装失败",
      "count": 1,
      "affected_repos": ["c/d"],
      "sample_urls": ["u2"],
      "aliases": ["安装报错"],
      "confidence": 0.92,
      "priority": "P0"
    }
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-05")
    assert len(report.top_pain_points) == 1
    assert report.top_pain_points[0].topic == "安装失败"
    assert report.top_pain_points[0].count == 3
    assert set(report.top_pain_points[0].affected_repos) == {"a/b", "c/d"}
    assert set(report.top_pain_points[0].aliases) == {"install failure", "安装报错"}
    assert report.top_pain_points[0].confidence == 0.92
    assert report.top_pain_points[0].priority == "P0"
    assert report.top_pain_points[0].review_reason == "影响首次使用"
    assert report.generated_files == 2
    assert report.parsed_files == 2
    assert report.failed_files == 0
    assert report.failed_samples == []


def test_load_issue_agent_report_tracks_failed_files(tmp_path: Path) -> None:
    base_dir = tmp_path / "issues"
    snapshot = base_dir / "2026-02-05" / "analysis"
    snapshot.mkdir(parents=True, exist_ok=True)

    (snapshot / "valid.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-05",
  "signals": [
    {"topic": "安装失败", "count": 2, "affected_repos": ["a/b"], "sample_urls": ["u1"]}
  ]
}""",
        encoding="utf-8",
    )
    (snapshot / "bad-json.analysis.json").write_text("{oops", encoding="utf-8")
    (snapshot / "bad-schema.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-05",
  "signals": [
    {
      "topic": "类型错误",
      "count": "xx",
      "affected_repos": ["a/b"],
      "sample_urls": ["u1"]
    }
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-05")
    assert report.generated_files == 3
    assert report.parsed_files == 1
    assert report.failed_files == 2
    assert "bad-json.analysis.json" in report.failed_samples
    assert "bad-schema.analysis.json" in report.failed_samples


def test_load_issue_agent_report_marks_missing_analysis_outputs(tmp_path: Path) -> None:
    base_dir = tmp_path / "issues"
    snapshot_dir = base_dir / "2026-02-06"
    analysis_dir = snapshot_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    (snapshot_dir / "repo1.jsonl").write_text(
        '{"repo":"a/b","issue_id":1}\n',
        encoding="utf-8",
    )
    (snapshot_dir / "repo2.jsonl").write_text(
        '{"repo":"c/d","issue_id":2}\n',
        encoding="utf-8",
    )
    (analysis_dir / "repo1.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-06",
  "signals": [
    {"topic": "安装失败", "count": 1, "affected_repos": ["a/b"], "sample_urls": ["u1"]}
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-06")
    assert report.expected_files == 2
    assert report.generated_files == 1
    assert report.parsed_files == 1
    assert report.failed_files == 1
    assert "repo2.analysis.json (missing)" in report.failed_samples


def test_load_issue_agent_report_sorts_by_priority_then_confidence(
    tmp_path: Path,
) -> None:
    base_dir = tmp_path / "issues"
    snapshot = base_dir / "2026-02-07" / "analysis"
    snapshot.mkdir(parents=True, exist_ok=True)

    (snapshot / "repo1.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-07",
  "signals": [
    {
      "topic": "高频低优先级",
      "count": 20,
      "affected_repos": ["a/b"],
      "sample_urls": ["u1"],
      "priority": "P2",
      "confidence": 0.99
    },
    {
      "topic": "低频高优先级",
      "count": 3,
      "affected_repos": ["c/d"],
      "sample_urls": ["u2"],
      "priority": "P0",
      "confidence": 0.70
    },
    {
      "topic": "中优先级高置信度",
      "count": 5,
      "affected_repos": ["e/f"],
      "sample_urls": ["u3"],
      "priority": "P1",
      "confidence": 0.95
    }
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-07")
    topics = [item.topic for item in report.top_pain_points]
    assert topics[:3] == ["低频高优先级", "中优先级高置信度", "高频低优先级"]


def test_load_issue_agent_report_has_quality_gate_metrics(tmp_path: Path) -> None:
    base_dir = tmp_path / "issues"
    snapshot_dir = base_dir / "2026-02-08"
    analysis_dir = snapshot_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    (snapshot_dir / "repo1.jsonl").write_text(
        '{"repo":"a/b","issue_id":1}\n',
        encoding="utf-8",
    )
    (snapshot_dir / "repo2.jsonl").write_text(
        '{"repo":"c/d","issue_id":2}\n',
        encoding="utf-8",
    )
    (analysis_dir / "repo1.analysis.json").write_text(
        """{
  "repo": "a/b",
  "snapshot_date": "2026-02-08",
  "signals": [
    {"topic": "安装失败", "count": 1, "affected_repos": ["a/b"], "sample_urls": ["u1"]}
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-08")
    assert report.quality_status == "poor"
    assert 0 <= report.quality_score < 0.8


def test_summarize_issue_agent_run_status_variants() -> None:
    no_data = IssueAgentReport(
        expected_files=0,
        generated_files=0,
        parsed_files=0,
        failed_files=0,
    )
    assert summarize_issue_agent_run_status(no_data) == "no_data"

    success = IssueAgentReport(
        expected_files=2,
        generated_files=2,
        parsed_files=2,
        failed_files=0,
    )
    assert summarize_issue_agent_run_status(success) == "success"

    partial = IssueAgentReport(
        expected_files=3,
        generated_files=3,
        parsed_files=2,
        failed_files=1,
    )
    assert summarize_issue_agent_run_status(partial) == "partial_failure"

    failed = IssueAgentReport(
        expected_files=3,
        generated_files=1,
        parsed_files=0,
        failed_files=3,
    )
    assert summarize_issue_agent_run_status(failed) == "failed"
