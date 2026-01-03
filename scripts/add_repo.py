#!/usr/bin/env python3
"""添加仓库到配置脚本

用于 GitHub Action 自动添加新仓库到监控列表。
"""

import argparse
import re
import sys
from pathlib import Path

# 分类到注释标记的映射
CATEGORY_MARKERS: dict[str, dict[str, str | None]] = {
    "Anthropic 核心产品": {
        "start": "# Anthropic 核心产品",
        "end": "# Anthropic SDK & Agent",
    },
    "Anthropic SDK & Agent": {
        "start": "# Anthropic SDK & Agent",
        "end": "# Anthropic 工具与集成",
    },
    "Anthropic 工具与集成": {
        "start": "# Anthropic 工具与集成",
        "end": "# Anthropic 研究与评估",
    },
    "Anthropic 研究与评估": {
        "start": "# Anthropic 研究与评估",
        "end": "# AI 编程助手",
    },
    "AI 编程助手": {
        "start": "# AI 编程助手",
        "end": "# Agent 框架",
    },
    "Agent 框架": {
        "start": "# Agent 框架",
        "end": "# Agentic AI 核心框架",
    },
    "Agentic AI 核心框架": {
        "start": "# Agentic AI 核心框架",
        "end": "# 自主 AI 编程代理",
    },
    "自主 AI 编程代理": {
        "start": "# 自主 AI 编程代理",
        "end": None,  # 最后一个分类
    },
    "其他": {
        "start": "# 其他",
        "end": None,
    },
}


def validate_repo_format(repo: str) -> bool:
    """验证仓库格式

    Args:
        repo: 仓库路径，格式应为 owner/repo

    Returns:
        格式是否有效
    """
    pattern = r"^[a-zA-Z0-9_-]+/[a-zA-Z0-9._-]+$"
    return bool(re.match(pattern, repo))


def get_category_markers(
    category: str,
) -> dict[str, str | None] | None:
    """获取分类对应的注释标记

    Args:
        category: 分类名称

    Returns:
        包含 start 和 end 标记的字典，如果分类不存在返回 None
    """
    return CATEGORY_MARKERS.get(category)


def parse_issue_body(body: str) -> dict[str, str]:
    """解析 Issue 表单内容

    Args:
        body: Issue 正文内容

    Returns:
        包含 repo, category, reason 的字典
    """
    result = {"repo": "", "category": "", "reason": ""}

    # 解析 GitHub 仓库
    repo_match = re.search(
        r"### GitHub 仓库\s*\n\s*([a-zA-Z0-9_-]+/[a-zA-Z0-9._-]+)", body
    )
    if repo_match:
        result["repo"] = repo_match.group(1).strip()

    # 解析分类
    category_match = re.search(r"### 分类\s*\n\s*(.+?)(?:\n\s*###|$)", body)
    if category_match:
        result["category"] = category_match.group(1).strip()

    # 解添加理由
    reason_match = re.search(
        r"### 添加理由\s*\n\s*(.+?)(?:\n\s*###|\n\s*\*|- \[|\Z)", body, re.DOTALL
    )
    if reason_match:
        result["reason"] = reason_match.group(1).strip()

    return result


def add_repo_to_config(config_file: str, repo: str, category: str) -> bool:
    """添加仓库到配置文件

    Args:
        config_file: 配置文件路径
        repo: 仓库路径
        category: 分类名称

    Returns:
        是否添加成功
    """
    config_path = Path(config_file)

    # 读取配置文件
    content = config_path.read_text()

    # 检查仓库是否已存在
    if f'"{repo}"' in content or f"'{repo}'" in content:
        print(f"仓库 {repo} 已存在")
        return False

    # 获取分类标记
    markers = get_category_markers(category)
    if not markers:
        print(f"无效分类: {category}")
        return False

    start_marker = markers["start"]
    end_marker = markers["end"]

    # 找到插入位置
    lines = content.split("\n")
    start_idx: int | None = None
    end_idx: int | None = None

    for i, line in enumerate(lines):
        if start_marker and start_marker in line:
            start_idx = i
        if end_marker and end_marker in line:
            end_idx = i
            break
        elif not end_marker and line.strip() == "]":
            # 最后一个分类，找到列表结束
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        print(f"无法找到插入位置: {category}")
        return False

    # 找到该分类下最后一个仓库（在 end_idx 之前）
    insert_idx = end_idx
    for i in range(end_idx - 1, start_idx, -1):
        if '"' in lines[i] or "'" in lines[i]:
            insert_idx = i + 1
            break

    # 获取缩进
    indent = "            "  # 12 个空格，与配置文件一致

    # 插入新仓库
    new_line = f'{indent}"{repo}",'
    lines.insert(insert_idx, new_line)

    # 写回文件
    config_path.write_text("\n".join(lines))
    print(f"已添加仓库: {repo} 到分类: {category}")
    return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="添加仓库到配置")
    parser.add_argument("--repo", required=True, help="仓库路径，格式：owner/repo")
    parser.add_argument("--category", required=True, help="分类名称")
    parser.add_argument(
        "--config-file",
        default="src/trendpluse/config.py",
        help="配置文件路径",
    )
    parser.add_argument(
        "--parse-issue",
        help="解析 Issue 表单内容",
    )

    args = parser.parse_args()

    # 验证仓库格式
    if not validate_repo_format(args.repo):
        print(f"无效仓库格式: {args.repo}")
        sys.exit(1)

    # 添加仓库
    success = add_repo_to_config(args.config_file, args.repo, args.category)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
