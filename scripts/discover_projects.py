#!/usr/bin/env python3
"""项目发现脚本

自动发现热门 GitHub 项目并生成报告。
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console

from trendpluse.config import get_settings
from trendpluse.discovery import (
    Deduplicator,
    DiscoveryReporter,
    KeywordSearcher,
    QualityEvaluator,
    TrendingCollector,
)
from trendpluse.logger import get_logger, setup_logger
from trendpluse.models.discovery import DiscoveryReport

logger = get_logger(__name__)
console = Console()


def load_monitored_repos() -> set[str]:
    """加载已在监控的仓库列表

    Returns:
        仓库名称集合
    """
    settings = get_settings()
    return set(settings.github_repos)


def discover(
    github_token: str,
    languages: list[str] | None = None,
    keywords: list[str] | None = None,
    min_quality_score: float = 60.0,
    days: int = 30,
    output_dir: Path | None = None,
) -> DiscoveryReport:
    """执行项目发现流程

    Args:
        github_token: GitHub 访问令牌
        languages: Trending 语言列表
        keywords: 关键词列表
        min_quality_score: 最低质量分数
        days: 回溯天数
        output_dir: 输出目录

    Returns:
        发现报告
    """
    # 默认参数
    if languages is None:
        languages = ["python", "typescript", "javascript", "go"]
    if keywords is None:
        keywords = ["AI agent", "LLM", "Claude", "RAG"]

    # 加载已监控仓库
    monitored_repos = load_monitored_repos()
    logger.info(f"已监控仓库: {len(monitored_repos)} 个")

    # 1. 采集 Trending 项目
    console.print("[cyan]采集 Trending 项目...[/cyan]")
    trending_collector = TrendingCollector(github_token)
    trending_projects = trending_collector.discover(
        languages=languages,
        days=days,
        min_stars=1000,
        max_results=30,
    )
    logger.info(f"Trending 发现 {len(trending_projects)} 个项目")

    # 2. 关键词搜索
    console.print("[cyan]关键词搜索项目...[/cyan]")
    keyword_searcher = KeywordSearcher(
        github_token=github_token,
        keywords=keywords,
        min_stars=500,
        max_results=20,
    )
    keyword_projects = keyword_searcher.discover(days=days)
    logger.info(f"关键词发现 {len(keyword_projects)} 个项目")

    # 3. 合并所有候选项目
    all_candidates = trending_projects + keyword_projects
    logger.info(f"候选项目总数: {len(all_candidates)}")

    # 4. 质量评估
    console.print("[cyan]质量评估...[/cyan]")
    evaluator = QualityEvaluator(min_quality_score=min_quality_score)
    evaluated = evaluator.evaluate(all_candidates)

    # 5. 过滤已监控仓库
    new_projects = [p for p in evaluated if p.repo not in monitored_repos]
    already_monitored = len(evaluated) - len(new_projects)
    logger.info(f"新项目: {len(new_projects)}, 已监控: {already_monitored}")

    # 6. 去重
    console.print("[cyan]去重...[/cyan]")
    deduplicator = Deduplicator()
    deduplicated, removed_count = deduplicator.deduplicate_with_count(new_projects)

    # 7. 按质量分数排序
    deduplicated.sort(key=lambda p: p.quality_score, reverse=True)

    # 8. 生成报告
    report = DiscoveryReport(
        date=datetime.now().strftime("%Y-%m-%d"),
        total_discovered=len(all_candidates),
        passed_quality=len([p for p in evaluated if p.recommended]),
        high_priority=len(
            [p for p in deduplicated if p.recommendation_priority == "high"]
        ),
        duplicates_removed=removed_count,
        already_monitored=already_monitored,
        candidates=deduplicated,
    )

    # 9. 保存报告
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        reporter = DiscoveryReporter()

        # Markdown 报告
        md_file = output_dir / f"discovery-{report.date}.md"
        reporter.save_markdown(report, md_file)

        # JSON 报告
        json_file = output_dir / f"discovery-{report.date}.json"
        reporter.save_json(report, json_file)

        console.print(f"[green]报告已保存:[/green] {md_file.name}, {json_file.name}")

    return report


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
        default=Path("data/discovery/reports"),
        help="报告输出目录",
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
