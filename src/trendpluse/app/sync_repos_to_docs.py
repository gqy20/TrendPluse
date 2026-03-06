"""同步监控仓库列表到文档。"""

import re
from pathlib import Path

from trendpluse.app.repos_doc_generator import (
    generate_repos_markdown,
    parse_repos_from_config,
)
from trendpluse.config import Settings


def find_monitored_repos_section(content: str) -> tuple[int, int] | None:
    """查找监控项目部分的位置。"""
    lines = content.split("\n")

    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if line.strip() == "### 📋 监控项目":
            start_idx = i
            break

    if start_idx is None:
        return None

    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        if line.strip().startswith("### ") and not line.strip().startswith("#### "):
            end_idx = i
            break

    if end_idx is None:
        end_idx = len(lines)

    return start_idx, end_idx


def update_index_file(index_path: Path, dry_run: bool = False) -> bool:
    """更新 index.md 文件。"""
    content = index_path.read_text(encoding="utf-8")
    categories = parse_repos_from_config(Settings().monitored_repo_configs)
    new_section = generate_repos_markdown(categories)
    section_range = find_monitored_repos_section(content)

    if section_range is None:
        print("⚠️  未找到现有监控项目部分，将在文件末尾追加")
        updated_content = content + "\n" + new_section
    else:
        start_idx, end_idx = section_range
        lines = content.split("\n")
        updated_lines = lines[:start_idx] + [new_section.strip()] + lines[end_idx:]
        updated_content = "\n".join(updated_lines)

    if dry_run:
        print("📋 试运行模式，不会修改文件：")
        print(new_section)
        return True

    index_path.write_text(updated_content, encoding="utf-8")
    print(f"✅ 已更新 {index_path}")
    return True


def run_sync_repos_to_docs(
    *,
    dry_run: bool = False,
    check: bool = False,
    project_root: Path | None = None,
) -> int:
    """执行监控仓库文档同步。"""
    settings = Settings()
    repos = settings.monitored_repo_configs

    print(f"📊 从配置读取到 {len(repos)} 个仓库")

    project_root = project_root or Path.cwd().resolve()
    index_path = project_root / "docs" / "index.md"

    if not index_path.exists():
        print(f"❌ 文件不存在: {index_path}")
        return 1

    if check:
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

        existing_normalized = re.sub(r"\s+", "", existing_section)
        new_normalized = re.sub(r"\s+", "", new_section)

        if existing_normalized != new_normalized:
            print("❌ 文档不是最新的，需要运行同步")
            if existing_normalized not in new_normalized:
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
        print("✅ 文档是最新的")
        return 0

    success = update_index_file(index_path, dry_run=dry_run)
    return 0 if success else 1
