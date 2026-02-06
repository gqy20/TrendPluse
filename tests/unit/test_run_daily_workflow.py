"""run-daily workflow 配置测试"""

from pathlib import Path


def test_run_daily_enables_issue_agent_analysis():
    """daily workflow 应开启 Issue Agent 分析环境变量。"""
    content = Path(".github/workflows/run-daily.yml").read_text(encoding="utf-8")
    assert 'ENABLE_ISSUE_AGENT_ANALYSIS: "true"' in content
