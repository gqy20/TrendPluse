"""飞书卡片格式化器

将 DailyReport 转换为飞书卡片格式。
"""

import re

# Issue 数据需要延迟导入以避免循环导入
from trendpluse.models.issue_agent import IssueAgentReport
from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleasesData,
    ReleaseSummary,
    ReportStats,
    Signal,
)
from trendpluse.utils.formatters import (
    filter_high_impact,
    format_source_url,
    get_impact_emoji,
    get_release_type_emoji,
)

# 默认报告 URL 模板
DEFAULT_REPORT_URL_TEMPLATE = "https://home.gqy20.top/TrendPluse/reports/report-{date}/"


class FeishuFormatter:
    """飞书卡片格式化器

    将 DailyReport 对象转换为飞书交互卡片格式。
    """

    def __init__(self, report_url_template: str | None = None):
        """初始化格式化器

        Args:
            report_url_template: 报告 URL 模板，使用 {date} 作为占位符
        """
        self.report_url_template = report_url_template or DEFAULT_REPORT_URL_TEMPLATE

    def format_card(self, report: DailyReport) -> dict:
        """将日报格式化为飞书卡片

        Args:
            report: 每日报告对象

        Returns:
            飞书卡片字典
        """
        elements: list[dict] = []

        # 0. 添加醒目的主标题和日期（使用粗体而非标题，减小字体）
        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**📊 TrendPulse 每日报告**\n\n📅 {report.date}",
                },
            }
        )

        # 1. 摘要
        elements.append(self._create_summary_element(report.summary_brief))

        # 2. 高影响信号（如果有）
        elements.extend(self._create_signals_section(report))

        # 3. Release 信号（如果有，与 MarkdownReporter 一致）
        if report.release_signals:
            elements.append({"tag": "hr"})
            elements.extend(
                self._create_release_signals_section(report.release_signals)
            )

        # 4. Breaking Changes（如果有，使用折叠面板）
        if report.breaking_changes:
            elements.append({"tag": "hr"})
            content = self._generate_breaking_changes_content(report.breaking_changes)
            elements.append(
                self._create_collapsible_panel(
                    title=f"⚠️ Breaking Changes ({len(report.breaking_changes)}个)",
                    content=content,
                    expanded=False,  # 与其他面板保持一致，默认折叠
                    icon="down-small-ccm_outlined",
                )
            )

        # 5. 版本发布（如果有）- 使用折叠面板
        if report.releases and report.releases.releases:
            elements.append({"tag": "hr"})
            content = self._generate_releases_content(report.releases)
            elements.append(
                self._create_collapsible_panel(
                    title=f"🎯 版本发布 ({report.releases.total_count}个版本)",
                    content=content,
                    expanded=False,
                    icon="down-small-ccm_outlined",
                )
            )

        # 6. 活跃度信息（如果有）- 使用折叠面板
        if report.activity:
            elements.append({"tag": "hr"})
            content = self._generate_activity_content(report.activity)
            elements.append(
                self._create_collapsible_panel(
                    title="📈 仓库活跃度详情",
                    content=content,
                    expanded=False,
                    icon="down-small-ccm_outlined",
                )
            )

        # 7. Issue 洞察（Agent）- 使用折叠面板
        if report.issue_insights:
            elements.append({"tag": "hr"})
            content = self._generate_issue_insights_content(report.issue_insights)
            elements.append(
                self._create_collapsible_panel(
                    title="🧠 Issue 洞察（Agent）",
                    content=content,
                    expanded=False,
                    icon="down-small-ccm_outlined",
                )
            )

        # 8. 统计信息 - 使用折叠面板
        elements.append({"tag": "hr"})
        stats_content = self._generate_stats_content(report.stats)
        elements.append(
            self._create_collapsible_panel(
                title="📊 统计信息",
                content=stats_content,
                expanded=False,
                icon="down-small-ccm_outlined",
            )
        )

        # 9. 查看详情按钮（JSON V2 格式：按钮直接在 elements 中）
        report_url = self.report_url_template.format(date=report.date)
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "button",
                "text": {"tag": "plain_text", "content": "📖 查看完整报告"},
                "url": report_url,
                "type": "primary",
            }
        )

        return {
            "msg_type": "interactive",
            "card": {
                "schema": "2.0",
                "config": {
                    "update_multi": True,
                },
                "body": {
                    "elements": elements,
                },
            },
        }

    def _create_summary_element(self, summary: str) -> dict:
        """创建摘要元素

        移除摘要中重复的日期信息（因为主标题已包含日期）。

        Args:
            summary: 摘要文本

        Returns:
            摘要元素字典
        """
        # 移除摘要中的日期信息，避免与主标题重复
        # 摘要格式: "今日 (YYYY-MM-DD) 发现..." -> "今日 发现..."
        cleaned_summary = re.sub(r"今日 \(\d{4}-\d{2}-\d{2}\) ", "今日 ", summary)
        # 另一种可能格式: "今日 (YYYY-MM-DD)未发现..." -> "今日未发现..."
        cleaned_summary = re.sub(r"今日 \(\d{4}-\d{2}-\d{2}\)", "今日", cleaned_summary)

        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": cleaned_summary,
            },
        }

    def _create_signals_section(self, report: DailyReport) -> list[dict]:
        """创建高影响信号部分（与 MarkdownReporter 一致：按分类分组）

        工程信号和研究信号使用折叠面板，Commit 信号使用普通展示。

        Args:
            report: 日报对象

        Returns:
            信号元素列表
        """
        elements: list[dict] = []

        # 工程信号（使用折叠面板，默认折叠与其他面板一致）
        engineering_signals = filter_high_impact(
            report.engineering_signals, threshold=4
        )
        if engineering_signals:
            elements.append({"tag": "hr"})
            content = self._generate_signals_content(engineering_signals)
            elements.append(
                self._create_collapsible_panel(
                    title=f"🔧 工程信号 ({len(engineering_signals)}个)",
                    content=content,
                    expanded=False,  # 默认折叠，与其他面板保持一致
                )
            )
        else:
            # 即使没有信号也显示空状态
            elements.append({"tag": "hr"})
            elements.append(
                self._create_collapsible_panel(
                    title="🔧 工程信号",
                    content="暂无信号。\n",
                    expanded=False,
                )
            )

        # 研究信号（使用折叠面板）
        research_signals = filter_high_impact(report.research_signals, threshold=4)
        if research_signals:
            elements.append({"tag": "hr"})
            content = self._generate_signals_content(research_signals)
            elements.append(
                self._create_collapsible_panel(
                    title=f"🔬 研究信号 ({len(research_signals)}个)",
                    content=content,
                    expanded=False,
                )
            )
        else:
            # 即使没有信号也显示空状态
            elements.append({"tag": "hr"})
            elements.append(
                self._create_collapsible_panel(
                    title="🔬 研究信号",
                    content="暂无信号。\n",
                    expanded=False,
                )
            )

        # Commit 信号（仅在有内容时显示，与 MarkdownReporter 一致）
        if report.commit_signals:
            commit_signals = filter_high_impact(report.commit_signals, threshold=4)
            elements.append({"tag": "hr"})
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "**💾 Commit 信号**\n\n",
                    },
                }
            )
            if commit_signals:
                elements.extend(self._create_signal_items(commit_signals))
            else:
                elements.append(
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": "暂无 commit 信号。\n",
                        },
                    }
                )

        return elements

    def _generate_signals_content(self, signals: list[Signal]) -> str:
        """生成信号内容（不包含外层标题，用于折叠面板）

        Args:
            signals: 信号列表

        Returns:
            Markdown 格式的内容字符串
        """
        if not signals:
            return "暂无信号。\n"

        content_parts = []
        for i, signal in enumerate(signals):
            type_emoji = self._get_type_emoji(signal.type)
            impact_stars = "⭐" * signal.impact_score
            repos = ", ".join(f"`{r}`" for r in signal.related_repos)

            # 来源链接（格式化显示）
            sources_md = "\n".join(
                f"- [{format_source_url(url)}]({url})" for url in signal.sources
            )

            # 构建单个信号内容，使用 ##### 五级标题
            signal_content = f"##### {type_emoji} {signal.title}\n\n"
            signal_content += (
                f"\n**类型**: `{signal.type}` | **影响**: {impact_stars} "
                f"({signal.impact_score}/5) | **分类**: `{signal.category}`\n\n"
            )
            signal_content += f"**为什么重要**: {signal.why_it_matters}\n\n"
            signal_content += f"**相关仓库**: {repos}\n\n"
            signal_content += f"**来源**:\n{sources_md}\n\n"

            content_parts.append(signal_content)

            # 信号之间添加分割线（最后一个信号除外）
            if i < len(signals) - 1:
                content_parts.append("---\n\n")

        return "".join(content_parts)

    def _create_signal_items(self, signals: list[Signal]) -> list[dict]:
        """创建单个信号列表的元素

        Args:
            signals: 信号列表

        Returns:
            信号元素列表（每个信号一个 div，之间用 hr 分隔）
        """
        elements: list[dict] = []

        for i, signal in enumerate(signals):
            type_emoji = self._get_type_emoji(signal.type)
            impact_stars = "⭐" * signal.impact_score
            repos = ", ".join(f"`{r}`" for r in signal.related_repos)

            # 来源链接（格式化显示）
            sources_md = "\n".join(
                f"- [{format_source_url(url)}]({url})" for url in signal.sources
            )

            # 构建单个信号内容，使用 ##### 五级标题
            content = f"##### {type_emoji} {signal.title}\n\n"
            content += (
                f"\n**类型**: `{signal.type}` | **影响**: {impact_stars} "
                f"({signal.impact_score}/5) | **分类**: `{signal.category}`\n\n"
            )
            content += f"**为什么重要**: {signal.why_it_matters}\n\n"
            content += f"**相关仓库**: {repos}\n\n"
            content += f"**来源**:\n{sources_md}\n\n"

            # 添加信号 div
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content,
                    },
                }
            )

            # 信号之间添加分割线（最后一个信号除外）
            if i < len(signals) - 1:
                elements.append({"tag": "hr"})

        return elements

    def _generate_releases_content(self, releases: ReleasesData) -> str:
        """生成版本发布内容（不包含外层标题，用于折叠面板）

        Args:
            releases: ReleasesData 对象

        Returns:
            Markdown 格式的内容字符串
        """
        lines: list[str] = []

        # 总览（不包含外层标题，因为已在折叠面板标题中）
        lines.append("**总览**\n\n")
        lines.append(f"- **新发布版本**: {releases.total_count} 个\n")
        lines.append(f"- **涉及仓库**: {releases.unique_repos_count} 个\n")

        # 详细 Release 列表（最多 10 个，飞书卡片不宜过长）
        if releases.releases:
            lines.append("\n**最新发布**\n\n")

            for release in releases.releases[:10]:
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

                # Release 标题（仓库链接）
                repo_link = f"[{repo_name}](https://github.com/{release.repo})"
                lines.append(f"##### {type_emoji} {repo_link} `{version}`\n\n")
                lines.append(f"**发布者**: `{author}` | **时间**: {date}\n\n")

                # 优先使用 AI 总结
                if ai_summary:
                    change_emoji = ReleaseSummary.get_change_type_emoji(
                        ai_summary.change_type
                    )
                    lines.append(
                        f"**变更类型**: {change_emoji} {ai_summary.change_type}\n\n"
                    )
                    lines.append("**变更摘要**:\n")
                    for change in ai_summary.key_changes:
                        lines.append(f"- {change}\n")
                    lines.append("\n")
                    if ai_summary.summary_cn:
                        lines.append(f"{ai_summary.summary_cn}\n\n")
                elif summary:
                    # 回退到原始摘要（截取前 150 字符，飞书不宜过长）
                    summary_text = summary[:150].replace("\n", " ")
                    if len(summary) > 150:
                        summary_text += "..."
                    lines.append(f"**摘要**: {summary_text}\n\n")

                # Assets
                if assets_count > 0:
                    lines.append(f"**资产**: {assets_count} 个文件\n\n")

                lines.append(f"**链接**: [查看详情]({url})\n\n")

        return "".join(lines)

    def _create_release_signals_section(self, signals: list[Signal]) -> list[dict]:
        """创建 Release 信号部分（与 MarkdownReporter 一致）

        Args:
            signals: Release 信号列表

        Returns:
            Release 信号元素列表
        """
        elements: list[dict] = []

        if not signals:
            return elements

        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**🎯 Release 信号**\n\n",
                },
            }
        )

        # 筛选高影响信号（评分 >= 4）
        high_impact = [s for s in signals if s.impact_score >= 4]
        if not high_impact:
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "暂无 release 信号。\n",
                    },
                }
            )
            return elements

        # 按评分降序，最多 5 个
        sorted_signals = sorted(high_impact, key=lambda x: (-x.impact_score, x.title))[
            :5
        ]

        elements.extend(self._create_signal_items(sorted_signals))

        return elements

    def _generate_breaking_changes_content(self, breaking_changes: list[dict]) -> str:
        """生成 Breaking Changes 内容（不包含外层标题，用于折叠面板）

        Args:
            breaking_changes: breaking changes 列表

        Returns:
            Markdown 格式的内容字符串
        """
        lines = []

        for bc in breaking_changes:
            repo_name = bc["repo"].replace("_", "\\_")
            tag_name = bc["tag_name"]
            repo_link = f"[{repo_name}](https://github.com/{bc['repo']})"

            lines.append(f"**{repo_link}** `{tag_name}`\n\n")

            for change in bc.get("changes", []):
                impact = change.get("impact", "unknown")
                category = change.get("category", "")
                description = change.get("description", "")
                impact_emoji = get_impact_emoji(impact)

                lines.append(f"- {impact_emoji} **[{category}]** {description}\n")

            lines.append("\n")

        return "".join(lines)

    def _generate_activity_content(self, activity: ActivityData) -> str:
        """生成活跃度内容（不包含外层标题，用于折叠面板）

        Args:
            activity: ActivityData 对象

        Returns:
            Markdown 格式的内容字符串
        """
        lines: list[str] = []

        # 总览指标（不包含外层标题，因为已在折叠面板标题中）
        lines.append("**总览**\n\n")
        lines.append(f"- **总 Commit 数**: {activity.total_commits}\n")
        lines.append(f"- **活跃仓库数**: {activity.active_repos_count}\n")

        # 活跃仓库 TOP 3（飞书卡片不宜过长，显示 TOP 3）
        if activity.top_repos:
            lines.append("\n**活跃仓库 TOP 3**\n\n")
            for i, repo in enumerate(activity.top_repos[:3], 1):
                lines.append(f"{i}. **{repo.repo}** ({repo.commits} commits)\n")

        return "".join(lines)

    def _generate_stats_content(self, stats: ReportStats) -> str:
        """生成统计信息内容（不包含外层标题，用于折叠面板）

        Args:
            stats: 统计数据字典

        Returns:
            Markdown 格式的内容字符串
        """
        # 不包含外层标题，因为已在折叠面板标题中
        content = ""
        content += f"• 分析 PR 数: {stats.get('total_prs_analyzed', 0)}\n"
        content += f"• 高影响信号: {stats.get('high_impact_signals', 0)}\n"
        content += f"• 新发布版本: {stats.get('total_releases', 0)}\n"
        content += f"• 分析 Commit 数: {stats.get('total_commits_analyzed', 0)}\n"
        return content

    def _generate_issue_insights_content(self, report: IssueAgentReport) -> str:
        lines: list[str] = [
            f"• 预期文件: {report.expected_files}\n",
            f"• 生成文件: {report.generated_files}\n",
            f"• 解析文件: {report.parsed_files}\n",
            f"• 失败文件: {report.failed_files}\n\n",
            f"• 质量等级: {report.quality_status}\n",
            f"• 质量分: {report.quality_score:.3f}\n\n",
        ]

        if not report.top_pain_points:
            lines.append("暂无可用的 Issue 洞察。\n")
            if report.failed_samples:
                samples = ", ".join(f"`{s}`" for s in report.failed_samples[:3])
                lines.append(f"失败样例: {samples}\n")
            return "".join(lines)

        lines.append("**用户痛点 TOP 3**\n\n")
        for idx, pain_point in enumerate(report.top_pain_points[:3], 1):
            repos_str = ", ".join(f"`{r}`" for r in pain_point.affected_repos[:2])
            if len(pain_point.affected_repos) > 2:
                repos_str += f" (+{len(pain_point.affected_repos) - 2})"
            lines.append(f"{idx}. **{pain_point.topic}** ({pain_point.count}次)\n")
            lines.append(f"   受影响: {repos_str}\n")

        sample_urls = report.top_pain_points[0].sample_urls
        if sample_urls:
            lines.append("\n**示例**\n\n")
            for url in sample_urls[:3]:
                lines.append(f"- {url}\n")

        return "".join(lines)

    def _get_type_emoji(self, signal_type: str) -> str:
        """获取信号类型的表情

        Args:
            signal_type: 信号类型

        Returns:
            类型表情
        """
        return Signal.get_type_emoji(signal_type)

    def _create_collapsible_panel(
        self,
        title: str,
        content: str,
        expanded: bool = False,
        icon: str | None = None,
    ) -> dict:
        """创建折叠面板组件

        Args:
            title: 面板标题
            content: 面板内容（Markdown 格式）
            expanded: 是否默认展开
            icon: 可选图标 token

        Returns:
            折叠面板字典
        """
        panel: dict = {
            "tag": "collapsible_panel",
            "expanded": expanded,
            "header": {
                "title": {
                    "tag": "markdown",
                    "content": title,
                },
                "vertical_align": "center",
            },
            "border": {
                "color": "grey",
                "corner_radius": "5px",
            },
            "vertical_spacing": "8px",
            "padding": "8px 8px 8px 8px",
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content,
                    },
                }
            ],
        }

        # 添加图标（可选）
        if icon:
            header: dict = panel["header"]
            header["icon"] = {
                "tag": "standard_icon",
                "token": icon,
                "size": "16px 16px",
            }
            header["icon_position"] = "right"
            header["icon_expanded_angle"] = -180

        return panel
