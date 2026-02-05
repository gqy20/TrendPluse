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
