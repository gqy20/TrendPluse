"""GitHub Events 采集器

使用 PyGithub 直接从 GitHub API 获取事件。
"""

import time
from datetime import datetime

from github import GithubException

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.collectors.parallel import parallel_execute
from trendpluse.logger import get_logger

logger = get_logger(__name__)


class GitHubEventsCollector(BaseGitHubCollector):
    """从 GitHub API 直接获取事件"""

    def fetch_events(
        self,
        repos: list[str],
        since: datetime,
        max_workers: int | None = None,
    ) -> list[dict]:
        """并行获取指定仓库的 GitHub 事件

        Args:
            repos: 仓库列表，格式 ["owner/repo", ...]
            since: 起始时间
            max_workers: 最大线程数（默认为 min(32, len(repos) + 4)）

        Returns:
            事件列表
        """
        # 确保 since 有时区信息
        since = self.ensure_timezone_aware(since)

        # 失败仓库追踪（list.append 在 CPython 下线程安全）
        failed_repos: list[str] = []

        # 定义获取单个仓库事件的函数
        def _fetch_one(repo_name: str) -> list[dict]:
            """获取单个仓库的事件"""
            events = []
            try:
                repo = self.client.get_repo(repo_name)

                # 获取最近的 Pull Request
                pulls = repo.get_pulls(
                    state="all",
                    sort="created",
                    direction="desc",
                )

                for pr in pulls:
                    # 只获取指定时间之后的 PR
                    if pr.created_at < since:
                        break

                    # 提取标签信息
                    labels = []
                    if hasattr(pr, "labels") and pr.labels:
                        for label in pr.labels:
                            labels.append({"name": label.name})

                    events.append(
                        {
                            "type": "PullRequestEvent",
                            "repo": {"name": repo_name},
                            "payload": {
                                "pull_request": {
                                    "number": pr.number,
                                    "title": pr.title,
                                    "body": pr.body,
                                    "state": pr.state,
                                    "merged": pr.merged,
                                    "draft": pr.draft or False,
                                    "labels": labels,
                                    "author": (pr.user.login if pr.user else "Unknown"),
                                    "additions": pr.additions,
                                    "deletions": pr.deletions,
                                    "changed_files": pr.changed_files,
                                }
                            },
                            "created_at": pr.created_at.isoformat(),
                        }
                    )

            except GithubException as e:
                # 记录错误但继续处理其他仓库
                logger.error(f"获取仓库 {repo_name} 事件失败: {e}")
                failed_repos.append(repo_name)

            return events

        # 单仓库耗时记录（并行度调优观测：定位拖慢整批的仓库）
        repo_timings: dict[str, float] = {}
        original_fetch_one = _fetch_one

        def _timed_fetch_one(repo_name: str) -> list[dict]:
            """包装单仓库采集以记录耗时。"""
            started = time.perf_counter()
            try:
                return original_fetch_one(repo_name)
            finally:
                repo_timings[repo_name] = time.perf_counter() - started

        # 并行获取所有仓库的事件
        all_events_lists = parallel_execute(
            _timed_fetch_one, repos, max_workers=max_workers
        )

        # 合并所有事件列表
        events = []
        for event_list in all_events_lists:
            events.extend(event_list)

        # 运行汇总：成功/失败/事件总数一目了然
        ok_count = len(repos) - len(failed_repos)
        logger.info(
            "Events collection done: repos=%d ok=%d failed=%d events=%d",
            len(repos),
            ok_count,
            len(failed_repos),
            len(events),
        )
        if failed_repos:
            preview = ", ".join(failed_repos[:10])
            suffix = " ..." if len(failed_repos) > 10 else ""
            logger.warning(
                "事件采集失败仓库 %d 个: %s%s",
                len(failed_repos),
                preview,
                suffix,
            )

        # 最慢仓库 Top 5：并行池的"长尾轮次"由此定位
        slowest = sorted(repo_timings.items(), key=lambda kv: -kv[1])[:5]
        if slowest:
            logger.info(
                "Slowest repos: %s",
                ", ".join(f"{repo}={elapsed:.1f}s" for repo, elapsed in slowest),
            )

        return events
