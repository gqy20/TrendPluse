"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""

import asyncio
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from anthropic import Anthropic

from trendpluse.agents.issue_agent import IssueAgentRunner
from trendpluse.analyzers.breaking_changes_detector import (
    BreakingChangesDetector,
)
from trendpluse.analyzers.commit_analyzer import CommitAnalyzer
from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.analyzers.weekly_aggregator import WeeklyAggregator
from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.issues import IssueCollector
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import DEFAULT_SIGNAL_HISTORY_PATH, Settings
from trendpluse.logger import get_logger
from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleasesData,
    RepoActivity,
    ReportStats,
    Signal,
    WeeklyActivity,
    WeeklyReport,
)
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.readers.commit_material_builder import CommitMaterialBuilder
from trendpluse.readers.github_pr_reader import GitHubPRReader
from trendpluse.readers.release_material_builder import ReleaseMaterialBuilder
from trendpluse.reporters.markdown_reporter import MarkdownReporter
from trendpluse.utils.issue_agent_io import load_issue_agent_report
from trendpluse.utils.issue_io import dump_issues_to_jsonl

logger = get_logger(__name__)


class TrendPulsePipeline:
    """TrendPulse 主流程"""

    def __init__(self, settings: Settings | None = None):
        """初始化 Pipeline

        Args:
            settings: 配置对象，None 则从环境变量加载
        """
        self.settings = settings or Settings()

        # 初始化 LLM 客户端
        if self.settings.anthropic_base_url:
            llm_client = Anthropic(
                api_key=self.settings.anthropic_api_key,
                base_url=self.settings.anthropic_base_url,
            )
        else:
            llm_client = Anthropic(api_key=self.settings.anthropic_api_key)

        # 初始化组件
        self.collector = GitHubEventsCollector(token=self.settings.github_token)
        self.activity_collector = ActivityCollector(token=self.settings.github_token)
        self.release_collector = ReleaseCollector(token=self.settings.github_token)
        self.issue_collector = IssueCollector(token=self.settings.github_token)
        self.commit_analyzer = CommitAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        self.release_analyzer = ReleaseAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        self.release_summarizer = ReleaseSummarizer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        self.breaking_changes_detector = BreakingChangesDetector(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        self.filter = EventFilter(
            max_count=self.settings.max_candidates,
            enable_open_prs=self.settings.enable_open_prs,
            open_pr_min_changed_files=self.settings.open_pr_min_changed_files,
        )
        self.pr_reader = GitHubPRReader(token=self.settings.github_token)
        self.analyzer = TrendAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        # 初始化信号去重器
        self.deduplicator = SignalDeduplicator(
            llm_client=llm_client,
            lookback_days=self.settings.days_to_lookback,  # 与 PR 回溯天数一致
            history_path=DEFAULT_SIGNAL_HISTORY_PATH,
            model=self.settings.anthropic_model,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        self.reporter = MarkdownReporter()
        self.commit_material_builder = CommitMaterialBuilder()
        self.release_material_builder = ReleaseMaterialBuilder()

        # 初始化飞书通知器（如果配置了 webhook URL）
        self.notifier: FeishuNotifier | None = None
        if self.settings.feishu_webhook_url:
            self.notifier = FeishuNotifier(
                webhook_url=self.settings.feishu_webhook_url,
                at_mobiles=self.settings.feishu_at_mobiles_list,
                max_signals=self.settings.feishu_max_signals,
                secret=self.settings.feishu_secret or None,
            )

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
        (
            activity_data,
            detailed_commits,
            releases_data,
            detailed_releases,
            commit_signals,
            release_signals,
            breaking_changes,
        ) = self._collect_daily_inputs(day_ago)
        self._collect_issue_artifacts(date.strftime("%Y-%m-%d"))

        candidates = self._collect_pr_candidates(day_ago)

        if not candidates:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        pr_materials = self._read_pr_materials(candidates)
        if not pr_materials:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        signals = self.analyzer.analyze_materials(pr_materials)
        if not signals:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        pr_signals = self.deduplicator.deduplicate(signals)
        report = self.analyzer.aggregate_and_generate_report(
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
            date=date.strftime("%Y-%m-%d"),
        )
        self._finalize_daily_report(
            report=report,
            date=date,
            activity_data=activity_data,
            releases_data=releases_data,
            breaking_changes=breaking_changes,
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
            detailed_commits=detailed_commits,
            detailed_releases=detailed_releases,
        )
        return report

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
        (
            activity_data,
            detailed_commits,
            releases_data,
            detailed_releases,
            commit_signals,
            release_signals,
            breaking_changes,
        ) = await self._collect_daily_inputs_async(day_ago, date.strftime("%Y-%m-%d"))

        step_start = time.perf_counter()
        candidates = self._collect_pr_candidates(day_ago)
        logger.info(
            "Candidate collection done in %.2fs (candidates=%d)",
            time.perf_counter() - step_start,
            len(candidates),
        )

        if not candidates:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        step_start = time.perf_counter()
        pr_refs = self.pr_reader.refs_from_candidates(candidates)
        pr_materials = self.pr_reader.read_many(
            pr_refs,
            max_workers=self.settings.max_parallel_workers,
        )
        logger.info(
            "PR detail fetch done in %.2fs (prs=%d)",
            time.perf_counter() - step_start,
            len(pr_materials),
        )

        if not pr_materials:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        step_start = time.perf_counter()
        signals = await self.analyzer.analyze_materials_async(pr_materials)
        logger.info(
            "PR analysis done in %.2fs (signals=%d)",
            time.perf_counter() - step_start,
            len(signals),
        )

        if not signals:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        step_start = time.perf_counter()
        pr_signals = self.deduplicator.deduplicate(signals)
        logger.info(
            "Deduplication done in %.2fs (signals=%d)",
            time.perf_counter() - step_start,
            len(pr_signals),
        )

        step_start = time.perf_counter()
        report = await self.analyzer.aggregate_and_generate_report_async(
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
            date=date.strftime("%Y-%m-%d"),
        )
        logger.info("Aggregation done in %.2fs", time.perf_counter() - step_start)
        self._finalize_daily_report(
            report=report,
            date=date,
            activity_data=activity_data,
            releases_data=releases_data,
            breaking_changes=breaking_changes,
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
            detailed_commits=detailed_commits,
            detailed_releases=detailed_releases,
        )
        logger.info("Daily pipeline total time %.2fs", time.perf_counter() - start_time)

        return report

    def _collect_daily_inputs(
        self, day_ago: datetime
    ) -> tuple[
        ActivityData,
        list[dict[str, Any]],
        ReleasesData,
        list[dict[str, Any]],
        list[Any],
        list[Any],
        list[Any],
    ]:
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
        self._apply_release_summaries(releases_data, detailed_releases)
        commit_signals = self._analyze_commit_signals(detailed_commits)
        release_signals = self._analyze_release_signals(detailed_releases)
        breaking_changes = self._detect_breaking_changes(detailed_releases)
        return (
            activity_data,
            detailed_commits,
            releases_data,
            detailed_releases,
            commit_signals,
            release_signals,
            breaking_changes,
        )

    async def _collect_daily_inputs_async(
        self, day_ago: datetime, snapshot_date: str
    ) -> tuple[
        ActivityData,
        list[dict[str, Any]],
        ReleasesData,
        list[dict[str, Any]],
        list[Any],
        list[Any],
        list[Any],
    ]:
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
        commit_signals, release_signals, breaking_changes = (
            self._resolve_async_analysis_results(results, detailed_releases)
        )
        self._apply_release_summary_results(
            releases_data=releases_data,
            detailed_releases=detailed_releases,
            results=results,
        )
        return (
            activity_data,
            detailed_commits,
            releases_data,
            detailed_releases,
            commit_signals,
            release_signals,
            breaking_changes,
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
            release_materials = self.release_material_builder.build(detailed_releases)
            tasks["release_summaries"] = asyncio.create_task(
                self.release_summarizer.summarize_materials_async(release_materials)
            )
            tasks["release_signals"] = asyncio.create_task(
                self.release_analyzer.analyze_materials_async(release_materials)
            )
            tasks["breaking_changes"] = asyncio.create_task(
                self.breaking_changes_detector.detect_breaking_changes_async(
                    {"detailed_releases": detailed_releases}
                )
            )

        if detailed_commits:
            commit_materials = self.commit_material_builder.build(detailed_commits)
            tasks["commit_signals"] = asyncio.create_task(
                self.commit_analyzer.analyze_materials_async(commit_materials)
            )

        step_start = time.perf_counter()
        detailed_issues, _issues_stats = self.issue_collector.fetch_issues(
            repos=self.settings.github_repos,
            snapshot_date=snapshot_date,
            max_workers=self.settings.max_parallel_workers,
            max_issues_per_repo=self.settings.max_issues_per_repo,
        )
        if detailed_issues:
            dump_issues_to_jsonl(
                detailed_issues,
                self.settings.issue_dump_dir,
                snapshot_date,
            )
        await self._run_issue_agent_analysis_async(snapshot_date)
        logger.info(
            "Issue collection done in %.2fs (issues=%d)",
            time.perf_counter() - step_start,
            len(detailed_issues),
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

    def _resolve_async_analysis_results(
        self,
        results: dict[str, object],
        detailed_releases: list[dict[str, Any]],
    ) -> tuple[list[Any], list[Any], list[Any]]:
        """解析异步分析结果。"""
        commit_signals: list[Any] = []
        commit_result = results.get("commit_signals")
        if isinstance(commit_result, list):
            commit_signals = commit_result

        release_signals: list[Any] = []
        release_result = results.get("release_signals")
        if isinstance(release_result, list):
            release_signals = release_result
        if detailed_releases and not release_signals:
            logger.warning(
                "ReleaseAnalyzer(异步) 未产出信号，启用 deterministic fallback "
                "(releases=%d)",
                len(detailed_releases),
            )
            release_signals = self._build_release_fallback_signals(detailed_releases)

        breaking_changes: list[Any] = []
        breaking_result = results.get("breaking_changes")
        if isinstance(breaking_result, list):
            breaking_changes = breaking_result

        return commit_signals, release_signals, breaking_changes

    def _apply_release_summary_results(
        self,
        *,
        releases_data: ReleasesData,
        detailed_releases: list[dict[str, Any]],
        results: dict[str, object],
    ) -> None:
        """将异步 release 总结结果回填到 release 数据。"""
        summary_result = results.get("release_summaries")
        if not detailed_releases or not isinstance(summary_result, dict):
            return
        for release in releases_data.releases:
            key = f"{release.repo}@{release.version}"
            if key in summary_result:
                release.ai_summary = summary_result[key]

    def _apply_release_summaries(
        self, releases_data: ReleasesData, detailed_releases: list[dict[str, Any]]
    ) -> None:
        """为 release 数据附加 AI 总结。"""
        if not detailed_releases:
            return
        release_materials = self.release_material_builder.build(detailed_releases)
        summaries = self.release_summarizer.summarize_materials(release_materials)
        for release in releases_data.releases:
            key = f"{release.repo}@{release.version}"
            if key in summaries:
                release.ai_summary = summaries[key]

    def _analyze_commit_signals(
        self, detailed_commits: list[dict[str, Any]]
    ) -> list[Any]:
        """分析 commit 技术信号。"""
        if not detailed_commits:
            return []
        commit_materials = self.commit_material_builder.build(detailed_commits)
        return self.commit_analyzer.analyze_materials(commit_materials)

    def _analyze_release_signals(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """分析 release 信号。"""
        if not detailed_releases:
            return []
        release_materials = self.release_material_builder.build(detailed_releases)
        release_signals = self.release_analyzer.analyze_materials(release_materials)
        if release_signals:
            return release_signals
        logger.warning(
            "ReleaseAnalyzer 未产出信号，启用 deterministic fallback (releases=%d)",
            len(detailed_releases),
        )
        return self._build_release_fallback_signals(detailed_releases)

    def _detect_breaking_changes(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Any]:
        """检测 breaking changes。"""
        if not detailed_releases:
            return []
        return self.breaking_changes_detector.detect_breaking_changes(
            {"detailed_releases": detailed_releases}
        )

    def _collect_issue_artifacts(self, snapshot_date: str) -> None:
        """收集 issue 落盘与 agent 分析产物。"""
        detailed_issues, _issues_stats = self.issue_collector.fetch_issues(
            repos=self.settings.github_repos,
            snapshot_date=snapshot_date,
            max_workers=self.settings.max_parallel_workers,
            max_issues_per_repo=self.settings.max_issues_per_repo,
        )
        if detailed_issues:
            dump_issues_to_jsonl(
                detailed_issues,
                self.settings.issue_dump_dir,
                snapshot_date,
            )
        self._run_issue_agent_analysis(snapshot_date)

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

    def _finalize_daily_report(
        self,
        *,
        report: DailyReport,
        date: datetime,
        activity_data: ActivityData,
        releases_data: ReleasesData,
        breaking_changes: list[Any],
        pr_signals: list[Any],
        commit_signals: list[Any],
        release_signals: list[Any],
        detailed_commits: list[dict[str, Any]],
        detailed_releases: list[dict[str, Any]],
    ) -> None:
        """填充日报对象并保存发送。"""
        if not isinstance(report.release_signals, list) or not report.release_signals:
            report.release_signals = release_signals
        report.commit_signals = []
        report.activity = activity_data
        report.releases = releases_data
        report.breaking_changes = breaking_changes if breaking_changes else None
        report.monitored_repos = self.settings.github_repos
        report.issue_insights = load_issue_agent_report(
            self.settings.issue_dump_dir,
            date.strftime("%Y-%m-%d"),
        )
        self._finalize_report_stats(
            report=report,
            pr_signals_count=len(pr_signals),
            commit_signals_count=len(commit_signals),
            release_signals_count=len(release_signals),
            total_commits_analyzed=len(detailed_commits),
            total_releases=releases_data.total_count,
            total_releases_analyzed=len(detailed_releases),
            total_breaking_changes=len(breaking_changes),
        )
        output_path = self._get_output_path(date)
        self.reporter.save_report(report, output_path)
        self._save_report_json(report, output_path)
        self._send_notification(report)

    def _run_issue_agent_analysis(self, snapshot_date: str) -> None:
        if getattr(self.settings, "enable_issue_agent_analysis", False) is not True:
            return
        if not self.settings.anthropic_api_key:
            logger.warning("已启用 Issue Agent 分析但未配置 ANTHROPIC_API_KEY，跳过")
            return
        try:
            asyncio.run(self._run_issue_agent_analysis_async(snapshot_date))
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"Issue Agent 分析失败，已跳过: {exc}")

    async def _run_issue_agent_analysis_async(self, snapshot_date: str) -> None:
        if getattr(self.settings, "enable_issue_agent_analysis", False) is not True:
            return

        input_dir = Path(self.settings.issue_dump_dir) / snapshot_date
        if not input_dir.exists():
            return
        if not any(input_dir.glob("*.jsonl")):
            return

        output_dir = input_dir / "analysis"
        try:
            runner = IssueAgentRunner(
                model=self.settings.issue_agent_model,
                retry_max_attempts=self.settings.issue_agent_retry_max_attempts,
                retry_wait_seconds=self.settings.issue_agent_retry_wait_seconds,
            )
            result = await runner.analyze_directory(input_dir, output_dir)
            if isinstance(result, int):  # 兼容旧实现
                logger.info("Issue Agent 分析完成: files=%d", result)
            else:
                logger.info(
                    "Issue Agent 分析完成: expected=%d, succeeded=%d, failed=%d, "
                    "failed_samples=%s",
                    result.expected_files,
                    result.succeeded_files,
                    result.failed_files,
                    ",".join(result.failed_samples) if result.failed_samples else "-",
                )
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"Issue Agent 分析失败，已跳过: {exc}")

    def _generate_empty_report(
        self,
        date: datetime,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """生成空报告

        Args:
            date: 日期
            activity_data: 活跃度数据（可选）
            commit_signals: commit 信号列表（可选）
            releases_data: Release 数据（可选）
        Returns:
            空的每日报告
        """
        date_str = date.strftime("%Y-%m-%d")

        # 计算信号数量
        commit_count = len(commit_signals) if commit_signals else 0
        release_count = releases_data.total_count if releases_data else 0

        # 动态生成摘要
        if commit_count == 0 and release_count == 0:
            summary_brief = f"今日 ({date_str}) 未发现符合条件的趋势信号。"
        else:
            summary_brief = (
                f"今日 ({date_str}) 发现 {commit_count} 个 Commit 信号，"
                f"{release_count} 个 Release 信号。"
            )

        # 统计高影响信号（impact_score >= 4）
        high_impact_count = 0
        if commit_signals:
            high_impact_count = sum(
                1 for s in commit_signals if getattr(s, "impact_score", 0) >= 4
            )

        # 分类 commit_signals 到 engineering/research
        engineering_signals: list = []
        research_signals: list = []
        if commit_signals:
            for signal in commit_signals:
                if signal.category == "engineering":
                    engineering_signals.append(signal)
                elif signal.category == "research":
                    research_signals.append(signal)

        report = DailyReport(
            date=date_str,
            summary_brief=summary_brief,
            engineering_signals=engineering_signals,
            research_signals=research_signals,
            commit_signals=[],  # 清空，避免与工程/研究信号重复显示
        )

        # 添加活跃度和 release 数据（如果有）
        if activity_data:
            report.activity = activity_data
        if releases_data:
            report.releases = releases_data

        # 添加监控的仓库列表
        report.monitored_repos = self.settings.github_repos
        report.issue_insights = load_issue_agent_report(
            self.settings.issue_dump_dir,
            date.strftime("%Y-%m-%d"),
        )
        self._finalize_report_stats(
            report=report,
            pr_signals_count=0,
            commit_signals_count=commit_count,
            release_signals_count=release_count,
            total_commits_analyzed=activity_data.total_commits if activity_data else 0,
            total_releases=releases_data.total_count if releases_data else 0,
            total_releases_analyzed=releases_data.total_count if releases_data else 0,
            total_breaking_changes=0,
            override_high_impact=high_impact_count,
        )

        return report

    def _handle_empty_report(
        self,
        date: datetime,
        activity_data: ActivityData | None = None,
        commit_signals: list | None = None,
        releases_data: ReleasesData | None = None,
    ) -> DailyReport:
        """处理空报告场景

        统一处理无候选事件、无 PR 详情、无信号等情况。

        Args:
            date: 日期
            activity_data: 活跃度数据
            commit_signals: commit 信号列表
            releases_data: Release 数据
        Returns:
            保存并发送后的空报告
        """
        report = self._generate_empty_report(
            date, activity_data, commit_signals, releases_data
        )
        output_path = self._get_output_path(date)
        self.reporter.save_report(report, output_path)
        self._save_report_json(report, output_path)
        self._send_notification(report)
        return report

    def _send_notification(self, report: DailyReport) -> None:
        """发送飞书通知

        Args:
            report: 每日报告
        """
        if self.notifier:
            try:
                self.notifier.send_report(report)
            except Exception as e:
                # 通知失败不影响主流程，但记录日志以便排查
                logger.warning(f"发送飞书通知失败: {e}")

    def _get_output_path(self, date: datetime) -> str:
        """获取报告输出路径

        Args:
            date: 日期

        Returns:
            输出文件路径
        """
        # 输出到 reports/daily 子目录
        reports_dir = Path("reports/daily")
        filename = f"report-{date.strftime('%Y-%m-%d')}.md"
        return str(reports_dir / filename)

    def _save_report_json(self, report: DailyReport, output_path: str) -> None:
        """保存报告 JSON 数据

        Args:
            report: 每日报告对象
            output_path: Markdown 输出路径（用于推断 JSON 路径）
        """
        # 将 .md 替换为 .json
        json_path = str(Path(output_path).with_suffix(".json"))

        # Pydantic 模型支持 .model_dump_json() 直接序列化为 JSON
        json_data = report.model_dump_json(indent=2, ensure_ascii=False)

        Path(json_path).write_text(json_data, encoding="utf-8")

    def _build_release_fallback_signals(
        self, detailed_releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """构建 release 信号兜底结果

        当 LLM 解析失败或返回空列表时，使用确定性规则产出最基础的 release 信号，
        避免“有 release 数据但无 release 信号”的数据断层。
        """
        signals: list[Signal] = []
        for idx, release in enumerate(detailed_releases):
            repo = str(release.get("repo", "")).strip()
            tag_name = str(
                release.get("tag_name") or release.get("name") or f"unknown-{idx + 1}"
            ).strip()
            source_url = str(release.get("html_url", "")).strip()
            version_info = release.get("version_info") or {}
            major = int(version_info.get("major", 0)) if version_info else 0
            is_prerelease = bool(version_info.get("is_prerelease", False))

            impact_score = 4 if major >= 1 and not is_prerelease else 3
            title = f"{repo} 发布 {tag_name}" if repo else f"版本发布 {tag_name}"
            why_it_matters = (
                f"{repo} 发布新版本 {tag_name}，建议评估变更影响与兼容性。"
                if repo
                else f"检测到新版本 {tag_name}，建议评估变更影响与兼容性。"
            )

            signals.append(
                Signal(
                    id=f"release-fallback-{idx}",
                    title=title,
                    type="release",
                    category="engineering",
                    impact_score=impact_score,
                    why_it_matters=why_it_matters,
                    sources=[source_url] if source_url else [],
                    related_repos=[repo] if repo else [],
                )
            )
        return signals

    def _finalize_report_stats(
        self,
        report: DailyReport,
        *,
        pr_signals_count: int,
        commit_signals_count: int,
        release_signals_count: int,
        total_commits_analyzed: int,
        total_releases: int,
        total_releases_analyzed: int,
        total_breaking_changes: int,
        override_high_impact: int | None = None,
    ) -> None:
        """统一生成日报统计字段，保证跨天口径一致。"""
        engineering_signals = (
            report.engineering_signals
            if isinstance(report.engineering_signals, list)
            else []
        )
        research_signals = (
            report.research_signals if isinstance(report.research_signals, list) else []
        )
        commit_signals = (
            report.commit_signals if isinstance(report.commit_signals, list) else []
        )
        release_signals = (
            report.release_signals if isinstance(report.release_signals, list) else []
        )

        all_signals = (
            engineering_signals + research_signals + commit_signals + release_signals
        )
        unique_repos: set[str] = set()
        for signal in all_signals:
            related_repos = getattr(signal, "related_repos", [])
            if not isinstance(related_repos, list):
                continue
            for repo in related_repos:
                if isinstance(repo, str) and repo.strip():
                    unique_repos.add(repo.strip().lower())
        if report.releases:
            for release in report.releases.releases:
                if release.repo:
                    unique_repos.add(release.repo.strip().lower())

        high_impact_count = (
            override_high_impact
            if override_high_impact is not None
            else sum(
                1
                for signal in all_signals
                if isinstance(getattr(signal, "impact_score", 0), int)
                and getattr(signal, "impact_score", 0) >= 4
            )
        )

        report.stats = ReportStats(
            total_signals=pr_signals_count
            + commit_signals_count
            + release_signals_count,
            pr_count=pr_signals_count,
            commit_count=commit_signals_count,
            release_count=release_signals_count,
            unique_repos=len(unique_repos),
            total_prs_analyzed=pr_signals_count,
            total_commits_analyzed=total_commits_analyzed,
            total_releases=total_releases,
            total_releases_analyzed=total_releases_analyzed,
            high_impact_signals=high_impact_count,
            total_breaking_changes=total_breaking_changes,
        )

    def run_weekly(self, date: datetime | None = None) -> WeeklyReport:
        """运行周报生成流程

        Args:
            date: 参考日期，None 则使用今天

        Returns:
            周报
        """
        if date is None:
            date = datetime.now()

        # 计算上周的时间范围（周一到周日）
        start_date, end_date = self._get_last_week_range(date)

        # 加载上周的所有日报
        daily_reports = self._load_daily_reports(start_date, end_date)

        if not daily_reports:
            raise ValueError(
                f"没有找到 {start_date.strftime('%Y-%m-%d')} "
                f"到 {end_date.strftime('%Y-%m-%d')} 的日报数据"
            )

        # 聚合生成周报
        weekly_report = self._aggregate_weekly_report(
            daily_reports, start_date, end_date
        )

        # 保存报告
        output_path = self._get_weekly_output_path(end_date)
        self.reporter.save_weekly_report(weekly_report, output_path)
        self._save_weekly_report_json(weekly_report, output_path)

        return weekly_report

    def _get_last_week_range(self, date: datetime) -> tuple[datetime, datetime]:
        """获取上周的时间范围（周一 00:00:00 到 周日 23:59:59）

        Args:
            date: 参考日期

        Returns:
            (开始日期, 结束日期)
        """
        # 获取本周一
        weekday = date.weekday()  # 0=周一, 6=周日
        this_monday = date - timedelta(days=weekday)

        # 上周一是本周一减 7 天
        last_monday = this_monday - timedelta(days=7)

        # 上周日是本周一减 1 天
        last_sunday = this_monday - timedelta(days=1)

        # 设置时间边界
        start_date = last_monday.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = last_sunday.replace(
            hour=23, minute=59, second=59, microsecond=999999
        )

        return start_date, end_date

    def _load_daily_reports(
        self, start_date: datetime, end_date: datetime
    ) -> list[DailyReport]:
        """加载指定时间范围内的日报

        Args:
            start_date: 开始日期
            end_date: 结束日期

        Returns:
            日报列表
        """
        reports = []
        current_date = start_date

        daily_reports_dir = Path(self.settings.output_dir)

        while current_date <= end_date:
            filename = f"report-{current_date.strftime('%Y-%m-%d')}.json"
            json_path = daily_reports_dir / filename

            if json_path.exists():
                try:
                    content = json_path.read_text(encoding="utf-8")
                    report = DailyReport.model_validate_json(content)
                    reports.append(report)
                except Exception as e:
                    logger.warning(f"加载日报失败 {json_path}: {e}")

            current_date += timedelta(days=1)

        return reports

    def _aggregate_weekly_report(
        self, daily_reports: list[DailyReport], start_date: datetime, end_date: datetime
    ) -> WeeklyReport:
        """聚合日报生成周报

        使用 AI 聚合器对信号进行整合分析，识别核心技术趋势。

        Args:
            daily_reports: 日报列表
            start_date: 开始日期
            end_date: 结束日期

        Returns:
            周报
        """
        # 周标识
        week_id = WeeklyReport.get_week_id(end_date)

        # 收集所有信号（去重）
        all_signals = []
        seen_signal_ids = set()

        for report in daily_reports:
            for signal in (
                report.engineering_signals
                + report.research_signals
                + report.commit_signals
                + report.release_signals
            ):
                if signal.id not in seen_signal_ids:
                    seen_signal_ids.add(signal.id)
                    all_signals.append(signal)

        # 使用 AI 聚合器分析信号
        aggregator = WeeklyAggregator(
            api_key=self.settings.anthropic_api_key,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=self.settings.llm_retry_max_attempts,
            retry_wait_min=self.settings.llm_retry_wait_min,
            retry_wait_max=self.settings.llm_retry_wait_max,
        )
        ai_result = aggregator.aggregate(all_signals)

        # 按 impact_score 降序排序，用于显示
        engineering_signals = [s for s in all_signals if s.category == "engineering"]
        research_signals = [s for s in all_signals if s.category == "research"]

        engineering_signals.sort(key=lambda s: s.impact_score, reverse=True)
        research_signals.sort(key=lambda s: s.impact_score, reverse=True)

        # 统计数据
        total_prs = sum(r.stats.get("total_prs_analyzed", 0) for r in daily_reports)
        high_impact = sum(1 for s in all_signals if s.impact_score >= 4)
        total_commits = sum(
            r.activity.total_commits for r in daily_reports if r.activity
        )
        total_releases = sum(r.stats.get("total_releases", 0) for r in daily_reports)

        # 聚合活跃度
        weekly_activity = self._aggregate_activity(daily_reports)

        return WeeklyReport(
            week_id=week_id,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            summary_brief=ai_result.summary_brief,
            core_trends=ai_result.core_trends,
            engineering_signals=engineering_signals[:10],
            research_signals=research_signals[:10],
            daily_reports_count=len(daily_reports),
            total_prs_analyzed=total_prs,
            high_impact_signals=high_impact,
            total_commits=total_commits,
            total_releases=total_releases,
            weekly_activity=weekly_activity,
        )

    def _aggregate_activity(self, daily_reports: list[DailyReport]) -> WeeklyActivity:
        """聚合活跃度数据

        Args:
            daily_reports: 日报列表

        Returns:
            周活跃度
        """
        # 累积所有仓库的 commits
        repo_commits: dict[str, int] = {}
        repo_contributors: dict[str, set[str]] = {}

        for report in daily_reports:
            if report.activity and report.activity.top_repos:
                for repo in report.activity.top_repos:
                    if repo.repo not in repo_commits:
                        repo_commits[repo.repo] = 0
                        repo_contributors[repo.repo] = set()

                    repo_commits[repo.repo] += repo.commits

                    for contributor in repo.top_contributors:
                        repo_contributors[repo.repo].add(contributor)

        # 构建 top repos
        top_repos = [
            RepoActivity(
                repo=repo_name,
                commits=commits,
                top_contributors=list(repo_contributors[repo_name])[:3],
            )
            for repo_name, commits in sorted(
                repo_commits.items(), key=lambda x: x[1], reverse=True
            )
        ]

        return WeeklyActivity(
            total_commits=sum(repo_commits.values()),
            active_repos_count=len(repo_commits),
            top_repos=top_repos,
        )

    def _get_weekly_output_path(self, date: datetime) -> str:
        """获取周报输出路径: reports/weekly/weekly-YYYY-Www.md

        Args:
            date: 日期（用于计算周数）

        Returns:
            输出文件路径
        """
        reports_dir = Path("reports/weekly")
        week_id = WeeklyReport.get_week_id(date)
        filename = f"weekly-{week_id}.md"
        return str(reports_dir / filename)

    def _save_weekly_report_json(self, report: WeeklyReport, output_path: str) -> None:
        """保存周报 JSON 数据

        Args:
            report: 周报对象
            output_path: Markdown 输出路径（用于推断 JSON 路径）
        """
        json_path = str(Path(output_path).with_suffix(".json"))
        json_data = report.model_dump_json(indent=2, ensure_ascii=False)
        Path(json_path).write_text(json_data, encoding="utf-8")
