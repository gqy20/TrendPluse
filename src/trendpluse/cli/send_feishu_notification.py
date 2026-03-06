"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。

现在直接读取 JSON 数据，不再从 Markdown 反向解析。
"""

import argparse
import os
from datetime import datetime

from dotenv import load_dotenv
from rich.console import Console

from trendpluse.app.feishu_notifications import (
    find_daily_report_json,
    load_daily_report_from_json,
)
from trendpluse.cli.feishu_common import (
    build_feishu_notifier,
    ensure_webhook_configured,
    exit_on_send_failure,
    load_feishu_cli_config,
    print_exception_and_exit,
    print_feishu_target,
)
from trendpluse.cli.report_json_common import print_daily_report_summary

console = Console()


def build_daily_report_url_template(deployment_url: str) -> str | None:
    """根据部署地址构建日报链接模板。"""
    base_url = deployment_url.strip().rstrip("/")
    if not base_url:
        return None
    return f"{base_url}/reports/report-{{date}}/"


def resolve_report_date(raw_report_date: str | None) -> str:
    """解析报告日期，空值时回退到当天。"""
    cleaned = (raw_report_date or "").strip()
    if cleaned:
        return cleaned
    return datetime.now().strftime("%Y-%m-%d")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="发送 TrendPulse 日报飞书通知")
    parser.parse_args()

    load_dotenv()

    # 获取环境变量
    config = load_feishu_cli_config()
    deployment_url = os.getenv("DEPLOYMENT_URL", "")
    report_date = resolve_report_date(os.getenv("REPORT_DATE"))

    ensure_webhook_configured(console, config)

    console.print("[bold]发送飞书通知[/bold]")
    console.print(f"  日期: {report_date}")
    console.print(f"  部署 URL: {deployment_url or '未设置'}")
    console.print(f"  @ 提醒: {len(config.at_mobiles)} 个")

    # 查找 JSON 报告文件
    json_path = find_daily_report_json(report_date)

    if not json_path:
        console.print(f"[yellow]报告文件不存在: report-{report_date}.json[/yellow]")
        raise SystemExit(1)

    console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
    report = load_daily_report_from_json(str(json_path), console)

    try:
        print_daily_report_summary(console, report)

        # 初始化通知器
        notifier = build_feishu_notifier(
            config,
            report_url_template=build_daily_report_url_template(deployment_url),
        )
        print_feishu_target(console, config)

        # 发送通知
        console.print("  正在发送...")
        success = notifier.send_report(report)
        exit_on_send_failure(console, bool(success))

    except Exception as e:
        print_exception_and_exit(console, e)


if __name__ == "__main__":
    main()
