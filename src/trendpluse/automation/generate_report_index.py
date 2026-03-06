"""生成报告索引

从 reports/ 目录读取所有报告，生成 MkDocs 索引页面。
"""

import re
from datetime import datetime
from pathlib import Path
from typing import TypedDict


class _ProjectInfo(TypedDict):
    """项目信息"""

    repo: str
    stars: int


def ensure_reports_structure(reports_dir: Path) -> None:
    """确保 reports 目录结构存在

    Args:
        reports_dir: 报告根目录
    """
    (reports_dir / "daily").mkdir(parents=True, exist_ok=True)
    (reports_dir / "weekly").mkdir(parents=True, exist_ok=True)
    (reports_dir / "discovery").mkdir(parents=True, exist_ok=True)
    print(f"目录结构已创建: {reports_dir}")


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
        # 摘要在标题后的空行之后，找到第一个非空行
        lines = content.split("\n")
        summary_match = None
        for i in range(2, min(10, len(lines))):
            if lines[i].strip().startswith(">"):
                summary_match = re.search(r"> (.+)", lines[i])
                break

        summary = summary_match.group(1) if summary_match else "暂无摘要"

        # 提取统计信息
        stats = {}
        stats_pattern = r"- \*\*(.+?)\*\*:\s*(\d+)"
        for match in re.finditer(stats_pattern, content):
            stats[match.group(1)] = match.group(2)

        # 使用报告日期作为发布时间（而非文件修改时间，避免 CI 环境时间戳问题）
        # 从文件名中提取的日期已经足够准确
        published_date = datetime.strptime(date_str, "%Y-%m-%d")
        published = published_date.strftime("%Y-%m-%d")

        return {
            "date": date_str,
            "summary": summary,
            "stats": stats,
            "published": published,
            "path": report_path,
        }
    except Exception as e:
        print(f"解析报告失败 {report_path}: {e}")
        return None


def extract_weekly_report_info(weekly_path: Path) -> dict | None:
    """从周报文件中提取信息

    Args:
        weekly_path: 周报文件路径

    Returns:
        包含周报信息的字典，如果解析失败返回 None
    """
    try:
        content = weekly_path.read_text(encoding="utf-8")

        # 提取日期范围和周标识（支持多行标题）
        week_match = re.search(
            r"# TrendPulse 周报 "
            r"\((\d{4}-W\d+): (\d{4}-\d{2}-\d{2}) ~\s*"
            r"(\d{4}-\d{2}-\d{2})\)",
            content,
        )
        if not week_match:
            return None

        week_id = week_match.group(1)
        start_date = week_match.group(2)
        end_date = week_match.group(3)

        # 提取摘要
        lines = content.split("\n")
        summary_match = None
        for i in range(2, min(10, len(lines))):
            if lines[i].strip().startswith(">"):
                summary_match = re.search(r"> (.+)", lines[i])
                break

        summary = summary_match.group(1) if summary_match else "暂无摘要"

        return {
            "week_id": week_id,
            "start_date": start_date,
            "end_date": end_date,
            "summary": summary,
            "path": weekly_path,
        }
    except Exception as e:
        print(f"解析周报失败 {weekly_path}: {e}")
        return None


def generate_index(reports_dir: Path, output_path: Path) -> None:
    """生成报告索引页面

    Args:
        reports_dir: 报告目录
        output_path: 输出文件路径
    """
    # 从子目录查找日报和周报文件
    daily_dir = reports_dir / "daily"
    weekly_dir = reports_dir / "weekly"

    daily_files = []
    weekly_files = []

    if daily_dir.exists():
        daily_files = sorted(daily_dir.glob("report-*.md"), reverse=True)

    if weekly_dir.exists():
        weekly_files = sorted(weekly_dir.glob("weekly-*.md"), reverse=True)

    # 提取日报信息
    daily_reports = []
    for report_file in daily_files:
        info = extract_report_info(report_file)
        if info:
            daily_reports.append(info)

    # 提取周报信息
    weekly_reports = []
    for weekly_file in weekly_files:
        info = extract_weekly_report_info(weekly_file)
        if info:
            weekly_reports.append(info)

    if not daily_reports and not weekly_reports:
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
        "## 最新周报\n",
    ]

    # 最新周报（显示最近 4 周）
    for report in weekly_reports[:4]:
        week_id = report["week_id"]
        start_date = report["start_date"]
        end_date = report["end_date"]
        summary = report["summary"]

        index_lines.extend(
            [
                f"### [{week_id}](weekly-{week_id}.md)\n",
                "\n",
                f"**时间范围**: {start_date} ~ {end_date}\n",
                "\n",
                f"{summary}\n",
                "\n",
            ]
        )

    index_lines.extend(["\n", "## 最新日报\n"])

    # 最新日报列表
    for report in daily_reports[:10]:
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
    total_signals = sum(int(r["stats"].get("分析 PR 数", 0)) for r in daily_reports)

    # 计算本月报告数
    current_month = datetime.now().strftime("%Y-%m")
    monthly_count = len([r for r in daily_reports if r["date"][:7] == current_month])

    index_lines.extend(
        [
            "\n",
            "## 统计信息\n",
            "\n",
            "| 指标 | 数值 |\n",
            "|------|------|\n",
            f"| 总报告数 | {len(daily_reports)} |\n",
            f"| 总分析 PR 数 | {total_signals} |\n",
            f"| 本月报告数 | {monthly_count} |\n",
        ]
    )

    # 写入文件
    index_content = "".join(index_lines)  # 元素已包含 \n，直接拼接
    output_path.write_text(index_content, encoding="utf-8")

    print(f"索引已生成: {output_path}")
    print(f"  - 总日报数: {len(daily_reports)}")
    print(f"  - 总周报数: {len(weekly_reports)}")


def sync_reports_to_docs(reports_dir: Path, docs_reports_dir: Path) -> None:
    """同步报告文件到 docs 目录

    Args:
        reports_dir: 源报告目录
        docs_reports_dir: 目标文档报告目录
    """
    docs_reports_dir.mkdir(parents=True, exist_ok=True)

    # 从子目录复制日报和周报文件
    daily_dir = reports_dir / "daily"
    weekly_dir = reports_dir / "weekly"

    if daily_dir.exists():
        for report_file in daily_dir.glob("report-*.md"):
            dest_file = docs_reports_dir / report_file.name
            dest_file.write_text(
                report_file.read_text(encoding="utf-8"), encoding="utf-8"
            )
            print(f"已复制日报: {report_file.name}")

    if weekly_dir.exists():
        for report_file in weekly_dir.glob("weekly-*.md"):
            dest_file = docs_reports_dir / report_file.name
            dest_file.write_text(
                report_file.read_text(encoding="utf-8"), encoding="utf-8"
            )
            print(f"已复制周报: {report_file.name}")


def sync_discovery_reports_to_docs(reports_dir: Path, docs_dir: Path) -> None:
    """同步发现报告到 docs 目录

    将发现报告同步到 docs/discovery-reports/ 子目录（不是根目录）。

    Args:
        reports_dir: 源报告目录
        docs_dir: 目标文档目录
    """
    discovery_dir = reports_dir / "discovery"
    if not discovery_dir.exists():
        return

    # 创建 discovery-reports 子目录
    discovery_reports_dir = docs_dir / "discovery-reports"
    discovery_reports_dir.mkdir(parents=True, exist_ok=True)

    # 只同步 Markdown 文件（JSON 不需要同步到 docs）
    for report_file in discovery_dir.glob("discovery-*.md"):
        dest_file = discovery_reports_dir / report_file.name
        dest_file.write_text(report_file.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"已复制发现报告: {report_file.name}")


def extract_discovery_report_info(report_path: Path) -> dict | None:
    """从发现报告中提取信息

    Args:
        report_path: 发现报告文件路径

    Returns:
        包含报告信息的字典，如果解析失败返回 None
    """
    try:
        content = report_path.read_text(encoding="utf-8")

        # 提取日期
        date_match = re.search(r"# 项目发现报告 \((\d{4}-\d{2}-\d{2})\)", content)
        if not date_match:
            return None
        date_str = date_match.group(1)

        # 提取概览数据
        stats = {}
        stats_pattern = r"\|\s*(.+?)\s*\|\s*(\d+)\s*\|"
        in_overview = False
        for line in content.split("\n"):
            if "## 发现概览" in line:
                in_overview = True
                continue
            if in_overview:
                if line.startswith("|") and "---" not in line:
                    match = re.search(stats_pattern, line)
                    if match:
                        key = match.group(1).strip()
                        value = match.group(2)
                        stats[key] = value
                elif line.startswith("##"):
                    break

        # 映射中文字段名
        key_mapping = {
            "总发现数": "total_discovered",
            "通过质量评估": "passed_quality",
            "高优先级": "high_priority",
            "去重移除": "duplicates_removed",
            "已在监控": "already_monitored",
        }
        mapped_stats = {}
        for cn_key, en_key in key_mapping.items():
            if cn_key in stats:
                mapped_stats[en_key] = stats[cn_key]

        # 提取高优先级推荐 Top 5
        top_projects: list[_ProjectInfo] = []
        in_high_priority = False
        project_header_pattern = (
            r"###\s+\d+\.\s+([/\w.-]+)"  # 匹配 "### 1. owner/repo" (包含 .)
        )
        stars_pattern = r"\|\s*Stars\s*\|\s*([\d,]+)\s*\|"  # 匹配表格中的 Stars 行

        for line in content.split("\n"):
            if "## 🌟 高优先级推荐" in line or "## 高优先级推荐" in line:
                in_high_priority = True
                continue
            if in_high_priority:
                if line.startswith("###"):
                    match = re.search(project_header_pattern, line)
                    if match:
                        repo = match.group(1)
                        top_projects.append({"repo": repo, "stars": 0})
                elif top_projects and "| Stars |" in line:
                    match = re.search(stars_pattern, line)
                    if match:
                        stars_str = match.group(1).replace(",", "")
                        if top_projects and top_projects[-1]["stars"] == 0:
                            top_projects[-1]["stars"] = int(stars_str)
                elif line.startswith("##") and "高优先级" not in line:
                    break
                if len(top_projects) >= 5 and all(p["stars"] > 0 for p in top_projects):
                    break

        return {
            "date": date_str,
            "stats": mapped_stats,
            "top_projects": top_projects,
        }
    except Exception as e:
        print(f"解析发现报告失败 {report_path}: {e}")
        return None


def generate_discovery_index(reports_dir: Path, docs_dir: Path) -> None:
    """生成发现历史索引页面

    Args:
        reports_dir: 报告目录
        docs_dir: 文档目录
    """
    discovery_dir = reports_dir / "discovery"
    if not discovery_dir.exists():
        return

    # 查找最新的发现报告
    discovery_files = sorted(discovery_dir.glob("discovery-*.md"), reverse=True)
    if not discovery_files:
        print("没有找到发现报告文件")
        return

    latest_report = discovery_files[0]
    info = extract_discovery_report_info(latest_report)

    if not info:
        print(f"无法解析最新的发现报告: {latest_report}")
        return

    date = info["date"]
    stats = info["stats"]
    top_projects = info["top_projects"]

    # 生成内容
    lines = [
        "# 项目发现历史\n",
        "\n",
        "自动发现的 GitHub 热门项目报告，每周一更新。\n",
        "\n",
        "## 最新报告\n",
        "\n",
        f"### [{date}](discovery-reports/discovery-{date}.md)\n",
        "\n",
        "**发现概览**:<br/>\n",
    ]

    # 添加概览数据
    overview_lines = [
        f"- 总发现数: {stats.get('total_discovered', 'N/A')}<br/>\n",
        f"- 通过质量评估: {stats.get('passed_quality', 'N/A')}<br/>\n",
        f"- 高优先级: {stats.get('high_priority', 'N/A')}<br/>\n",
        f"- 去重移除: {stats.get('duplicates_removed', 'N/A')}<br/>\n",
        f"- 已在监控: {stats.get('already_monitored', 'N/A')}<br/>\n",
        "\n",
        "**高优先级推荐 Top 5**:<br/>\n",
        "\n",
    ]

    # 添加 Top 5 项目
    for i, project in enumerate(top_projects, 1):
        repo_link = f"[{project['repo']}](https://github.com/{project['repo']})"
        overview_lines.append(f"{i}. {repo_link} - {project['stars']:,} ⭐<br/>\n")

    lines.extend(overview_lines)

    # 添加历史报告表格（包含所有报告）
    lines.extend(
        [
            "\n",
            "## 历史报告\n",
            "\n",
            "| 日期 | 总发现 | 高优先级 | 报告 |\n",
            "|------|--------|----------|------|\n",
        ]
    )

    for report_file in discovery_files[:10]:  # 显示最近 10 个
        info = extract_discovery_report_info(report_file)
        if info:
            date = info["date"]
            total = info["stats"].get("total_discovered", "N/A")
            high = info["stats"].get("high_priority", "N/A")
            report_url = f"discovery-reports/discovery-{date}.md"
            lines.append(f"| {date} | {total} | {high} | [查看]({report_url}) |\n")

    # 添加说明部分
    lines.extend(
        [
            "\n",
            "## 关于发现功能\n",
            "\n",
            "### 发现来源\n",
            "\n",
            "项目通过以下方式自动发现：\n",
            "\n",
            "1. **GitHub Trending** - 爬取各语言的 Trending 页面\n",
            "2. **关键词搜索** - 基于 AI 相关关键词搜索\n",
            "\n",
            "### 质量评估\n",
            "\n",
            "每个发现的项目会经过多维度质量评估：\n",
            "\n",
            "- **Stars 指标** (20分): 项目受欢迎程度\n",
            "- **活跃度指标** (30分): 最近提交时间\n",
            "- **社区指标** (20分): Forks 和 Watchers 数量\n",
            "- **代码质量** (20分): License 和 Open Issues 比例\n",
            "- **相关性** (15分): 与 AI/LLM 主题的相关度\n",
            "\n",
            "**总质量分**: 0-100 分，≥60 分为推荐\n",
            "\n",
            "### 推荐优先级\n",
            "\n",
            "- **高优先级** (high): 质量分数 ≥ 85\n",
            "- **中优先级** (medium): 70 ≤ 质量分数 < 85\n",
            "- **低优先级** (low): 60 ≤ 质量分数 < 70\n",
            "\n",
            "### 运行方式\n",
            "\n",
            "```bash\n",
            "# 本地运行发现\n",
            "uv run trendpluse-discover-projects\n",
            "\n",
            "# 自定义参数\n",
            "uv run trendpluse-discover-projects \\\n",
            "  --days 7 \\\n",
            "  --min-quality 60.0 \\\n",
            "  --languages python typescript go \\\n",
            '  --keywords "AI agent" "LLM" "Claude" "RAG"\n',
            "```\n",
            "\n",
            "### 自动运行\n",
            "\n",
            "项目发现通过 GitHub Actions 每周一 UTC 00:10\n",
            "(北京时间 08:10) 自动运行。\n",
            "\n",
            "查看工作流: [discover-repos.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-repos.yml)\n",
        ]
    )

    # 写入文件
    discovery_index_path = docs_dir / "discovery.md"
    discovery_index_path.write_text("".join(lines), encoding="utf-8")
    print(f"发现索引已生成: {discovery_index_path}")


def run_generate_report_index(project_root: Path | None = None) -> None:
    """生成报告索引并同步文档。"""
    # 默认以当前工作目录作为项目根目录，便于在仓库中直接执行
    project_root = project_root or Path.cwd().resolve()
    reports_dir = project_root / "reports"
    docs_reports_dir = project_root / "docs" / "reports"
    docs_dir = project_root / "docs"
    index_path = docs_reports_dir / "index.md"

    # 确保目录结构存在
    ensure_reports_structure(reports_dir)

    # 同步报告文件
    sync_reports_to_docs(reports_dir, docs_reports_dir)

    # 同步发现报告
    sync_discovery_reports_to_docs(reports_dir, docs_dir)

    # 生成发现历史索引
    generate_discovery_index(reports_dir, docs_dir)

    # 生成索引
    generate_index(reports_dir, index_path)
