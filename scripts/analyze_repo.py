#!/usr/bin/env python3
"""兼容入口：仓库分析。"""
# ruff: noqa: F401

import sys

from trendpluse.cli.analyze_repo import (
    analyze_repository,
    generate_markdown_report,
    main,
    parse_github_url,
)

if __name__ == "__main__":
    sys.exit(main())
