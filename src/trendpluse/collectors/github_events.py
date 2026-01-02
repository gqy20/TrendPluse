"""GitHub Events 采集器

使用 PyGithub 直接从 GitHub API 获取事件。
"""
from datetime import datetime, timezone

from github import Github, GithubException


class GitHubEventsCollector:
    """从 GitHub API 直接获取事件"""

    def __init__(self, token: str = ""):
        """初始化 GitHub 客户端

        Args:
            token: GitHub Personal Access Token（可选）
        """
        if token:
            self.client = Github(login_or_token=token)
        else:
            self.client = Github()

    def fetch_events(
        self,
        repos: list[str],
        since: datetime,
    ) -> list[dict]:
        """获取指定仓库的 GitHub 事件

        Args:
            repos: 仓库列表，格式 ["owner/repo", ...]
            since: 起始时间

        Returns:
            事件列表，格式与 GHArchiveCollector 一致
        """
        events = []

        # 确保 since 有时区信息（用于与 GitHub API 返回的时间比较）
        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)

        for repo_name in repos:
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

                    events.append({
                        "type": "PullRequestEvent",
                        "repo": {"name": repo_name},
                        "payload": {
                            "pull_request": {
                                "number": pr.number,
                                "title": pr.title,
                                "body": pr.body,
                            }
                        },
                        "created_at": pr.created_at.isoformat(),
                    })

            except GithubException as e:
                # 记录错误但继续处理其他仓库
                print(f"获取仓库 {repo_name} 事件失败: {e}")
                continue

        return events
