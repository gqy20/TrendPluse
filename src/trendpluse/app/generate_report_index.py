"""生成报告索引。

从 reports/ 目录读取所有报告，生成 MkDocs 索引页面。
"""

import re
from datetime import datetime
from pathlib import Path
from typing import TypedDict

from trendpluse.app.sync_repos_to_docs import update_index_file


class _ProjectInfo(TypedDict):
    """项目信息。"""

    repo: str
    stars: int


def _get_stat_value(stats: dict[str, str], *keys: str) -> str:
    """按候选键顺序读取统计值。"""
    for key in keys:
        value = stats.get(key)
        if isinstance(value, str) and value:
            return value
    return "0"


def ensure_reports_structure(reports_dir: Path) -> None:
    """确保 reports 目录结构存在。"""
    (reports_dir / "daily").mkdir(parents=True, exist_ok=True)
    (reports_dir / "weekly").mkdir(parents=True, exist_ok=True)
    (reports_dir / "discovery").mkdir(parents=True, exist_ok=True)
    print(f"目录结构已创建: {reports_dir}")


def extract_report_info(report_path: Path) -> dict | None:
    """从报告文件中提取信息。"""
    try:
        content = report_path.read_text(encoding="utf-8")

        date_match = re.search(r"# TrendPulse 每日报告 - (\d{4}-\d{2}-\d{2})", content)
        if not date_match:
            return None
        date_str = date_match.group(1)

        lines = content.split("\n")
        summary_match = None
        for i in range(2, min(10, len(lines))):
            if lines[i].strip().startswith(">"):
                summary_match = re.search(r"> (.+)", lines[i])
                break

        summary = summary_match.group(1) if summary_match else "暂无摘要"

        stats = {}
        stats_pattern = r"- \*\*(.+?)\*\*:\s*(\d+)"
        for match in re.finditer(stats_pattern, content):
            stats[match.group(1)] = match.group(2)

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
    """从周报文件中提取信息。"""
    try:
        content = weekly_path.read_text(encoding="utf-8")

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
    """生成报告索引页面。"""
    daily_dir = reports_dir / "daily"
    weekly_dir = reports_dir / "weekly"

    daily_files = []
    weekly_files = []

    if daily_dir.exists():
        daily_files = sorted(daily_dir.glob("report-*.md"), reverse=True)

    if weekly_dir.exists():
        weekly_files = sorted(weekly_dir.glob("weekly-*.md"), reverse=True)

    daily_reports = []
    for report_file in daily_files:
        info = extract_report_info(report_file)
        if info:
            daily_reports.append(info)

    weekly_reports = []
    for weekly_file in weekly_files:
        info = extract_weekly_report_info(weekly_file)
        if info:
            weekly_reports.append(info)

    if not daily_reports and not weekly_reports:
        print("没有找到报告文件")
        index_content = """# 趋势报告归档

!!! warning "暂无报告"
    报告生成中，请稍后查看...

    报告将在每天 UTC 0:00（北京时间 8:00）自动更新。
"""
        output_path.write_text(index_content, encoding="utf-8")
        return

    latest_daily = daily_reports[0] if daily_reports else None
    latest_weekly = weekly_reports[0] if weekly_reports else None

    total_signals = sum(int(r["stats"].get("分析 PR 数", 0)) for r in daily_reports)
    current_month = datetime.now().strftime("%Y-%m")
    monthly_count = len([r for r in daily_reports if r["date"][:7] == current_month])

    index_lines = [
        "# 趋势报告归档\n",
        "\n",
        "!!! note\n",
        "    所有报告按时间倒序排列，最新的报告在最前面。\n",
        "\n",
        "## 站点概览\n",
        "\n",
        "| 指标 | 数值 | 指标 | 数值 |\n",
        "|------|------|------|------|\n",
        f"| 总日报数 | {len(daily_reports)} | 总周报数 | {len(weekly_reports)} |\n",
        f"| 总分析 PR 数 | {total_signals} | 本月报告数 | {monthly_count} |\n",
        "\n",
    ]

    if latest_daily:
        latest_stats = latest_daily["stats"]
        index_lines.extend(
            [
                "## 今日聚焦\n",
                "\n",
                f"### [{latest_daily['date']}](report-{latest_daily['date']}.md)\n",
                "\n",
                f"> {latest_daily['summary']}\n",
                "\n",
                "| 指标 | 数值 | 指标 | 数值 |\n",
                "|------|------|------|------|\n",
                f"| 分析 PR 数 | {_get_stat_value(latest_stats, '分析 PR 数')} | "
                f"高影响信号 | {_get_stat_value(latest_stats, '高影响信号数')} |\n",
                f"| 涉及仓库数 | {_get_stat_value(latest_stats, '涉及仓库数')} | "
                "Release 数 | "
                f"{_get_stat_value(latest_stats, 'Release 数', '分析 Release 数')} |\n",
                f"| Commit 数 | {_get_stat_value(latest_stats, '分析 Commit 数')} | "
                "Breaking Changes | "
                f"{_get_stat_value(latest_stats, 'Breaking Changes 数')} |\n",
                "\n",
            ]
        )

    if latest_weekly:
        index_lines.extend(
            [
                "## 最新周报\n",
                "\n",
                f"### [{latest_weekly['week_id']}]"
                f"(weekly-{latest_weekly['week_id']}.md)\n",
                "\n",
                f"**时间范围**: {latest_weekly['start_date']} ~ "
                f"{latest_weekly['end_date']}\n",
                "\n",
                f"{latest_weekly['summary']}\n",
                "\n",
            ]
        )

    index_lines.extend(
        [
            "## 最近日报\n",
            "\n",
            "| 日期 | 高影响 | 分析 PR | Release | 报告 |\n",
            "|------|----------|---------|---------|------|\n",
        ]
    )

    for report in daily_reports[:10]:
        stats = report["stats"]
        date = report["date"]
        high_impact = _get_stat_value(stats, "高影响信号数")
        prs = _get_stat_value(stats, "分析 PR 数")
        releases = _get_stat_value(stats, "Release 数", "分析 Release 数")
        index_lines.append(
            f"| {date} | {high_impact} | {prs} | {releases} | "
            f"[查看](report-{date}.md) |\n"
        )

    index_lines.extend(
        [
            "\n",
            "## 最近周报\n",
            "\n",
            "| 周期 | 起止时间 | 报告 |\n",
            "|------|----------|------|\n",
        ]
    )

    for report in weekly_reports[:8]:
        week_id = report["week_id"]
        index_lines.append(
            f"| {week_id} | {report['start_date']} ~ {report['end_date']} | "
            f"[查看](weekly-{week_id}.md) |\n"
        )

    index_lines.extend(
        [
            "\n",
            "## 阅读建议\n",
            "\n",
            "- 想快速掌握当天变化，先看“今日聚焦”。\n",
            "- 想追踪连续趋势，优先读最新周报。\n",
            "- 想按时间回看，使用最近日报和最近周报表格入口。\n",
        ]
    )

    index_content = "".join(index_lines)
    output_path.write_text(index_content, encoding="utf-8")

    print(f"索引已生成: {output_path}")
    print(f"  - 总日报数: {len(daily_reports)}")
    print(f"  - 总周报数: {len(weekly_reports)}")


def sync_reports_to_docs(reports_dir: Path, docs_reports_dir: Path) -> None:
    """同步报告文件到 docs 目录。"""
    docs_reports_dir.mkdir(parents=True, exist_ok=True)

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
    """同步发现报告到 docs 目录。"""
    discovery_dir = reports_dir / "discovery"
    if not discovery_dir.exists():
        return

    discovery_reports_dir = docs_dir / "discovery-reports"
    discovery_reports_dir.mkdir(parents=True, exist_ok=True)

    for report_file in discovery_dir.glob("discovery-*.md"):
        dest_file = discovery_reports_dir / report_file.name
        dest_file.write_text(report_file.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"已复制发现报告: {report_file.name}")


def extract_discovery_report_info(report_path: Path) -> dict | None:
    """从发现报告中提取信息。"""
    try:
        content = report_path.read_text(encoding="utf-8")

        date_match = re.search(r"# 项目发现报告 \((\d{4}-\d{2}-\d{2})\)", content)
        if not date_match:
            return None
        date_str = date_match.group(1)

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

        top_projects: list[_ProjectInfo] = []
        category_distribution: list[dict[str, str]] = []
        in_high_priority = False
        in_category_distribution = False
        project_header_pattern = r"^###\s+([/\w.-]+)\s*$"
        stars_pattern = r"\|\s*Stars\s*\|\s*([\d,]+)\s*\|"
        category_row_pattern = r"\|\s*(.+?)\s*\|\s*(\d+)\s*\|"

        for line in content.split("\n"):
            if "### 📋 分类分布" in line:
                in_category_distribution = True
                continue
            if in_category_distribution:
                if line.startswith("|") and "---" not in line and "分类" not in line:
                    match = re.search(category_row_pattern, line)
                    if match:
                        category_distribution.append(
                            {"name": match.group(1).strip(), "count": match.group(2)}
                        )
                elif line.startswith("##"):
                    in_category_distribution = False

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
            "category_distribution": category_distribution[:5],
        }
    except Exception as e:
        print(f"解析发现报告失败 {report_path}: {e}")
        return None


def generate_discovery_index(reports_dir: Path, docs_dir: Path) -> None:
    """生成发现历史索引页面。"""
    discovery_dir = reports_dir / "discovery"
    if not discovery_dir.exists():
        return

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
    category_distribution = info.get("category_distribution", [])

    lines = [
        "# 项目发现历史\n",
        "\n",
        "自动发现 GitHub 热门项目，并按质量、相关性与可跟踪性进行筛选与归档。\n",
        "\n",
        "## 页面说明\n",
        "\n",
        "- 先看“本期概览”，判断本轮发现规模与推荐密度。\n",
        "- 再看“高优先级推荐 Top 5”，快速锁定值得纳入监控的项目。\n",
        "- 最后用“历史报告”表格回看不同日期的发现结果。\n",
        "\n",
        "## 本期概览\n",
        "\n",
        f"### [{date}](discovery-reports/discovery-{date}.md)\n",
        "\n",
        "| 指标 | 数值 | 指标 | 数值 |\n",
        "|------|------|------|------|\n",
    ]

    overview_lines = [
        f"| 总发现数 | {stats.get('total_discovered', 'N/A')} | "
        f"通过质量评估 | {stats.get('passed_quality', 'N/A')} |\n",
        f"| 高优先级 | {stats.get('high_priority', 'N/A')} | "
        f"去重移除 | {stats.get('duplicates_removed', 'N/A')} |\n",
        f"| 已在监控 | {stats.get('already_monitored', 'N/A')} | "
        f"完整报告 | [查看](discovery-reports/discovery-{date}.md) |\n",
        "\n",
    ]

    if category_distribution:
        overview_lines.extend(
            [
                "### 分类分布 Top 5\n",
                "\n",
                "| 分类 | 数量 |\n",
                "|------|------|\n",
            ]
        )
        for item in category_distribution:
            overview_lines.append(f"| {item['name']} | {item['count']} |\n")
        overview_lines.append("\n")

    overview_lines.extend(
        [
            "## 高优先级推荐 Top 5\n",
            "\n",
            "| 项目 | Stars |\n",
            "|------|-------|\n",
        ]
    )

    for project in top_projects:
        repo_link = f"[{project['repo']}](https://github.com/{project['repo']})"
        overview_lines.append(f"| {repo_link} | {project['stars']:,} |\n")

    if not top_projects:
        overview_lines.append("| 暂无 | - |\n")

    overview_lines.extend(
        [
            "\n",
        ]
    )

    lines.extend(overview_lines)

    lines.extend(
        [
            "\n",
            "## 历史报告\n",
            "\n",
            "| 日期 | 总发现 | 高优先级 | 报告 |\n",
            "|------|--------|----------|------|\n",
        ]
    )

    for report_file in discovery_files[:10]:
        info = extract_discovery_report_info(report_file)
        if info:
            date = info["date"]
            total = info["stats"].get("total_discovered", "N/A")
            high = info["stats"].get("high_priority", "N/A")
            report_url = f"discovery-reports/discovery-{date}.md"
            lines.append(f"| {date} | {total} | {high} | [查看]({report_url}) |\n")

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
            "查看工作流: [discover-projects.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-projects.yml)\n",
        ]
    )

    discovery_index_path = docs_dir / "discovery.md"
    discovery_index_path.write_text("".join(lines), encoding="utf-8")
    print(f"发现索引已生成: {discovery_index_path}")


def run_generate_report_index(project_root: Path | None = None) -> None:
    """生成报告索引并同步文档。"""
    project_root = project_root or Path.cwd().resolve()
    reports_dir = project_root / "reports"
    docs_reports_dir = project_root / "docs" / "reports"
    docs_dir = project_root / "docs"
    index_path = docs_reports_dir / "index.md"

    ensure_reports_structure(reports_dir)
    sync_reports_to_docs(reports_dir, docs_reports_dir)
    sync_discovery_reports_to_docs(reports_dir, docs_dir)
    generate_discovery_index(reports_dir, docs_dir)
    generate_index(reports_dir, index_path)
    update_index_file(docs_dir / "index.md")
