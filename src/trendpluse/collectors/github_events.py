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
        enable_open_pr_diff: bool = False,
    ) -> list[dict]:
        """并行获取指定仓库的 GitHub 事件

        Args:
            repos: 仓库列表，格式 ["owner/repo", ...]
            since: 起始时间
            max_workers: 最大线程数（默认为 min(32, len(repos) + 4)）
            enable_open_pr_diff: 是否为 open PR 读取 diff 字段
                （additions/deletions/changed_files，供 EventFilter 规模筛选）。
                list 端点不返回这些字段，读取会触发 per-PR 补全请求，
                故仅在启用 open PR 筛选（enable_open_prs）时开启。

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

                    # 性能关键：list 端点不返回 merged 布尔与 diff 字段，
                    # 直接读会触发 PyGithub 对每个 PR 的单 PR 详情补全请求
                    # （实测 10 PR 11 次请求；OpenHands 单日 90 个 open PR
                    # 曾因此耗时 100s+）。merged 用 merged_at 等价判断；
                    # diff 三字段仅在启用 open PR 规模筛选时按需读取，
                    # merged PR 的 diff 由 detail fetch 阶段天然提供。
                    is_merged = pr.merged_at is not None
                    additions = deletions = changed_files = None
                    if enable_open_pr_diff and pr.state == "open":
                        additions = pr.additions
                        deletions = pr.deletions
                        changed_files = pr.changed_files

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
                                    "merged": is_merged,
                                    "draft": pr.draft or False,
                                    "labels": labels,
                                    "author": (pr.user.login if pr.user else "Unknown"),
                                    "additions": additions,
                                    "deletions": deletions,
                                    "changed_files": changed_files,
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
