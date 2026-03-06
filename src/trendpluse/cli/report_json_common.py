"""CLI 报告 JSON 公共辅助。"""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path

from rich.console import Console

from trendpluse.models.signal import DailyReport, WeeklyReport


def find_report_json_file(relative_path: str) -> Path | None:
    """查找仓库内的报告 JSON 文件。"""
    report_path = Path(relative_path).resolve()
    if report_path.exists():
        return report_path
    return None


def load_report_model[ReportModel: (DailyReport, WeeklyReport)](
    json_path: str, model_cls: type[ReportModel]
) -> ReportModel:
    """从 JSON 文件加载报告模型。"""
    content = Path(json_path).read_text(encoding="utf-8")
    data = json.loads(content)
    return model_cls(**data)


def load_daily_report_model(json_path: str, console: Console) -> DailyReport:
    """从 JSON 文件加载日报对象，并补齐必要默认值。"""
    content = Path(json_path).read_text(encoding="utf-8")
    data = json.loads(content)

    required_fields = ["summary_brief", "stats"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        console.print(f"[yellow]报告数据不完整，缺少字段: {missing_fields}[/yellow]")
        console.print("[yellow]使用默认值填充[/yellow]")

        data.setdefault("summary_brief", "报告数据不完整，可能是数据采集或分析失败。")
        data.setdefault("stats", {})
        data.setdefault("engineering_signals", [])
        data.setdefault("research_signals", [])
        data.setdefault("commit_signals", [])
        data.setdefault("release_signals", [])

    return DailyReport(**data)


def resolve_week_id(week_id_input: str, today: datetime | None = None) -> str:
    """解析或计算默认的周报标识。"""
    if week_id_input:
        return week_id_input

    current = today or datetime.now()
    weekday = current.weekday()
    this_monday = current - timedelta(days=weekday)
    last_sunday = this_monday - timedelta(days=1)
    return WeeklyReport.get_week_id(last_sunday)


def print_daily_report_summary(console: Console, report: DailyReport) -> None:
    """打印日报摘要。"""
    console.print("  [dim]报告数据:[/dim]")
    console.print(f"    - Commit 信号: {len(report.commit_signals)} 个")
    console.print(f"    - 工程信号: {len(report.engineering_signals)} 个")
    console.print(f"    - 研究信号: {len(report.research_signals)} 个")
    console.print(f"    - Release 信号: {len(report.release_signals)} 个")
    releases_count = report.releases.total_count if report.releases else 0
    console.print(f"    - Release 数据: {releases_count} 个")
    repos_count = len(report.activity.top_repos) if report.activity else 0
    console.print(f"    - 活跃仓库: {repos_count} 个")
    console.print(f"    - 统计信息: {report.stats}")


def print_weekly_report_summary(console: Console, report: WeeklyReport) -> None:
    """打印周报摘要。"""
    console.print("  [dim]周报数据:[/dim]")
    console.print(f"    - 周标识: {report.week_id}")
    console.print(f"    - 时间范围: {report.start_date} ~ {report.end_date}")
    console.print(f"    - 包含日报: {report.daily_reports_count} 天")
    console.print(f"    - 核心趋势: {len(report.core_trends)} 个")
    console.print(f"    - 工程信号: {len(report.engineering_signals)} 个")
    console.print(f"    - 研究信号: {len(report.research_signals)} 个")
    console.print(f"    - 总 PR 数: {report.total_prs_analyzed}")
    console.print(f"    - 总 Commit 数: {report.total_commits}")
