"""应用依赖装配。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from anthropic import Anthropic

from trendpluse.analyzers.breaking_changes_detector import BreakingChangesDetector
from trendpluse.analyzers.daily_summary_agent import DailySummaryAgent
from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.sdk_commit_analyzer import SDKCommitAnalyzer
from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.app.daily import DailyPipelineApp
from trendpluse.app.issue_agent import IssueWorkflowCoordinator
from trendpluse.app.release_processor import ReleaseProcessor
from trendpluse.app.report_finalizer import DailyReportFinalizer
from trendpluse.app.weekly import WeeklyPipelineApp
from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.commit_material_builder import CommitMaterialBuilder
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.github_pr_reader import GitHubPRReader
from trendpluse.collectors.issues import IssueCollector
from trendpluse.collectors.release_material_builder import ReleaseMaterialBuilder
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import DEFAULT_SIGNAL_HISTORY_PATH
from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.reports.builder import DailyReportBuilder
from trendpluse.reports.publisher import ReportPublisher


@dataclass(frozen=True)
class CollectorComponents:
    """采集与材料装配组件集合。"""

    collector: Any
    activity_collector: Any
    release_collector: Any
    issue_collector: Any
    event_filter: Any
    pr_reader: Any
    commit_material_builder: Any
    release_material_builder: Any


@dataclass(frozen=True)
class AnalyzerComponents:
    """分析组件集合。"""

    commit_analyzer: Any
    release_analyzer: Any
    release_summarizer: Any
    breaking_changes_detector: Any
    analyzer: Any
    deduplicator: Any


@dataclass(frozen=True)
class ReportingComponents:
    """报告相关组件集合。"""

    reporter: MarkdownReporter
    notifier: FeishuNotifier | None
    builder: DailyReportBuilder
    publisher: ReportPublisher


@dataclass(frozen=True)
class AppComponents:
    """主流程编排组件集合。"""

    issue_workflow: IssueWorkflowCoordinator
    daily_report_finalizer: DailyReportFinalizer
    daily_app: DailyPipelineApp
    weekly_app: WeeklyPipelineApp


def build_collector_components(
    *,
    settings: Any,
    github_events_collector_factory=GitHubEventsCollector,
    activity_collector_factory=ActivityCollector,
    release_collector_factory=ReleaseCollector,
    issue_collector_factory=IssueCollector,
    event_filter_factory=EventFilter,
    pr_reader_factory=GitHubPRReader,
    commit_material_builder_factory=CommitMaterialBuilder,
    release_material_builder_factory=ReleaseMaterialBuilder,
) -> CollectorComponents:
    """构建采集与材料装配组件。"""
    return CollectorComponents(
        collector=github_events_collector_factory(token=settings.github_token),
        activity_collector=activity_collector_factory(token=settings.github_token),
        release_collector=release_collector_factory(token=settings.github_token),
        issue_collector=issue_collector_factory(token=settings.github_token),
        event_filter=event_filter_factory(
            max_count=settings.max_candidates,
            enable_open_prs=settings.enable_open_prs,
            open_pr_min_changed_files=settings.open_pr_min_changed_files,
        ),
        pr_reader=pr_reader_factory(token=settings.github_token),
        commit_material_builder=commit_material_builder_factory(),
        release_material_builder=release_material_builder_factory(),
    )


def build_analyzer_components(
    *,
    settings: Any,
    llm_client: Anthropic,
    commit_analyzer_factory=SDKCommitAnalyzer,
    release_analyzer_factory=ReleaseAnalyzer,
    release_summarizer_factory=ReleaseSummarizer,
    breaking_changes_detector_factory=BreakingChangesDetector,
    trend_analyzer_factory=TrendAnalyzer,
    signal_deduplicator_factory=SignalDeduplicator,
) -> AnalyzerComponents:
    """构建分析组件。"""
    llm_kwargs = {
        "api_key": settings.anthropic_api_key,
        "model": settings.anthropic_model,
        "base_url": settings.anthropic_base_url,
        "retry_max_attempts": settings.llm_retry_max_attempts,
        "retry_wait_min": settings.llm_retry_wait_min,
        "retry_wait_max": settings.llm_retry_wait_max,
    }
    return AnalyzerComponents(
        commit_analyzer=commit_analyzer_factory(
            model=settings.anthropic_model,
            max_turns=30,
            max_budget_usd=3.0,
            batch_size=200,
        ),
        release_analyzer=release_analyzer_factory(**llm_kwargs),
        release_summarizer=release_summarizer_factory(**llm_kwargs),
        breaking_changes_detector=breaking_changes_detector_factory(**llm_kwargs),
        analyzer=trend_analyzer_factory(**llm_kwargs),
        deduplicator=signal_deduplicator_factory(
            llm_client=llm_client,
            lookback_days=settings.days_to_lookback,
            history_path=DEFAULT_SIGNAL_HISTORY_PATH,
            model=settings.anthropic_model,
            retry_max_attempts=settings.llm_retry_max_attempts,
            retry_wait_min=settings.llm_retry_wait_min,
            retry_wait_max=settings.llm_retry_wait_max,
        ),
    )


def build_reporting_components(
    *,
    settings: Any,
    issue_insights_loader,
    reporter_factory=MarkdownReporter,
    notifier_factory=FeishuNotifier,
) -> ReportingComponents:
    """构建报告相关组件。"""
    reporter = reporter_factory()
    notifier: FeishuNotifier | None = None
    configured_output_dir = getattr(settings, "output_dir", None)
    daily_output_dir = (
        configured_output_dir
        if isinstance(configured_output_dir, str) and configured_output_dir
        else "reports/daily"
    )
    if settings.feishu_webhook_url:
        notifier = notifier_factory(
            webhook_url=settings.feishu_webhook_url,
            at_mobiles=settings.feishu_at_mobiles_list,
            max_signals=settings.feishu_max_signals,
            secret=settings.feishu_secret or None,
        )

    builder = DailyReportBuilder(
        settings=settings,
        issue_insights_loader=issue_insights_loader,
    )
    publisher = ReportPublisher(
        reporter=reporter,
        daily_output_dir=daily_output_dir,
        weekly_output_dir="reports/weekly",
        notifier=notifier,
    )
    return ReportingComponents(
        reporter=reporter,
        notifier=notifier,
        builder=builder,
        publisher=publisher,
    )


def build_app_components(
    *,
    settings: Any,
    collectors: CollectorComponents,
    analyzers: AnalyzerComponents,
    reporting: ReportingComponents,
) -> AppComponents:
    """构建 daily/weekly 编排组件。"""
    issue_workflow = IssueWorkflowCoordinator(
        issue_collector=collectors.issue_collector,
        issue_dump_dir=settings.issue_dump_dir,
        enable_issue_agent_analysis=settings.enable_issue_agent_analysis,
        anthropic_api_key=settings.anthropic_api_key,
        max_parallel_workers=settings.max_parallel_workers,
        max_issues_per_repo=settings.max_issues_per_repo,
        issue_agent_model=settings.issue_agent_model,
        issue_agent_retry_max_attempts=settings.issue_agent_retry_max_attempts,
        issue_agent_retry_wait_seconds=settings.issue_agent_retry_wait_seconds,
        issue_agent_review_confidence_threshold=(
            settings.issue_agent_review_confidence_threshold
        ),
        issue_agent_total_timeout_seconds=settings.issue_agent_total_timeout_seconds,
        issue_agent_max_turns=settings.issue_agent_max_turns,
        issue_agent_max_budget_usd=settings.issue_agent_max_budget_usd,
    )
    release_workflow = ReleaseProcessor(
        release_material_builder=collectors.release_material_builder,
        release_summarizer=analyzers.release_summarizer,
        release_analyzer=analyzers.release_analyzer,
        breaking_changes_detector=analyzers.breaking_changes_detector,
    )
    daily_report_finalizer = DailyReportFinalizer(
        builder=reporting.builder,
        publisher=reporting.publisher,
        summary_enhancer=(
            DailySummaryAgent(
                reports_dir=getattr(settings, "output_dir", "reports/daily"),
                history_index_path=getattr(
                    settings,
                    "daily_history_index_path",
                    "data/history/daily-report-index.json",
                ),
                model=getattr(settings, "daily_summary_agent_model", None),
                max_turns=getattr(settings, "daily_summary_agent_max_turns", 20),
                max_budget_usd=getattr(
                    settings,
                    "daily_summary_agent_max_budget_usd",
                    5.0,
                ),
                retry_max_attempts=getattr(
                    settings,
                    "daily_summary_agent_retry_max_attempts",
                    2,
                ),
                retry_wait_seconds=getattr(
                    settings,
                    "daily_summary_agent_retry_wait_seconds",
                    0.0,
                ),
            )
            if getattr(settings, "enable_daily_summary_agent", False) is True
            and bool(settings.anthropic_api_key)
            else None
        ),
    )
    return AppComponents(
        issue_workflow=issue_workflow,
        daily_report_finalizer=daily_report_finalizer,
        daily_app=DailyPipelineApp(
            settings=settings,
            activity_collector=collectors.activity_collector,
            release_collector=collectors.release_collector,
            issue_workflow=issue_workflow,
            release_workflow=release_workflow,
            commit_material_builder=collectors.commit_material_builder,
            commit_analyzer=analyzers.commit_analyzer,
            collector=collectors.collector,
            event_filter=collectors.event_filter,
            pr_reader=collectors.pr_reader,
            analyzer=analyzers.analyzer,
            deduplicator=analyzers.deduplicator,
            daily_report_finalizer=daily_report_finalizer,
        ),
        weekly_app=WeeklyPipelineApp(
            settings=settings,
            output_service=reporting.publisher,
        ),
    )
