"""TrendPulse 运行脚本

执行每日 GitHub 趋势分析。
"""

import argparse
import asyncio
import os
import sys
from datetime import datetime

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

from trendpluse.app.runtime import run_daily_pipeline
from trendpluse.config import Settings
from trendpluse.logger import get_logger

console = Console()
logger = get_logger(__name__)


def check_env_vars() -> bool:
    """检查必需的环境变量

    支持多种环境变量名：ANTHROPIC_API_KEY、ANTHROPIC_AUTH_KEY、ANTHROPIC_AUTH_TOKEN
    """
    # 检查 API Key（支持多种环境变量名）
    api_key = (
        os.getenv("ANTHROPIC_API_KEY")
        or os.getenv("ANTHROPIC_AUTH_KEY")
        or os.getenv("ANTHROPIC_AUTH_TOKEN")
    )

    if not api_key:
        console.print(
            Panel(
                "[bold red]缺少必需的环境变量:[/bold red]\n"
                "  - ANTHROPIC_API_KEY 或 ANTHROPIC_AUTH_KEY 或 ANTHROPIC_AUTH_TOKEN",
                title="[bold red]配置错误[/bold red]",
                border_style="red",
            )
        )
        return False

    # 显示可选变量状态
    optional_vars = ["GITHUB_TOKEN", "ANTHROPIC_BASE_URL"]
    for var in optional_vars:
        value = os.getenv(var)
        status = "[green]✓[/green]" if value else "[yellow]✗[/yellow] (未设置)"
        console.print(f"{var}: {status}")

    return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="运行 TrendPulse 每日趋势分析")
    parser.parse_args()

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
            "\n  # 或使用备选环境变量:"
            "\n  # ANTHROPIC_AUTH_KEY=your-api-key"
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

        # 运行每日分析
        console.print("\n[bold]开始分析...[/bold]")
        logger.info("Daily pipeline started")
        date = datetime.now()
        result = asyncio.run(run_daily_pipeline(settings=settings, date=date))
        report = result.report
        logger.info("Daily pipeline finished")

        # 显示结果
        result_text = (
            f"[bold green]分析完成！[/bold green]\n\n"
            f"日期: {report.date}\n"
            f"摘要: {report.summary_brief}\n"
            f"工程信号: {len(report.engineering_signals)}\n"
            f"研究信号: {len(report.research_signals)}\n"
            f"分析 PR 数: {report.stats.total_prs_analyzed}"
        )

        # 添加活跃度数据（如果有）
        if report.activity:
            result_text += (
                f"\n\n[bold cyan]仓库活跃度:[/bold cyan]\n"
                f"  总 Commit 数: {report.activity.total_commits}\n"
                f"  活跃仓库数: {report.activity.active_repos_count}"
            )

        console.print(
            Panel(
                result_text,
                title="[bold green]分析结果[/bold green]",
                border_style="green",
            )
        )

        # 显示报告路径
        if result.output_path.exists():
            console.print(f"\n[green]报告已保存到:[/green] {result.output_path}")

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
