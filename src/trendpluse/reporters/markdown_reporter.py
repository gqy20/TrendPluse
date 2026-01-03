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
            f"- [{self._format_source_url(url)}]({url})" for url in signal.sources
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

        # 统计信息
        stats_section = self._render_stats(report.stats)

        return (
            header
            + engineering_section
            + "\n\n"
            + research_section
            + commit_section
            + release_signals_section
            + release_section
            + breaking_changes_section
            + activity_section
            + stats_section
        )

    def _render_monitored_repos(self, repos: list[str]) -> str:
        """渲染监控仓库列表

        Args:
            repos: 仓库列表

        Returns:
            Markdown 格式的监控仓库列表
        """
        lines = ["## 📋 监控仓库\n\n"]

        # 按组织分组
        repos_by_org: dict[str, list[str]] = {}
        for repo in repos:
            org = repo.split("/")[0]
            if org not in repos_by_org:
                repos_by_org[org] = []
            repos_by_org[org].append(repo)

        # 排序组织名称
        sorted_orgs = sorted(repos_by_org.keys())

        for org in sorted_orgs:
            org_repos = sorted(repos_by_org[org])
            lines.append(f"### {org}\n\n")
            for repo in org_repos:
                repo_name = repo.replace("_", "\\_")
                repo_link = f"[{repo_name}](https://github.com/{repo})"
                lines.append(f"- {repo_link}\n")
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
                impact_emoji = {
                    "high": "🔴",
                    "medium": "🟡",
                    "low": "🟢",
                }.get(impact, "⚪")

                category = change.get("category", "")
                description = change.get("description", "")

                lines.append(f"- {impact_emoji} **[{category}]** {description}\n")

            lines.append("\n")

        return "".join(lines)

    def _render_stats(self, stats: dict) -> str:
        """渲染统计信息

        Args:
            stats: 统计数据

        Returns:
            Markdown 格式的统计信息
        """
        lines = ["\n---\n", "\n## 📊 统计信息\n\n"]

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
        lines = ["---\n", "\n## 📈 仓库活跃度\n\n"]

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
                repo_link = f"[{repo_name}](https://github.com/{repo['repo']})"
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
                    f"| {repo_link} | {commits} | {new_contribs} | {contrib_list} |\n"
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
            "total_releases_analyzed": "分析 Release 数",
            "total_breaking_changes": "Breaking Changes 数",
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

    def _format_source_url(self, url: str) -> str:
        """格式化 source URL 显示文本

        Args:
            url: GitHub URL

        Returns:
            格式化的显示文本（包含 commit SHA 或 PR 号码）
        """
        if "github.com/" in url:
            # 移除协议前缀
            clean_url = url.replace("https://github.com/", "").replace(
                "http://github.com/", ""
            )

            # 检测 commit 链接
            if "/commit/" in clean_url:
                parts = clean_url.split("/commit/")
                repo = parts[0]
                sha = parts[1].split("/")[0]  # 提取 SHA，可能后面有 ? 或 #
                short_sha = sha[:7]  # 显示前 7 位
                return f"{repo}@{short_sha}"

            # 检测 PR 链接
            elif "/pull/" in clean_url:
                parts = clean_url.split("/pull/")
                repo = parts[0]
                pr_num = parts[1].split("/")[0]
                return f"{repo}#{pr_num}"

            # 默认：提取仓库名
            else:
                parts = clean_url.split("/")
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
            "release": "🎯",
        }
        return emojis.get(signal_type, "📌")

    def _render_releases(self, releases: dict) -> str:
        """渲染 Release 信息

        Args:
            releases: Release 数据字典

        Returns:
            Markdown 格式的 Release 信息
        """
        lines = ["---", "\n## 🎯 版本发布动态\n\n"]

        # 总览
        lines.append("### 总览\n\n")
        lines.append(f"- **新发布版本**: {releases.get('total_releases', 0)} 个\n")
        lines.append(f"- **涉及仓库**: {releases.get('repos_with_releases', 0)} 个\n")

        # 详细 Release 列表（最多 10 个）
        detailed_releases = releases.get("detailed_releases", [])[:10]
        if detailed_releases:
            lines.append("\n### 最新发布\n\n")

            for release in detailed_releases:
                repo_name = release["repo"].replace("_", "\\_")
                tag_name = release["tag_name"]
                name = release.get("name", "")
                prerelease = release.get("prerelease", False)
                author = release.get("author", "Unknown")
                created_at = release.get("created_at", "")[:10]

                # 版本类型标记
                version_info = release.get("version_info", {})
                if version_info:
                    is_major = (
                        version_info.get("minor", 0) == 0
                        and version_info.get("patch", 0) == 0
                    )
                    type_emoji = "🚀" if is_major else "⚡"
                else:
                    type_emoji = "📦"

                prerelease_tag = " `[预发布]` " if prerelease else ""

                release_header = (
                    f"#### {type_emoji} "
                    f"[{repo_name}](https://github.com/{release['repo']}) "
                    f"{tag_name}{prerelease_tag}\n\n"
                )
                lines.append(release_header)
                if name and name != tag_name:
                    lines.append(f"**{name}**\n\n")
                lines.append(f"**发布者**: `{author}` | **时间**: {created_at}\n\n")

                # Release Notes 摘要
                body = release.get("body", "")
                if body:
                    # 取前 200 字符
                    summary = body[:200].replace("\n", " ")
                    if len(body) > 200:
                        summary += "..."
                    lines.append(f"**摘要**: {summary}\n\n")

                # Assets
                assets = release.get("assets", [])
                if assets:
                    lines.append(f"**资产**: {len(assets)} 个文件\n\n")

                lines.append(f"**链接**: [查看详情]({release['html_url']})\n\n")

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
