"""Issue Agent 结果读取与聚合"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from os import PathLike
from pathlib import Path

from pydantic import ValidationError

from trendpluse.models.issue_agent import IssueAgentPainPoint, IssueAgentReport

logger = logging.getLogger(__name__)


def load_issue_agent_report(
    base_dir: str | PathLike[str] | object,
    snapshot_date: str,
) -> IssueAgentReport:
    """读取并合并 Agent 输出结果。

    读取目录：{base_dir}/{snapshot_date}/analysis/*.analysis.json
    """
    if not isinstance(base_dir, (str, PathLike)):
        return IssueAgentReport()

    analysis_dir = Path(base_dir) / snapshot_date / "analysis"
    if not analysis_dir.exists():
        return IssueAgentReport()

    files = sorted(analysis_dir.glob("*.analysis.json"))
    merged_counts: dict[str, int] = defaultdict(int)
    merged_repos: dict[str, set[str]] = defaultdict(set)
    merged_urls: dict[str, list[str]] = defaultdict(list)
    parsed_files = 0
    failed_files = 0
    failed_samples: list[str] = []

    for path in files:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            validated = IssueAgentReport.model_validate(raw)
        except (json.JSONDecodeError, ValidationError):
            failed_files += 1
            if len(failed_samples) < 5:
                failed_samples.append(path.name)
            continue

        parsed_files += 1
        for item in validated.top_pain_points:
            topic = item.topic.strip()
            if not topic:
                continue
            count = item.count
            merged_counts[topic] += max(1, count)
            for repo in item.affected_repos:
                merged_repos[topic].add(str(repo))
            for url in item.sample_urls:
                merged_urls[topic].append(str(url))

    merged: list[IssueAgentPainPoint] = []
    for topic, count in merged_counts.items():
        merged.append(
            IssueAgentPainPoint(
                topic=topic,
                count=count,
                affected_repos=sorted(merged_repos[topic]),
                sample_urls=merged_urls[topic][:5],
            )
        )

    merged.sort(key=lambda p: p.count, reverse=True)
    if failed_files > 0:
        logger.warning(
            "Issue Agent 分析文件解析失败: failed=%d, samples=%s",
            failed_files,
            ",".join(failed_samples),
        )
    return IssueAgentReport(
        top_pain_points=merged[:5],
        parsed_files=parsed_files,
        failed_files=failed_files,
        failed_samples=failed_samples,
    )
