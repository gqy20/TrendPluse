#!/usr/bin/env python3
"""兼容入口：添加仓库到配置。"""
# ruff: noqa: F401

from trendpluse.automation.add_repo import (
    CATEGORY_MARKERS,
    add_repo_to_config,
    batch_add_repos_to_config,
    get_category_markers,
    is_repo_in_config,
    load_batch_items,
    main,
    parse_issue_body,
    validate_repo_format,
)

if __name__ == "__main__":
    main()
