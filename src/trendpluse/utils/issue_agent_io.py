"""Issue Agent 结果读取与聚合"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from os import PathLike
from pathlib import Path

from pydantic import ValidationError

from trendpluse.models.issue_agent import (
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)

logger = logging.getLogger(__name__)


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
            count = item.count
            merged_counts[topic] += max(1, count)
            for repo in item.affected_repos:
                merged_repos[topic].add(str(repo))
            for url in item.sample_urls:
                merged_urls[topic].append(str(url))
            for alias in item.aliases:
                merged_aliases[topic].add(str(alias))
            if item.confidence is not None:
                merged_confidences[topic].append(float(item.confidence))
            if item.priority in {"P0", "P1", "P2"}:
                merged_priorities[topic].add(item.priority)
            if item.review_reason:
                merged_reasons[topic].append(item.review_reason)
            if item.summary:
                merged_summaries[topic].append(item.summary)
            if item.category:
                merged_categories[topic].add(item.category)
            if item.id:
                merged_source_signal_ids[topic].add(item.id)
            for source_issue in item.source_issues:
                merged_source_issues[topic][source_issue.url] = source_issue

    merged: list[IssueAgentPainPoint] = []
    for topic, count in merged_counts.items():
        priority = None
        if merged_priorities[topic]:
            priority = sorted(merged_priorities[topic], key=lambda p: int(p[1]))[0]
        merged.append(
            IssueAgentPainPoint(
                topic=topic,
                count=count,
                affected_repos=sorted(merged_repos[topic]),
                sample_urls=merged_urls[topic][:5],
                aliases=sorted(merged_aliases[topic]),
                confidence=max(merged_confidences[topic])
                if merged_confidences[topic]
                else None,
                priority=priority,
                summary=merged_summaries[topic][0] if merged_summaries[topic] else None,
                category=sorted(merged_categories[topic])[0]
                if merged_categories[topic]
                else None,
                review_reason=merged_reasons[topic][0]
                if merged_reasons[topic]
                else None,
                source_issues=list(merged_source_issues[topic].values())[:10],
                source_signal_ids=sorted(merged_source_signal_ids[topic]),
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
    return IssueAgentReport(
        top_pain_points=merged[:5],
        repo_reports=repo_reports,
        expected_files=expected_files,
        generated_files=generated_files,
        parsed_files=parsed_files,
        failed_files=total_failed_files,
        failed_samples=all_failed_samples,
        quality_score=quality_score,
        quality_status=quality_status,
    )


def _parse_repo_issue_signal_report(
    *,
    raw: dict,
    path: Path,
    snapshot_date: str,
) -> RepoIssueSignalReport:
    """解析仓库级 Issue Signal 报告。"""
    report = RepoIssueSignalReport.model_validate(raw)
    if not report.repo:
        report.repo = path.stem.removesuffix(".analysis").replace("__", "/")
    if not report.snapshot_date:
        report.snapshot_date = snapshot_date
    return report
