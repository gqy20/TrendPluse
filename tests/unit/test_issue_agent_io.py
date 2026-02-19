"""Issue Agent 聚合读取测试"""

from pathlib import Path

from trendpluse.utils.issue_agent_io import load_issue_agent_report


def test_load_issue_agent_report_merges_topics(tmp_path: Path) -> None:
    base_dir = tmp_path / "issues"
    snapshot = base_dir / "2026-02-05" / "analysis"
    snapshot.mkdir(parents=True, exist_ok=True)

    (snapshot / "repo1.analysis.json").write_text(
        """{
  "top_pain_points": [
    {"topic": "安装失败", "count": 2, "affected_repos": ["a/b"], "sample_urls": ["u1"]}
  ]
}""",
        encoding="utf-8",
    )
    (snapshot / "repo2.analysis.json").write_text(
        """{
  "top_pain_points": [
    {"topic": "安装失败", "count": 1, "affected_repos": ["c/d"], "sample_urls": ["u2"]}
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-02-05")
    assert len(report.top_pain_points) == 1
    assert report.top_pain_points[0].topic == "安装失败"
    assert report.top_pain_points[0].count == 3
    assert set(report.top_pain_points[0].affected_repos) == {"a/b", "c/d"}
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
  "top_pain_points": [
    {"topic": "安装失败", "count": 2, "affected_repos": ["a/b"], "sample_urls": ["u1"]}
  ]
}""",
        encoding="utf-8",
    )
    (snapshot / "bad-json.analysis.json").write_text("{oops", encoding="utf-8")
    (snapshot / "bad-schema.analysis.json").write_text(
        """{
  "top_pain_points": [
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
  "top_pain_points": [
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
