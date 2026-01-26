"""GitHub Events 采集器

使用 PyGithub 直接从 GitHub API 获取事件。
"""

from datetime import datetime

from github import GithubException

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.collectors.parallel import parallel_execute


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
                                    "merged": pr.merged,
                                    "labels": labels,
                                    "author": pr.user.login if pr.user else "Unknown",
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
                print(f"获取仓库 {repo_name} 事件失败: {e}")

            return events

        # 并行获取所有仓库的事件
        all_events_lists = parallel_execute(_fetch_one, repos, max_workers=max_workers)

        # 合并所有事件列表
        events = []
        for event_list in all_events_lists:
            events.extend(event_list)

        return events
