"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trendpluse.config import Settings
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.pipeline import TrendPulsePipeline

console = Console()


def load_report_from_markdown(report_date: str) -> str:
    """从 markdown 报告加载基本信息

    Args:
        report_date: 报告日期 (YYYY-MM-DD)

    Returns:
        报告文件路径
    """
    report_path = Path(f"reports/report-{report_date}.md")
    if report_path.exists():
        return str(report_path)
    return ""


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

    try:
        # 初始化 pipeline
        settings = Settings()
        pipeline = TrendPulsePipeline(settings=settings)

        # 生成报告（复用已有逻辑）
        date_obj = datetime.strptime(report_date, "%Y-%m-%d")
        report = pipeline.run_daily(date=date_obj)

        # 初始化通知器
        notifier = FeishuNotifier(
            webhook_url=webhook_url,
            at_mobiles=at_mobiles,
            secret=secret or None,
        )

        # 发送报告通知
        success = notifier.send_report(report)

        if success:
            console.print("[green]✓ 飞书通知发送成功[/green]")
        else:
            console.print("[red]✗ 飞书通知发送失败[/red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[red]发送通知失败:[/red] {e}")
        # 降级：发送简单通知
        try:
            notifier = FeishuNotifier(
                webhook_url=webhook_url,
                at_mobiles=at_mobiles,
                secret=secret or None,
            )

            title = f"📊 TrendPulse 每日报告 - {report_date}"
            content = "每日分析报告已生成并部署。"

            if deployment_url:
                content += f"\n\n🔗 [查看报告]({deployment_url})"

            success = notifier.send(title, content, url=deployment_url)

            if success:
                console.print("[green]✓ 简单通知发送成功[/green]")
            else:
                console.print("[red]✗ 简单通知发送失败[/red]")
                sys.exit(1)

        except Exception as e2:
            console.print(f"[red]降级通知也失败:[/red] {e2}")
            sys.exit(1)


if __name__ == "__main__":
    main()
