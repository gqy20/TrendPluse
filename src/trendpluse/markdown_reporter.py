"""Markdown 报告生成器

将每日报告渲染为 Markdown 格式。
"""

from pathlib import Path

from trendpluse.models.issue_agent import IssueAgentReport
from trendpluse.models.signal import (
    ActivityData,
    CoreTrend,  # noqa: F401 (used in WeeklyReport.core_trends type annotation)
    DailyReport,
    ReleasesData,
    ReleaseSummary,
    ReportStats,
    Signal,
    WeeklyActivity,
    WeeklyReport,
)
from trendpluse.utils.formatters import (
    format_source_url,
    get_impact_emoji,
    get_release_type_emoji,
)


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
            f"- [{format_source_url(url)}]({url})" for url in signal.sources
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

        if category == "工程":
            header = "## 🔧 工程信号\n\n"
        elif category == "研究":
            header = "## 🔬 研究信号\n\n"
        elif category == "重点":
            header = "## 重点信号\n\n"
        else:
            header = f"## {category}信号\n\n"

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

        engineering_section = self.render_signals(report.engineering_signals, "工程")
        research_section = "\n\n" + self.render_signals(report.research_signals, "研究")
        # Commit 信号（仅在有内容时渲染）
        commit_section = ""
        if report.commit_signals:
            commit_section = "\n" + self._render_commit_signals(report.commit_signals)

        # Release 信号（仅在有内容时渲染）
        release_signals_section = ""
        if report.release_signals:
            release_signals_section = "\n" + self._render_release_signals(
                report.release_signals
            )

        # Release 信息（仅在有内容时渲染）
        release_section = ""
        if report.releases:
            release_section = "\n\n" + self._render_releases(report.releases)

        # Breaking Changes（仅在有内容时渲染）
        breaking_changes_section = ""
        if report.breaking_changes:
            breaking_changes_section = "\n\n" + self._render_breaking_changes(
                report.breaking_changes
            )

        # 活跃度信息（仅在有内容时渲染）
        activity_section = ""
        if report.activity:
            activity_section = "\n\n" + self._render_activity(report.activity)

        # Issue Agent 信息（仅在有内容时渲染）
        issue_insights_section = ""
        if report.issue_insights:
            issue_insights_section = "\n\n" + self._render_issue_insights(
                report.issue_insights
            )

        # 统计信息
        stats_section = self._render_stats(report.stats)

        return (
            header
            + engineering_section
            + research_section
            + commit_section
            + release_signals_section
            + release_section
            + breaking_changes_section
            + activity_section
            + issue_insights_section
            + stats_section
        )

    def _render_issue_insights(self, report: IssueAgentReport) -> str:
        cross_repo_points = [
            item for item in report.top_pain_points if len(item.affected_repos) > 1
        ]
        single_repo_points = [
            item for item in report.top_pain_points if len(item.affected_repos) <= 1
        ]
        lines = ["---\n", "## 🧠 Issue 洞察（Agent）\n\n"]
        lines.append(
            "预期文件: "
            f"{report.expected_files}，生成文件: {report.generated_files}，"
            f"解析成功: {report.parsed_files}，失败文件: {report.failed_files}\n\n"
        )
        lines.append(
            "质量等级: "
            f"`{report.quality_status}`，质量分: `{report.quality_score:.3f}`\n\n"
        )
        lines.append(
            "语义指标: "
            f"跨仓库项: `{report.cross_repo_item_count}`，"
            f"other 分类: `{report.other_category_count}`，"
            f"分类覆盖率: `{report.category_coverage * 100:.1f}%`\n\n"
        )

        if report.summary_brief:
            lines.append("### 全局摘要\n\n")
            lines.append(f"{report.summary_brief}\n\n")

        if report.global_highlights:
            lines.append("### 全局亮点\n\n")
            for item in report.global_highlights:
                lines.append(f"- {item}\n")
            lines.append("\n")

        if not report.top_pain_points:
            lines.append("暂无可用的 Issue 洞察。\n")
            if report.failed_samples:
                lines.append(
                    f"失败样例: {', '.join(f'`{s}`' for s in report.failed_samples)}\n"
                )
            return "".join(lines)

        if cross_repo_points:
            lines.append("### 跨仓库共性问题\n\n")
            lines.append("| 排名 | 痛点 | 提及次数 | 受影响仓库 |\n")
            lines.append("|------|------|----------|------------|\n")
            for idx, pain_point in enumerate(cross_repo_points[:5], 1):
                repos_str = ", ".join(f"`{r}`" for r in pain_point.affected_repos[:2])
                if len(pain_point.affected_repos) > 2:
                    repos_str += f" (+{len(pain_point.affected_repos) - 2})"
                lines.append(
                    f"| {idx} | {pain_point.topic} | "
                    f"{pain_point.count} | {repos_str} |\n"
                )
        else:
            lines.append("### 跨仓库共性问题\n\n")
            lines.append("暂无跨仓库共性问题。\n\n")

        if single_repo_points:
            lines.append("### 高影响单仓问题\n\n")
            lines.append("| 排名 | 痛点 | 提及次数 | 仓库 |\n")
            lines.append("|------|------|----------|------|\n")
            for idx, pain_point in enumerate(single_repo_points[:5], 1):
                repo_name = (
                    f"`{pain_point.affected_repos[0]}`"
                    if pain_point.affected_repos
                    else "`未知仓库`"
                )
                lines.append(
                    f"| {idx} | {pain_point.topic} | "
                    f"{pain_point.count} | {repo_name} |\n"
                )

        representative_points = cross_repo_points or single_repo_points
        top_sources = (
            representative_points[0].source_issues if representative_points else []
        )
        if top_sources:
            lines.append("\n**代表 Issue**:\n\n")
            for source in top_sources[:3]:
                label = source.title or format_source_url(source.url)
                lines.append(f"- [`{source.repo}`] [{label}]({source.url})\n")

        if report.repo_reports:
            lines.append("\n### 仓库级信号\n\n")
            for repo_report in report.repo_reports[:5]:
                lines.append(f"#### `{repo_report.repo}`\n\n")
                if not repo_report.signals:
                    lines.append("- 暂无有效信号\n\n")
                    continue
                for signal in repo_report.signals[:3]:
                    lines.append(f"- **{signal.topic}**（{signal.count}）")
                    if signal.summary:
                        lines.append(f"：{signal.summary}")
                    lines.append("\n")
                    for source in signal.source_issues[:2]:
                        issue_label = (
                            f"#{source.issue_number} {source.title}".strip()
                            if source.issue_number is not None
                            else (source.title or format_source_url(source.url))
                        )
                        lines.append(f"  - [{issue_label}]({source.url})\n")
                lines.append("\n")

        return "".join(lines)

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

    def _render_release_signals(self, signals: list[Signal]) -> str:
        """渲染 release 信号

        Args:
            signals: release 信号列表

        Returns:
            Markdown 格式的 release 信号
        """
        header = "## 🎯 Release 信号\n\n"

        if not signals:
            return header + "暂无 release 信号。\n"

        signals_md = "\n\n".join(self.render_signal(signal) for signal in signals)

        return header + signals_md

    def _render_breaking_changes(self, breaking_changes: list[dict]) -> str:
        """渲染 Breaking Changes

        Args:
            breaking_changes: breaking changes 列表

        Returns:
            Markdown 格式的 breaking changes
        """
        lines = ["---", "\n## ⚠️ Breaking Changes\n\n"]

        for bc in breaking_changes:
            repo_name = bc["repo"].replace("_", "\\_")
            tag_name = bc["tag_name"]
            repo_link = f"[{repo_name}](https://github.com/{bc['repo']})"

            lines.append(f"### {repo_link} `{tag_name}`\n\n")

            for change in bc.get("changes", []):
                impact = change.get("impact", "unknown")
                category = change.get("category", "")
                description = change.get("description", "")
                impact_emoji = get_impact_emoji(impact)

                lines.append(f"- {impact_emoji} **[{category}]** {description}\n")

            lines.append("\n")

        return "".join(lines)

    def _render_stats(self, stats: ReportStats) -> str:
        """渲染统计信息

        Args:
            stats: 统计数据

        Returns:
            Markdown 格式的统计信息
        """
        lines = ["\n---\n", "\n## 📊 统计信息\n\n"]
        ordered_keys = [
            "total_signals",
            "pr_count",
            "commit_count",
            "release_count",
            "unique_repos",
            "high_impact_signals",
            "total_prs_analyzed",
            "total_commits_analyzed",
            "total_releases",
            "total_releases_analyzed",
            "total_breaking_changes",
        ]

        for key in ordered_keys:
            if key not in type(stats).model_fields:
                continue
            value = getattr(stats, key)
            if value is None:
                continue
            label = self._format_stat_label(key)
            lines.append(f"- **{label}**: {value}\n")

        return "".join(lines)

    def _render_activity(self, activity: ActivityData) -> str:
        """渲染活跃度信息

        Args:
            activity: 活跃度数据

        Returns:
            Markdown 格式的活跃度信息
        """
        lines = ["---\n", "\n## 📈 仓库活跃度\n\n"]

        # 总览指标
        lines.append("### 总览\n\n")
        lines.append(f"- **总 Commit 数**: {activity.total_commits}\n")
        lines.append(f"- **活跃仓库数**: {activity.active_repos_count}\n")

        # 活跃仓库详情（最多 10 个）
        if activity.top_repos:
            lines.append("\n### 活跃仓库 TOP 10\n\n")
            lines.append("| 仓库 | Commits | Top 贡献者 |\n")
            lines.append("|------|---------|------------|\n")

            for repo in activity.top_repos[:10]:
                repo_name = repo.repo.replace("_", "\\_")
                repo_link = f"[{repo_name}](https://github.com/{repo.repo})"
                commits = repo.commits

                # Top 贡献者（最多 3 个）
                top_contribs = repo.top_contributors[:3]
                if top_contribs:
                    contrib_list = ", ".join(top_contribs)
                else:
                    contrib_list = "-"

                table_row = f"| {repo_link} | {commits} | {contrib_list} |\n"
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
            "total_signals": "总信号数",
            "pr_count": "PR 信号数",
            "commit_count": "Commit 信号数",
            "release_count": "Release 信号数",
            "unique_repos": "涉及仓库数",
            "total_prs_analyzed": "分析 PR 数",
            "total_releases": "Release 数",
            "high_impact_signals": "高影响信号数",
            "total_commits_analyzed": "分析 Commit 数",
            "total_releases_analyzed": "分析 Release 数",
            "total_breaking_changes": "Breaking Changes 数",
        }
        return labels.get(key, key)

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
        return Signal.get_type_emoji(signal_type)

    def _render_releases(self, releases: ReleasesData) -> str:
        """渲染 Release 信息

        Args:
            releases: Release 数据

        Returns:
            Markdown 格式的 Release 信息
        """
        lines = ["---", "\n## 🎯 版本发布动态\n\n"]

        # 总览
        lines.append("### 总览\n\n")
        lines.append(f"- **新发布版本**: {releases.total_count} 个\n")
        lines.append(f"- **涉及仓库**: {releases.unique_repos_count} 个\n")

        # 详细 Release 列表（显示所有版本）
        if releases.releases:
            lines.append("\n### 最新发布\n\n")

            for release in releases.releases:
                repo_name = release.repo.replace("_", "\\_")
                version = release.version
                author = release.author
                date = release.date
                summary = release.summary
                assets_count = release.assets_count
                url = release.url
                ai_summary = release.ai_summary

                # 使用公共函数判断版本类型
                type_emoji = get_release_type_emoji(version, assets_count)

                release_header = (
                    f"#### {type_emoji} "
                    f"[{repo_name}](https://github.com/{release.repo}) "
                    f"{version}\n\n"
                )
                lines.append(release_header)
                lines.append(f"**发布者**: `{author}` | **时间**: {date}\n\n")

                # 优先使用 AI 总结，否则使用原始摘要
                if ai_summary:
                    # AI 生成的结构化总结
                    change_emoji = ReleaseSummary.get_change_type_emoji(
                        ai_summary.change_type
                    )
                    lines.append(
                        f"**变更类型**: {change_emoji} {ai_summary.change_type}\n\n"
                    )
                    lines.append("**变更摘要**:\n\n")

                    for change in ai_summary.key_changes:
                        lines.append(f"- {change}\n")
                    lines.append("\n")

                    if ai_summary.summary_cn:
                        lines.append(f"{ai_summary.summary_cn}\n\n")
                elif summary:
                    # 回退到原始摘要（截取前 200 字符）
                    summary_text = summary[:200].replace("\n", " ")
                    if len(summary) > 200:
                        summary_text += "..."
                    lines.append(f"**摘要**: {summary_text}\n\n")

                # Assets
                if assets_count > 0:
                    lines.append(f"**资产**: {assets_count} 个文件\n\n")

                lines.append(f"**链接**: [查看详情]({url})\n\n")

        return "".join(lines)

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

    def render_weekly_report(self, report: WeeklyReport) -> str:
        """渲染周报

        Args:
            report: 周报对象

        Returns:
            Markdown 格式的周报
        """
        header = f"""# TrendPulse 周报 ({report.week_id}: {report.start_date} ~
{report.end_date})

> {report.summary_brief}

"""

        stats_section = self._render_weekly_stats(report)
        core_trends_section = self._render_core_trends(report)

        focus_signals = sorted(
            report.engineering_signals + report.research_signals,
            key=lambda item: item.impact_score,
            reverse=True,
        )
        focus_signals_section = ""
        if focus_signals:
            focus_signals_section = "\n\n" + self.render_signals(
                focus_signals[:10], "重点"
            )

        # 活跃度
        activity_section = ""
        if report.weekly_activity:
            activity_section = "\n\n" + self._render_weekly_activity(
                report.weekly_activity
            )

        return (
            header
            + stats_section
            + "\n\n"
            + core_trends_section
            + focus_signals_section
            + activity_section
        )

    def _render_weekly_stats(self, report: WeeklyReport) -> str:
        """渲染周报统计

        Args:
            report: 周报对象

        Returns:
            Markdown 格式的统计概览
        """
        lines = [
            "## 📊 本周总览\n\n",
            "| 指标 | 数值 |\n",
            "|------|------|\n",
            f"| 包含日报数 | {report.daily_reports_count} 天 |\n",
            f"| 分析 PR 数 | {report.total_prs_analyzed} |\n",
            f"| 高影响信号 | {report.high_impact_signals} |\n",
            f"| 总 Commit 数 | {report.total_commits} |\n",
            f"| 总 Release 数 | {report.total_releases} |\n",
        ]
        return "".join(lines)

    def _render_core_trends(self, report: WeeklyReport) -> str:
        """渲染核心趋势（AI 语义分组）

        Args:
            report: 周报对象

        Returns:
            Markdown 格式的核心趋势
        """
        lines = ["## 🔥 核心趋势\n\n"]

        # 优先使用 AI 生成的 core_trends
        if report.core_trends:
            for i, trend in enumerate(report.core_trends, 1):
                impact_stars = "⭐" * trend.impact_level
                theme_emoji = self._get_theme_emoji(trend.theme)

                lines.append(f"### {i}. {trend.title}\n\n")
                lines.append(f"**主题**: {theme_emoji} `{trend.theme}` | ")
                lines.append(f"**影响**: {impact_stars}\n\n")
                lines.append(f"{trend.description}\n\n")
                lines.append(f"**相关信号数**: {len(trend.signal_ids)}\n\n")
        else:
            # 降级：取前 5 个高影响信号
            all_signals = sorted(
                report.engineering_signals + report.research_signals,
                key=lambda s: s.impact_score,
                reverse=True,
            )[:5]

            if not all_signals:
                return lines[0] + "本周暂无核心趋势。\n"

            for i, signal in enumerate(all_signals, 1):
                type_emoji = self.get_type_emoji(signal.type)
                impact_stars = "⭐" * signal.impact_score

                lines.append(f"### {i}. {signal.title}\n\n")
                lines.append(
                    f"**类型**: {type_emoji} `{signal.type}` | "
                    f"**影响**: {impact_stars}\n\n"
                )
                lines.append(f"{signal.why_it_matters}\n\n")

        return "".join(lines)

    def _get_theme_emoji(self, theme: str) -> str:
        """获取主题表情

        Args:
            theme: 主题名称

        Returns:
            主题表情
        """
        theme_emojis = {
            "architecture": "🏗️",
            "tooling": "🛠️",
            "performance": "⚡",
            "safety": "🛡️",
            "research": "🔬",
            "workflow": "⚙️",
            "ecosystem": "🌐",
        }
        return theme_emojis.get(theme, "📌")

    def _render_weekly_activity(self, activity: WeeklyActivity) -> str:
        """渲染周活跃度

        Args:
            activity: 周活跃度对象

        Returns:
            Markdown 格式的活跃度排名
        """
        lines = ["---\n", "\n## 🏆 活跃度排名\n\n"]

        # 总览
        lines.append("### 总览\n\n")
        lines.append(f"- **总 Commit 数**: {activity.total_commits}\n")
        lines.append(f"- **活跃仓库数**: {activity.active_repos_count}\n")

        # TOP 10
        if activity.top_repos:
            lines.append("\n### TOP 10\n\n")
            lines.append("| 排名 | 仓库 | Commits |\n")
            lines.append("|------|------|--------|\n")

            for i, repo in enumerate(activity.top_repos[:10], 1):
                repo_name = repo.repo.replace("_", "\\_")
                repo_link = f"[{repo_name}](https://github.com/{repo.repo})"
                table_row = f"| {i} | {repo_link} | {repo.commits} |\n"
                lines.append(table_row)

        return "".join(lines)

    def save_weekly_report(self, report: WeeklyReport, output_path: str) -> None:
        """保存周报到文件

        Args:
            report: 周报对象
            output_path: 输出文件路径
        """
        markdown = self.render_weekly_report(report)
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown, encoding="utf-8")
