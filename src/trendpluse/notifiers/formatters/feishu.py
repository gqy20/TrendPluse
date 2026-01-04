"""飞书卡片格式化器

将 DailyReport 转换为飞书卡片格式。
"""

from trendpluse.models.signal import ActivityData, DailyReport, Signal


class FeishuFormatter:
    """飞书卡片格式化器

    将 DailyReport 对象转换为飞书交互卡片格式。
    """

    def __init__(self, report_url_template: str | None = None):
        """初始化格式化器

        Args:
            report_url_template: 报告 URL 模板，使用 {date} 作为占位符
        """
        self.report_url_template = report_url_template or (
            "https://home.gqy20.top/TrendPluse/reports/report-{date}.html"
        )

    def format_card(self, report: DailyReport) -> dict:
        """将日报格式化为飞书卡片

        Args:
            report: 每日报告对象

        Returns:
            飞书卡片字典
        """
        elements: list[dict] = []

        # 1. 摘要
        elements.append(self._create_summary_element(report.summary_brief))

        # 2. 高影响信号（如果有）
        high_impact_signals = self._get_high_impact_signals(report)
        if high_impact_signals:
            elements.append({"tag": "hr"})
            elements.append(self._create_signals_section(high_impact_signals))

        # 3. 版本发布（如果有）
        if report.releases and report.releases.releases:
            elements.append({"tag": "hr"})
            elements.append(self._create_releases_section(report.releases))

        # 4. 活跃仓库 TOP 3（如果有）
        if report.activity and report.activity.top_repos:
            elements.append({"tag": "hr"})
            elements.append(self._create_activity_section(report.activity))

        # 5. 统计信息
        elements.append({"tag": "hr"})
        elements.append(self._create_stats_section(report.stats))

        # 6. 查看详情按钮
        report_url = self.report_url_template.format(date=report.date)
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "📖 查看完整报告"},
                        "url": report_url,
                        "type": "primary",
                    }
                ],
            }
        )

        return {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": f"📊 TrendPulse 每日报告 - {report.date}",
                    },
                },
                "elements": elements,
            },
        }

    def _create_summary_element(self, summary: str) -> dict:
        """创建摘要元素

        Args:
            summary: 摘要文本

        Returns:
            摘要元素字典
        """
        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": summary,
            },
        }

    def _create_signals_section(self, signals: list[Signal]) -> dict:
        """创建高影响信号部分

        Args:
            signals: 信号列表

        Returns:
            信号部分元素
        """
        content = "### 🔥 高影响信号\n\n"
        for signal in signals:
            type_emoji = self._get_type_emoji(signal.type)
            impact_stars = "⭐" * signal.impact_score
            repos = ", ".join(f"`{r}`" for r in signal.related_repos)

            content += f"{type_emoji} **{signal.title}**\n"
            content += f"{impact_stars} | {repos}\n"
            content += f"{signal.why_it_matters}\n\n"

        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content,
            },
        }

    def _create_releases_section(self, releases) -> dict:
        """创建版本发布部分

        Args:
            releases: ReleasesData 对象

        Returns:
            版本发布部分元素
        """
        content = f"### 🎯 版本发布 ({releases.total_count}个)\n\n"
        for release in releases.releases[:5]:
            content += f"• **{release.repo}** {release.version}"
            if release.date:
                content += f" ({release.date})"
            content += "\n"

        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content,
            },
        }

    def _create_activity_section(self, activity: ActivityData) -> dict:
        """创建活跃度部分

        Args:
            activity: ActivityData 对象

        Returns:
            活跃度部分元素
        """
        content = "### 🔥 活跃仓库 TOP 3\n\n"
        for i, repo in enumerate(activity.top_repos[:3], 1):
            content += f"{i}. **{repo.repo}** ({repo.commits} commits)\n"

        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content,
            },
        }

    def _create_stats_section(self, stats: dict) -> dict:
        """创建统计信息部分

        Args:
            stats: 统计数据字典

        Returns:
            统计信息部分元素
        """
        content = "### 📊 统计信息\n\n"
        content += f"• 分析 PR 数: {stats.get('total_prs_analyzed', 0)}\n"
        content += f"• 高影响信号: {stats.get('high_impact_signals', 0)}\n"
        content += f"• 新发布版本: {stats.get('total_releases', 0)}\n"
        content += f"• 分析 Commit 数: {stats.get('total_commits_analyzed', 0)}"

        return {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content,
            },
        }

    def _get_high_impact_signals(self, report: DailyReport) -> list[Signal]:
        """获取高影响信号

        Args:
            report: 日报对象

        Returns:
            高影响信号列表（按评分降序）
        """
        all_signals = []
        for signals in [
            report.engineering_signals,
            report.research_signals,
            report.commit_signals,
            report.release_signals,
        ]:
            all_signals.extend(signals)

        # 筛选高影响信号（评分 >= 4），按评分降序，最多 5 个
        return sorted(
            [s for s in all_signals if s.impact_score >= 4],
            key=lambda x: (-x.impact_score, x.title),
        )[:5]

    def _get_type_emoji(self, signal_type: str) -> str:
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
