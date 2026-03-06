"""discovery 候选到监控列表的桥接脚本"""

import json
from pathlib import Path

from trendpluse.automation.add_repo import batch_add_repos_to_config

PRIORITY_ORDER = {"low": 1, "medium": 2, "high": 3}


def _priority_allowed(priority: str, min_priority: str) -> bool:
    """判断优先级是否满足阈值"""
    return PRIORITY_ORDER.get(priority, 0) >= PRIORITY_ORDER.get(min_priority, 0)


def _to_float(value: object) -> float:
    """将任意值安全转换为 float"""
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def bridge_actionable_to_monitoring(
    actionable_file: str,
    config_file: str,
    min_priority: str = "medium",
    max_add_per_run: int = 10,
    apply_changes: bool = False,
) -> dict:
    """将 discovery actionable 清单桥接到监控列表"""
    data = json.loads(Path(actionable_file).read_text(encoding="utf-8"))
    candidates = data.get("candidates", [])

    selected_candidates: list[dict[str, object]] = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue

        priority = str(candidate.get("priority", "low")).strip().lower()
        if not _priority_allowed(priority, min_priority):
            continue

        repo = str(candidate.get("repo", "")).strip()
        category = str(
            candidate.get("category") or candidate.get("suggested_category") or "其他"
        ).strip()
        quality_score_raw = candidate.get("quality_score", 0)
        quality_score = (
            float(quality_score_raw)
            if isinstance(quality_score_raw, int | float)
            else 0.0
        )
        selected_candidates.append(
            {
                "repo": repo,
                "category": category,
                "priority": priority,
                "quality_score": quality_score,
            }
        )

    # 先按优先级，再按质量分，最后按 repo 名称稳定排序
    selected_candidates.sort(
        key=lambda c: (
            -PRIORITY_ORDER.get(str(c.get("priority", "low")), 0),
            -_to_float(c.get("quality_score", 0.0)),
            str(c.get("repo", "")),
        )
    )

    capped = selected_candidates[:max_add_per_run]
    selected_items = [
        {"repo": str(item["repo"]), "category": str(item["category"])}
        for item in capped
    ]

    result = {
        "actionable_file": actionable_file,
        "min_priority": min_priority,
        "max_add_per_run": max_add_per_run,
        "total_candidates": len(candidates),
        "selected_before_cap": len(selected_candidates),
        "selected_count": len(selected_items),
        "selected_items": selected_items,
        "batch_result": None,
    }

    if apply_changes:
        result["batch_result"] = batch_add_repos_to_config(
            config_file=config_file,
            items=selected_items,
        )

    return result


def run_bridge_discovery_command(
    *,
    actionable_file: str,
    config_file: str = "repos.json",
    min_priority: str = "medium",
    max_add_per_run: int = 10,
    apply: bool = False,
) -> int:
    """执行 discovery 桥接命令。"""
    result = bridge_actionable_to_monitoring(
        actionable_file=actionable_file,
        config_file=config_file,
        min_priority=min_priority,
        max_add_per_run=max_add_per_run,
        apply_changes=apply,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0
