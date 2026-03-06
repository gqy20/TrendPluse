"""报告输出服务。"""

from datetime import datetime
from pathlib import Path
from typing import Any, Protocol

from trendpluse.logger import get_logger
from trendpluse.models.signal import DailyReport, WeeklyReport

logger = get_logger(__name__)


class DailyNotifier(Protocol):
    """日报通知协议。"""

    def send_report(self, report: Any) -> bool | None:
        """发送日报通知。"""


class ReportWriter(Protocol):
    """报告写入协议。"""

    def save_report(self, report: DailyReport, output_path: str) -> None:
        """保存日报 Markdown。"""

    def save_weekly_report(self, report: WeeklyReport, output_path: str) -> None:
        """保存周报 Markdown。"""


class ReportOutputService:
    """负责日报/周报的落盘与通知。"""

    def __init__(
        self,
        *,
        reporter: ReportWriter,
        daily_output_dir: str,
        weekly_output_dir: str,
        notifier: DailyNotifier | None = None,
    ) -> None:
        self.reporter = reporter
        self.daily_output_dir = Path(daily_output_dir)
        self.weekly_output_dir = Path(weekly_output_dir)
        self.notifier = notifier

    def save_daily(self, report: DailyReport, date: datetime) -> str:
        """保存日报 Markdown 与 JSON。"""
        output_path = self.daily_output_dir / f"report-{date.strftime('%Y-%m-%d')}.md"
        self.reporter.save_report(report, str(output_path))
        self._save_json(report, output_path)
        return str(output_path)

    def save_weekly(self, report: WeeklyReport, date: datetime) -> str:
        """保存周报 Markdown 与 JSON。"""
        week_id = WeeklyReport.get_week_id(date)
        output_path = self.weekly_output_dir / f"weekly-{week_id}.md"
        self.reporter.save_weekly_report(report, str(output_path))
        self._save_json(report, output_path)
        return str(output_path)

    def notify_daily(self, report: DailyReport) -> None:
        """发送日报通知。"""
        if self.notifier is None:
            return
        try:
            self.notifier.send_report(report)
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"发送飞书通知失败: {exc}")

    def _save_json(self, report: DailyReport | WeeklyReport, output_path: Path) -> None:
        """保存 JSON 数据。"""
        json_path = output_path.with_suffix(".json")
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(
            report.model_dump_json(indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
