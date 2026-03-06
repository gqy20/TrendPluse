"""discovery 桥接命令入口。"""

import argparse

from trendpluse.automation.bridge_discovery_to_monitoring import (
    run_bridge_discovery_command,
)


def main() -> int:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="桥接 discovery 候选到监控列表")
    parser.add_argument(
        "--actionable-file",
        required=True,
        help="discover 生成的 actionable 文件路径",
    )
    parser.add_argument(
        "--config-file",
        default="repos.json",
        help="配置文件路径",
    )
    parser.add_argument(
        "--min-priority",
        default="medium",
        choices=["low", "medium", "high"],
        help="最小优先级阈值",
    )
    parser.add_argument(
        "--max-add-per-run",
        type=int,
        default=10,
        help="每次最多新增仓库数量（默认 10）",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="是否实际写入配置文件（默认仅预览）",
    )
    args = parser.parse_args()
    return run_bridge_discovery_command(
        actionable_file=args.actionable_file,
        config_file=args.config_file,
        min_priority=args.min_priority,
        max_add_per_run=args.max_add_per_run,
        apply=args.apply,
    )


if __name__ == "__main__":
    raise SystemExit(main())
