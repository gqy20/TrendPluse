"""discovery 到监控列表桥接脚本测试。"""

from __future__ import annotations

import json
from pathlib import Path


def _write_repo_config(path: Path) -> None:
    path.write_text(
        json.dumps(
            [
                {
                    "url": "https://github.com/openai/swarm",
                    "description": "Swarm",
                },
                {
                    "url": "https://github.com/cline/cline",
                    "description": "Cline",
                },
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def test_bridge_actionable_to_monitoring(tmp_path: Path):
    """测试：仅将高/中优先级仓库写入监控列表。"""
    actionable_path = tmp_path / "discovery-actionable.json"
    actionable_path.write_text(
        json.dumps(
            {
                "date": "2026-03-01",
                "candidates": [
                    {
                        "repo": "owner/high-one",
                        "priority": "high",
                        "suggested_category": "Agentic AI 核心框架",
                    },
                    {
                        "repo": "owner/medium-one",
                        "priority": "medium",
                        "suggested_category": "其他",
                    },
                    {
                        "repo": "owner/low-one",
                        "priority": "low",
                        "suggested_category": "Agentic AI 核心框架",
                    },
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    config_path = tmp_path / "repos.json"
    _write_repo_config(config_path)

    from trendpluse.app.bridge_discovery_to_monitoring import (
        bridge_actionable_to_monitoring,
    )

    result = bridge_actionable_to_monitoring(
        actionable_file=str(actionable_path),
        config_file=str(config_path),
        min_priority="medium",
        apply_changes=True,
    )

    assert result["selected_count"] == 2
    assert "owner/high-one" in result["batch_result"]["added"]
    assert "owner/medium-one" in result["batch_result"]["added"]
    assert "owner/low-one" not in result["batch_result"]["added"]

    updated_entries = json.loads(config_path.read_text(encoding="utf-8"))
    urls = [entry["url"] for entry in updated_entries]
    assert "https://github.com/owner/high-one" in urls
    assert "https://github.com/owner/medium-one" in urls


def test_bridge_respects_max_add_per_run(tmp_path: Path):
    """测试：bridge 应限制每次最多新增数量。"""
    actionable_path = tmp_path / "discovery-actionable.json"
    actionable_path.write_text(
        json.dumps(
            {
                "date": "2026-03-01",
                "candidates": [
                    {
                        "repo": "owner/high-low-score",
                        "priority": "high",
                        "quality_score": 70,
                        "suggested_category": "Agentic AI 核心框架",
                    },
                    {
                        "repo": "owner/high-top-score",
                        "priority": "high",
                        "quality_score": 95,
                        "suggested_category": "Agentic AI 核心框架",
                    },
                    {
                        "repo": "owner/medium-top-score",
                        "priority": "medium",
                        "quality_score": 99,
                        "suggested_category": "其他",
                    },
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    config_path = tmp_path / "repos.json"
    _write_repo_config(config_path)

    from trendpluse.app.bridge_discovery_to_monitoring import (
        bridge_actionable_to_monitoring,
    )

    result = bridge_actionable_to_monitoring(
        actionable_file=str(actionable_path),
        config_file=str(config_path),
        min_priority="medium",
        max_add_per_run=1,
        apply_changes=True,
    )

    assert result["selected_before_cap"] == 3
    assert result["selected_count"] == 1
    assert result["batch_result"]["added"] == ["owner/high-top-score"]
