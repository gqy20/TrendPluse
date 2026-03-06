"""归一化日报统计命令入口。"""

import argparse

from trendpluse.app.normalize_daily_report_stats import (
    run_normalize_daily_report_stats,
)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="归一化日报 stats 字段")
    parser.add_argument(
        "--reports-dir",
        default="reports/daily",
        help="日报目录路径（默认: reports/daily）",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="执行写入修复（默认仅预览）",
    )
    args = parser.parse_args()
    run_normalize_daily_report_stats(args.reports_dir, apply=args.apply)


if __name__ == "__main__":
    main()
