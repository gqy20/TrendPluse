"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""

from datetime import datetime
from pathlib import Path

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_api import GitHubDetailFetcher
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.config import Settings
from trendpluse.models.signal import DailyReport
from trendpluse.reporters.markdown_reporter import MarkdownReporter


class TrendPulsePipeline:
    """TrendPulse 主流程"""

    def __init__(self, settings: Settings | None = None):
        """初始化 Pipeline

        Args:
            settings: 配置对象，None 则从环境变量加载
        """
        self.settings = settings or Settings()

        # 初始化组件
        self.collector = GitHubEventsCollector(token=self.settings.github_token)
        self.activity_collector = ActivityCollector(token=self.settings.github_token)
        self.filter = EventFilter(max_count=self.settings.max_candidates)
        self.fetcher = GitHubDetailFetcher(token=self.settings.github_token)
        self.analyzer = TrendAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        self.reporter = MarkdownReporter()

    def run_daily(self, date: datetime | None = None) -> DailyReport:
        """运行每日分析流程

        Args:
            date: 分析日期，None 则使用今天

        Returns:
            每日报告
        """
        if date is None:
            date = datetime.now()

        # 0. 收集仓库活跃度数据（独立于 PR 分析）
        activity_data = self.activity_collector.collect_activity(
            repos=self.settings.github_repos,
            since=date,
        )

        # 1. 从 GH Archive 获取事件
        events = self.collector.fetch_events(
            repos=self.settings.github_repos,
            since=date,
        )

        # 2. 筛选候选事件
        candidates = self.filter.filter_candidates(events)

        # 如果没有候选事件，返回带活跃度的空报告
        if not candidates:
            report = self._generate_empty_report(date, activity_data)
            # 保存空报告（包含活跃度数据）
            output_path = self._get_output_path(date)
            self.reporter.save_report(report, output_path)
            return report

        # 3. 获取详细信息
        pr_details = self.fetcher.fetch_multiple_pr_details(candidates)

        if not pr_details:
            report = self._generate_empty_report(date, activity_data)
            # 保存空报告（包含活跃度数据）
            output_path = self._get_output_path(date)
            self.reporter.save_report(report, output_path)
            return report

        # 4. AI 分析提取信号
        signals = self.analyzer.analyze_prs(pr_details)

        if not signals:
            report = self._generate_empty_report(date, activity_data)
            # 保存空报告（包含活跃度数据）
            output_path = self._get_output_path(date)
            self.reporter.save_report(report, output_path)
            return report

        # 5. 生成每日报告
        report = self.analyzer.generate_report(signals, date=date.strftime("%Y-%m-%d"))

        # 6. 添加活跃度数据
        report.activity = activity_data

        # 7. 保存报告
        output_path = self._get_output_path(date)
        self.reporter.save_report(report, output_path)

        return report

    def _generate_empty_report(
        self, date: datetime, activity_data: dict | None = None
    ) -> DailyReport:
        """生成空报告

        Args:
            date: 日期
            activity_data: 活跃度数据（可选）

        Returns:
            空的每日报告
        """
        date_str = date.strftime("%Y-%m-%d")
        report = DailyReport(
            date=date_str,
            summary_brief=f"今日 ({date_str}) 未发现符合条件的趋势信号。",
            engineering_signals=[],
            research_signals=[],
            stats={"total_prs_analyzed": 0, "high_impact_signals": 0},
        )

        # 添加活跃度数据（如果有）
        if activity_data:
            report.activity = activity_data

        return report

    def _get_output_path(self, date: datetime) -> str:
        """获取报告输出路径

        Args:
            date: 日期

        Returns:
            输出文件路径
        """
        # 默认输出到 reports 目录
        reports_dir = Path("reports")
        filename = f"report-{date.strftime('%Y-%m-%d')}.md"
        return str(reports_dir / filename)
