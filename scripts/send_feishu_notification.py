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
    # 找到 Commit 信号标题的结束位置
    commit_start = content.find("## 💾 Commit 信号")
    if commit_start != -1:
        commit_header_end = commit_start + len("## 💾 Commit 信号")
        # 用正则找下一个真正的 ## 标题（后面不是 #）
        # 注意：使用 \n##[^#] 而不是 \n\n##[^#]，因为有些分隔使用 --- 而不是空行
        next_heading_match = re.search(r"\n##[^#]", content[commit_header_end:])
        if next_heading_match:
            commit_end = commit_header_end + next_heading_match.start()
        else:
            commit_end = len(content)
        commit_text = content[commit_header_end:commit_end]

        # 按 ### 分割每个信号（跳过第一个空元素）
        parts = commit_text.split("\n### ")
        for sig_text in parts[1:]:  # 跳过第一个空元素
            if not sig_text.strip():
                continue
            lines = sig_text.strip().split("\n")
            signal_title = lines[0].strip()

            # 查找类型和影响
            sig_type = None
            impact = None
            score = 0
            for line in lines:
                type_match = re.search(r"\*\*类型\*\*:\s*`([^`]+)`", line)
                impact_match = re.search(r"\*\*影响\*\*:\s*([⭐]+)\s*\((\d+)/5\)", line)
                if type_match:
                    sig_type = type_match.group(1)
                if impact_match:
                    impact = impact_match.group(1)
                    score = int(impact_match.group(2))
                if sig_type and impact:
                    break

            if sig_type and impact:
                commit_signals.append(
                    {
                        "title": signal_title,
                        "type": sig_type,
                        "impact": impact,
                        "score": score,
                    }
                )

    # 提取版本发布（最新 5 个）
    releases: list[dict[str, str]] = []
    # 找到版本发布部分
    release_section_start = content.find("### 最新发布")
    if release_section_start != -1:
        # 从这里开始找 #### 开头的版本块
        release_text = content[release_section_start:]
        for match in re.finditer(r"####\s+([^\n]+)\n\n", release_text):
            if len(releases) >= 5:
                break
            # 标题行包含仓库链接和版本，例如: ⚡ [danielmiessler/fabric](...) v1.4.367
            header = match.group(1)

            # 从标题行提取仓库和版本
            repo_match = re.search(
                r"\[([\w-]+/[\w.-]+)\]\(https://github\.com/[\w-]+/[\w.-]+\)", header
            )
            # 版本是 URL 链接后的文本，可能是 v1.4.367 或 langchain-core==1.2.6 格式
            # 匹配 URL 的结束括号 ) 后面跟空格和版本号
            version_match = re.search(r"\)\s+(\S+)", header)

            if not repo_match or not version_match:
                continue

            # 获取这个块的内容（用于提取作者和日期）
            block_start = match.end()
            # 找下一个 #### 或部分结束
            next_match = re.search(r"\n\n####", release_text[block_start:])
            if next_match:
                block_end = block_start + next_match.start()
            else:
                # 找下一个 ## 标题或文件末尾
                end_match = re.search(r"\n\n##", release_text[block_start:])
                if end_match:
                    block_end = block_start + end_match.start()
                else:
                    block_end = len(release_text)

            block = release_text[block_start:block_end]

            # 从块中提取作者和日期
            author_match = re.search(r"\*\*发布者\*\*:\s*`([^`]+)`", block)
            time_match = re.search(r"\*\*时间\*\*:\s*(\d{4}-\d{2}-\d{2})", block)

            releases.append(
                {
                    "repo": repo_match.group(1),
                    "version": version_match.group(1).strip(),
                    "author": author_match.group(1) if author_match else "Unknown",
                    "date": time_match.group(1) if time_match else "",
                }
            )

    # 提取活跃仓库 TOP 3
    top_repos = []
    activity_start = content.find("### 活跃仓库 TOP 10")
    if activity_start != -1:
        activity_text = content[activity_start : activity_start + 2000]
        # 提取表格行
        for line in activity_text.split("\n"):
            # 跳过表头和分隔行（包含 --- 或全是 | 和空格）
            if not line.strip() or not line.startswith("|"):
                continue
            # 跳过表头 | 仓库 | 和分隔行 |------|
            if "| 仓库 |" in line or "|------" in line or line.count("---") > 0:
                continue
            # 必须包含链接格式 [name](url)
            if "](" not in line:
                continue

            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2 and parts[0] and parts[1].isdigit():
                repo_name = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", parts[0])
                top_repos.append({"repo": repo_name, "commits": parts[1]})
                if len(top_repos) >= 3:
                    break

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
