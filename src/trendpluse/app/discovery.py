"""项目发现应用编排。"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from rich.console import Console

from trendpluse.config import get_settings
from trendpluse.discovery import (
    Deduplicator,
    DiscoveryReporter,
    KeywordSearcher,
    ProjectClassifier,
    ProjectHighlightAnalyzer,
    QualityEvaluator,
    TrendingCollector,
)
from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveryReport

logger = get_logger(__name__)
console = Console()

MONITORING_CATEGORY_MAP: dict[str, str] = {
    "AI Agents": "Agentic AI 核心框架",
    "RAG/检索": "Agent 框架",
    "LLM 界面": "Anthropic 工具与集成",
    "机器学习框架": "Anthropic 研究与评估",
    "开发工具": "AI 编程助手",
    "DevOps/基础设施": "其他",
    "监控/观测": "其他",
    "Web 框架": "其他",
    "数据/基础设施": "Agent 框架",
    "学习资源": "Anthropic 研究与评估",
    "其他": "其他",
}


def build_actionable_candidates(
    candidates: list,
    max_candidates: int = 10,
) -> list[dict]:
    """构建可执行候选清单。"""
    classifier = ProjectClassifier()
    classified = classifier.classify_batch(candidates)

    actionable = []
    for project in candidates:
        if project.recommendation_priority not in ("high", "medium"):
            continue

        categories = classified.get(project.repo, ["其他"])
        suggested_category = "其他"
        for category in categories:
            mapped = MONITORING_CATEGORY_MAP.get(category)
            if mapped:
                suggested_category = mapped
                break

        actionable.append(
            {
                "repo": project.repo,
                "name": project.name,
                "priority": project.recommendation_priority,
                "quality_score": round(project.quality_score, 2),
                "discovery_source": project.discovery_source,
                "discovery_reason": project.discovery_reason,
                "classified_categories": categories,
                "suggested_category": suggested_category,
            }
        )

    priority_order = {"high": 3, "medium": 2, "low": 1}
    actionable.sort(
        key=lambda item: (
            -priority_order.get(str(item["priority"]), 0),
            -float(item["quality_score"]),
            str(item["repo"]),
        )
    )
    return actionable[:max_candidates]


def load_monitored_repos() -> set[str]:
    """加载已在监控的仓库列表。"""
    settings = get_settings()
    return set(settings.github_repos)


def discover(
    github_token: str,
    languages: list[str] | None = None,
    keywords: list[str] | None = None,
    min_quality_score: float = 60.0,
    days: int = 30,
    actionable_limit: int = 10,
    highlight_limit: int = 10,
    output_dir: Path | None = None,
) -> DiscoveryReport:
    """执行项目发现流程。"""
    if languages is None:
        languages = ["python", "typescript", "javascript", "go"]
    if keywords is None:
        keywords = ["AI agent", "LLM", "Claude", "RAG"]

    monitored_repos = load_monitored_repos()
    logger.info(f"已监控仓库: {len(monitored_repos)} 个")

    console.print("[cyan]采集 Trending 项目...[/cyan]")
    trending_collector = TrendingCollector(github_token)
    trending_projects = trending_collector.discover(
        languages=languages,
        days=days,
        min_stars=1000,
        max_results=30,
    )
    logger.info(f"Trending 发现 {len(trending_projects)} 个项目")

    console.print("[cyan]关键词搜索项目...[/cyan]")
    keyword_searcher = KeywordSearcher(
        github_token=github_token,
        keywords=keywords,
        min_stars=500,
        max_results=20,
    )
    keyword_projects = keyword_searcher.discover(days=days)
    logger.info(f"关键词发现 {len(keyword_projects)} 个项目")

    all_candidates = trending_projects + keyword_projects
    logger.info(f"候选项目总数: {len(all_candidates)}")

    console.print("[cyan]质量评估...[/cyan]")
    evaluator = QualityEvaluator(min_quality_score=min_quality_score)
    evaluated = evaluator.evaluate(all_candidates)

    new_projects = [p for p in evaluated if p.repo not in monitored_repos]
    already_monitored = len(evaluated) - len(new_projects)
    logger.info(f"新项目: {len(new_projects)}, 已监控: {already_monitored}")

    console.print("[cyan]去重...[/cyan]")
    deduplicator = Deduplicator()
    deduplicated, removed_count = deduplicator.deduplicate_with_count(new_projects)
    deduplicated.sort(key=lambda p: p.quality_score, reverse=True)

    console.print("[cyan]AI 分析项目亮点...[/cyan]")
    settings = get_settings()
    if settings.anthropic_api_key:
        highlight_analyzer = ProjectHighlightAnalyzer(
            api_key=settings.anthropic_api_key,
            model=settings.anthropic_model,
            base_url=settings.anthropic_base_url,
            retry_max_attempts=settings.llm_retry_max_attempts,
            retry_wait_min=settings.llm_retry_wait_min,
            retry_wait_max=settings.llm_retry_wait_max,
        )
        projects_to_analyze = [
            p for p in deduplicated if p.recommendation_priority in ("high", "medium")
        ][:highlight_limit]
        highlights = highlight_analyzer.analyze_batch(projects_to_analyze)
        for project in deduplicated:
            if project.repo in highlights:
                project.highlight = highlights[project.repo]
        logger.info(f"AI 分析完成 {len(highlights)} 个项目")
    else:
        console.print("[yellow]未配置 API Key，跳过 AI 分析[/yellow]")

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

    if output_dir:
        output_dir = Path(output_dir)
        if output_dir.name == "reports":
            output_dir = output_dir / "discovery"
        output_dir.mkdir(parents=True, exist_ok=True)

        reporter = DiscoveryReporter()
        md_file = output_dir / f"discovery-{report.date}.md"
        reporter.save_markdown(report, md_file)

        json_file = output_dir / f"discovery-{report.date}.json"
        reporter.save_json(report, json_file)

        actionable_file = output_dir / f"discovery-{report.date}-actionable.json"
        actionable_candidates = build_actionable_candidates(
            report.candidates, max_candidates=actionable_limit
        )
        actionable_data: dict[str, object] = {
            "date": report.date,
            "generated_at": datetime.now().isoformat(),
            "total_candidates": len(report.candidates),
            "selected_count": len(actionable_candidates),
            "candidates": actionable_candidates,
        }
        actionable_file.write_text(
            json.dumps(actionable_data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        console.print(
            "[green]报告已保存:[/green] "
            f"{md_file.name}, {json_file.name}, {actionable_file.name}"
        )

    return report
