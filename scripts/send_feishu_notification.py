#!/usr/bin/env python3
"""兼容入口：发送飞书通知。"""
# ruff: noqa: F401

from trendpluse.cli.send_feishu_notification import (
    find_report_json,
    load_report_from_json,
    main,
)

if __name__ == "__main__":
    main()
