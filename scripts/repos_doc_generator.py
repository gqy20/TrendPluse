"""兼容入口：仓库文档生成器。"""
# ruff: noqa: F401

from trendpluse.automation.repos_doc_generator import (
    REPO_CATEGORIES,
    RepoCategory,
    generate_repos_markdown,
    parse_repos_from_config,
)
