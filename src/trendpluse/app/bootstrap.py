"""应用依赖装配。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from trendpluse.markdown_reporter import MarkdownReporter
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.reports.builder import DailyReportBuilder
from trendpluse.reports.publisher import ReportPublisher


@dataclass(frozen=True)
class ReportingComponents:
    """报告相关组件集合。"""

    reporter: MarkdownReporter
    notifier: FeishuNotifier | None
    builder: DailyReportBuilder
    publisher: ReportPublisher


def build_reporting_components(
    *,
    settings: Any,
    issue_insights_loader,
) -> ReportingComponents:
    """构建报告相关组件。"""
    reporter = MarkdownReporter()
    notifier: FeishuNotifier | None = None
    configured_output_dir = getattr(settings, "output_dir", None)
    daily_output_dir = (
        configured_output_dir
        if isinstance(configured_output_dir, str) and configured_output_dir
        else "reports/daily"
    )
    if settings.feishu_webhook_url:
        notifier = FeishuNotifier(
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
