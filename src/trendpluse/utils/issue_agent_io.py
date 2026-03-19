"""Issue Agent 结果读取与聚合"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from os import PathLike
from pathlib import Path
from typing import cast

from pydantic import ValidationError

from trendpluse.models.agent_usage import AgentMetricsSummary
from trendpluse.models.issue_agent import (
    ISSUE_AGENT_CATEGORY_VALUES,
    IssueAgentCategory,
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)

logger = logging.getLogger(__name__)


def _merge_key(pain_point: IssueAgentPainPoint) -> str:
    """生成全局聚合键，优先使用 category，兼容旧 topic 聚合。"""
    if pain_point.category and pain_point.category.strip():
        return f"category:{pain_point.category.strip()}"
    return f"topic:{pain_point.topic.strip()}"


def _sort_key(pain_point: IssueAgentPainPoint) -> tuple[int, float, int]:
    priority_rank = {"P0": 0, "P1": 1, "P2": 2}
    rank = priority_rank.get(pain_point.priority or "", 3)
    confidence = pain_point.confidence if pain_point.confidence is not None else -1.0
    return (rank, -confidence, -pain_point.count)


def _compute_quality_metrics(
    *,
    expected_files: int,
    generated_files: int,
    parsed_files: int,
    failed_files: int,
) -> tuple[float, str]:
    if expected_files == 0 and generated_files == 0:
        return 1.0, "no_data"

    coverage = generated_files / expected_files if expected_files > 0 else 0.0
    parse_rate = parsed_files / generated_files if generated_files > 0 else 0.0
    score = round(min(1.0, max(0.0, 0.7 * coverage + 0.3 * parse_rate)), 3)

    if failed_files == 0 and coverage >= 0.95 and parse_rate >= 0.95:
        return score, "good"
    if coverage >= 0.8 and parse_rate >= 0.8:
        return score, "warning"
    return score, "poor"


def _compute_semantic_quality_metrics(
    pain_points: list[IssueAgentPainPoint],
) -> tuple[int, int, float]:
    """计算语义层质量指标。"""
    if not pain_points:
        return 0, 0, 1.0

    cross_repo_item_count = sum(
        1 for item in pain_points if len(set(item.affected_repos)) > 1
    )
    other_category_count = sum(1 for item in pain_points if item.category == "other")
    categorized_count = sum(1 for item in pain_points if item.category is not None)
    category_coverage = round(categorized_count / len(pain_points), 3)
    return cross_repo_item_count, other_category_count, category_coverage


def _normalize_category(values: set[str]) -> IssueAgentCategory | None:
    """从聚合值中提取合法 category。"""
    if not values:
        return None
    for value in sorted(values):
        if value in ISSUE_AGENT_CATEGORY_VALUES:
            return cast(IssueAgentCategory, value)
    return None


def summarize_issue_agent_run_status(report: IssueAgentReport) -> str:
    """根据 Issue Agent 报告汇总运行状态。"""
    if report.expected_files == 0 and report.generated_files == 0:
        return "no_data"
    if report.parsed_files > 0 and report.failed_files == 0:
        return "success"
    if report.parsed_files > 0 and report.failed_files > 0:
        return "partial_failure"
    if report.expected_files > 0 and report.parsed_files == 0:
        return "failed"
    return "unknown"


def load_issue_agent_report(
    base_dir: str | PathLike[str] | object,
    snapshot_date: str,
) -> IssueAgentReport:
    """读取并合并 Agent 输出结果。

    读取目录：{base_dir}/{snapshot_date}/analysis/*.analysis.json
    """
    if not isinstance(base_dir, (str, PathLike)):
        return IssueAgentReport()

    snapshot_dir = Path(base_dir) / snapshot_date
    input_files = sorted(snapshot_dir.glob("*.jsonl"))
    expected_files = len(input_files)

    analysis_dir = snapshot_dir / "analysis"
    if not analysis_dir.exists():
        missing_samples = [
            f"{path.stem}.analysis.json (missing)" for path in input_files[:5]
        ]
        quality_score, quality_status = _compute_quality_metrics(
            expected_files=expected_files,
            generated_files=0,
            parsed_files=0,
            failed_files=expected_files,
        )
        return IssueAgentReport(
            expected_files=expected_files,
            generated_files=0,
            failed_files=expected_files,
            failed_samples=missing_samples,
            quality_score=quality_score,
            quality_status=quality_status,
        )

    files = sorted(analysis_dir.glob("*.analysis.json"))
    generated_files = len(files)
    existing_analysis_names = {path.name for path in files}
    missing_files = [
        f"{path.stem}.analysis.json (missing)"
        for path in input_files
        if f"{path.stem}.analysis.json" not in existing_analysis_names
    ]
    merged_topics: dict[str, list[str]] = defaultdict(list)
    merged_counts: dict[str, int] = defaultdict(int)
    merged_repos: dict[str, set[str]] = defaultdict(set)
    merged_urls: dict[str, list[str]] = defaultdict(list)
    merged_aliases: dict[str, set[str]] = defaultdict(set)
    merged_confidences: dict[str, list[float]] = defaultdict(list)
    merged_priorities: dict[str, set[str]] = defaultdict(set)
    merged_reasons: dict[str, list[str]] = defaultdict(list)
    merged_summaries: dict[str, list[str]] = defaultdict(list)
    merged_categories: dict[str, set[str]] = defaultdict(set)
    merged_source_issues: dict[str, dict[str, IssueAgentSourceIssue]] = defaultdict(
        dict
    )
    merged_source_signal_ids: dict[str, set[str]] = defaultdict(set)
    parsed_files = 0
    failed_files = 0
    failed_samples: list[str] = []
    repo_reports: list[RepoIssueSignalReport] = []

    for path in files:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            validated_repo = _parse_repo_issue_signal_report(
                raw=raw,
                path=path,
                snapshot_date=snapshot_date,
            )
        except (json.JSONDecodeError, ValidationError):
            failed_files += 1
            if len(failed_samples) < 5:
                failed_samples.append(path.name)
            continue

        parsed_files += 1
        repo_reports.append(validated_repo)
        for item in validated_repo.signals:
            topic = item.topic.strip()
            if not topic:
                continue
            key = _merge_key(item)
            merged_topics[key].append(topic)
            count = item.count
            merged_counts[key] += max(1, count)
            for repo in item.affected_repos:
                merged_repos[key].add(str(repo))
            for url in item.sample_urls:
                merged_urls[key].append(str(url))
            for alias in item.aliases:
                merged_aliases[key].add(str(alias))
            if item.confidence is not None:
                merged_confidences[key].append(float(item.confidence))
            if item.priority in {"P0", "P1", "P2"}:
                merged_priorities[key].add(item.priority)
            if item.review_reason:
                merged_reasons[key].append(item.review_reason)
            if item.summary:
                merged_summaries[key].append(item.summary)
            if item.category:
                merged_categories[key].add(item.category)
            if item.id:
                merged_source_signal_ids[key].add(item.id)
            for source_issue in item.source_issues:
                merged_source_issues[key][source_issue.url] = source_issue

    merged: list[IssueAgentPainPoint] = []
    for key, count in merged_counts.items():
        priority = None
        if merged_priorities[key]:
            priority = sorted(merged_priorities[key], key=lambda p: int(p[1]))[0]
        topic = merged_topics[key][0] if merged_topics[key] else key
        merged.append(
            IssueAgentPainPoint(
                topic=topic,
                count=count,
                affected_repos=sorted(merged_repos[key]),
                sample_urls=merged_urls[key][:5],
                aliases=sorted(merged_aliases[key]),
                confidence=max(merged_confidences[key])
                if merged_confidences[key]
                else None,
                priority=priority,
                summary=merged_summaries[key][0] if merged_summaries[key] else None,
                category=_normalize_category(merged_categories[key]),
                review_reason=merged_reasons[key][0] if merged_reasons[key] else None,
                source_issues=list(merged_source_issues[key].values())[:10],
                source_signal_ids=sorted(merged_source_signal_ids[key]),
            )
        )

    merged.sort(key=_sort_key)
    if failed_files > 0:
        logger.warning(
            "Issue Agent 分析文件解析失败: failed=%d, samples=%s",
            failed_files,
            ",".join(failed_samples),
        )

    all_failed_samples = (failed_samples + missing_files)[:5]
    total_failed_files = failed_files + len(missing_files)
    quality_score, quality_status = _compute_quality_metrics(
        expected_files=expected_files,
        generated_files=generated_files,
        parsed_files=parsed_files,
        failed_files=total_failed_files,
    )
    top_pain_points = merged[:5]
    (
        cross_repo_item_count,
        other_category_count,
        category_coverage,
    ) = _compute_semantic_quality_metrics(top_pain_points)

    return IssueAgentReport(
        top_pain_points=top_pain_points,
        repo_reports=repo_reports,
        expected_files=expected_files,
        generated_files=generated_files,
        parsed_files=parsed_files,
        failed_files=total_failed_files,
        failed_samples=all_failed_samples,
        quality_score=quality_score,
        quality_status=quality_status,
        cross_repo_item_count=cross_repo_item_count,
        other_category_count=other_category_count,
        category_coverage=category_coverage,
        agent_metrics_summary=AgentMetricsSummary.from_runs(
            [repo.agent_run_metrics for repo in repo_reports]
        ),
    )


def _parse_repo_issue_signal_report(
    *,
    raw: dict,
    path: Path,
    snapshot_date: str,
) -> RepoIssueSignalReport:
    """解析仓库级 Issue Signal 报告。"""
    report = RepoIssueSignalReport.model_validate(raw)
    if not isinstance(report, RepoIssueSignalReport):
        raise TypeError("Invalid RepoIssueSignalReport")
    if not report.repo:
        report.repo = path.stem.removesuffix(".analysis").replace("__", "/")
    if not report.snapshot_date:
        report.snapshot_date = snapshot_date
    return report
