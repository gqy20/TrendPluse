"""报告发布器。"""

from __future__ import annotations

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


class ReportPublisher:
    """负责日报/周报的落盘与通知。"""

    def __init__(
        self,
        *,
        daily_output_dir: str,
        weekly_output_dir: str,
        notifier: DailyNotifier | None = None,
    ) -> None:
        self.daily_output_dir = Path(daily_output_dir)
        self.weekly_output_dir = Path(weekly_output_dir)
        self.notifier = notifier

    def save_daily(self, report: DailyReport, date: datetime) -> str:
        """保存日报 JSON(唯一真源格式)。"""
        json_path = self.daily_output_dir / f"report-{date.strftime('%Y-%m-%d')}.json"
        self._write_json(report, json_path)
        return str(json_path)

    def save_weekly(self, report: WeeklyReport, date: datetime) -> str:
        """保存周报 JSON(唯一真源格式)。"""
        week_id = WeeklyReport.get_week_id(date)
        json_path = self.weekly_output_dir / f"weekly-{week_id}.json"
        self._write_json(report, json_path)
        return str(json_path)

    def notify_daily(self, report: DailyReport) -> None:
        """发送日报通知。"""
        if self.notifier is None:
            return
        try:
            self.notifier.send_report(report)
        except Exception as exc:  # pragma: no cover - 防御性日志
            logger.warning(f"发送飞书通知失败: {exc}")

    def _write_json(self, report: DailyReport | WeeklyReport, json_path: Path) -> None:
        """写入 JSON 数据。

        末尾补一个换行符：入库的历史报告均带换行（pre-commit 的
        end-of-file-fixer 也会强制补），落盘时不补会导致每次重写都产生
        仅差一个换行符的脏 diff。
        """
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(
            report.model_dump_json(indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
