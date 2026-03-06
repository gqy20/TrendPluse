"""Issue 工作流服务。"""

from __future__ import annotations

from trendpluse.app.issue_agent import IssueWorkflowCoordinator
from trendpluse.utils.issue_agent_io import load_issue_agent_report  # noqa: F401
from trendpluse.utils.issue_io import dump_issues_to_jsonl  # noqa: F401
from trendpluse.workflows.issue_agent_runner import IssueAgentRunner  # noqa: F401


class IssueWorkflowService(IssueWorkflowCoordinator):
    """负责 issue 抓取、落盘、agent 分析与结果读取。"""

    def __init__(self, **kwargs):
        """保持旧模块 patch 面稳定。"""
        super().__init__(
            runner_factory=kwargs.pop("runner_factory", IssueAgentRunner),
            issue_dumper=kwargs.pop("issue_dumper", dump_issues_to_jsonl),
            issue_report_loader=kwargs.pop(
                "issue_report_loader", load_issue_agent_report
            ),
            **kwargs,
        )
