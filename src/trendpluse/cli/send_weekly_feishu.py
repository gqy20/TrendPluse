"""发送周报飞书通知脚本

用于发送周报到飞书。
"""

import argparse
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from trendpluse.cli.feishu_common import (
    build_feishu_notifier,
    ensure_webhook_configured,
    exit_on_send_failure,
    load_feishu_cli_config,
    print_exception_and_exit,
    print_feishu_target,
)
from trendpluse.cli.report_json_common import (
    find_report_json_file,
    load_report_model,
    print_weekly_report_summary,
    resolve_week_id,
)
from trendpluse.models.signal import WeeklyReport

console = Console()


def find_weekly_report_json(week_id: str) -> Path | None:
    """查找周报 JSON 文件

    Args:
        week_id: 周标识 (YYYY-Www)

    Returns:
        找到的文件路径（绝对路径），未找到返回 None
    """
    return find_report_json_file(f"reports/weekly/weekly-{week_id}.json")


def load_weekly_report_from_json(json_path: str) -> WeeklyReport:
    """从 JSON 文件加载 WeeklyReport 对象

    Args:
        json_path: JSON 文件路径

    Returns:
        WeeklyReport 对象
    """
    return load_report_model(json_path, WeeklyReport)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="发送 TrendPulse 周报飞书通知")
    parser.parse_args()

    load_dotenv()

    # 获取环境变量
    config = load_feishu_cli_config()
    week_id_input = os.getenv("WEEK_ID", "")

    week_id = resolve_week_id(week_id_input, datetime.now())

    # 检查 webhook URL
    ensure_webhook_configured(console, config)

    console.print("[bold]发送周报飞书通知[/bold]")
    console.print(f"  周标识: {week_id}")
    console.print(f"  @ 提醒: {len(config.at_mobiles)} 个")

    # 查找周报 JSON 文件
    json_path = find_weekly_report_json(week_id)

    if not json_path:
        console.print(
            f"[yellow]周报文件不存在: reports/weekly/weekly-{week_id}.json[/yellow]"
        )
        raise SystemExit(1)
    else:
        console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
        report = load_weekly_report_from_json(str(json_path))

    try:
        print_weekly_report_summary(console, report)

        # 初始化通知器
        notifier = build_feishu_notifier(config)
        print_feishu_target(console, config)

        # 发送周报摘要文本，避免 WeeklyReport -> DailyReport 的临时转换层
        console.print("  正在发送...")
        weekly_url = (
            f"https://home.gqy20.top/TrendPluse/reports/weekly-{report.week_id}/"
        )
        content = (
            f"📅 周期: {report.start_date} ~ {report.end_date}\n"
            f"🧭 摘要: {report.summary_brief}\n"
            f"📊 日报天数: {report.daily_reports_count}\n"
            f"📌 核心趋势: {len(report.core_trends)}\n"
            f"🔧 工程信号: {len(report.engineering_signals)}\n"
            f"🔬 研究信号: {len(report.research_signals)}"
        )
        success = notifier.send(
            title=f"TrendPulse 周报 {report.week_id}",
            content=content,
            url=weekly_url,
        )
        exit_on_send_failure(console, bool(success))

    except Exception as e:
        print_exception_and_exit(console, e)


if __name__ == "__main__":
    main()
