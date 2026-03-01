"""CLI 冒烟测试。

仅验证命令可展示帮助信息，不执行实际业务流程。
"""

import sys
from collections.abc import Callable

import pytest

from trendpluse.automation.add_repo import main as add_repo_main
from trendpluse.automation.bridge_discovery_to_monitoring import (
    main as bridge_discovery_main,
)
from trendpluse.automation.generate_report_index import main as generate_index_main
from trendpluse.automation.normalize_daily_report_stats import (
    main as normalize_stats_main,
)
from trendpluse.automation.sync_repos_to_docs import main as sync_repos_main
from trendpluse.cli.analyze_issues_with_agent import main as analyze_issues_main
from trendpluse.cli.analyze_repo import main as analyze_repo_main
from trendpluse.cli.discover_projects import main as discover_projects_main
from trendpluse.cli.run import main as run_main
from trendpluse.cli.run_weekly import main as run_weekly_main
from trendpluse.cli.send_feishu_notification import main as send_feishu_main
from trendpluse.cli.send_weekly_feishu import main as send_weekly_feishu_main


@pytest.mark.parametrize(
    ("entry", "prog_name"),
    [
        (run_main, "trendpluse-run"),
        (run_weekly_main, "trendpluse-run-weekly"),
        (discover_projects_main, "trendpluse-discover-projects"),
        (analyze_issues_main, "trendpluse-analyze-issues"),
        (analyze_repo_main, "trendpluse-analyze-repo"),
        (send_feishu_main, "trendpluse-send-feishu"),
        (send_weekly_feishu_main, "trendpluse-send-weekly-feishu"),
        (add_repo_main, "trendpluse-add-repo"),
        (bridge_discovery_main, "trendpluse-bridge-discovery"),
        (generate_index_main, "trendpluse-generate-report-index"),
        (sync_repos_main, "trendpluse-sync-repos-to-docs"),
        (normalize_stats_main, "trendpluse-normalize-daily-stats"),
    ],
)
def test_cli_help_exit_code_zero(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    entry: Callable[[], object],
    prog_name: str,
) -> None:
    """所有 CLI 入口在 `--help` 下都应以 0 退出。"""
    monkeypatch.setattr(sys, "argv", [prog_name, "--help"])
    with pytest.raises(SystemExit) as exc_info:
        entry()

    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out.lower()
