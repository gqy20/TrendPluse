"""报告摘要生成器

从每日报告中提取关键信息，生成精简的摘要数据。
"""

from trendpluse.models.signal import DailyReport


class ReportSummarizer:
    """报告摘要生成器

    从 DailyReport 提取关键信息，用于生成飞书卡片消息。
    """

    def summarize(self, report: DailyReport) -> dict:
        """生成报告摘要

        Args:
            report: 每日报告对象

        Returns:
            包含以下字段的字典：
            - title: 报告标题
            - summary: 报告摘要
            - highlights: 高影响信号列表（最多 5 个）
            - stats: 统计信息
            - top_repos: 活跃仓库 TOP 3
            - report_url: 报告链接
        """
        # 提取所有信号并按评分排序
        all_signals = []
        for signals in [
            report.engineering_signals,
            report.research_signals,
            report.commit_signals,
            report.release_signals,
        ]:
            all_signals.extend(signals)

        # 筛选高影响信号（评分 >= 4），按评分降序，最多 5 个
        high_impact_signals = sorted(
            [s for s in all_signals if s.impact_score >= 4],
            key=lambda x: (-x.impact_score, x.title),
        )[:5]

        # 提取活跃仓库 TOP 3
        top_repos = []
        if report.activity and report.activity.get("repo_activity"):
            repo_activity = sorted(
                report.activity["repo_activity"],
                key=lambda x: -x.get("commit_count", 0),
            )[:3]
            for repo in repo_activity:
                top_repos.append(
                    {
                        "repo": repo["repo"],
                        "commits": repo["commit_count"],
                        "new_contributors": repo.get("new_contributors", 0),
                    }
                )

        # 生成报告 URL
        report_url = f"https://github.com/qy113/TrendPluse/blob/main/docs/reports/report-{report.date}.md"

        return {
            "title": f"📊 TrendPulse 每日报告 - {report.date}",
            "summary": report.summary_brief,
            "highlights": [
                {
                    "id": s.id,
                    "title": s.title,
                    "type": s.type,
                    "category": s.category,
                    "impact_score": s.impact_score,
                    "why_it_matters": s.why_it_matters,
                    "sources": s.sources,
                    "related_repos": s.related_repos,
                }
                for s in high_impact_signals
            ],
            "stats": {
                "total_prs_analyzed": report.stats.get("total_prs_analyzed", 0),
                "total_releases": report.stats.get("total_releases", 0),
                "high_impact_signals": report.stats.get("high_impact_signals", 0),
                "total_commits_analyzed": report.stats.get("total_commits_analyzed", 0),
            },
            "top_repos": top_repos,
            "report_url": report_url,
        }
