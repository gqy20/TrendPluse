"""Issue 采集器

从 GitHub API 采集 Issues，支持快照去重和时间窗口过滤。
"""

from datetime import UTC, datetime, timedelta

from github import GithubException

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.collectors.parallel import parallel_execute
from trendpluse.logger import get_logger
from trendpluse.models.issue import IssueInfo
from trendpluse.snapshots.issue_snapshot import IssueSnapshot

logger = get_logger(__name__)


class IssueCollector(BaseGitHubCollector):
    """Issue 采集器

    从指定仓库采集 Issues，支持快照去重和时间窗口过滤。
    """

    # 时间窗口配置（聚焦最近 5 天的趋势）
    CREATE_WINDOW_DAYS = 5  # 5天内创建的 Issue
    ACTIVE_WINDOW_DAYS = 3  # 3天内有新回复

    def __init__(self, token: str, snapshot_dir: str = "data/issue_snapshots"):
        """初始化 Issue 采集器

        Args:
            token: GitHub 访问令牌
            snapshot_dir: 快照存储目录
        """
        super().__init__(token)
        self.snapshot = IssueSnapshot(snapshot_dir)

    def fetch_issues(
        self,
        repos: list[str],
        snapshot_date: str | None = None,
        max_workers: int | None = None,
    ) -> tuple[list[IssueInfo], dict[str, int]]:
        """采集指定仓库的 Issues

        Args:
            repos: 仓库列表，格式 ["owner/repo", ...]
            snapshot_date: 快照日期字符串 YYYY-MM-DD（用于去重）
            max_workers: 最大线程数

        Returns:
            (Issue 列表, 统计信息字典)
        """
        # 加载已分析的 Issue IDs
        analyzed_ids = self.snapshot.load_analyzed_ids(snapshot_date or "")

        # 并行获取所有仓库的 Issues
        all_issues = parallel_execute(
            lambda repo: self._fetch_repo_issues(repo, analyzed_ids),
            repos,
            max_workers=max_workers,
        )

        # 合并结果
        issues = []
        for issue_list in all_issues:
            issues.extend(issue_list)

        stats = {
            "total_fetched": len(issues),
            "filtered_by_duplicate": len(analyzed_ids),
            "repos_processed": len(repos),
        }

        return issues, stats

    def _fetch_repo_issues(
        self,
        repo_name: str,
        analyzed_ids: set[tuple[str, int]],
    ) -> list[IssueInfo]:
        """获取单个仓库的 Issues

        Args:
            repo_name: 仓库名称 owner/repo
            analyzed_ids: 已分析的 Issue IDs 集合

        Returns:
            Issue 列表
        """
        issues = []
        try:
            repo = self.client.get_repo(repo_name)

            # 计算时间窗口（使用 since 参数减少 API 请求）
            now = datetime.now(UTC)
            since_date = now - timedelta(days=self.CREATE_WINDOW_DAYS)

            # 获取 Issues（使用 since 参数进行服务端过滤）
            # 这会大幅减少 API 请求次数，避免 403 错误
            github_issues = repo.get_issues(
                state="all",
                since=since_date,  # ← 关键优化：服务端过滤
                sort="created",
                direction="desc",
            )

            for issue in github_issues:
                # 跳过 PR（GitHub API 把 PR 也当作 Issue）
                if hasattr(issue, "pull_request") and issue.pull_request:
                    continue

                # 检查快照去重
                issue_key = (repo_name, issue.number)
                if issue_key in analyzed_ids:
                    continue

                # 检查时间窗口
                if not self._should_analyze(issue, now):
                    continue

                # 转换为 IssueInfo
                issue_info = self._convert_to_issue_info(issue, repo_name, now)
                issues.append(issue_info)

        except GithubException as e:
            logger.error(f"获取仓库 {repo_name} Issues 失败: {e}")

        return issues

    def _should_analyze(self, issue, now: datetime) -> bool:
        """判断 Issue 是否需要分析

        实现双时间窗口逻辑：
        1. 最近 CREATE_WINDOW_DAYS (30) 天内创建
        2. 或最近 ACTIVE_WINDOW_DAYS (3) 天有新回复

        注意：由于已使用 since 参数过滤，这里的条件1几乎总是满足。
        条件2主要用于捕获旧 Issue 的最近活动。

        Args:
            issue: GitHub Issue 对象
            now: 当前时间

        Returns:
            True 如果需要分析，False 否则
        """
        created_at = self.ensure_timezone_aware(issue.created_at)
        updated_at = self.ensure_timezone_aware(issue.updated_at)

        # 条件1: 最近 90 天创建
        if (now - created_at).days <= self.CREATE_WINDOW_DAYS:
            return True

        # 条件2: 最近 3 天有更新（有新回复）
        if (now - updated_at).days <= self.ACTIVE_WINDOW_DAYS:
            return True

        return False

    def _convert_to_issue_info(
        self,
        issue,
        repo_name: str,
        now: datetime,
    ) -> IssueInfo:
        """转换 GitHub Issue 对象为 IssueInfo

        Args:
            issue: GitHub Issue 对象
            repo_name: 仓库名称
            now: 当前时间

        Returns:
            IssueInfo 对象
        """
        # 获取最后评论距今天数
        last_comment_days = self._get_last_comment_days(issue, now)

        # 获取标签
        labels = []
        if hasattr(issue, "labels") and issue.labels:
            labels = [label.name for label in issue.labels]

        # 获取作者
        author = issue.user.login if issue.user else "Unknown"

        return IssueInfo(
            repo=repo_name,
            issue_id=issue.number,
            title=issue.title,
            body=issue.body,
            state=issue.state,
            author=author,
            created_at=self.ensure_timezone_aware(issue.created_at),
            updated_at=self.ensure_timezone_aware(issue.updated_at),
            closed_at=(
                self.ensure_timezone_aware(issue.closed_at) if issue.closed_at else None
            ),
            comments=issue.comments,
            labels=labels,
            url=issue.html_url,
            last_comment_days=last_comment_days,
            is_recently_active=last_comment_days <= self.ACTIVE_WINDOW_DAYS,
        )

    def _get_last_comment_days(self, issue, now: datetime) -> int:
        """获取最后评论距今天数

        Args:
            issue: GitHub Issue 对象
            now: 当前时间

        Returns:
            距今天数（最小为 0，避免时钟偏差导致负值）
        """
        updated_at = self.ensure_timezone_aware(issue.updated_at)
        return max(0, (now - updated_at).days)

    def save_snapshot(
        self,
        date: str,
        analyzed_issues: list[dict[str, object]],
    ) -> None:
        """保存快照

        Args:
            date: 快照日期 YYYY-MM-DD
            analyzed_issues: 已分析的 Issue 列表
        """
        self.snapshot.save(date, analyzed_issues)
