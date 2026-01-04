"""发送飞书通知脚本

用于 GitHub Actions 在部署完成后发送飞书通知。
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trendpluse.notifiers.feishu import FeishuNotifier

console = Console()


def extract_summary_from_markdown(report_path: str) -> dict:
    """从 Markdown 报告提取摘要信息

    Args:
        report_path: 报告文件路径

    Returns:
        包含标题、摘要、Commit 信号、版本发布、活跃度等的字典
    """
    content = Path(report_path).read_text(encoding="utf-8")

    # 提取标题和第一段（摘要）
    title_match = re.search(r"^# (.+)", content, re.MULTILINE)
    title = title_match.group(1) if title_match else "TrendPulse 每日报告"

    # 提取引用块（摘要）
    summary_match = re.search(r"^> (.+)", content, re.MULTILINE)
    summary = summary_match.group(1) if summary_match else "每日趋势分析报告已生成"

    # 尝试提取统计信息
    stats = {}
    stats_section = re.search(
        r"## 📊 统计信息\n\n(.*?)(?=\n\n---|\n*$)", content, re.DOTALL
    )
    if stats_section:
        for line in stats_section.group(1).split("\n"):
            if "- **" in line:
                match = re.search(r"- \*\*(.+?)\*\*:\s*(.+)", line)
                if match:
                    stats[match.group(1)] = match.group(2)

    # 提取 Commit 信号
    commit_signals = []
    commit_section = re.search(
        r"## 💾 Commit 信号\n\n(.*?)(?=##\s|\n\n---|\n*$)", content, re.DOTALL
    )
    if commit_section:
        # 每个信号以 ### 开头
        signal_blocks = re.findall(
            r"###\s+([^\n]+)\n\n(\*\*类型\*\*:.+?)(?=\n\n###\s|\n\n##|\n\n---|\Z)",
            commit_section.group(1),
            re.DOTALL,
        )
        for signal_title, block in signal_blocks:
            # 提取类型和影响
            type_match = re.search(r"\*\*类型\*\*:\s*`([^`]+)`", block)
            impact_match = re.search(r"\*\*影响\*\*:\s*([⭐]+)\s*\((\d+)/5\)", block)

            if type_match and impact_match:
                commit_signals.append(
                    {
                        "title": signal_title.strip(),
                        "type": type_match.group(1),
                        "impact": impact_match.group(1),
                        "score": int(impact_match.group(2)),
                    }
                )

    # 提取版本发布（最新 5 个）
    releases = []
    release_section = re.search(
        r"## 🎯 版本发布动态\n\n.*?### 最新发布\n\n(.*?)(?=##\s|\n\n---|\n*$)",
        content,
        re.DOTALL,
    )
    if release_section:
        # 每个发布以 #### 开头
        release_blocks = re.findall(
            r"####\s+[^\n]+\n\n((?:(?!####).)+?)", release_section.group(1), re.DOTALL
        )
        for block in release_blocks[:5]:
            # 提取仓库名和版本号 - 匹配 [repo](url) version 格式
            repo_match = re.search(
                r"\[([^\]]+)\]\(https://github\.com/[^/]+/[^)]+\)\s+([^\n]+)", block
            )

            # 提取发布者
            author_match = re.search(r"\*\*发布者\*\*:\s*`([^`]+)`", block)
            # 提取时间
            time_match = re.search(r"\*\*时间\*\*:\s*(\d{4}-\d{2}-\d{2})", block)

            if repo_match:
                releases.append(
                    {
                        "repo": repo_match.group(1),
                        "version": repo_match.group(2).strip(),
                        "author": author_match.group(1) if author_match else "Unknown",
                        "date": time_match.group(1) if time_match else "",
                    }
                )

    # 提取活跃仓库 TOP 3
    top_repos = []
    activity_section = re.search(
        r"### 活跃仓库 TOP 10\n\n(.*?)(?=##\s|\n\n---|\n*$)", content, re.DOTALL
    )
    if activity_section:
        # 跳过表头，提取前 3 行数据
        table_lines = activity_section.group(1).split("\n")
        data_lines = [
            line
            for line in table_lines
            if line.startswith("|") and not line.startswith("| 仓库|")
        ]
        for line in data_lines[:3]:
            parts = [p.strip() for p in line.split("|")[1:-1]]  # 去掉首尾空元素
            if len(parts) >= 2:
                # parts[0] 是仓库名（带链接），parts[1] 是 commit 数
                repo_name = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", parts[0])
                top_repos.append({"repo": repo_name, "commits": parts[1]})

    return {
        "title": title,
        "summary": summary,
        "stats": stats,
        "commit_signals": commit_signals,
        "releases": releases,
        "top_repos": top_repos,
    }


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
        # 提取报告信息
        info = extract_summary_from_markdown(str(report_path))

        # 初始化通知器
        notifier = FeishuNotifier(
            webhook_url=webhook_url,
            at_mobiles=at_mobiles,
            secret=secret or None,
        )

        # 构建通知内容
        content = info["summary"]

        # 添加 Commit 信号（如果有）
        if info.get("commit_signals"):
            content += "\n\n━━━━━━━━━━━━━━━━━━\n"
            content += f"**💾 Commit 信号 ({len(info['commit_signals'])}个)**"
            content += "\n━━━━━━━━━━━━━━━━━━"
            for sig in info["commit_signals"]:
                title = sig["title"]
                # 简化标题，移除 emoji 重复
                title = re.sub(r"^[\U0001F300-\U0001F9FF]+\s+", "", title)
                content += f"\n\n{sig['impact']} **{title}**"

        # 添加版本发布（如果有）
        if info.get("releases"):
            content += "\n\n━━━━━━━━━━━━━━━━━━\n"
            content += f"**🎯 版本发布 ({len(info['releases'])}个)**"
            content += "\n━━━━━━━━━━━━━━━━━━"
            for rel in info["releases"][:5]:
                content += f"\n• **{rel['repo']}** {rel['version']}"
                if rel.get("date"):
                    content += f" ({rel['date']})"

        # 添加活跃仓库 TOP 3（如果有）
        if info.get("top_repos"):
            content += "\n\n━━━━━━━━━━━━━━━━━━\n"
            content += "**📈 仓库活跃度 TOP 3**"
            content += "\n━━━━━━━━━━━━━━━━━━"
            for i, repo in enumerate(info["top_repos"], 1):
                content += f"\n{i}. **{repo['repo']}** ({repo['commits']} commits)"

        # 添加统计信息
        if info["stats"]:
            content += "\n\n━━━━━━━━━━━━━━━━━━\n"
            content += "**📊 统计信息**"
            content += "\n━━━━━━━━━━━━━━━━━━"
            for key, value in info["stats"].items():
                content += f"\n• {key}: {value}"

        # 添加部署链接
        if deployment_url:
            content += f"\n\n🔗 **[查看完整报告]({deployment_url})**"

        # 发送通知
        success = notifier.send(info["title"], content, url=deployment_url)

        if success:
            console.print("[green]✓ 飞书通知发送成功[/green]")
        else:
            console.print("[red]✗ 飞书通知发送失败[/red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[red]发送通知失败:[/red] {e}")
        # 降级：发送最简单的通知
        try:
            notifier = FeishuNotifier(
                webhook_url=webhook_url,
                at_mobiles=at_mobiles,
                secret=secret or None,
            )

            title = f"📊 TrendPulse 每日报告 - {report_date}"
            content = "每日趋势分析报告已生成并部署到 GitHub Pages。"

            if deployment_url:
                content += f"\n\n🔗 [查看报告]({deployment_url})"

            success = notifier.send(title, content, url=deployment_url)

            if success:
                console.print("[green]✓ 简化通知发送成功[/green]")
            else:
                console.print("[red]✗ 简化通知发送失败[/red]")
                sys.exit(1)

        except Exception as e2:
            console.print(f"[red]降级通知也失败:[/red] {e2}")
            sys.exit(1)


if __name__ == "__main__":
    main()
