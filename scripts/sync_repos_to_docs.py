#!/usr/bin/env python3
"""同步监控仓库列表到文档

从 config.py 读取 github_repos，自动更新 docs/index.md 中的监控项目部分。
"""

# ruff: noqa: E402
# mypy: disable-error-code="import-not-found"

import re
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root / "scripts"))

# 直接从 scripts 目录导入
import repos_doc_generator

from trendpluse.config import Settings  # type: ignore[import-not-found]

parse_repos_from_config = repos_doc_generator.parse_repos_from_config
generate_repos_markdown = repos_doc_generator.generate_repos_markdown


def find_monitored_repos_section(content: str) -> tuple[int, int] | None:
    """查找监控项目部分的位置

    Args:
        content: Markdown 文件内容

    Returns:
        (start_line, end_line) 或 None
    """
    lines = content.split("\n")

    start_idx = None
    end_idx = None

    # 查找开始标记
    for i, line in enumerate(lines):
        if line.strip() == "### 📋 监控项目":
            start_idx = i
            break

    if start_idx is None:
        return None

    # 查找结束标记（下一个 ### 级别的标题）
    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        # 只匹配 ### 开头的标题（精确匹配，不包括 ####）
        if line.strip().startswith("### ") and not line.strip().startswith("#### "):
            end_idx = i
            break

    if end_idx is None:
        end_idx = len(lines)

    return start_idx, end_idx


def update_index_file(
    index_path: Path, repos: list[str], dry_run: bool = False
) -> bool:
    """更新 index.md 文件

    Args:
        index_path: index.md 文件路径
        repos: 仓库列表
        dry_run: 是否为试运行

    Returns:
        是否成功更新
    """
    # 读取现有内容
    content = index_path.read_text(encoding="utf-8")

    # 生成新的监控项目部分
    categories = parse_repos_from_config(repos)
    new_section = generate_repos_markdown(categories)

    # 查找并替换监控项目部分
    section_range = find_monitored_repos_section(content)

    if section_range is None:
        print("⚠️  未找到现有监控项目部分，将在文件末尾追加")
        # 在文件末尾追加
        updated_content = content + "\n" + new_section
    else:
        start_idx, end_idx = section_range
        lines = content.split("\n")

        # 替换监控项目部分
        updated_lines = lines[:start_idx] + [new_section.strip()] + lines[end_idx:]
        updated_content = "\n".join(updated_lines)

    # 写入文件
    if dry_run:
        print("📋 试运行模式，不会修改文件：")
        print(new_section)
        return True

    index_path.write_text(updated_content, encoding="utf-8")
    print(f"✅ 已更新 {index_path}")
    return True


def main() -> int:
    """主函数

    Returns:
        退出码
    """
    import argparse

    parser = argparse.ArgumentParser(description="同步监控仓库列表到文档")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="试运行模式，不修改文件",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="检查模式，如果文档不是最新的则返回非零退出码",
    )

    args = parser.parse_args()

    # 获取配置
    settings = Settings()
    repos = settings.github_repos

    print(f"📊 从配置读取到 {len(repos)} 个仓库")

    # 更新文档
    project_root = Path(__file__).parent.parent
    index_path = project_root / "docs" / "index.md"

    if not index_path.exists():
        print(f"❌ 文件不存在: {index_path}")
        return 1

    if args.check:
        # 检查模式：重新生成并比较
        content = index_path.read_text(encoding="utf-8")
        categories = parse_repos_from_config(repos)
        new_section = generate_repos_markdown(categories).strip()

        section_range = find_monitored_repos_section(content)
        if section_range is None:
            print("❌ 未找到监控项目部分")
            return 1

        start_idx, end_idx = section_range
        lines = content.split("\n")
        existing_section = "\n".join(lines[start_idx:end_idx]).strip()

        # 标准化比较（移除空白差异）
        existing_normalized = re.sub(r"\s+", "", existing_section)
        new_normalized = re.sub(r"\s+", "", new_section)

        if existing_normalized != new_normalized:
            print("❌ 文档不是最新的，需要运行同步")
            if existing_normalized not in new_normalized:
                # 显示差异的调试信息
                import difflib

                diff = difflib.unified_diff(
                    existing_section.splitlines(keepends=True),
                    new_section.splitlines(keepends=True),
                    fromfile="existing",
                    tofile="new",
                    lineterm="",
                )
                print("差异:")
                print("".join(diff))
            return 1
        else:
            print("✅ 文档是最新的")
            return 0

    # 正常更新模式
    success = update_index_file(index_path, repos, dry_run=args.dry_run)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
