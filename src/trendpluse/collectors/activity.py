"""仓库活跃度采集器

统计仓库的活跃度指标，包括 commit 数量、活跃仓库数、新贡献者等。
"""

from datetime import UTC, datetime, timedelta
from typing import Any

from github import Github, GithubException


class ActivityCollector:
    """仓库活跃度采集器

    统计以下指标：
    - 总 commit 数量
    - 活跃仓库数量（有新 commit）
    - 新贡献者数量（首次提交）
    - 各仓库的活跃度详情
    """

    def __init__(self, token: str = ""):
        """初始化采集器

        Args:
            token: GitHub Personal Access Token（可选）
        """
        if token:
            self.client = Github(login_or_token=token)
        else:
            self.client = Github()

    def collect_activity(
        self,
        repos: list[str],
        since: datetime,
    ) -> dict[str, Any]:
        """收集仓库活跃度数据

        Args:
            repos: 仓库列表
            since: 起始时间

        Returns:
            活跃度数据字典
        """
        # 确保 since 有时区信息
        if since.tzinfo is None:
            since = since.replace(tzinfo=UTC)

        activity_data = {
            "total_commits": 0,
            "active_repos": 0,
            "new_contributors": 0,
            "repo_activity": [],
            "detailed_commits": [],  # 新增：详细 commit 列表
            "period_start": since.isoformat(),
            "period_end": datetime.now(UTC).isoformat(),
        }

        for repo_name in repos:
            try:
                repo = self.client.get_repo(repo_name)
                repo_activity, repo_commits = self._collect_repo_activity(
                    repo, since, repo_name
                )
                activity_data["repo_activity"].append(repo_activity)
                activity_data["detailed_commits"].extend(repo_commits)

                if repo_activity["commit_count"] > 0:
                    activity_data["active_repos"] += 1
                    activity_data["total_commits"] += repo_activity["commit_count"]
                    activity_data["new_contributors"] += repo_activity[
                        "new_contributors"
                    ]

            except GithubException as e:
                print(f"获取仓库 {repo_name} 活跃度失败: {e}")
                continue

        # 按活跃度排序
        activity_data["repo_activity"].sort(
            key=lambda x: x["commit_count"], reverse=True
        )

        return activity_data

    def _collect_repo_activity(
        self,
        repo: Any,
        since: datetime,
        repo_name: str,
    ) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        """收集单个仓库的活跃度

        Args:
            repo: PyGithub Repository 对象
            since: 起始时间
            repo_name: 仓库名称

        Returns:
            (仓库活跃度数据, 详细 commit 列表)
        """
        activity = {
            "repo": repo_name,
            "commit_count": 0,
            "new_contributors": 0,
            "top_contributors": [],
            "recent_commits": [],
        }

        detailed_commits = []  # 新增：详细 commit 列表

        try:
            # 获取时间范围内的 commits（过去一天）
            # 注意：get_commits() 可能返回大量数据，需要限制
            since_date = since - timedelta(days=1)
            commits = repo.get_commits(since=since_date, until=since)
            # 转换为列表以便安全迭代
            commits_list = list(commits)

            print(f"[DEBUG] {repo_name}: 获取到 {len(commits_list)} 个 commits")

            # 用于统计新贡献者
            # 策略：检查该时间之前的贡献者集合
            existing_contributors = set()

            # 先获取一段时间之前的贡献者（采样，避免过多请求）
            try:
                past_since = since - timedelta(days=30)
                past_commits = repo.get_commits(since=past_since, until=since)
                # 转换为列表并安全切片
                past_commits_list = list(past_commits)
                for commit in past_commits_list[:100]:  # 采样 100 个
                    if commit and commit.author:
                        existing_contributors.add(commit.author.login)
            except GithubException:
                pass  # 如果获取失败，existing_contributors 保持为空

            # 统计当前时间范围的 commits
            contributor_commits: dict[str, int] = {}
            new_contributors_set = set()

            for commit in commits_list:
                activity["commit_count"] += 1

                # 构建详细 commit 信息
                detailed_commit = {
                    "repo": repo_name,
                    "sha": commit.sha,
                    "message": commit.commit.message.split("\n")[0][:200],  # 限制长度
                    "author": commit.author.login if commit.author else "Unknown",
                    "timestamp": commit.commit.author.date.isoformat(),
                    "files_changed": [],  # PyGithub 不直接提供，留空
                    "additions": 0,  # 需要额外 API 调用，暂时设为 0
                    "deletions": 0,  # 需要额外 API 调用，暂时设为 0
                }
                detailed_commits.append(detailed_commit)

                # 记录最近的 commits（最多 5 个）
                if len(activity["recent_commits"]) < 5:
                    author_login = commit.author.login if commit.author else "Unknown"
                    commit_msg = commit.commit.message.split("\n")[0][:80]
                    activity["recent_commits"].append(
                        {
                            "sha": commit.sha[:7],
                            "message": commit_msg,
                            "author": author_login,
                            "timestamp": commit.commit.author.date.isoformat(),
                        }
                    )

                # 统计贡献者
                if commit.author:
                    author = commit.author.login
                    contributor_commits[author] = contributor_commits.get(author, 0) + 1

                    # 判断是否为新贡献者
                    if author not in existing_contributors:
                        new_contributors_set.add(author)

            activity["new_contributors"] = len(new_contributors_set)

            # Top 贡献者（最多 5 个）
            sorted_contributors = sorted(
                contributor_commits.items(), key=lambda x: x[1], reverse=True
            )[:5]

            activity["top_contributors"] = [
                {"login": login, "commits": count}
                for login, count in sorted_contributors
            ]

        except GithubException as e:
            print(f"处理仓库 {repo_name} commits 失败: {e}")

        return activity, detailed_commits
