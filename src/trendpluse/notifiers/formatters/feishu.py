"""飞书卡片格式化器

将 DailyReport 转换为飞书卡片格式。
"""

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleaseInfo,
    Signal,
)


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
            elements.extend(self._create_signals_section(high_impact_signals))

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

        # 6. 查看详情按钮（JSON V2 格式：按钮直接在 elements 中）
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
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": f"📊 TrendPulse 每日报告 - {report.date}",
                    },
                },
                "body": {
                    "elements": elements,
                },
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

    def _create_signals_section(self, signals: list[Signal]) -> list[dict]:
        """创建高影响信号部分

        Args:
            signals: 信号列表

        Returns:
            信号元素列表（每个信号一个 div，之间用 hr 分隔）
        """
        elements: list[dict] = []

        # 添加标题
        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "### 🔥 高影响信号\n\n",
                },
            }
        )

        for i, signal in enumerate(signals):
            type_emoji = self._get_type_emoji(signal.type)
            impact_stars = "⭐" * signal.impact_score
            repos = ", ".join(f"`{r}`" for r in signal.related_repos)

            # 来源链接（格式化显示）
            sources_md = "\n".join(
                f"- [{self._format_source_url(url)}]({url})" for url in signal.sources
            )

            # 构建单个信号内容
            content = f"{type_emoji} **{signal.title}**\n\n"
            content += (
                f"**类型**: `{signal.type}` | **影响**: {impact_stars} "
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

    def _create_releases_section(self, releases) -> dict:
        """创建版本发布部分

        Args:
            releases: ReleasesData 对象

        Returns:
            版本发布部分元素
        """
        # 按仓库去重，保留日期最新的版本
        latest_by_repo: dict[str, ReleaseInfo] = {}
        for r in releases.releases:
            repo = r.repo
            # 如果该仓库还没记录，或者当前版本日期更新，则替换
            if repo not in latest_by_repo or r.date > latest_by_repo[repo].date:
                latest_by_repo[repo] = r

        unique_releases = list(latest_by_repo.values())[:5]

        content = f"### 🎯 版本发布 ({len(unique_releases)}个仓库)\n\n"
        for release in unique_releases:
            # 飞书 Markdown 链接语法：[text](url)
            content += f"• [{release.repo}]({release.url}) {release.version}"
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
        return Signal.get_type_emoji(signal_type)
