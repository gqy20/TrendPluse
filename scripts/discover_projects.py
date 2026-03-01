#!/usr/bin/env python3
"""兼容入口：项目发现脚本。"""
# ruff: noqa: F401

import sys

from trendpluse.cli.discover_projects import (
    MONITORING_CATEGORY_MAP,
    discover,
    load_monitored_repos,
    main,
)

if __name__ == "__main__":
    sys.exit(main())
