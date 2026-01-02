"""TrendPulse 运行脚本

执行每日 GitHub 趋势分析。
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trendpluse.config import Settings
from trendpluse.pipeline import TrendPulsePipeline

console = Console()


def check_env_vars() -> bool:
    """检查必需的环境变量"""
    required_vars = ["ANTHROPIC_API_KEY"]
    optional_vars = ["GITHUB_TOKEN", "ANTHROPIC_BASE_URL"]

    missing = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        console.print(
            Panel(
                "[bold red]缺少必需的环境变量:[/bold red]\n"
                + "\n".join(f"  - {var}" for var in missing),
                title="[bold red]配置错误[/bold red]",
                border_style="red",
            )
        )
        return False

    # 显示可选变量状态
    for var in optional_vars:
        value = os.getenv(var)
        status = "[green]✓[/green]" if value else "[yellow]✗[/yellow] (未设置)"
        console.print(f"{var}: {status}")

    return True


def main():
    """主函数"""
    load_dotenv()

    console.print(
        Panel.fit(
            "[bold cyan]TrendPulse[/bold cyan] - "
            "[bold green]GitHub 趋势分析[/bold green]",
            border_style="cyan",
        )
    )

    # 检查环境变量
    if not check_env_vars():
        console.print(
            "\n[yellow]提示: 创建 .env 文件并设置以下变量:[/yellow]"
            "\n  ANTHROPIC_API_KEY=your-api-key"
            "\n  ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic"
            "\n  GITHUB_TOKEN=your-github-token"
        )
        sys.exit(1)

    try:
        # 加载配置
        console.print("\n[bold]加载配置...[/bold]")
        settings = Settings()
        console.print(f"  ✓ 监控仓库: {len(settings.github_repos)} 个")
        console.print(f"  ✓ 模型: {settings.anthropic_model}")
        console.print(f"  ✓ API: {settings.anthropic_base_url}")

        # 初始化 Pipeline
        console.print("\n[bold]初始化 Pipeline...[/bold]")
        pipeline = TrendPulsePipeline(settings=settings)
        console.print("  ✓ 所有组件已就绪")

        # 运行每日分析
        console.print("\n[bold]开始分析...[/bold]")
        date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        report = pipeline.run_daily(date=date)

        # 显示结果
        result_text = (
            f"[bold green]分析完成！[/bold green]\n\n"
            f"日期: {report.date}\n"
            f"摘要: {report.summary_brief}\n"
            f"工程信号: {len(report.engineering_signals)}\n"
            f"研究信号: {len(report.research_signals)}\n"
            f"分析 PR 数: {report.stats.get('total_prs_analyzed', 0)}"
        )

        # 添加活跃度数据（如果有）
        if report.activity:
            result_text += (
                f"\n\n[bold cyan]仓库活跃度:[/bold cyan]\n"
                f"  总 Commit 数: {report.activity.get('total_commits', 0)}\n"
                f"  活跃仓库数: {report.activity.get('active_repos', 0)}\n"
                f"  新贡献者数: {report.activity.get('new_contributors', 0)}"
            )

        console.print(
            Panel(
                result_text,
                title="[bold green]分析结果[/bold green]",
                border_style="green",
            )
        )

        # 显示报告路径
        output_path = pipeline._get_output_path(date)
        if Path(output_path).exists():
            console.print(f"\n[green]报告已保存到:[/green] {output_path}")

    except Exception as e:
        console.print(
            Panel(
                f"[bold red]运行失败:[/bold red]\n\n{e}",
                title="[bold red]错误[/bold red]",
                border_style="red",
            )
        )
        raise


if __name__ == "__main__":
    main()
