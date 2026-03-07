"""Issue 抓取与 Agent 协调。"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from pathlib import Path
from typing import Any

from trendpluse.logger import get_logger
from trendpluse.models.issue_agent import IssueAgentBatchResult
from trendpluse.utils.issue_agent_io import load_issue_agent_report
from trendpluse.utils.issue_io import dump_issues_to_jsonl

logger = get_logger(__name__)


def _default_issue_runner_factory(**kwargs: Any) -> Any:
    """延迟导入 IssueAgentRunner。"""
    from trendpluse.analyzers.issue_agent_runner import IssueAgentRunner

    return IssueAgentRunner(**kwargs)


class IssueWorkflowCoordinator:
    """负责 issue 抓取、落盘、agent 分析与结果读取。"""

    def __init__(
        self,
        *,
        issue_collector: Any,
        issue_dump_dir: str,
        enable_issue_agent_analysis: bool,
        anthropic_api_key: str,
        max_parallel_workers: int,
        max_issues_per_repo: int,
        issue_agent_model: str | None = None,
        issue_agent_retry_max_attempts: int = 3,
        issue_agent_retry_wait_seconds: float = 1.0,
        issue_agent_review_confidence_threshold: float = 0.6,
        issue_agent_attempt_timeout_seconds: float = 120.0,
        issue_agent_total_timeout_seconds: float = 600.0,
        runner_factory: Callable[..., Any] | None = None,
        issue_dumper: Callable[[list[Any], str, str], Any] | None = None,
        issue_report_loader: Callable[[str, str], Any] | None = None,
    ) -> None:
        self.issue_collector = issue_collector
        self.issue_dump_dir = issue_dump_dir
        self.enable_issue_agent_analysis = enable_issue_agent_analysis
        self.anthropic_api_key = anthropic_api_key
        self.max_parallel_workers = max_parallel_workers
        self.max_issues_per_repo = max_issues_per_repo
        self.issue_agent_model = issue_agent_model
        self.issue_agent_retry_max_attempts = issue_agent_retry_max_attempts
        self.issue_agent_retry_wait_seconds = issue_agent_retry_wait_seconds
        self.issue_agent_review_confidence_threshold = (
            issue_agent_review_confidence_threshold
        )
        self.issue_agent_attempt_timeout_seconds = issue_agent_attempt_timeout_seconds
        self.issue_agent_total_timeout_seconds = issue_agent_total_timeout_seconds
        self.runner_factory = runner_factory or _default_issue_runner_factory
        self.issue_dumper = issue_dumper or dump_issues_to_jsonl
        self.issue_report_loader = issue_report_loader or load_issue_agent_report

    def collect_and_analyze(self, repos: list[str], snapshot_date: str) -> None:
        """同步抓取 issue 并执行后续分析。"""
        detailed_issues, _issues_stats = self.issue_collector.fetch_issues(
            repos=repos,
            snapshot_date=snapshot_date,
            max_workers=self.max_parallel_workers,
            max_issues_per_repo=self.max_issues_per_repo,
        )
        if detailed_issues:
            self.issue_dumper(detailed_issues, self.issue_dump_dir, snapshot_date)
        self.run_issue_agent_analysis(snapshot_date)

    async def collect_and_analyze_async(
        self, repos: list[str], snapshot_date: str
    ) -> None:
        """异步抓取 issue 并执行后续分析。"""
        detailed_issues, _issues_stats = self.issue_collector.fetch_issues(
            repos=repos,
            snapshot_date=snapshot_date,
            max_workers=self.max_parallel_workers,
            max_issues_per_repo=self.max_issues_per_repo,
        )
        if detailed_issues:
            self.issue_dumper(detailed_issues, self.issue_dump_dir, snapshot_date)
        await self.run_issue_agent_analysis_async(snapshot_date)

    def run_issue_agent_analysis(self, snapshot_date: str) -> None:
        """同步触发 issue agent 分析。"""
        if self.enable_issue_agent_analysis is not True:
            return
        if not self.anthropic_api_key:
            logger.warning("已启用 Issue Agent 分析但未配置 ANTHROPIC_API_KEY，跳过")
            return
        try:
            asyncio.run(self.run_issue_agent_analysis_async(snapshot_date))
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"Issue Agent 分析失败，已跳过: {exc}")

    async def run_issue_agent_analysis_async(self, snapshot_date: str) -> None:
        """异步触发 issue agent 分析。"""
        if self.enable_issue_agent_analysis is not True:
            return

        input_dir = Path(self.issue_dump_dir) / snapshot_date
        if not input_dir.exists():
            logger.info("未找到 Issue 输入目录，跳过分析: %s", input_dir)
            return
        if not any(input_dir.glob("*.jsonl")):
            logger.info("Issue 输入目录为空，跳过分析: %s", input_dir)
            return

        output_dir = input_dir / "analysis"
        try:
            runner = self.runner_factory(
                model=self.issue_agent_model,
                retry_max_attempts=self.issue_agent_retry_max_attempts,
                retry_wait_seconds=self.issue_agent_retry_wait_seconds,
                max_concurrency=self.max_parallel_workers,
                review_confidence_threshold=(
                    self.issue_agent_review_confidence_threshold
                ),
                total_timeout_seconds=self.issue_agent_total_timeout_seconds,
                attempt_timeout_seconds=self.issue_agent_attempt_timeout_seconds,
            )
            result: IssueAgentBatchResult = await runner.analyze_directory(
                input_dir, output_dir
            )
            logger.info(
                "Issue Agent 分析完成: expected=%d, succeeded=%d, failed=%d, "
                "failed_samples=%s",
                result.expected_files,
                result.succeeded_files,
                result.failed_files,
                ",".join(result.failed_samples) if result.failed_samples else "-",
            )
            if result.failed_files > 0:
                logger.warning(
                    "Issue Agent 存在失败样本: failed=%d, failed_samples=%s",
                    result.failed_files,
                    ",".join(result.failed_samples) if result.failed_samples else "-",
                )
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"Issue Agent 分析失败，已跳过: {exc}")

    def load_insights(self, snapshot_date: str) -> Any:
        """读取 issue agent 分析结果。"""
        return self.issue_report_loader(self.issue_dump_dir, snapshot_date)
