"""Issue Agent 结果读取与聚合"""

from __future__ import annotations

import json
from collections import defaultdict
from os import PathLike
from pathlib import Path

from trendpluse.models.issue_agent import IssueAgentPainPoint, IssueAgentReport


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

    merged_counts: dict[str, int] = defaultdict(int)
    merged_repos: dict[str, set[str]] = defaultdict(set)
    merged_urls: dict[str, list[str]] = defaultdict(list)

    for path in sorted(analysis_dir.glob("*.analysis.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        pain_points = data.get("top_pain_points", [])
        if not isinstance(pain_points, list):
            continue

        for item in pain_points:
            topic = str(item.get("topic", "")).strip()
            if not topic:
                continue
            count = int(item.get("count", 1))
            merged_counts[topic] += max(1, count)
            for repo in item.get("affected_repos", []) or []:
                merged_repos[topic].add(str(repo))
            for url in item.get("sample_urls", []) or []:
                merged_urls[topic].append(str(url))

    merged = []
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
    return IssueAgentReport(top_pain_points=merged[:5])
