"""TrendPulse 主流程

协调各个组件完成每日趋势分析。
"""

from datetime import datetime, timedelta
from pathlib import Path

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
from trendpluse.collectors.filter import EventFilter
from trendpluse.collectors.github_api import GitHubDetailFetcher
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import Settings
from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleasesData,
)
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.reporters.markdown_reporter import MarkdownReporter


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
        self.commit_analyzer = CommitAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        self.release_analyzer = ReleaseAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        self.release_summarizer = ReleaseSummarizer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        self.breaking_changes_detector = BreakingChangesDetector(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        self.filter = EventFilter(max_count=self.settings.max_candidates)
        self.fetcher = GitHubDetailFetcher(token=self.settings.github_token)
        self.analyzer = TrendAnalyzer(
            api_key=self.settings.anthropic_api_key,
            model=self.settings.anthropic_model,
            base_url=self.settings.anthropic_base_url,
        )
        # 初始化信号去重器
        self.deduplicator = SignalDeduplicator(
            llm_client=llm_client,
            lookback_days=self.settings.days_to_lookback,  # 与 PR 回溯天数一致
            history_path="data/signal_history.json",
        )
        self.reporter = MarkdownReporter()

        # 初始化飞书通知器（如果配置了 webhook URL）
        self.notifier: FeishuNotifier | None = None
        if self.settings.feishu_webhook_url:
            self.notifier = FeishuNotifier(
                webhook_url=self.settings.feishu_webhook_url,
                at_mobiles=self.settings.feishu_at_mobiles_list,
                max_signals=getattr(self.settings, "feishu_max_signals", 5),
                secret=getattr(self.settings, "feishu_secret", "") or None,
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

        # 0. 收集仓库活跃度数据（独立于 PR 分析）
        activity_data, detailed_commits = self.activity_collector.collect_activity(
            repos=self.settings.github_repos,
            since=date,
        )

        # 0.3. 收集 Releases 数据（只分析最近 24 小时）
        # 从当前时间往前推 24 小时
        day_ago = date - timedelta(days=1)
        releases_data, detailed_releases = self.release_collector.collect_releases(
            repos=self.settings.github_repos,
            since=day_ago,
            include_prereleases=getattr(self.settings, "include_prereleases", False),
        )

        # 0.4. 为 Releases 生成 AI 总结
        if detailed_releases:
            summaries = self.release_summarizer.summarize_releases(detailed_releases)
            # 将 AI 总结附加到对应的 ReleaseInfo
            for release in releases_data.releases:
                key = f"{release.repo}@{release.version}"
                if key in summaries:
                    release.ai_summary = summaries[key]

        # 0.5. 分析 commits 提取信号
        commit_signals = []
        if detailed_commits:
            commit_signals = self.commit_analyzer.analyze_commits(detailed_commits)

        # 0.6. 分析 releases 提取信号
        release_signals = []
        if detailed_releases:
            # 构造分析器需要的格式
            release_analysis_data = {"detailed_releases": detailed_releases}
            release_signals = self.release_analyzer.analyze_releases(
                release_analysis_data
            )

        # 0.7. 检测 breaking changes
        breaking_changes = []
        if detailed_releases:
            release_analysis_data = {"detailed_releases": detailed_releases}
            breaking_changes = self.breaking_changes_detector.detect_breaking_changes(
                release_analysis_data
            )

        # 1. 从 GitHub API 获取 PR（只分析最近 24 小时）
        # 从当前时间往前推 24 小时
        events = self.collector.fetch_events(
            repos=self.settings.github_repos,
            since=day_ago,
        )

        # 2. 筛选候选事件
        candidates = self.filter.filter_candidates(events)

        # 如果没有候选事件，返回带活跃度、commit 和 release 信号的空报告
        if not candidates:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        # 3. 获取详细信息
        pr_details = self.fetcher.fetch_multiple_pr_details(candidates)

        if not pr_details:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        # 4. AI 分析提取信号
        signals = self.analyzer.analyze_prs(pr_details)

        if not signals:
            return self._handle_empty_report(
                date, activity_data, commit_signals, releases_data
            )

        # 4.5. 信号去重（只对 PR 信号去重）
        pr_signals = self.deduplicator.deduplicate(signals)

        # 5. 使用跨类型聚合生成高层次趋势报告
        report = self.analyzer.aggregate_and_generate_report(
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
            date=date.strftime("%Y-%m-%d"),
        )

        # 5.5. 确保低层次信号被清空（避免重复显示）
        # 虽然 TrendAnalyzer 尝试清空这些字段，但 LLM 返回的对象可能不遵守
        # 这里强制清空以确保 Markdown 报告不会重复显示
        report.commit_signals = []
        report.release_signals = []

        # 6. 添加活跃度、release 数据和 breaking changes
        report.activity = activity_data
        report.releases = releases_data
        report.breaking_changes = breaking_changes if breaking_changes else None
        report.monitored_repos = self.settings.github_repos
        # 更新统计信息（聚合时已包含部分统计）
        report.stats["total_commits_analyzed"] = len(detailed_commits)
        report.stats["total_releases"] = releases_data.total_count
        report.stats["total_releases_analyzed"] = len(detailed_releases)
        report.stats["total_breaking_changes"] = len(breaking_changes)

        # 7. 保存报告（同时保存 Markdown 和 JSON）
        output_path = self._get_output_path(date)
        self.reporter.save_report(report, output_path)
        self._save_report_json(report, output_path)
        self._send_notification(report)

        return report

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
            stats={
                "total_prs_analyzed": 0,
                "high_impact_signals": high_impact_count,
                "total_commits_analyzed": activity_data.total_commits
                if activity_data
                else 0,
                "total_releases": releases_data.total_count if releases_data else 0,
            },
        )

        # 添加活跃度和 release 数据（如果有）
        if activity_data:
            report.activity = activity_data
        if releases_data:
            report.releases = releases_data

        # 添加监控的仓库列表
        report.monitored_repos = self.settings.github_repos

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
            except Exception:
                # 通知失败不影响主流程
                pass

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
