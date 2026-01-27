"""Markdown 报告生成器

将每日报告渲染为 Markdown 格式。
"""

from pathlib import Path

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleasesData,
    ReleaseSummary,
    Signal,
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
        lines.append(f"- **新贡献者数**: {activity.new_contributors}\n")

        # 活跃仓库详情（最多 10 个）
        if activity.top_repos:
            lines.append("\n### 活跃仓库 TOP 10\n\n")
            lines.append("| 仓库 | Commits | 新贡献者 | Top 贡献者 |\n")
            lines.append("|------|--------|---------|------------|\n")

            for repo in activity.top_repos[:10]:
                repo_name = repo.repo.replace("_", "\\_")
                repo_link = f"[{repo_name}](https://github.com/{repo.repo})"
                commits = repo.commits
                new_contribs = repo.new_contributors

                # Top 贡献者（最多 3 个）
                top_contribs = repo.top_contributors[:3]
                if top_contribs:
                    contrib_list = ", ".join(top_contribs)
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

    def render_signal_card(self, signal: Signal) -> str:
        """渲染单个信号的 HTML 卡片

        生成符合 Bento Grid 设计系统的 HTML 卡片格式。

        Args:
            signal: 信号对象

        Returns:
            HTML 格式的信号卡片
        """
        # 确定影响级别样式
        if signal.impact_score >= 4:
            impact_class = "signal-high-impact"
        elif signal.impact_score >= 3:
            impact_class = "signal-medium-impact"
        else:
            impact_class = "signal-low-impact"

        # 获取类型图标
        type_emoji = self.get_type_emoji(signal.type)
        impact_stars = "⭐" * signal.impact_score

        # 生成来源链接 HTML
        sources_html = "\n".join(
            f'          <li><a href="{url}" target="_blank" '
            f'rel="noopener">{format_source_url(url)}</a></li>'
            for url in signal.sources
        )

        # 生成相关仓库标签
        repos_html = ", ".join(
            f'<code class="repo-tag">{repo}</code>' for repo in signal.related_repos
        )

        # 构建完整的 HTML 卡片
        return f"""<div class="signal-card {impact_class}">
  <details class="signal-details">
    <summary>
      <div class="signal-header">
        <div class="signal-icon">{type_emoji}</div>
        <div class="signal-title-area">
          <h4 class="signal-title">{signal.title}</h4>
          <div class="signal-meta">
            <span class="signal-type-badge {signal.type}">{signal.type}</span>
            <div class="signal-impact">
              <span class="signal-stars">{impact_stars}</span>
              <span class="signal-score">({signal.impact_score}/5)</span>
            </div>
          </div>
        </div>
      </div>
    </summary>
    <div class="signal-body">
      <div class="signal-section">
        <span class="signal-label">为什么重要</span>
        <p>{signal.why_it_matters}</p>
      </div>
      <div class="signal-section">
        <span class="signal-label">相关仓库</span>
        <div class="signal-repos">{repos_html}</div>
      </div>
    </div>
    <div class="signal-footer">
      <span class="signal-footer-label">来源</span>
      <ul class="signal-sources">
{sources_html}
      </ul>
    </div>
  </details>
</div>"""

    def render_bento_grid(self, signals: list[Signal], category: str) -> str:
        """渲染 Bento Grid 格式的信号列表

        生成包含信号卡片的 Bento Grid 布局。

        Args:
            signals: 信号列表
            category: 分类名称（工程/研究）

        Returns:
            HTML 格式的 Bento Grid
        """
        emoji = "🔧" if category == "工程" else "🔬"

        if not signals:
            return f"""<h2>{emoji} {category}信号</h2>
<div class="bento-grid">
  <div class="signal-card signal-empty">
    <div class="signal-body">
      <p>暂无信号。</p>
    </div>
  </div>
</div>"""

        # 生成所有信号卡片
        cards_html = "\n".join(self.render_signal_card(signal) for signal in signals)

        return f"""<h2>{emoji} {category}信号</h2>
<div class="bento-grid">
{cards_html}
</div>"""
