"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""
from datetime import datetime
from pathlib import Path

from trendpluse.config import Settings
from trendpluse.collectors.gh_archive import GHArchiveCollector
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_api import GitHubDetailFetcher
from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.reporters.markdown_reporter import MarkdownReporter
from trendpluse.models.signal import DailyReport


class TrendPulsePipeline:
    """TrendPulse 主流程"""

    def __init__(self, settings: Settings | None = None):
        """初始化 Pipeline

        Args:
            settings: 配置对象，None 则从环境变量加载
        """
        self.settings = settings or Settings()

        # 初始化组件
        self.collector = GHArchiveCollector()
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

        # 1. 从 GH Archive 获取事件
        events = self.collector.fetch_events(
            repos=self.settings.github_repos,
            since=date,
        )

        # 2. 筛选候选事件
        candidates = self.filter.filter_candidates(events)

        # 如果没有候选事件，返回空报告
        if not candidates:
            return self._generate_empty_report(date)

        # 3. 获取详细信息
        pr_details = self.fetcher.fetch_multiple_pr_details(candidates)

        if not pr_details:
            return self._generate_empty_report(date)

        # 4. AI 分析提取信号
        signals = self.analyzer.analyze_prs(pr_details)

        if not signals:
            return self._generate_empty_report(date)

        # 5. 生成每日报告
        report = self.analyzer.generate_report(signals, date=date.strftime("%Y-%m-%d"))

        # 6. 保存报告
        output_path = self._get_output_path(date)
        self.reporter.save_report(report, output_path)

        return report

    def _generate_empty_report(self, date: datetime) -> DailyReport:
        """生成空报告

        Args:
            date: 日期

        Returns:
            空的每日报告
        """
        return DailyReport(
            date=date.strftime("%Y-%m-%d"),
            summary_brief=f"今日 ({date.strftime('%Y-%m-%d')}) 未发现符合条件的趋势信号。",
            engineering_signals=[],
            research_signals=[],
            stats={"total_prs_analyzed": 0, "high_impact_signals": 0},
        )

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
