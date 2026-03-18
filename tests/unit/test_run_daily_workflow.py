"""run-daily workflow 配置测试"""

from pathlib import Path


def test_run_daily_enables_issue_agent_analysis():
    """daily workflow 应开启 Issue Agent 分析环境变量。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert 'ENABLE_ISSUE_AGENT_ANALYSIS: "true"' in content


def test_run_daily_warns_on_summary_validation_degradation():
    """daily workflow 应对 summary 校验失败发出告警而非中断。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert "Validate Daily Summary fields" in content
    assert "validate_smoke_daily_summary" in content
    assert "::warning::Daily summary validation degraded:" in content


def test_run_daily_smoke_uses_summary_validation():
    """smoke workflow 应校验 summary agent 关键输出字段。"""
    content = Path(".github/workflows/run-daily-smoke.yml").read_text(encoding="utf-8")
    assert "validate_smoke_daily_summary" in content
