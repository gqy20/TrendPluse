#!/usr/bin/env python3
"""兼容入口：同步监控仓库列表到文档。"""
# ruff: noqa: F401

import sys

from trendpluse.automation.sync_repos_to_docs import (
    find_monitored_repos_section,
    main,
    update_index_file,
)

if __name__ == "__main__":
    sys.exit(main())
