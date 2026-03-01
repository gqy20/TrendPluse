#!/usr/bin/env python3
"""discovery 候选到监控列表的桥接脚本"""

import argparse
import json
from pathlib import Path

from scripts.add_repo import batch_add_repos_to_config

PRIORITY_ORDER = {"low": 1, "medium": 2, "high": 3}


def _priority_allowed(priority: str, min_priority: str) -> bool:
    """判断优先级是否满足阈值"""
    return PRIORITY_ORDER.get(priority, 0) >= PRIORITY_ORDER.get(min_priority, 0)


def bridge_actionable_to_monitoring(
    actionable_file: str,
    config_file: str,
    min_priority: str = "medium",
    apply_changes: bool = False,
) -> dict:
    """将 discovery actionable 清单桥接到监控列表"""
    data = json.loads(Path(actionable_file).read_text(encoding="utf-8"))
    candidates = data.get("candidates", [])

    selected_items: list[dict[str, str]] = []
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
        selected_items.append({"repo": repo, "category": category})

    result = {
        "actionable_file": actionable_file,
        "min_priority": min_priority,
        "total_candidates": len(candidates),
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


def main() -> int:
    """命令行入口"""
    parser = argparse.ArgumentParser(description="桥接 discovery 候选到监控列表")
    parser.add_argument(
        "--actionable-file",
        required=True,
        help="discover 生成的 actionable 文件路径",
    )
    parser.add_argument(
        "--config-file",
        default="src/trendpluse/config.py",
        help="配置文件路径",
    )
    parser.add_argument(
        "--min-priority",
        default="medium",
        choices=["low", "medium", "high"],
        help="最小优先级阈值",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="是否实际写入配置文件（默认仅预览）",
    )

    args = parser.parse_args()

    result = bridge_actionable_to_monitoring(
        actionable_file=args.actionable_file,
        config_file=args.config_file,
        min_priority=args.min_priority,
        apply_changes=args.apply,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
