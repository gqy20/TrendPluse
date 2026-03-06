"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。

现在直接读取 JSON 数据，不再从 Markdown 反向解析。
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
    load_daily_report_model,
    print_daily_report_summary,
)
from trendpluse.models.signal import DailyReport

console = Console()


def find_report_json(report_date: str) -> Path | None:
    """查找报告 JSON 文件

    仅支持仓库内新目录结构：
    1. reports/daily/report-{date}.json

    Args:
        report_date: 报告日期 (YYYY-MM-DD)

    Returns:
        找到的文件路径（绝对路径），未找到返回 None
    """
    filename = f"report-{report_date}.json"
    return find_report_json_file(f"reports/daily/{filename}")


def load_report_from_json(json_path: str) -> DailyReport:
    """从 JSON 文件加载 DailyReport 对象

    如果数据不完整（例如只包含 date），会提供默认值以确保返回有效的 DailyReport。

    Args:
        json_path: JSON 文件路径

    Returns:
        DailyReport 对象
    """
    return load_daily_report_model(json_path, console)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="发送 TrendPulse 日报飞书通知")
    parser.parse_args()

    load_dotenv()

    # 获取环境变量
    config = load_feishu_cli_config()
    deployment_url = os.getenv("DEPLOYMENT_URL", "")
    report_date = os.getenv("REPORT_DATE", datetime.now().strftime("%Y-%m-%d"))

    ensure_webhook_configured(console, config)

    console.print("[bold]发送飞书通知[/bold]")
    console.print(f"  日期: {report_date}")
    console.print(f"  部署 URL: {deployment_url or '未设置'}")
    console.print(f"  @ 提醒: {len(config.at_mobiles)} 个")

    # 查找 JSON 报告文件
    json_path = find_report_json(report_date)

    if not json_path:
        console.print(f"[yellow]报告文件不存在: report-{report_date}.json[/yellow]")
        raise SystemExit(1)
    else:
        # 直接读取 JSON
        console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
        report = load_report_from_json(str(json_path))

    try:
        print_daily_report_summary(console, report)

        # 初始化通知器
        notifier = build_feishu_notifier(config)
        print_feishu_target(console, config)

        # 发送通知
        console.print("  正在发送...")
        success = notifier.send_report(report)
        exit_on_send_failure(console, bool(success))

    except Exception as e:
        print_exception_and_exit(console, e)


if __name__ == "__main__":
    main()
