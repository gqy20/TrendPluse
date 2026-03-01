#!/usr/bin/env python3
"""兼容入口：归一化每日报告统计字段。"""
# ruff: noqa: F401

from trendpluse.automation.normalize_daily_report_stats import (
    REQUIRED_KEYS,
    as_int,
    compute_high_impact,
    compute_unique_repos,
    main,
    normalize_file,
    normalize_stats,
)

if __name__ == "__main__":
    main()
