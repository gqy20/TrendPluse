"""Issue 洞察新架构测试。"""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from trendpluse.app.pipeline import TrendPulsePipeline
from trendpluse.utils.issue_agent_io import load_issue_agent_report


def test_load_issue_agent_report_supports_repo_signals_and_global_aggregation(
    tmp_path: Path,
) -> None:
    """仓库级 signals 应可汇总为带来源的全局洞察。"""
    base_dir = tmp_path / "issues"
    snapshot_dir = base_dir / "2026-03-07"
    analysis_dir = snapshot_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    (snapshot_dir / "owner__repo1.jsonl").write_text(
        '{"repo":"owner/repo1","issue_id":1}\n', encoding="utf-8"
    )
    (snapshot_dir / "owner__repo2.jsonl").write_text(
        '{"repo":"owner/repo2","issue_id":2}\n', encoding="utf-8"
    )

    (analysis_dir / "owner__repo1.analysis.json").write_text(
        """{
  "repo": "owner/repo1",
  "snapshot_date": "2026-03-07",
  "signals": [
    {
      "id": "sig-r1-1",
      "repo": "owner/repo1",
      "topic": "登录失效",
      "summary": "升级后频繁掉登录态",
      "count": 2,
      "priority": "P1",
      "confidence": 0.81,
      "affected_repos": ["owner/repo1"],
      "sample_urls": ["https://github.com/owner/repo1/issues/101"],
      "source_issues": [
        {
          "repo": "owner/repo1",
          "issue_number": 101,
          "title": "Login expires after upgrade",
          "url": "https://github.com/owner/repo1/issues/101"
        }
      ]
    }
  ]
}""",
        encoding="utf-8",
    )
    (analysis_dir / "owner__repo2.analysis.json").write_text(
        """{
  "repo": "owner/repo2",
  "snapshot_date": "2026-03-07",
  "signals": [
    {
      "id": "sig-r2-1",
      "repo": "owner/repo2",
      "topic": "登录失效",
      "summary": "OAuth 回调后会话丢失",
      "count": 1,
      "priority": "P0",
      "confidence": 0.93,
      "affected_repos": ["owner/repo2"],
      "sample_urls": ["https://github.com/owner/repo2/issues/9"],
      "source_issues": [
        {
          "repo": "owner/repo2",
          "issue_number": 9,
          "title": "OAuth callback loses session",
          "url": "https://github.com/owner/repo2/issues/9"
        }
      ]
    }
  ]
}""",
        encoding="utf-8",
    )

    report = load_issue_agent_report(str(base_dir), "2026-03-07")

    assert len(report.repo_reports) == 2
    assert len(report.top_pain_points) == 1
    merged = report.top_pain_points[0]
    assert merged.topic == "登录失效"
    assert merged.count == 3
    assert merged.priority == "P0"
    assert {item.repo for item in merged.source_issues} == {
        "owner/repo1",
        "owner/repo2",
    }
    assert {item.issue_number for item in merged.source_issues} == {101, 9}


@patch("trendpluse.app.pipeline.build_app_components")
@patch("trendpluse.app.pipeline.build_reporting_components")
@patch("trendpluse.app.pipeline.build_analyzer_components")
@patch("trendpluse.app.pipeline.build_collector_components")
@patch("trendpluse.app.pipeline.IssueGlobalSummarizer")
def test_trend_pipeline_wires_issue_insight_loader(
    mock_summarizer_cls: Mock,
    mock_build_collectors: Mock,
    mock_build_analyzers: Mock,
    mock_build_reporting: Mock,
    mock_build_apps: Mock,
) -> None:
    """主流程应先读取 issue 洞察，再经过全局汇总器。"""
    loaded = object()
    summarized = object()
    settings = SimpleNamespace(
        anthropic_base_url="",
        anthropic_api_key="test-key",
        anthropic_model="glm-4.7",
    )
    mock_build_collectors.return_value = SimpleNamespace()
    mock_build_analyzers.return_value = SimpleNamespace()
    reporting = SimpleNamespace(
        builder=SimpleNamespace(issue_insights_loader=lambda _date: None)
    )
    mock_build_reporting.return_value = reporting
    mock_summarizer = mock_summarizer_cls.return_value
    mock_summarizer.summarize.return_value = summarized
    mock_build_apps.return_value = SimpleNamespace(
        issue_workflow=SimpleNamespace(load_insights=lambda _date: loaded),
        daily_app=SimpleNamespace(),
        weekly_app=SimpleNamespace(),
    )

    TrendPulsePipeline(settings=settings)

    assert reporting.builder.issue_insights_loader("2026-03-07") is summarized
    mock_summarizer.summarize.assert_called_once_with(loaded)
