"""添加仓库命令入口。"""

import argparse

from trendpluse.app.add_repo import run_add_repo_command


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="添加仓库到配置")
    parser.add_argument("--repo", help="仓库路径，格式：owner/repo")
    parser.add_argument("--category", help="分类名称")
    parser.add_argument(
        "--batch-file",
        help=(
            "批量输入文件（JSON），支持 [{repo,category}] 或 discovery actionable 格式"
        ),
    )
    parser.add_argument(
        "--config-file",
        default="repos.json",
        help="配置文件路径",
    )
    args = parser.parse_args()
    raise SystemExit(
        run_add_repo_command(
            repo=args.repo,
            category=args.category,
            batch_file=args.batch_file,
            config_file=args.config_file,
        )
    )


if __name__ == "__main__":
    main()
