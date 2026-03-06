"""同步监控仓库到文档命令入口。"""

import argparse
from pathlib import Path

from trendpluse.app.sync_repos_to_docs import run_sync_repos_to_docs


def main() -> int:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="同步监控仓库列表到文档")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="试运行模式，不修改文件",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="检查模式，如果文档不是最新的则返回非零退出码",
    )
    args = parser.parse_args()
    return run_sync_repos_to_docs(
        dry_run=args.dry_run,
        check=args.check,
        project_root=Path.cwd().resolve(),
    )


if __name__ == "__main__":
    raise SystemExit(main())
