"""仓库活跃度采集器

统计仓库的活跃度指标，包括 commit 数量、活跃仓库数、新贡献者等。
"""

from datetime import datetime, timedelta
from typing import Any

from github import GithubException

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.collectors.parallel import parallel_map
from trendpluse.models.signal import ActivityData, RepoActivity

# GraphQL 查询模板
GRAPHQL_COMMIT_QUERY = """
query($owner: String!, $repo: String!, $since: DateTime!) {
    repository(owner: $owner, name: $repo) {
        defaultBranchRef {
            target {
                ... on Commit {
                    history(since: $since, first: 100) {
                        nodes {
                            oid
                            message
                            author { user { login } }
                            committedDate
                            additions
                            deletions
                            changedFiles
                        }
                    }
                }
            }
        }
    }
}
"""


class ActivityCollector(BaseGitHubCollector):
    """仓库活跃度采集器

    统计以下指标：
    - 总 commit 数量
    - 活跃仓库数量（有新 commit）
    - 新贡献者数量（首次提交）
    - 各仓库的活跃度详情
    """

    def collect_activity(
        self,
        repos: list[str],
        since: datetime,
        max_workers: int | None = None,
    ) -> tuple[ActivityData, list[dict]]:
        """并行收集仓库活跃度数据

        Args:
            repos: 仓库列表
            since: 起始时间
            max_workers: 最大线程数（默认为 min(32, len(repos) + 4)）

        Returns:
            (ActivityData 对象, 详细 commit 列表)
        """
        # 确保 since 有时区信息
        since = self.ensure_timezone_aware(since)

        # 定义采集单个仓库的函数
        def _collect_one(repo_name: str) -> tuple[RepoActivity, list[dict]]:
            """采集单个仓库的活跃度"""
            repo = self.client.get_repo(repo_name)
            return self._collect_repo_activity(repo, since, repo_name)

        # 并行采集所有仓库
        results = parallel_map(_collect_one, repos, max_workers=max_workers)

        # 处理结果
        top_repos: list[RepoActivity] = []
        all_detailed_commits: list[dict] = []

        total_commits = 0
        active_repos_count = 0
        total_new_contributors = 0

        for repo_activity, repo_commits in results:
            if repo_activity:
                top_repos.append(repo_activity)
                all_detailed_commits.extend(repo_commits)

                if repo_activity.commits > 0:
                    active_repos_count += 1
                    total_commits += repo_activity.commits
                    total_new_contributors += repo_activity.new_contributors

        # 按活跃度排序
        top_repos.sort(key=lambda x: -x.commits)

        # 构建 ActivityData
        activity_data = ActivityData(
            total_commits=total_commits,
            active_repos_count=active_repos_count,
            new_contributors=total_new_contributors,
            top_repos=top_repos,
        )

        return activity_data, all_detailed_commits

    def _collect_repo_activity(
        self,
        repo: Any,
        since: datetime,
        repo_name: str,
    ) -> tuple[RepoActivity, list[dict]]:
        """收集单个仓库的活跃度

        Args:
            repo: PyGithub Repository 对象
            since: 起始时间
            repo_name: 仓库名称

        Returns:
            (RepoActivity 对象, 详细 commit 列表)
        """
        commits_count = 0
        new_contributors_count = 0
        top_contributors: list[str] = []

        detailed_commits: list[dict] = []

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
                commits_count += 1

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

                # 统计贡献者
                if commit.author:
                    author = commit.author.login
                    contributor_commits[author] = contributor_commits.get(author, 0) + 1

                    # 判断是否为新贡献者
                    if author not in existing_contributors:
                        new_contributors_set.add(author)

            new_contributors_count = len(new_contributors_set)

            # Top 贡献者（最多 5 个），只保留登录名
            sorted_contributors = sorted(
                contributor_commits.items(), key=lambda x: x[1], reverse=True
            )[:5]
            top_contributors = [login for login, _ in sorted_contributors]

        except GithubException as e:
            print(f"处理仓库 {repo_name} commits 失败: {e}")

        # 构建 RepoActivity 对象
        repo_activity = RepoActivity(
            repo=repo_name,
            commits=commits_count,
            new_contributors=new_contributors_count,
            top_contributors=top_contributors,
        )

        return repo_activity, detailed_commits

    def collect_activity_graphql(
        self,
        repos: list[str],
        since: datetime,
        max_workers: int | None = None,
    ) -> tuple[ActivityData, list[dict]]:
        """使用 GraphQL 并行收集仓库活跃度数据

        Args:
            repos: 仓库列表（格式：owner/repo）
            since: 起始时间
            max_workers: 最大线程数（默认为 min(32, len(repos) + 4)）

        Returns:
            (ActivityData 对象, 详细 commit 列表)
        """
        # 确保 since 有时区信息
        since = self.ensure_timezone_aware(since)

        # 定义采集单个仓库的函数
        def _collect_one_graphql(repo_name: str) -> tuple[RepoActivity, list[dict]]:
            """使用 GraphQL 采集单个仓库的活跃度"""
            owner, repo = repo_name.split("/", 1)
            return self._collect_repo_activity_graphql(owner, repo, since, repo_name)

        # 并行采集所有仓库
        results = parallel_map(_collect_one_graphql, repos, max_workers=max_workers)

        # 处理结果
        top_repos: list[RepoActivity] = []
        all_detailed_commits: list[dict] = []

        total_commits = 0
        active_repos_count = 0
        total_new_contributors = 0

        for repo_activity, repo_commits in results:
            if repo_activity:
                top_repos.append(repo_activity)
                all_detailed_commits.extend(repo_commits)

                if repo_activity.commits > 0:
                    active_repos_count += 1
                    total_commits += repo_activity.commits
                    total_new_contributors += repo_activity.new_contributors

        # 按活跃度排序
        top_repos.sort(key=lambda x: -x.commits)

        # 构建 ActivityData
        activity_data = ActivityData(
            total_commits=total_commits,
            active_repos_count=active_repos_count,
            new_contributors=total_new_contributors,
            top_repos=top_repos,
        )

        return activity_data, all_detailed_commits

    def _collect_repo_activity_graphql(
        self,
        owner: str,
        repo: str,
        since: datetime,
        repo_name: str,
    ) -> tuple[RepoActivity, list[dict]]:
        """使用 GraphQL 收集单个仓库的活跃度

        Args:
            owner: 仓库所有者
            repo: 仓库名称
            since: 起始时间
            repo_name: 完整仓库名称（owner/repo）

        Returns:
            (RepoActivity 对象, 详细 commit 列表)
        """
        commits_count = 0
        new_contributors_count = 0
        top_contributors: list[str] = []
        detailed_commits: list[dict] = []

        try:
            # 执行 GraphQL 查询
            variables = {
                "owner": owner,
                "repo": repo,
                "since": since.isoformat(),
            }
            result = self.execute_query(GRAPHQL_COMMIT_QUERY, variables)

            # 解析响应
            repository = result.get("repository", {})
            default_branch_ref = repository.get("defaultBranchRef", {})
            target = default_branch_ref.get("target", {})
            history = target.get("history", {})
            nodes = history.get("nodes", [])

            # 统计贡献者
            contributor_commits: dict[str, int] = {}
            new_contributors_set = set()

            for node in nodes:
                commits_count += 1

                # 提取作者信息
                author_user = node.get("author", {})
                author_info = author_user.get("user", {})
                author_login = (
                    author_info.get("login", "Unknown") if author_info else "Unknown"
                )

                # 构建详细 commit 信息（GraphQL 提供完整数据！）
                detailed_commit = {
                    "repo": repo_name,
                    "sha": node.get("oid", ""),
                    "message": node.get("message", "")[:200],  # 限制长度
                    "author": author_login,
                    "timestamp": node.get("committedDate", ""),
                    "files_changed": node.get("changedFiles", 0),  # GraphQL 提供！
                    "additions": node.get("additions", 0),  # GraphQL 提供！
                    "deletions": node.get("deletions", 0),  # GraphQL 提供！
                }
                detailed_commits.append(detailed_commit)

                # 统计贡献者
                if author_login != "Unknown":
                    contributor_commits[author_login] = (
                        contributor_commits.get(author_login, 0) + 1
                    )
                    # 简化处理：暂时假设所有贡献者都是新的
                    # TODO: 实现更精确的新贡献者检测
                    new_contributors_set.add(author_login)

            new_contributors_count = len(new_contributors_set)

            # Top 贡献者（最多 5 个）
            sorted_contributors = sorted(
                contributor_commits.items(), key=lambda x: x[1], reverse=True
            )[:5]
            top_contributors = [login for login, _ in sorted_contributors]

        except Exception as e:
            print(f"处理仓库 {repo_name} GraphQL 查询失败: {e}")

        # 构建 RepoActivity 对象
        repo_activity = RepoActivity(
            repo=repo_name,
            commits=commits_count,
            new_contributors=new_contributors_count,
            top_contributors=top_contributors,
        )

        return repo_activity, detailed_commits
