"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal, cast

from dotenv import load_dotenv
from rich.console import Console

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleaseInfo,
    ReleasesData,
    RepoActivity,
    Signal,
)
from trendpluse.notifiers.feishu import FeishuNotifier

console = Console()


def parse_daily_report_from_markdown(report_path: str, report_date: str) -> DailyReport:
    """从 Markdown 报告解析并重建 DailyReport 对象

    Args:
        report_path: 报告文件路径
        report_date: 报告日期

    Returns:
        DailyReport 对象
    """
    content = Path(report_path).read_text(encoding="utf-8")

    # 提取标题和第一段（摘要）
    summary_match = re.search(r"^> (.+)", content, re.MULTILINE)
    summary = summary_match.group(1) if summary_match else "每日趋势分析报告"

    # 初始化信号列表
    engineering_signals = []
    research_signals = []
    commit_signals = []
    release_signals = []

    # 解析工程信号
    eng_start = content.find("## 🔧 工程信号")
    if eng_start != -1:
        eng_end = content.find("\n\n##", eng_start + 1)
        if eng_end == -1:
            eng_end = len(content)
        eng_text = content[eng_start:eng_end]
        engineering_signals = _parse_signals_from_markdown(eng_text)

    # 解析研究信号
    research_start = content.find("## 🔬 研究信号")
    if research_start != -1:
        research_end = content.find("\n\n##", research_start + 1)
        if research_end == -1:
            research_end = len(content)
        research_text = content[research_start:research_end]
        research_signals = _parse_signals_from_markdown(research_text)

    # 解析 Commit 信号
    commit_start = content.find("## 💾 Commit 信号")
    if commit_start != -1:
        commit_end = content.find("\n\n##", commit_start + 1)
        if commit_end == -1:
            commit_end = len(content)
        commit_text = content[commit_start:commit_end]
        commit_signals = _parse_signals_from_markdown(commit_text)

    # 解析 Release 信号
    rel_sig_start = content.find("## 🎯 Release 信号")
    if rel_sig_start != -1:
        rel_sig_end = content.find("\n\n##", rel_sig_start + 1)
        if rel_sig_end == -1:
            rel_sig_end = len(content)
        rel_sig_text = content[rel_sig_start:rel_sig_end]
        release_signals = _parse_signals_from_markdown(rel_sig_text)

    # 解析活跃度数据
    activity = None
    activity_start = content.find("## 📈 仓库活跃度")
    if activity_start != -1:
        activity = _parse_activity_from_markdown(content[activity_start:])

    # 解析 Release 数据
    releases = None
    release_start = content.find("## 🎯 版本发布动态")
    if release_start != -1:
        release_end = content.find("\n\n##", release_start + 1)
        if release_end == -1:
            release_end = len(content)
        releases = _parse_releases_from_markdown(content[release_start:release_end])

    # 解析统计信息
    stats = {}
    stats_section = re.search(r"## 📊 统计信息\n\n(.*?)(?=\n*$|$)", content, re.DOTALL)
    if stats_section:
        for line in stats_section.group(1).split("\n"):
            if "- **" in line:
                match = re.search(r"- \*\*(.+?)\*\*:\s*(.+)", line)
                if match:
                    stats[match.group(1)] = match.group(2)

    # 构建 DailyReport
    return DailyReport(
        date=report_date,
        summary_brief=summary,
        engineering_signals=engineering_signals,
        research_signals=research_signals,
        commit_signals=commit_signals,
        release_signals=release_signals,
        activity=activity,
        releases=releases,
        stats=stats,
    )


def _parse_signals_from_markdown(text: str) -> list[Signal]:
    """从 Markdown 文本解析信号列表

    Args:
        text: 包含信号的 Markdown 文本

    Returns:
        信号列表
    """
    signals = []
    # 按 ### 分割每个信号
    parts = text.split("\n### ")
    for sig_text in parts[1:]:  # 跳过第一个空元素
        if not sig_text.strip():
            continue

        lines = sig_text.strip().split("\n")
        if not lines:
            continue

        # 提取标题（第一行，移除 emoji）
        title = lines[0].strip()
        title = re.sub(r"^[\U0001F300-\U0001F9FF]+\s+", "", title)

        # 默认值
        sig_type = "capability"
        category = "engineering"
        impact_score = 3
        why_it_matters = ""
        sources = []
        related_repos = []

        # 解析字段
        for i, line in enumerate(lines):
            # 类型
            type_match = re.search(r"\*\*类型\*\*:\s*`([^`]+)`", line)
            if type_match:
                sig_type = type_match.group(1)

            # 分类
            cat_match = re.search(r"\*\*分类\*\*:\s*`([^`]+)`", line)
            if cat_match:
                category = cat_match.group(1)

            # 影响评分
            score_match = re.search(r"\*\*影响\*\*:.+?\((\d+)/5\)", line)
            if score_match:
                impact_score = int(score_match.group(1))

            # 为什么重要
            why_match = re.search(r"\*\*为什么重要\*\*:\s*(.+)", line)
            if why_match:
                why_it_matters = why_match.group(1)

            # 相关仓库
            repos_match = re.search(r"\*\*相关仓库\*\*:\s*(.+)", line)
            if repos_match:
                repo_str = repos_match.group(1)
                related_repos = [
                    r.strip("` ") for r in repo_str.split(",") if r.strip()
                ]

            # 来源链接
            if line.startswith("- [") and "](" in line:
                url_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
                if url_match:
                    sources.append(url_match.group(2))

        # 生成 ID
        sig_id = f"{sig_type}-{title[:20].replace(' ', '-')}"

        signals.append(
            Signal(
                id=sig_id,
                title=title,
                type=cast(
                    Literal[
                        "capability",
                        "abstraction",
                        "workflow",
                        "eval",
                        "safety",
                        "performance",
                        "commit",
                        "release",
                    ],
                    sig_type,
                ),
                category=cast(Literal["engineering", "research"], category),
                impact_score=impact_score,
                why_it_matters=why_it_matters,
                sources=sources,
                related_repos=related_repos,
            )
        )

    return signals


def _parse_activity_from_markdown(text: str) -> ActivityData:
    """从 Markdown 文本解析活跃度数据

    Args:
        text: 包含活跃度数据的 Markdown 文本

    Returns:
        ActivityData 对象
    """
    # 默认值
    total_commits = 0
    active_repos_count = 0
    new_contributors = 0
    top_repos = []

    # 提取总览指标
    total_match = re.search(r"- \*\*总 Commit 数\*\*:\s*(\d+)", text)
    if total_match:
        total_commits = int(total_match.group(1))

    active_match = re.search(r"- \*\*活跃仓库数\*\*:\s*(\d+)", text)
    if active_match:
        active_repos_count = int(active_match.group(1))

    new_match = re.search(r"- \*\*新贡献者数\*\*:\s*(\d+)", text)
    if new_match:
        new_contributors = int(new_match.group(1))

    # 提取表格数据
    table_start = text.find("| 仓库 |")
    if table_start != -1:
        table_text = text[table_start:]
        lines = table_text.split("\n")
        for line in lines:
            if not line.startswith("|") or "| 仓库 |" in line or "|------" in line:
                continue
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 3 and parts[0] and parts[1].isdigit():
                # 提取仓库名（去掉链接格式）
                repo_name = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", parts[0])
                top_repos.append(
                    RepoActivity(
                        repo=repo_name,
                        commits=int(parts[1]),
                        new_contributors=int(parts[2]) if parts[2].isdigit() else 0,
                        top_contributors=[],
                    )
                )

    return ActivityData(
        total_commits=total_commits,
        active_repos_count=active_repos_count,
        new_contributors=new_contributors,
        top_repos=top_repos[:10],
    )


def _parse_releases_from_markdown(text: str) -> ReleasesData:
    """从 Markdown 文本解析 Release 数据

    Args:
        text: 包含 Release 数据的 Markdown 文本

    Returns:
        ReleasesData 对象
    """
    releases = []

    # 查找所有 #### 开头的版本块
    for match in re.finditer(r"####\s+([^\n]+)\n\n", text):
        header = match.group(1)

        # 提取仓库和版本
        repo_match = re.search(
            r"\[([\w-]+/[\w.-]+)\]\(https://github\.com/[\w-]+/[\w.-]+\)", header
        )
        version_match = re.search(r"\)\s+(\S+)", header)

        if not repo_match or not version_match:
            continue

        # 获取块内容
        block_start = match.end()
        next_match = re.search(r"\n\n####", text[block_start:])
        if next_match:
            block_end = block_start + next_match.start()
        else:
            block_end = len(text)

        block = text[block_start:block_end]

        # 提取详细信息
        author_match = re.search(r"\*\*发布者\*\*:\s*`([^`]+)`", block)
        date_match = re.search(r"\*\*时间\*\*:\s*(\d{4}-\d{2}-\d{2})", block)
        summary_match = re.search(r"\*\*摘要\*\*:\s*(.+?)(?=\n\n|\n\*\*)", block)
        assets_match = re.search(r"\*\*资产\*\*:\s*(\d+)", block)

        # 提取 URL
        url_match = re.search(r"\*\*链接\*:\s*\[.+?\]\(([^)]+)\)", block)

        releases.append(
            ReleaseInfo(
                repo=repo_match.group(1),
                version=version_match.group(1).strip(),
                author=author_match.group(1) if author_match else "Unknown",
                date=date_match.group(1) if date_match else "",
                summary=summary_match.group(1).strip() if summary_match else "",
                assets_count=int(assets_match.group(1)) if assets_match else 0,
                url=url_match.group(1) if url_match else "",
            )
        )

    return ReleasesData(
        total_count=len(releases),
        unique_repos_count=len(set(r.repo for r in releases)),
        releases=releases,
    )


def main():
    """主函数"""
    load_dotenv()

    # 获取环境变量
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL", "")
    secret = os.getenv("FEISHU_SECRET", "")
    at_mobiles_str = os.getenv("FEISHU_AT_MOBILES", "")
    deployment_url = os.getenv("DEPLOYMENT_URL", "")
    report_date = os.getenv("REPORT_DATE", datetime.now().strftime("%Y-%m-%d"))

    # 检查 webhook URL
    if not webhook_url:
        console.print("[yellow]FEISHU_WEBHOOK_URL 未配置，跳过通知[/yellow]")
        return

    # 解析 @ 提醒列表
    at_mobiles = (
        [m.strip() for m in at_mobiles_str.split(",") if m.strip()]
        if at_mobiles_str
        else []
    )

    console.print("[bold]发送飞书通知[/bold]")
    console.print(f"  日期: {report_date}")
    console.print(f"  部署 URL: {deployment_url or '未设置'}")
    console.print(f"  @ 提醒: {len(at_mobiles)} 个")

    # 查找报告文件
    report_path = Path(f"reports/report-{report_date}.md")

    if not report_path.exists():
        console.print(f"[yellow]报告文件不存在: {report_path}[/yellow]")
        return

    try:
        # 解析报告并重建 DailyReport 对象
        report = parse_daily_report_from_markdown(str(report_path), report_date)

        console.print(f"  解析到 {len(report.commit_signals)} 个 commit 信号")

        # 初始化通知器
        notifier = FeishuNotifier(
            webhook_url=webhook_url,
            at_mobiles=at_mobiles,
            secret=secret or None,
        )

        console.print(f"  Webhook URL: {webhook_url[:30]}...{webhook_url[-10:]}")
        console.print(f"  使用签名: {'是' if secret else '否'}")

        # 发送通知（使用 send_report 发送完整格式）
        console.print("  正在发送...")
        success = notifier.send_report(report)

        if success:
            console.print("[green]✓ 飞书通知发送成功[/green]")
        else:
            console.print("[red]✗ 飞书通知发送失败[/red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[red]发送通知失败:[/red] {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
