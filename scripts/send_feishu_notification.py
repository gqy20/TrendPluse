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


def load_report_from_json(json_path: str) -> DailyReport:
    """从 JSON 文件加载 DailyReport 对象

    Args:
        json_path: JSON 文件路径

    Returns:
        DailyReport 对象
    """
    content = Path(json_path).read_text(encoding="utf-8")
    data = json.loads(content)
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
    json_path = Path(f"reports/report-{report_date}.json")

    if not json_path.exists():
        console.print(f"[yellow]报告文件不存在: {json_path}[/yellow]")
        return
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

        # 构建飞书卡片（用于调试和保存 artifact）
        card = notifier._build_card(report)

        # 保存卡片数据到当前目录（GitHub Actions 会上传为 artifact）
        card_file = Path("feishu_card.json")
        card_file.write_text(json.dumps(card, ensure_ascii=False, indent=2))
        console.print(f"  [dim]卡片已保存到: {card_file}[/dim]")

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
