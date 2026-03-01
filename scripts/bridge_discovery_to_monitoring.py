#!/usr/bin/env python3
"""兼容入口：discovery 候选桥接到监控列表。"""
# ruff: noqa: F401

from trendpluse.automation.bridge_discovery_to_monitoring import (
    PRIORITY_ORDER,
    bridge_actionable_to_monitoring,
    main,
)

if __name__ == "__main__":
    raise SystemExit(main())
