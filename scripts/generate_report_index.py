#!/usr/bin/env python3
"""生成报告索引

从 reports/ 目录读取所有报告，生成 MkDocs 索引页面。
"""

import re
from datetime import datetime
from pathlib import Path


def extract_report_info(report_path: Path) -> dict | None:
    """从报告文件中提取信息

    Args:
        report_path: 报告文件路径

    Returns:
        包含报告信息的字典，如果解析失败返回 None
    """
    try:
        content = report_path.read_text(encoding="utf-8")

        # 提取日期
        date_match = re.search(r"# TrendPulse 每日报告 - (\d{4}-\d{2}-\d{2})", content)
        if not date_match:
            return None
        date_str = date_match.group(1)

        # 提取摘要（第一行引用块）
        # 摘要在标题后的空行之后，通常是第 3 行（索引 2）
        summary_match = re.search(r"> (.+)", content.split("\n")[2])
        summary = summary_match.group(1) if summary_match else "暂无摘要"

        # 提取统计信息
        stats = {}
        stats_pattern = r"- \*\*(.+?)\*\*:\s*(\d+)"
        for match in re.finditer(stats_pattern, content):
            stats[match.group(1)] = match.group(2)

        # 获取文件修改时间
        mtime = datetime.fromtimestamp(report_path.stat().st_mtime)

        return {
            "date": date_str,
            "summary": summary,
            "stats": stats,
            "published": mtime.strftime("%Y-%m-%d %H:%M"),
            "path": report_path,
        }
    except Exception as e:
        print(f"解析报告失败 {report_path}: {e}")
        return None


def generate_index(reports_dir: Path, output_path: Path) -> None:
    """生成报告索引页面

    Args:
        reports_dir: 报告目录
        output_path: 输出文件路径
    """
    # 查找所有报告文件
    report_files = sorted(reports_dir.glob("report-*.md"), reverse=True)

    # 提取报告信息
    reports = []
    for report_file in report_files:
        info = extract_report_info(report_file)
        if info:
            reports.append(info)

    if not reports:
        print("没有找到报告文件")
        # 生成空索引
        index_content = """# 趋势报告归档

!!! warning "暂无报告"
    报告生成中，请稍后查看...

    报告将在每天 UTC 0:00（北京时间 8:00）自动更新。
"""
        output_path.write_text(index_content, encoding="utf-8")
        return

    # 生成索引内容
    index_lines = [
        "# 趋势报告归档\n",
        "!!! note \n",
        "    所有报告按时间倒序排列，最新的报告在最前面。\n",
        "\n",
        "## 最新报告\n",
    ]

    # 最新报告列表
    for report in reports[:10]:
        date = report["date"]
        summary = report["summary"]
        published = report["published"]

        index_lines.extend(
            [
                f"### [{date}](report-{date}.md)\n",
                "\n",
                f"{summary}\n",
                "\n",
                f"*发布时间: {published}*\n",
                "\n",
            ]
        )

    # 统计信息
    total_signals = sum(int(r["stats"].get("分析 PR 数", 0)) for r in reports)

    # 计算本月报告数
    current_month = datetime.now().strftime("%Y-%m")
    monthly_count = len([r for r in reports if r["date"][:7] == current_month])

    index_lines.extend(
        [
            "## 统计信息\n",
            "\n",
            "| 指标 | 数值 |\n",
            "|------|------|\n",
            f"| 总报告数 | {len(reports)} |\n",
            f"| 总分析 PR 数 | {total_signals} |\n",
            f"| 本月报告数 | {monthly_count} |\n",
        ]
    )

    # 写入文件
    index_content = "\n".join(index_lines)
    output_path.write_text(index_content, encoding="utf-8")

    print(f"索引已生成: {output_path}")
    print(f"  - 总报告数: {len(reports)}")


def sync_reports_to_docs(reports_dir: Path, docs_reports_dir: Path) -> None:
    """同步报告文件到 docs 目录

    Args:
        reports_dir: 源报告目录
        docs_reports_dir: 目标文档报告目录
    """
    docs_reports_dir.mkdir(parents=True, exist_ok=True)

    # 复制所有报告文件
    for report_file in reports_dir.glob("report-*.md"):
        dest_file = docs_reports_dir / report_file.name
        dest_file.write_text(report_file.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"已复制: {report_file.name}")


def main():
    """主函数"""
    project_root = Path(__file__).parent.parent
    reports_dir = project_root / "reports"
    docs_reports_dir = project_root / "docs" / "reports"
    index_path = docs_reports_dir / "index.md"

    # 检查报告目录
    if not reports_dir.exists():
        print(f"报告目录不存在: {reports_dir}")
        return

    # 同步报告文件
    sync_reports_to_docs(reports_dir, docs_reports_dir)

    # 生成索引
    generate_index(reports_dir, index_path)


if __name__ == "__main__":
    main()
