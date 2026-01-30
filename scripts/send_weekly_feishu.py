"""发送周报飞书通知脚本

用于发送周报到飞书。
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

from trendpluse.models.signal import WeeklyReport
from trendpluse.notifiers.feishu import FeishuNotifier

console = Console()


def find_weekly_report_json(week_id: str) -> Path | None:
    """查找周报 JSON 文件

    Args:
        week_id: 周标识 (YYYY-Www)

    Returns:
        找到的文件路径（绝对路径），未找到返回 None
    """
    # 优先在 reports/ 目录查找（标准位置）
    reports_path = Path(f"reports/weekly-{week_id}.json").resolve()
    if reports_path.exists():
        return reports_path

    return None


def load_weekly_report_from_json(json_path: str) -> WeeklyReport:
    """从 JSON 文件加载 WeeklyReport 对象

    Args:
        json_path: JSON 文件路径

    Returns:
        WeeklyReport 对象
    """
    content = Path(json_path).read_text(encoding="utf-8")
    data = json.loads(content)
    return WeeklyReport(**data)


def main():
    """主函数"""
    load_dotenv()

    # 获取环境变量
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL", "")
    secret = os.getenv("FEISHU_SECRET", "")
    at_mobiles_str = os.getenv("FEISHU_AT_MOBILES", "")
    week_id_input = os.getenv("WEEK_ID", "")

    # 计算上周的 week_id（如果没有指定）
    if week_id_input:
        week_id = week_id_input
    else:
        today = datetime.now()
        year, week, _ = today.isocalendar()
        week_id = f"{year}-W{week:02d}"

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

    console.print("[bold]发送周报飞书通知[/bold]")
    console.print(f"  周标识: {week_id}")
    console.print(f"  @ 提醒: {len(at_mobiles)} 个")

    # 查找周报 JSON 文件
    json_path = find_weekly_report_json(week_id)

    if not json_path:
        console.print(f"[yellow]周报文件不存在: weekly-{week_id}.json[/yellow]")
        return
    else:
        console.print(f"  [dim]读取 JSON 文件: {json_path}[/dim]")
        report = load_weekly_report_from_json(str(json_path))

    try:
        # 详细解析结果输出
        console.print("  [dim]周报数据:[/dim]")
        console.print(f"    - 周标识: {report.week_id}")
        console.print(f"    - 时间范围: {report.start_date} ~ {report.end_date}")
        console.print(f"    - 包含日报: {report.daily_reports_count} 天")
        console.print(f"    - 核心趋势: {len(report.core_trends)} 个")
        console.print(f"    - 工程信号: {len(report.engineering_signals)} 个")
        console.print(f"    - 研究信号: {len(report.research_signals)} 个")
        console.print(f"    - 总 PR 数: {report.total_prs_analyzed}")
        console.print(f"    - 总 Commit 数: {report.total_commits}")

        # 初始化通知器
        notifier = FeishuNotifier(
            webhook_url=webhook_url,
            at_mobiles=at_mobiles,
            secret=secret or None,
        )

        console.print(f"  Webhook URL: {webhook_url[:30]}...{webhook_url[-10:]}")
        console.print(f"  使用签名: {'是' if secret else '否'}")

        # 发送通知 - 使用 send_report 方法
        # 注意：FeishuNotifier 期望 DailyReport，但 WeeklyReport 也有相似的字段
        # 我们需要构造一个兼容的格式或扩展 FeishuNotifier
        console.print("  正在发送...")

        # 将 WeeklyReport 转换为 DailyReport 格式用于飞书通知
        # 这是因为 FeishuNotifier 当前只支持 DailyReport
        # 作为临时方案，我们构造一个"伪日报"
        from trendpluse.models.signal import (
            ActivityData,
            DailyReport,
        )

        # 转换 WeeklyActivity 到 ActivityData（如果存在）
        activity = None
        if report.weekly_activity:
            activity = ActivityData(
                total_commits=report.weekly_activity.total_commits,
                active_repos_count=report.weekly_activity.active_repos_count,
                top_repos=report.weekly_activity.top_repos,
            )

        daily_report = DailyReport(
            date=f"{report.start_date} ~ {report.end_date}",
            summary_brief=f"## {report.week_id} 周报\n\n{report.summary_brief}",
            engineering_signals=report.engineering_signals,
            research_signals=report.research_signals,
            stats={
                "total_prs_analyzed": report.total_prs_analyzed,
                "high_impact_signals": report.high_impact_signals,
                "total_commits_analyzed": report.total_commits,
                "total_releases": report.total_releases,
                "daily_reports_count": report.daily_reports_count,
            },
            activity=activity,
        )

        success = notifier.send_report(daily_report)

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
