"""TrendPulse 主流程。"""

from __future__ import annotations

from datetime import datetime

from anthropic import Anthropic

from trendpluse.analyzers.breaking_changes_detector import BreakingChangesDetector
from trendpluse.analyzers.commit_analyzer import CommitAnalyzer
from trendpluse.analyzers.release_analyzer import ReleaseAnalyzer
from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.app.bootstrap import (
    AppComponents,
    build_analyzer_components,
    build_app_components,
    build_collector_components,
    build_reporting_components,
)
from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.commit_material_builder import CommitMaterialBuilder
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.github_pr_reader import GitHubPRReader
from trendpluse.collectors.issues import IssueCollector
from trendpluse.collectors.release_material_builder import ReleaseMaterialBuilder
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import Settings
from trendpluse.issue_signal_aggregator import IssueGlobalSummarizer
from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import DailyReport, WeeklyReport
from trendpluse.notifiers.feishu import FeishuNotifier


class TrendPulsePipeline:
    """TrendPulse 主流程。"""

    def __init__(self, settings: Settings | None = None):
        """初始化 Pipeline。"""
        self.settings = settings or Settings()
        llm_client = self._build_llm_client()
        collectors = build_collector_components(
            settings=self.settings,
            github_events_collector_factory=GitHubEventsCollector,
            activity_collector_factory=ActivityCollector,
            release_collector_factory=ReleaseCollector,
            issue_collector_factory=IssueCollector,
            event_filter_factory=EventFilter,
            pr_reader_factory=GitHubPRReader,
            commit_material_builder_factory=CommitMaterialBuilder,
            release_material_builder_factory=ReleaseMaterialBuilder,
        )
        analyzers = build_analyzer_components(
            settings=self.settings,
            llm_client=llm_client,
            commit_analyzer_factory=CommitAnalyzer,
            release_analyzer_factory=ReleaseAnalyzer,
            release_summarizer_factory=ReleaseSummarizer,
            breaking_changes_detector_factory=BreakingChangesDetector,
            trend_analyzer_factory=TrendAnalyzer,
            signal_deduplicator_factory=SignalDeduplicator,
        )
        reporting = build_reporting_components(
            settings=self.settings,
            issue_insights_loader=lambda _date: None,
            reporter_factory=MarkdownReporter,
            notifier_factory=FeishuNotifier,
        )
        apps: AppComponents = build_app_components(
            settings=self.settings,
            collectors=collectors,
            analyzers=analyzers,
            reporting=reporting,
        )
        issue_global_summarizer = IssueGlobalSummarizer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
            retry_max_attempts=getattr(self.settings, "llm_retry_max_attempts", 3),
            retry_wait_min=getattr(self.settings, "llm_retry_wait_min", 1),
            retry_wait_max=getattr(self.settings, "llm_retry_wait_max", 10),
        )
        reporting.builder.issue_insights_loader = lambda date: (
            issue_global_summarizer.summarize(apps.issue_workflow.load_insights(date))
        )
        self.daily_app = apps.daily_app
        self.weekly_app = apps.weekly_app

    def _build_llm_client(self) -> Anthropic:
        """构建通用 LLM 客户端。"""
        if self.settings.anthropic_base_url:
            return Anthropic(
                api_key=self.settings.anthropic_api_key,
                base_url=self.settings.anthropic_base_url,
            )
        return Anthropic(api_key=self.settings.anthropic_api_key)

    def run_daily(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程。"""
        return self.daily_app.run_daily(date)

    async def run_daily_async(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程（异步）。"""
        return await self.daily_app.run_daily_async(date)

    def run_weekly(self, date: datetime | None = None) -> WeeklyReport:
        """运行周报生成流程。"""
        return self.weekly_app.run(date)
