"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。

现在直接读取 JSON 数据，不再从 Markdown 反向解析。
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trendpluse.models.signal import DailyReport
from trendpluse.notifiers.feishu import FeishuNotifier

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

    daily_path = Path(f"reports/daily/{filename}").resolve()
    if daily_path.exists():
        return daily_path

    return None


def load_report_from_json(json_path: str) -> DailyReport:
    """从 JSON 文件加载 DailyReport 对象

    如果数据不完整（例如只包含 date），会提供默认值以确保返回有效的 DailyReport。

    Args:
        json_path: JSON 文件路径

    Returns:
        DailyReport 对象
    """
    content = Path(json_path).read_text(encoding="utf-8")
    data = json.loads(content)

    # 检查数据是否完整，如果不完整则提供默认值
    required_fields = ["summary_brief", "stats"]
    missing_fields = [f for f in required_fields if f not in data]

    if missing_fields:
        console.print(f"[yellow]报告数据不完整，缺少字段: {missing_fields}[/yellow]")
        console.print("[yellow]使用默认值填充[/yellow]")

        # 提供必需字段的默认值
        if "summary_brief" not in data:
            data["summary_brief"] = "报告数据不完整，可能是数据采集或分析失败。"
        if "stats" not in data:
            data["stats"] = {}
        if "engineering_signals" not in data:
            data["engineering_signals"] = []
        if "research_signals" not in data:
            data["research_signals"] = []
        if "commit_signals" not in data:
            data["commit_signals"] = []
        if "release_signals" not in data:
            data["release_signals"] = []

    return DailyReport(**data)


def main():
    """主函数"""
    load_dotenv()

    # 获取环境变量
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL", "")
    secret = os.getenv("FEISHU_SECRET", "")
    at_mobiles_str = os.getenv("FEISHU_AT_MOBILES", "")
    deployment_url = os.getenv("DEPLOYMENT_URL", "")
    report_date = os.getenv("REPORT_DATE", datetime.now().strftime("%Y-%m-%d"))

    # 检查 webhook URL
    if not webhook_url:
        console.print("[yellow]FEISHU_WEBHOOK_URL 未配置，跳过通知[/yellow]")
        return

    # 解析 @ 提醒列表
    at_mobiles = (
        [m.strip() for m in at_mobiles_str.split(",") if m.strip()]
        if at_mobiles_str
        else []
    )

    console.print("[bold]发送飞书通知[/bold]")
    console.print(f"  日期: {report_date}")
    console.print(f"  部署 URL: {deployment_url or '未设置'}")
    console.print(f"  @ 提醒: {len(at_mobiles)} 个")

    # 查找 JSON 报告文件
    json_path = find_report_json(report_date)

    if not json_path:
        console.print(f"[yellow]报告文件不存在: report-{report_date}.json[/yellow]")
        sys.exit(1)
    else:
        # 直接读取 JSON
        console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
        report = load_report_from_json(str(json_path))

    try:
        # 详细解析结果输出
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

        # 初始化通知器
        notifier = FeishuNotifier(
            webhook_url=webhook_url,
            at_mobiles=at_mobiles,
            secret=secret or None,
        )

        console.print(f"  Webhook URL: {webhook_url[:30]}...{webhook_url[-10:]}")
        console.print(f"  使用签名: {'是' if secret else '否'}")

        # 发送通知
        console.print("  正在发送...")
        success = notifier.send_report(report)

        if success:
            console.print("[green]✓ 飞书通知发送成功[/green]")
        else:
            console.print("[red]✗ 飞书通知发送失败[/red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[red]发送通知失败:[/red] {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
