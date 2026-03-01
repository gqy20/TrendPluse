#!/usr/bin/env python3
"""兼容入口：发送周报飞书通知。"""
# ruff: noqa: F401

from trendpluse.cli.send_weekly_feishu import (
    find_weekly_report_json,
    load_weekly_report_from_json,
    main,
)

if __name__ == "__main__":
    main()
