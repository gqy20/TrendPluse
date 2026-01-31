#!/usr/bin/env python3
"""迁移 reports 目录到新的分类结构

将扁平的 reports/ 目录迁移到按类型隔离的结构：
- reports/daily/ - 日报
- reports/weekly/ - 周报
- reports/discovery/ - 发现报告
"""

import shutil
from pathlib import Path


def migrate_reports(old_reports_dir: Path, new_reports_dir: Path) -> None:
    """迁移报告文件到新结构

    Args:
        old_reports_dir: 旧的 reports 目录
        new_reports_dir: 新的 reports 目录
    """
    if not old_reports_dir.exists():
        print(f"旧目录不存在: {old_reports_dir}")
        return

    # 创建新目录结构
    (new_reports_dir / "daily").mkdir(parents=True, exist_ok=True)
    (new_reports_dir / "weekly").mkdir(parents=True, exist_ok=True)
    (new_reports_dir / "discovery").mkdir(parents=True, exist_ok=True)

    # 统计
    daily_count = 0
    weekly_count = 0
    discovery_count = 0

    # 迁移日报
    for file in old_reports_dir.glob("report-*.md"):
        if file.is_file():
            dest = new_reports_dir / "daily" / file.name
            shutil.copy2(file, dest)
            daily_count += 1
            print(f"已迁移日报: {file.name}")

    # 迁移 JSON 数据文件
    for file in old_reports_dir.glob("report-*.json"):
        if file.is_file():
            dest = new_reports_dir / "daily" / file.name
            shutil.copy2(file, dest)
            print(f"已迁移日报数据: {file.name}")

    # 迁移周报
    for file in old_reports_dir.glob("weekly-*.md"):
        if file.is_file():
            dest = new_reports_dir / "weekly" / file.name
            shutil.copy2(file, dest)
            weekly_count += 1
            print(f"已迁移周报: {file.name}")

    # 迁移发现报告
    for file in old_reports_dir.glob("discovery-*.md"):
        if file.is_file():
            dest = new_reports_dir / "discovery" / file.name
            shutil.copy2(file, dest)
            discovery_count += 1
            print(f"已迁移发现报告: {file.name}")

    for file in old_reports_dir.glob("discovery-*.json"):
        if file.is_file():
            dest = new_reports_dir / "discovery" / file.name
            shutil.copy2(file, dest)
            print(f"已迁移发现报告数据: {file.name}")

    print("\n迁移完成:")
    print(f"  - 日报: {daily_count}")
    print(f"  - 周报: {weekly_count}")
    print(f"  - 发现报告: {discovery_count}")
    print(f"  - 总计: {daily_count + weekly_count + discovery_count}")


def main():
    """主函数"""
    project_root = Path(__file__).parent.parent

    # 临时目录用于备份
    old_dir = project_root / "reports_old"
    new_dir = project_root / "reports"

    if old_dir.exists():
        print(f"备份目录已存在: {old_dir}")
        print("请先手动删除或重命名备份目录")
        return

    # 重命名当前目录为备份
    if new_dir.exists():
        new_dir.rename(old_dir)
        print(f"已备份旧目录: {old_dir}")

    # 创建新目录结构并迁移文件
    migrate_reports(old_dir, new_dir)

    print(f"\n新结构已创建: {new_dir}")
    print(f"备份保留在: {old_dir}")
    print("\n请确认迁移无误后，手动删除备份目录:")
    print(f"  rm -rf {old_dir}")


if __name__ == "__main__":
    main()
