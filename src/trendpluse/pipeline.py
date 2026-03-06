"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""

from datetime import datetime
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
from trendpluse.app.bootstrap import build_reporting_components
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
from trendpluse.config import DEFAULT_SIGNAL_HISTORY_PATH, Settings
from trendpluse.logger import get_logger
from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import (
    DailyReport,
    WeeklyReport,
)
from trendpluse.notifiers.feishu import FeishuNotifier

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
        components = build_reporting_components(
            settings=self.settings,
            issue_insights_loader=lambda _date: None,
            reporter_factory=MarkdownReporter,
            notifier_factory=FeishuNotifier,
        )
        self.reporter = components.reporter
        self.notifier = components.notifier
        self.output_service = components.publisher
        self.daily_report_builder = components.builder

    def _build_workflows(self) -> None:
        """初始化业务工作流。"""
        self.issue_workflow = IssueWorkflowCoordinator(
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
        self.release_workflow = ReleaseProcessor(
            release_material_builder=self.release_material_builder,
            release_summarizer=self.release_summarizer,
            release_analyzer=self.release_analyzer,
            breaking_changes_detector=self.breaking_changes_detector,
        )
        self.weekly_app = WeeklyPipelineApp(
            settings=self.settings,
            output_service=self.output_service,
        )
        self.daily_report_finalizer = DailyReportFinalizer(
            builder=self.daily_report_builder,
            publisher=self.output_service,
        )
        self.daily_app = DailyPipelineApp(
            settings=self.settings,
            activity_collector=self.activity_collector,
            release_collector=self.release_collector,
            issue_workflow=self.issue_workflow,
            release_workflow=self.release_workflow,
            commit_material_builder=self.commit_material_builder,
            commit_analyzer=self.commit_analyzer,
            collector=self.collector,
            event_filter=self.filter,
            pr_reader=self.pr_reader,
            analyzer=self.analyzer,
            deduplicator=self.deduplicator,
            daily_report_finalizer=self.daily_report_finalizer,
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
        return self.daily_app.run_daily(date)

    async def run_daily_async(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程（异步）

        Args:
            date: 分析日期，None 则使用今天

        Returns:
            每日报告
        """
        return await self.daily_app.run_daily_async(date)

    def _run_issue_agent_analysis(self, snapshot_date: str) -> None:
        daily_app = getattr(self, "daily_app", None)
        if daily_app is not None:
            daily_app.run_issue_agent_analysis(snapshot_date)
            return
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
        return self.weekly_app.run(date)
