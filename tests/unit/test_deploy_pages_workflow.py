"""deploy-pages workflow 配置测试"""

from pathlib import Path


def test_deploy_pages_runs_after_weekly_report_success() -> None:
    """Pages workflow 应在周报 workflow 成功后自动触发部署。"""
    content = Path(".github/workflows/deploy-pages.yml").read_text(encoding="utf-8")

    assert 'workflows: ["Run Daily Analysis", "Weekly Report"]' in content
    assert "github.event.workflow_run.conclusion == 'success'" in content
