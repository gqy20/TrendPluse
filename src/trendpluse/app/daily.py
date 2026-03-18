"""Daily 用例编排。"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime, timedelta
from typing import Any, cast

from trendpluse.logger import get_logger
from trendpluse.models.report_inputs import DailyPipelineInputs
from trendpluse.models.signal import DailyReport

logger = get_logger(__name__)


class DailyPipelineApp:
    """封装日报主流程编排。"""

    def __init__(
        self,
        *,
        settings,
        activity_collector,
        release_collector,
        issue_workflow,
        release_workflow,
        commit_material_builder,
        commit_analyzer,
        collector,
        event_filter,
        pr_reader,
        analyzer,
        deduplicator,
        daily_report_finalizer,
    ) -> None:
        self.settings = settings
        self.activity_collector = activity_collector
        self.release_collector = release_collector
        self.issue_workflow = issue_workflow
        self.release_workflow = release_workflow
        self.commit_material_builder = commit_material_builder
        self.commit_analyzer = commit_analyzer
        self.collector = collector
        self.filter = event_filter
        self.pr_reader = pr_reader
        self.analyzer = analyzer
        self.deduplicator = deduplicator
        self.daily_report_finalizer = daily_report_finalizer

    def run_daily(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程。"""
        if date is None:
            date = datetime.now()

        day_ago = date - timedelta(days=1)
        daily_inputs = self._collect_daily_inputs(day_ago)
        self._collect_issue_artifacts(date.strftime("%Y-%m-%d"))

        pr_signals = self._collect_pr_signals(day_ago)
        if not pr_signals:
            return cast(
                DailyReport,
                self.daily_report_finalizer.handle_empty_report(
                    date=date,
                    activity_data=daily_inputs.activity_data,
                    commit_signals=daily_inputs.commit_signals,
                    releases_data=daily_inputs.releases_data,
                ),
            )

        return self._build_daily_report(
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )

    async def run_daily_async(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程（异步）。"""
        start_time = time.perf_counter()

        if date is None:
            date = datetime.now()

        day_ago = date - timedelta(days=1)
        daily_inputs = await self._collect_daily_inputs_async(
            day_ago, date.strftime("%Y-%m-%d")
        )

        pr_signals = await self._collect_pr_signals_async(day_ago)
        if not pr_signals:
            return cast(
                DailyReport,
                self.daily_report_finalizer.handle_empty_report(
                    date=date,
                    activity_data=daily_inputs.activity_data,
                    commit_signals=daily_inputs.commit_signals,
                    releases_data=daily_inputs.releases_data,
                ),
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
        return cast(list[Any], self.commit_analyzer.analyze_materials(commit_materials))

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

        return cast(list[Any], self.deduplicator.deduplicate(signals))

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
        return cast(list[Any], pr_signals)

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
        return cast(list[dict[str, Any]], self.filter.filter_candidates(events))

    def _read_pr_materials(self, candidates: list[dict[str, Any]]) -> list[Any]:
        """读取 PR 分析材料。"""
        pr_refs = self.pr_reader.refs_from_candidates(candidates)
        return cast(
            list[Any],
            self.pr_reader.read_many(
                pr_refs,
                max_workers=self.settings.max_parallel_workers,
            ),
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
        return cast(DailyReport, report)

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
        await self.daily_report_finalizer.finalize_daily_report_async(
            report=report,
            date=date,
            daily_inputs=daily_inputs,
            pr_signals=pr_signals,
        )
        return cast(DailyReport, report)

    def run_issue_agent_analysis(self, snapshot_date: str) -> None:
        """兼容旧入口的 Issue Agent 分析。"""
        self.issue_workflow.run_issue_agent_analysis(snapshot_date)
