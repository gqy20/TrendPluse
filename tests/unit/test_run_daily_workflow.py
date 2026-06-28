"""run-daily workflow 配置测试"""

from pathlib import Path


def test_run_daily_disables_issue_agent_analysis():
    """daily workflow 临时关闭 Issue Agent（SDK 卡死，待排查）。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert 'ENABLE_ISSUE_AGENT_ANALYSIS: "false"' in content


def test_run_daily_warns_on_summary_validation_degradation():
    """daily workflow 应对 summary 校验失败发出告警而非中断。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert "Validate Daily Summary fields" in content
    assert "validate_smoke_daily_summary" in content
    assert "::warning::Daily summary validation degraded:" in content


def test_run_daily_exposes_issue_agent_semantic_quality_metrics():
    """daily workflow 应在 step summary 中展示 Issue Agent 语义质量指标。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert "cross_repo_item_count" in content
    assert "other_category_count" in content
    assert "category_coverage" in content
    assert "semantic_status" in content
    assert "Issue Agent semantic quality degraded" in content


def test_run_daily_smoke_uses_summary_validation():
    """smoke workflow 应校验 summary agent 关键输出字段。"""
    content = Path(".github/workflows/run-daily-smoke.yml").read_text(encoding="utf-8")
    assert "validate_smoke_daily_summary" in content
