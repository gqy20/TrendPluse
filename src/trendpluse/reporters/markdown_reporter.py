"""Markdown 报告生成器

将每日报告渲染为 Markdown 格式。
"""

from pathlib import Path

from trendpluse.models.signal import DailyReport, Signal


class MarkdownReporter:
    """Markdown 格式报告生成器"""

    def __init__(self, template_path: str | None = None):
        """初始化报告生成器

        Args:
            template_path: 自定义模板路径，None 使用默认模板
        """
        self.template_path = template_path

    def render_signal(self, signal: Signal) -> str:
        """渲染单个信号

        Args:
            signal: 信号对象

        Returns:
            Markdown 格式的信号
        """
        type_emoji = self.get_type_emoji(signal.type)
        impact_emoji = self.get_impact_emoji(signal.impact_score)

        sources_md = "\n".join(
            f"- [{self._extract_repo_name(url)}]({url})" for url in signal.sources
        )

        repos_md = ", ".join(f"`{repo}`" for repo in signal.related_repos)

        return f"""### {type_emoji} {signal.title}

**类型**: `{signal.type}` | **影响**: {impact_emoji} ({signal.impact_score}/5) | \
**分类**: `{signal.category}`

**为什么重要**: {signal.why_it_matters}

**相关仓库**: {repos_md}

**来源**:
{sources_md}
"""

    def render_signals(self, signals: list[Signal], category: str) -> str:
        """渲染信号列表

        Args:
            signals: 信号列表
            category: 分类名称（工程/研究）

        Returns:
            Markdown 格式的信号列表
        """
        if not signals:
            return f"## {category}信号\n\n暂无信号。"

        emoji = "🔧" if category == "工程" else "🔬"
        header = f"## {emoji} {category}信号\n\n"

        signals_md = "\n\n".join(self.render_signal(signal) for signal in signals)

        return header + signals_md

    def render_report(self, report: DailyReport) -> str:
        """渲染每日报告

        Args:
            report: 每日报告对象

        Returns:
            Markdown 格式的报告
        """
        header = f"""# TrendPulse 每日报告 - {report.date}

> {report.summary_brief}

"""

        # 工程信号
        engineering_section = self.render_signals(report.engineering_signals, "工程")

        # 研究信号
        research_section = self.render_signals(report.research_signals, "研究")

        # Commit 信号（仅在有内容时渲染）
        commit_section = ""
        if report.commit_signals:
            commit_section = "\n" + self._render_commit_signals(report.commit_signals)

        # 活跃度信息（仅在有内容时渲染）
        activity_section = ""
        if report.activity:
            activity_section = "\n" + self._render_activity(report.activity)

        # 统计信息
        stats_section = self._render_stats(report.stats)

        return (
            header
            + engineering_section
            + "\n\n"
            + research_section
            + commit_section
            + activity_section
            + stats_section
        )

    def _render_commit_signals(self, signals: list[Signal]) -> str:
        """渲染 commit 信号

        Args:
            signals: commit 信号列表

        Returns:
            Markdown 格式的 commit 信号
        """
        header = "## 💾 Commit 信号\n\n"

        if not signals:
            return header + "暂无 commit 信号。\n"

        signals_md = "\n\n".join(self.render_signal(signal) for signal in signals)

        return header + signals_md

    def _render_stats(self, stats: dict) -> str:
        """渲染统计信息

        Args:
            stats: 统计数据

        Returns:
            Markdown 格式的统计信息
        """
        lines = ["\n---\n", "## 📊 统计信息\n\n"]

        for key, value in stats.items():
            label = self._format_stat_label(key)
            lines.append(f"- **{label}**: {value}\n")

        return "".join(lines)

    def _render_activity(self, activity: dict) -> str:
        """渲染活跃度信息

        Args:
            activity: 活跃度数据

        Returns:
            Markdown 格式的活跃度信息
        """
        lines = ["---\n", "## 📈 仓库活跃度\n\n"]

        # 总览指标
        lines.append("### 总览\n\n")
        lines.append(f"- **总 Commit 数**: {activity['total_commits']}\n")
        lines.append(f"- **活跃仓库数**: {activity['active_repos']}\n")
        lines.append(f"- **新贡献者数**: {activity['new_contributors']}\n")

        # 活跃仓库详情（最多 10 个）
        if activity["repo_activity"]:
            lines.append("\n### 活跃仓库 TOP 10\n\n")
            lines.append("| 仓库 | Commits | 新贡献者 | Top 贡献者 |\n")
            lines.append("|------|--------|---------|------------|\n")

            for repo in activity["repo_activity"][:10]:
                repo_name = repo["repo"].replace("_", "\\_")
                commits = repo["commit_count"]
                new_contribs = repo["new_contributors"]

                # Top 贡献者（最多 3 个）
                top_contribs = repo["top_contributors"][:3]
                if top_contribs:
                    contrib_list = ", ".join(
                        f"{c['login']} ({c['commits']})" for c in top_contribs
                    )
                else:
                    contrib_list = "-"

                table_row = (
                    f"| {repo_name} | {commits} | {new_contribs} | {contrib_list} |\n"
                )
                lines.append(table_row)

        return "".join(lines)

    def _format_stat_label(self, key: str) -> str:
        """格式化统计标签

        Args:
            key: 统计键名

        Returns:
            格式化后的标签
        """
        labels = {
            "total_prs_analyzed": "分析 PR 数",
            "total_releases": "Release 数",
            "high_impact_signals": "高影响信号数",
            "total_commits_analyzed": "分析 Commit 数",
        }
        return labels.get(key, key)

    def _extract_repo_name(self, url: str) -> str:
        """从 URL 提取仓库名

        Args:
            url: GitHub URL

        Returns:
            仓库名称
        """
        if "github.com/" in url:
            parts = url.split("github.com/")[1].split("/")
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}"
        return "链接"

    def get_impact_emoji(self, score: int) -> str:
        """获取影响评分的表情

        Args:
            score: 影响评分 1-5

        Returns:
            星星表情字符串
        """
        return "⭐" * score

    def get_type_emoji(self, signal_type: str) -> str:
        """获取信号类型的表情

        Args:
            signal_type: 信号类型

        Returns:
            类型表情
        """
        emojis = {
            "capability": "🚀",
            "abstraction": "🎨",
            "workflow": "⚙️",
            "eval": "📊",
            "safety": "🛡️",
            "performance": "⚡",
            "commit": "💾",
        }
        return emojis.get(signal_type, "📌")

    def save_report(self, report: DailyReport, output_path: str) -> None:
        """保存报告到文件

        Args:
            report: 每日报告对象
            output_path: 输出文件路径
        """
        markdown = self.render_report(report)

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown, encoding="utf-8")
