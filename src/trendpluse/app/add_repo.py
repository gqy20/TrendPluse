"""添加仓库到监控配置。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# 分类名称保留用于 issue 表单校验与 bridge 结果透传。
CATEGORY_MARKERS: dict[str, dict[str, str | None]] = {
    "Anthropic 核心产品": {"start": None, "end": None},
    "Anthropic SDK & Agent": {"start": None, "end": None},
    "Anthropic 工具与集成": {"start": None, "end": None},
    "Anthropic 研究与评估": {"start": None, "end": None},
    "AI 编程助手": {"start": None, "end": None},
    "Agent 框架": {"start": None, "end": None},
    "Agentic AI 核心框架": {"start": None, "end": None},
    "自主 AI 编程代理": {"start": None, "end": None},
    "其他": {"start": None, "end": None},
}


def validate_repo_format(repo: str) -> bool:
    """验证仓库格式。"""
    pattern = r"^[a-zA-Z0-9_-]+/[a-zA-Z0-9._-]+$"
    return bool(re.match(pattern, repo))


def get_category_markers(category: str) -> dict[str, str | None] | None:
    """返回合法分类占位结构。"""
    return CATEGORY_MARKERS.get(category)


def parse_issue_body(body: str) -> dict[str, str]:
    """解析 Issue 表单内容。"""
    result = {"repo": "", "category": "", "reason": ""}

    repo_match = re.search(
        r"### GitHub 仓库\s*\n\s*([a-zA-Z0-9_-]+/[a-zA-Z0-9._-]+)", body
    )
    if repo_match:
        result["repo"] = repo_match.group(1).strip()

    category_match = re.search(r"### 分类\s*\n\s*(.+?)(?:\n\s*###|$)", body)
    if category_match:
        result["category"] = category_match.group(1).strip()

    reason_match = re.search(
        r"### 添加理由\s*\n\s*(.+?)(?:\n\s*###|\n\s*\*|- \[|\Z)", body, re.DOTALL
    )
    if reason_match:
        result["reason"] = reason_match.group(1).strip()

    return result


def _repo_to_url(repo: str) -> str:
    return f"https://github.com/{repo}"


def _load_repo_entries(config_file: str) -> list[dict[str, Any]]:
    config_path = Path(config_file)
    if not config_path.exists():
        return []

    data = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("监控仓库配置必须是 JSON 数组")
    return [item for item in data if isinstance(item, dict)]


def _write_repo_entries(config_file: str, entries: list[dict[str, Any]]) -> None:
    Path(config_file).write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def is_repo_in_config(config_file: str, repo: str) -> bool:
    """检查仓库是否已存在于配置中。"""
    target_url = _repo_to_url(repo)
    return any(
        str(item.get("url", "")).strip() == target_url
        for item in _load_repo_entries(config_file)
    )


def add_repo_to_config(config_file: str, repo: str, category: str) -> bool:
    """添加仓库到 repos.json 风格配置文件。"""
    entries = _load_repo_entries(config_file)
    target_url = _repo_to_url(repo)

    if any(str(item.get("url", "")).strip() == target_url for item in entries):
        print(f"仓库 {repo} 已存在")
        return False

    if get_category_markers(category) is None:
        print(f"无效分类: {category}")
        return False

    entries.append(
        {
            "url": target_url,
            "description": "",
            "category": category,
        }
    )
    entries.sort(key=lambda item: str(item.get("url", "")))
    _write_repo_entries(config_file, entries)
    print(f"已添加仓库: {repo} 到分类: {category}")
    return True


def batch_add_repos_to_config(
    config_file: str,
    items: list[dict[str, str]],
) -> dict[str, list[str]]:
    """批量添加仓库到配置文件。"""
    result: dict[str, list[str]] = {
        "added": [],
        "duplicates": [],
        "invalid_format": [],
        "invalid_category": [],
        "failed": [],
    }

    for item in items:
        repo = (item.get("repo") or "").strip()
        category = (item.get("category") or "").strip() or "其他"

        if not validate_repo_format(repo):
            result["invalid_format"].append(repo)
            continue
        if get_category_markers(category) is None:
            result["invalid_category"].append(repo)
            continue
        if is_repo_in_config(config_file, repo):
            result["duplicates"].append(repo)
            continue

        if add_repo_to_config(config_file=config_file, repo=repo, category=category):
            result["added"].append(repo)
        else:
            result["failed"].append(repo)

    return result


def load_batch_items(batch_file: str) -> list[dict[str, str]]:
    """从 JSON 文件读取批量添加项。"""
    data = json.loads(Path(batch_file).read_text(encoding="utf-8"))

    if isinstance(data, list):
        raw_items = data
    elif isinstance(data, dict):
        raw_items = data.get("candidates", [])
    else:
        raw_items = []

    items: list[dict[str, str]] = []
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        repo = str(item.get("repo", "")).strip()
        category = str(
            item.get("category") or item.get("suggested_category") or "其他"
        ).strip()
        items.append({"repo": repo, "category": category})
    return items


def run_add_repo_command(
    *,
    repo: str | None = None,
    category: str | None = None,
    batch_file: str | None = None,
    config_file: str = "repos.json",
) -> int:
    """执行添加仓库命令。"""
    if batch_file:
        items = load_batch_items(batch_file)
        result = batch_add_repos_to_config(config_file, items)
        print(
            "批量添加结果: "
            f"added={len(result['added'])}, "
            f"duplicates={len(result['duplicates'])}, "
            f"invalid_format={len(result['invalid_format'])}, "
            f"invalid_category={len(result['invalid_category'])}, "
            f"failed={len(result['failed'])}"
        )
        has_errors = bool(
            result["invalid_format"] or result["invalid_category"] or result["failed"]
        )
        return 1 if has_errors else 0

    if not repo or not category:
        print("单仓模式必须提供 --repo 和 --category")
        return 1

    if not validate_repo_format(repo):
        print(f"无效仓库格式: {repo}")
        return 1

    success = add_repo_to_config(config_file, repo, category)
    return 0 if success else 1
