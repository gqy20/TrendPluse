#!/usr/bin/env python3
"""项目发现命令入口。"""

import argparse
import sys
from pathlib import Path

from rich.console import Console

from trendpluse.app.discovery import discover
from trendpluse.config import get_settings
from trendpluse.logger import get_logger, setup_logger

logger = get_logger(__name__)
console = Console()


def main() -> int:
    """主入口

    Returns:
        退出码
    """
    parser = argparse.ArgumentParser(
        description="自动发现热门 GitHub 项目",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--token",
        default=None,
        help="GitHub 访问令牌 (默认从 GITHUB_TOKEN 环境变量读取)",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["python", "typescript", "javascript", "go"],
        help="Trending 语言列表",
    )
    parser.add_argument(
        "--keywords",
        nargs="+",
        default=["AI agent", "LLM", "Claude", "RAG"],
        help="搜索关键词列表",
    )
    parser.add_argument(
        "--min-quality",
        type=float,
        default=60.0,
        help="最低质量分数 (默认: 60.0)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="回溯天数 (默认: 30)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("reports"),
        help="报告输出目录",
    )
    parser.add_argument(
        "--actionable-limit",
        type=int,
        default=10,
        help="actionable 候选输出上限（默认: 10）",
    )
    parser.add_argument(
        "--highlight-limit",
        type=int,
        default=10,
        help="AI 亮点分析项目上限（默认: 10）",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="详细输出",
    )

    args = parser.parse_args()

    # 如果没有提供 token，从配置中获取
    if args.token is None:
        args.token = get_settings().github_token

    # 设置日志级别
    setup_logger("DEBUG" if args.verbose else "INFO")

    # 检查 token
    if not args.token:
        console.print("[red]错误: 未提供 GitHub token[/red]")
        console.print("请通过 --token 参数或 GITHUB_TOKEN 环境变量提供")
        return 1

    try:
        report = discover(
            github_token=args.token,
            languages=args.languages,
            keywords=args.keywords,
            min_quality_score=args.min_quality,
            days=args.days,
            actionable_limit=args.actionable_limit,
            highlight_limit=args.highlight_limit,
            output_dir=args.output_dir,
        )

        # 打印摘要
        console.print("\n[bold]发现摘要:[/bold]")
        console.print(f"  总发现数: {report.total_discovered}")
        console.print(f"  通过评估: {report.passed_quality}")
        console.print(f"  高优先级: {report.high_priority}")
        console.print(f"  去重移除: {report.duplicates_removed}")
        console.print(f"  已在监控: {report.already_monitored}")

        if report.high_priority > 0:
            console.print("\n[bold green]高优先级推荐:[/bold green]")
            for i, p in enumerate(report.candidates, 1):
                if p.recommendation_priority == "high":
                    console.print(
                        f"  {i}. {p.repo} (质量: {p.quality_score:.0f}, "
                        f"Stars: {p.stars:,})"
                    )

        return 0

    except Exception as e:
        console.print(f"[red]错误: {e}[/red]")
        logger.exception("发现流程失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
