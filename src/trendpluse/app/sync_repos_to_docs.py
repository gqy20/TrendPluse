"""同步监控仓库列表到文档。"""

import re
from pathlib import Path

from trendpluse.app.repos_doc_generator import (
    generate_homepage_repos_section,
    generate_repos_markdown,
    parse_repos_from_config,
)
from trendpluse.config import Settings

SECTION_START_MARKER = "<!-- monitored-repos-section:start -->"
SECTION_END_MARKER = "<!-- monitored-repos-section:end -->"


def find_monitored_repos_section(content: str) -> tuple[int, int] | None:
    """查找监控项目部分的位置。"""
    start_marker = content.find(SECTION_START_MARKER)
    end_marker = content.find(SECTION_END_MARKER)
    if start_marker != -1 and end_marker != -1 and end_marker > start_marker:
        return start_marker, end_marker + len(SECTION_END_MARKER)

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


def replace_monitored_repos_section(content: str, new_section: str) -> str:
    """替换首页中的监控仓库区块。"""
    start_marker = content.find(SECTION_START_MARKER)
    end_marker = content.find(SECTION_END_MARKER)
    if start_marker != -1 and end_marker != -1 and end_marker > start_marker:
        end_pos = end_marker + len(SECTION_END_MARKER)
        return (
            f"{content[:start_marker].rstrip()}\n\n"
            f"{new_section}\n\n"
            f"{content[end_pos:].lstrip()}"
        )

    section_range = find_monitored_repos_section(content)
    if section_range is None:
        print("⚠️  未找到现有监控项目部分，将在文件末尾追加")
        return content.rstrip() + "\n\n" + new_section + "\n"

    start_idx, end_idx = section_range
    lines = content.split("\n")
    updated_lines = lines[:start_idx] + [new_section.strip()] + lines[end_idx:]
    return "\n".join(updated_lines)


def extract_existing_monitored_repos_section(content: str) -> str | None:
    """提取首页中的监控仓库区块文本。"""
    start_marker = content.find(SECTION_START_MARKER)
    end_marker = content.find(SECTION_END_MARKER)
    if start_marker != -1 and end_marker != -1 and end_marker > start_marker:
        end_pos = end_marker + len(SECTION_END_MARKER)
        return content[start_marker:end_pos].strip()

    section_range = find_monitored_repos_section(content)
    if section_range is None:
        return None

    start_idx, end_idx = section_range
    lines = content.split("\n")
    return "\n".join(lines[start_idx:end_idx]).strip()


def update_index_file(index_path: Path, dry_run: bool = False) -> bool:
    """更新 index.md 文件。"""
    content = index_path.read_text(encoding="utf-8")
    categories = parse_repos_from_config(Settings().monitored_repo_configs)
    generated_block = generate_homepage_repos_section(categories).strip()
    new_section = f"{SECTION_START_MARKER}\n{generated_block}\n{SECTION_END_MARKER}"
    updated_content = replace_monitored_repos_section(content, new_section)

    if dry_run:
        print("📋 试运行模式，不会修改文件：")
        print(new_section)
        return True

    updated_content = updated_content.rstrip("\n") + "\n"

    if content == updated_content:
        print(f"ℹ️ 无需更新 {index_path}")
        return True

    index_path.write_text(updated_content, encoding="utf-8")
    print(f"✅ 已更新 {index_path}")
    return True


def write_monitored_repos_file(
    monitored_repos_path: Path, dry_run: bool = False
) -> bool:
    """生成完整监控仓库清单页面。"""
    categories = parse_repos_from_config(Settings().monitored_repo_configs)
    content = ("# 监控仓库清单\n\n" + generate_repos_markdown(categories)).rstrip(
        "\n"
    ) + "\n"

    if dry_run:
        print(f"📋 试运行模式，不会修改文件: {monitored_repos_path}")
        print(content)
        return True

    monitored_repos_path.parent.mkdir(parents=True, exist_ok=True)

    existing_content = (
        monitored_repos_path.read_text(encoding="utf-8")
        if monitored_repos_path.exists()
        else None
    )
    if existing_content == content:
        print(f"ℹ️ 无需更新 {monitored_repos_path}")
        return True

    monitored_repos_path.write_text(content, encoding="utf-8")
    print(f"✅ 已更新 {monitored_repos_path}")
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
    monitored_repos_path = project_root / "docs" / "monitored-repos.md"

    if not index_path.exists():
        print(f"❌ 文件不存在: {index_path}")
        return 1

    if check:
        content = index_path.read_text(encoding="utf-8")
        categories = parse_repos_from_config(repos)
        generated_block = generate_homepage_repos_section(categories).strip()
        new_section = f"{SECTION_START_MARKER}\n{generated_block}\n{SECTION_END_MARKER}"

        existing_section = extract_existing_monitored_repos_section(content)
        if existing_section is None:
            print("❌ 未找到监控项目部分")
            return 1

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
    success = (
        write_monitored_repos_file(monitored_repos_path, dry_run=dry_run) and success
    )
    return 0 if success else 1
