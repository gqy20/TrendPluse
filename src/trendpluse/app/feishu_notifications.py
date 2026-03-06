"""飞书通知应用辅助。"""

from __future__ import annotations

import re
from pathlib import Path

from rich.console import Console

from trendpluse.cli.report_json_common import (
    find_report_json_file,
    load_daily_report_model,
    load_report_model,
)
from trendpluse.models.signal import DailyReport, WeeklyReport


def find_daily_report_json(report_date: str) -> Path | None:
    """查找日报 JSON 文件。"""
    filename = f"report-{report_date}.json"
    return find_report_json_file(f"reports/daily/{filename}")


def find_latest_daily_report_json() -> Path | None:
    """查找最新存在的日报 JSON 文件。"""
    reports_dir = Path("reports/daily")
    if not reports_dir.exists():
        return None

    pattern = re.compile(r"report-(\d{4}-\d{2}-\d{2})\.json$")
    candidates = []
    for path in reports_dir.glob("report-*.json"):
        match = pattern.match(path.name)
        if match:
            candidates.append((match.group(1), path))

    if not candidates:
        return None

    _, latest_path = max(candidates, key=lambda item: item[0])
    return latest_path


def load_daily_report_from_json(json_path: str, console: Console) -> DailyReport:
    """从 JSON 文件加载日报对象。"""
    return load_daily_report_model(json_path, console)


def find_weekly_report_json(week_id: str) -> Path | None:
    """查找周报 JSON 文件。"""
    return find_report_json_file(f"reports/weekly/weekly-{week_id}.json")


def load_weekly_report_from_json(json_path: str) -> WeeklyReport:
    """从 JSON 文件加载周报对象。"""
    return load_report_model(json_path, WeeklyReport)


def build_weekly_notification_content(report: WeeklyReport) -> str:
    """构建周报飞书通知正文。"""
    return (
        f"📅 周期: {report.start_date} ~ {report.end_date}\n"
        f"🧭 摘要: {report.summary_brief}\n"
        f"📊 日报天数: {report.daily_reports_count}\n"
        f"📌 核心趋势: {len(report.core_trends)}\n"
        f"🔧 工程信号: {len(report.engineering_signals)}\n"
        f"🔬 研究信号: {len(report.research_signals)}"
    )


def build_weekly_notification_url(report: WeeklyReport) -> str:
    """构建周报链接。"""
    return f"https://home.gqy20.top/TrendPluse/reports/weekly-{report.week_id}/"
