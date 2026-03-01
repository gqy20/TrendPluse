#!/usr/bin/env python3
"""兼容入口：生成报告索引。"""
# ruff: noqa: F401

from trendpluse.automation.generate_report_index import (
    _ProjectInfo,
    ensure_reports_structure,
    extract_discovery_report_info,
    extract_report_info,
    extract_weekly_report_info,
    generate_discovery_index,
    generate_index,
    main,
    sync_discovery_reports_to_docs,
    sync_reports_to_docs,
)

if __name__ == "__main__":
    main()
