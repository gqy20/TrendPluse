"""run-weekly workflow 配置测试"""

from pathlib import Path


def test_run_weekly_resolves_week_id_with_project_environment() -> None:
    """weekly workflow 应使用 uv 环境解析周标识，避免裸 python 导入失败。"""
    content = Path(".github/workflows/run-weekly.yml").read_text(encoding="utf-8")

    assert "from trendpluse.cli.report_json_common import resolve_week_id" in content
    assert "WEEK_ID=$(uv run python -c " in content
    assert "WEEK_ID=$(python -c " not in content


def test_run_weekly_notify_checks_out_published_commit() -> None:
    """weekly workflow 应让通知任务检出周报提交后的最新提交。"""
    content = Path(".github/workflows/run-weekly.yml").read_text(encoding="utf-8")

    assert "commit_sha: ${{ steps.publish_report.outputs.commit_sha }}" in content
    assert 'echo "commit_sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"' in content
    assert "id: publish_report" in content
    assert "ref: ${{ needs.weekly.outputs.commit_sha }}" in content
