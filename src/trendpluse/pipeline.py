"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""

import asyncio
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from anthropic import Anthropic

from trendpluse.analyzers.breaking_changes_detector import (
    BreakingChangesDetector,
)
from trendpluse.analyzers.commit_analyzer import CommitAnalyzer
from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.commit_material_builder import CommitMaterialBuilder
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.github_pr_reader import GitHubPRReader
from trendpluse.collectors.issues import IssueCollector
from trendpluse.collectors.release_material_builder import ReleaseMaterialBuilder
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import DEFAULT_SIGNAL_HISTORY_PATH, Settings
from trendpluse.logger import get_logger
from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import (
    DailyReport,
    WeeklyReport,
)
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.workflows.daily_pipeline_inputs import DailyPipelineInputs
from trendpluse.workflows.daily_report_finalizer import DailyReportFinalizer
from trendpluse.workflows.issue_workflow import IssueWorkflowService
from trendpluse.workflows.release_workflow import ReleaseWorkflowService
from trendpluse.workflows.report_output import ReportOutputService
from trendpluse.workflows.weekly_report_workflow import WeeklyReportWorkflow

logger = get_logger(__name__)


class TrendPulsePipeline:
    """TrendPulse 主流程"""

    def __init__(self, settings: Settings | None = None):
        """初始化 Pipeline

        Args:
            settings: 配置对象，None 则从环境变量加载
        """
        self.settings = settings or Settings()
        llm_client = self._build_llm_client()
        self._build_collectors()
        self._build_analyzers(llm_client)
        self._build_output_components()
        self._build_workflows()

    def _build_llm_client(self) -> Anthropic:
        """构建通用 LLM 客户端。"""
        if self.settings.anthropic_base_url:
            return Anthropic(
                api_key=self.settings.anthropic_api_key,
                base_url=self.settings.anthropic_base_url,
            )
        return Anthropic(api_key=self.settings.anthropic_api_key)

    def _build_collectors(self) -> None:
        """初始化采集与材料装配组件。"""
        self.collector = GitHubEventsCollector(token=self.settings.github_token)
        self.activity_collector = ActivityCollector(token=self.settings.github_token)
        self.release_collector = ReleaseCollector(token=self.settings.github_token)
        self.issue_collector = IssueCollector(token=self.settings.github_token)
        self.filter = EventFilter(
            max_count=self.settings.max_candidates,
            enable_open_prs=self.settings.enable_open_prs,
            open_pr_min_changed_files=self.settings.open_pr_min_changed_files,
        )
        self.pr_reader = GitHubPRReader(token=self.settings.github_token)
        self.commit_material_builder = CommitMaterialBuilder()
        self.release_material_builder = ReleaseMaterialBuilder()

    def _build_analyzers(self, llm_client: Anthropic) -> None:
        """初始化分析组件。"""
        llm_kwargs = self._get_llm_component_kwargs()
        self.commit_analyzer = CommitAnalyzer(
            **llm_kwargs,
        )
        self.release_analyzer = ReleaseAnalyzer(
            **llm_kwargs,
        )
        self.release_summarizer = ReleaseSummarizer(
            **llm_kwargs,
        )
        self.breaking_changes_detector = BreakingChangesDetector(
            **llm_kwargs,
        )
        self.analyzer = TrendAnalyzer(
            **llm_kwargs,
        )
        self.deduplicator = SignalDeduplicator(
            llm_client=llm_client,
            lookback_days=self.settings.days_to_lookback,
            history_path=DEFAULT_SIGNAL_HISTORY_PATH,
            model=self.settings.anthropic_model,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )

    def _build_output_components(self) -> None:
        """初始化输出与通知组件。"""
        self.reporter = MarkdownReporter()
        self.notifier: FeishuNotifier | None = None
        configured_output_dir = getattr(self.settings, "output_dir", None)
        daily_output_dir = (
            configured_output_dir
            if isinstance(configured_output_dir, str) and configured_output_dir
            else "reports/daily"
        )
        if self.settings.feishu_webhook_url:
            self.notifier = FeishuNotifier(
                webhook_url=self.settings.feishu_webhook_url,
                at_mobiles=self.settings.feishu_at_mobiles_list,
                max_signals=self.settings.feishu_max_signals,
                secret=self.settings.feishu_secret or None,
            )
        self.output_service = ReportOutputService(
            reporter=self.reporter,
            daily_output_dir=daily_output_dir,
            weekly_output_dir="reports/weekly",
            notifier=self.notifier,
        )

    def _build_workflows(self) -> None:
        """初始化业务工作流。"""
        self.issue_workflow = IssueWorkflowService(
            issue_collector=self.issue_collector,
            issue_dump_dir=self.settings.issue_dump_dir,
            enable_issue_agent_analysis=self.settings.enable_issue_agent_analysis,
            anthropic_api_key=self.settings.anthropic_api_key,
            max_parallel_workers=self.settings.max_parallel_workers,
            max_issues_per_repo=self.settings.max_issues_per_repo,
            issue_agent_model=self.settings.issue_agent_model,
            issue_agent_retry_max_attempts=self.settings.issue_agent_retry_max_attempts,
            issue_agent_retry_wait_seconds=self.settings.issue_agent_retry_wait_seconds,
        )
        self.release_workflow = ReleaseWorkflowService(
            release_material_builder=self.release_material_builder,
            release_summarizer=self.release_summarizer,
            release_analyzer=self.release_analyzer,
            breaking_changes_detector=self.breaking_changes_detector,
        )
        self.weekly_report_workflow = WeeklyReportWorkflow(
            settings=self.settings,
            output_service=self.output_service,
        )
        self.daily_report_finalizer = DailyReportFinalizer(
            settings=self.settings,
            issue_workflow=self.issue_workflow,
            output_service=self.output_service,
        )

    def _get_llm_component_kwargs(self) -> dict[str, Any]:
        """返回 LLM 组件共用初始化参数。"""
        return {
            "api_key": self.settings.anthropic_api_key,
            "model": self.settings.anthropic_model,
            "base_url": self.settings.anthropic_base_url,
            "retry_max_attempts": self.settings.llm_retry_max_attempts,
            "retry_wait_min": self.settings.llm_retry_wait_min,
            "retry_wait_max": self.settings.llm_retry_wait_max,
        }

    def run_daily(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程

        Args:
            date: 分析日期，None 则使用今天

        Returns:
            每日报告
        """
        if date is None:
            date = datetime.now()

        day_ago = date - timedelta(days=1)
        daily_inputs = self._collect_daily_inputs(day_ago)
        self._collect_issue_artifacts(date.strftime("%Y-%m-%d"))

        pr_signals = self._collect_pr_signals(day_ago)
        if not pr_signals:
            return self.daily_report_finalizer.handle_empty_report(
                date=date,
                activity_data=daily_inputs.activity_data,
                commit_signals=daily_inputs.commit_signals,
                releases_data=daily_inputs.releases_data,
            )

        return self._build_daily_report(
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )

    async def run_daily_async(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程（异步）

        Args:
            date: 分析日期，None 则使用今天

        Returns:
            每日报告
        """
        start_time = time.perf_counter()

        if date is None:
            date = datetime.now()

        day_ago = date - timedelta(days=1)
        daily_inputs = await self._collect_daily_inputs_async(
            day_ago, date.strftime("%Y-%m-%d")
        )

        pr_signals = await self._collect_pr_signals_async(day_ago)
        if not pr_signals:
            return self.daily_report_finalizer.handle_empty_report(
                date=date,
                activity_data=daily_inputs.activity_data,
                commit_signals=daily_inputs.commit_signals,
                releases_data=daily_inputs.releases_data,
            )

        report = await self._build_daily_report_async(
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        logger.info("Daily pipeline total time %.2fs", time.perf_counter() - start_time)

        return report

    def _collect_daily_inputs(self, day_ago: datetime) -> DailyPipelineInputs:
        """同步收集日报所需的基础输入。"""
        activity_data, detailed_commits = (
            self.activity_collector.collect_activity_graphql(
                repos=self.settings.github_repos,
                since=day_ago,
                max_workers=self.settings.max_parallel_workers,
            )
        )
        releases_data, detailed_releases = self.release_collector.collect_releases(
            repos=self.settings.github_repos,
            since=day_ago,
            include_prereleases=self.settings.include_prereleases,
            max_workers=self.settings.max_parallel_workers,
        )
        release_result = self.release_workflow.run(releases_data, detailed_releases)
        commit_signals = self._analyze_commit_signals(detailed_commits)
        return DailyPipelineInputs(
            activity_data,
            detailed_commits,
            release_result.releases_data,
            release_result.detailed_releases,
            commit_signals,
            release_result.release_signals,
            release_result.breaking_changes,
        )

    async def _collect_daily_inputs_async(
        self, day_ago: datetime, snapshot_date: str
    ) -> DailyPipelineInputs:
        """异步收集日报所需的基础输入。"""
        step_start = time.perf_counter()
        activity_data, detailed_commits = (
            self.activity_collector.collect_activity_graphql(
                repos=self.settings.github_repos,
                since=day_ago,
                max_workers=self.settings.max_parallel_workers,
            )
        )
        logger.info(
            "Activity collection done in %.2fs (commits=%d)",
            time.perf_counter() - step_start,
            len(detailed_commits),
        )

        step_start = time.perf_counter()
        releases_data, detailed_releases = self.release_collector.collect_releases(
            repos=self.settings.github_repos,
            since=day_ago,
            include_prereleases=self.settings.include_prereleases,
            max_workers=self.settings.max_parallel_workers,
        )
        logger.info(
            "Release collection done in %.2fs (releases=%d)",
            time.perf_counter() - step_start,
            len(detailed_releases),
        )

        results = await self._run_async_analysis_tasks(
            detailed_commits=detailed_commits,
            detailed_releases=detailed_releases,
            snapshot_date=snapshot_date,
        )
        release_result = await self.release_workflow.run_async(
            releases_data, detailed_releases
        )
        commit_signals = self._resolve_async_commit_signals(results)
        return DailyPipelineInputs(
            activity_data,
            detailed_commits,
            release_result.releases_data,
            release_result.detailed_releases,
            commit_signals,
            release_result.release_signals,
            release_result.breaking_changes,
        )

    async def _run_async_analysis_tasks(
        self,
        *,
        detailed_commits: list[dict[str, Any]],
        detailed_releases: list[dict[str, Any]],
        snapshot_date: str,
    ) -> dict[str, object]:
        """运行异步分析任务并返回结果映射。"""
        tasks: dict[str, asyncio.Task[Any]] = {}

        if detailed_releases:
            # release 分析改由 release_workflow 统一编排
            pass

        if detailed_commits:
            commit_materials = self.commit_material_builder.build(detailed_commits)
            tasks["commit_signals"] = asyncio.create_task(
                self.commit_analyzer.analyze_materials_async(commit_materials)
            )

        step_start = time.perf_counter()
        await self.issue_workflow.collect_and_analyze_async(
            self.settings.github_repos,
            snapshot_date,
        )
        logger.info(
            "Issue workflow done in %.2fs",
            time.perf_counter() - step_start,
        )

        if not tasks:
            return {}

        task_names = list(tasks.keys())
        async_start = time.perf_counter()
        task_results = await asyncio.gather(*tasks.values(), return_exceptions=True)
        logger.info(
            "Async analysis done in %.2fs (tasks=%d)",
            time.perf_counter() - async_start,
            len(task_names),
        )
        return dict(zip(task_names, task_results))

    def _resolve_async_commit_signals(self, results: dict[str, object]) -> list[Any]:
        """解析异步 commit 分析结果。"""
        commit_signals: list[Any] = []
        commit_result = results.get("commit_signals")
        if isinstance(commit_result, list):
            commit_signals = commit_result
        return commit_signals

    def _analyze_commit_signals(
        self, detailed_commits: list[dict[str, Any]]
    ) -> list[Any]:
        """分析 commit 技术信号。"""
        if not detailed_commits:
            return []
        commit_materials = self.commit_material_builder.build(detailed_commits)
        return self.commit_analyzer.analyze_materials(commit_materials)

    def _collect_pr_signals(self, day_ago: datetime) -> list[Any]:
        """同步收集并分析 PR 信号。"""
        candidates = self._collect_pr_candidates(day_ago)
        if not candidates:
            return []

        pr_materials = self._read_pr_materials(candidates)
        if not pr_materials:
            return []

        signals = self.analyzer.analyze_materials(pr_materials)
        if not signals:
            return []

        return self.deduplicator.deduplicate(signals)

    async def _collect_pr_signals_async(self, day_ago: datetime) -> list[Any]:
        """异步收集并分析 PR 信号。"""
        step_start = time.perf_counter()
        candidates = self._collect_pr_candidates(day_ago)
        logger.info(
            "Candidate collection done in %.2fs (candidates=%d)",
            time.perf_counter() - step_start,
            len(candidates),
        )
        if not candidates:
            return []

        step_start = time.perf_counter()
        pr_materials = self._read_pr_materials(candidates)
        logger.info(
            "PR detail fetch done in %.2fs (prs=%d)",
            time.perf_counter() - step_start,
            len(pr_materials),
        )
        if not pr_materials:
            return []

        step_start = time.perf_counter()
        signals = await self.analyzer.analyze_materials_async(pr_materials)
        logger.info(
            "PR analysis done in %.2fs (signals=%d)",
            time.perf_counter() - step_start,
            len(signals),
        )
        if not signals:
            return []

        step_start = time.perf_counter()
        pr_signals = self.deduplicator.deduplicate(signals)
        logger.info(
            "Deduplication done in %.2fs (signals=%d)",
            time.perf_counter() - step_start,
            len(pr_signals),
        )
        return pr_signals

    def _collect_issue_artifacts(self, snapshot_date: str) -> None:
        """收集 issue 落盘与 agent 分析产物。"""
        self.issue_workflow.collect_and_analyze(
            self.settings.github_repos,
            snapshot_date,
        )

    def _collect_pr_candidates(self, day_ago: datetime) -> list[dict[str, Any]]:
        """收集并筛选 PR 候选事件。"""
        events = self.collector.fetch_events(
            repos=self.settings.github_repos,
            since=day_ago,
            max_workers=self.settings.max_parallel_workers,
        )
        return self.filter.filter_candidates(events)

    def _read_pr_materials(self, candidates: list[dict[str, Any]]) -> list[Any]:
        """读取 PR 分析材料。"""
        pr_refs = self.pr_reader.refs_from_candidates(candidates)
        return self.pr_reader.read_many(
            pr_refs,
            max_workers=self.settings.max_parallel_workers,
        )

    def _build_daily_report(
        self,
        *,
        date: datetime,
        daily_inputs: DailyPipelineInputs,
        pr_signals: list[Any],
    ) -> DailyReport:
        """同步聚合并完成日报收尾。"""
        report = self.analyzer.aggregate_and_generate_report(
            pr_signals=pr_signals,
            commit_signals=daily_inputs.commit_signals,
            release_signals=daily_inputs.release_signals,
            date=date.strftime("%Y-%m-%d"),
        )
        self.daily_report_finalizer.finalize_daily_report(
            report=report,
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        return report

    async def _build_daily_report_async(
        self,
        *,
        date: datetime,
        daily_inputs: DailyPipelineInputs,
        pr_signals: list[Any],
    ) -> DailyReport:
        """异步聚合并完成日报收尾。"""
        step_start = time.perf_counter()
        report = await self.analyzer.aggregate_and_generate_report_async(
            pr_signals=pr_signals,
            commit_signals=daily_inputs.commit_signals,
            release_signals=daily_inputs.release_signals,
            date=date.strftime("%Y-%m-%d"),
        )
        logger.info("Aggregation done in %.2fs", time.perf_counter() - step_start)
        self.daily_report_finalizer.finalize_daily_report(
            report=report,
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        return report

    def _run_issue_agent_analysis(self, snapshot_date: str) -> None:
        self.issue_workflow.run_issue_agent_analysis(snapshot_date)

    def _get_output_path(self, date: datetime) -> str:
        """获取报告输出路径

        Args:
            date: 日期

        Returns:
            输出文件路径
        """
        reports_dir = Path(self.settings.output_dir)
        filename = f"report-{date.strftime('%Y-%m-%d')}.md"
        return str(reports_dir / filename)

    def run_weekly(self, date: datetime | None = None) -> WeeklyReport:
        """运行周报生成流程。"""
        return self.weekly_report_workflow.run(date)
