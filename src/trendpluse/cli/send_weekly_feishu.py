"""发送周报飞书通知脚本

用于发送周报到飞书。
"""

import argparse
import os
from datetime import datetime

from dotenv import load_dotenv
from rich.console import Console

from trendpluse.app.feishu_notifications import (
    build_weekly_notification_content,
    build_weekly_notification_url,
    find_weekly_report_json,
    load_weekly_report_from_json,
)
from trendpluse.cli.feishu_common import (
    build_feishu_notifier,
    ensure_webhook_configured,
    exit_on_send_failure,
    load_feishu_cli_config,
    print_exception_and_exit,
    print_feishu_target,
)
from trendpluse.cli.report_json_common import (
    print_weekly_report_summary,
    resolve_week_id,
)

console = Console()


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

    console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
    report = load_weekly_report_from_json(str(json_path))

    try:
        print_weekly_report_summary(console, report)

        # 初始化通知器
        notifier = build_feishu_notifier(config)
        print_feishu_target(console, config)

        # 发送周报摘要文本，避免 WeeklyReport -> DailyReport 的临时转换层
        console.print("  正在发送...")
        weekly_url = build_weekly_notification_url(report)
        content = build_weekly_notification_content(report)
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
