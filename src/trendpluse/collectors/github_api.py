"""GitHub API 详情获取器

使用 PyGithub 获取 PR/Release 的详细信息。
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from github import GithubException

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.logger import get_logger
from trendpluse.utils.retry import create_github_retry_decorator

logger = get_logger(__name__)

# 创建重试装饰器（统一配置）
_github_retry = create_github_retry_decorator()


class GitHubDetailFetcher(BaseGitHubCollector):
    """从 GitHub API 获取详细信息"""

    @_github_retry
    def fetch_pr_details(self, repo_name: str, pr_number: int) -> dict:
        """获取 PR 详情

        Args:
            repo_name: 仓库名称，格式 "owner/repo"
            pr_number: PR 编号

        Returns:
            PR 详情字典
        """
        repo = self.client.get_repo(repo_name)
        pr = repo.get_pull(pr_number)

        return {
            "number": pr.number,
            "title": pr.title,
            "body": pr.body,
            "author": pr.user.login,
            "created_at": pr.created_at.isoformat(),
            "closed_at": pr.closed_at.isoformat() if pr.closed_at else None,
            "url": pr.html_url,
            "state": pr.state,
            "merged": pr.merged,
            "merge_commit_sha": pr.merge_commit_sha,
            "additions": pr.additions,
            "deletions": pr.deletions,
            "changed_files": pr.changed_files,
        }

    @_github_retry
    def fetch_release_details(self, repo_name: str, tag_name: str) -> dict:
        """获取 Release 详情

        Args:
            repo_name: 仓库名称，格式 "owner/repo"
            tag_name: 标签名称

        Returns:
            Release 详情字典
        """
        repo = self.client.get_repo(repo_name)
        release = repo.get_release(tag_name)

        return {
            "tag_name": release.tag_name,
            "name": release.name,
            "body": release.body,
            "author": release.author.login,
            "created_at": release.created_at.isoformat(),
            "published_at": release.published_at.isoformat(),
            "url": release.html_url,
            "prerelease": release.prerelease,
        }

    @_github_retry
    def fetch_pr_comments(self, repo_name: str, pr_number: int) -> list[dict]:
        """获取 PR 评论

        Args:
            repo_name: 仓库名称，格式 "owner/repo"
            pr_number: PR 编号

        Returns:
            评论列表
        """
        repo = self.client.get_repo(repo_name)
        pr = repo.get_pull(pr_number)

        comments = []
        for comment in pr.get_comments():
            comments.append(
                {
                    "author": comment.user.login,
                    "body": comment.body,
                    "created_at": comment.created_at.isoformat(),
                }
            )

        return comments

    def fetch_multiple_pr_details(
        self, candidates: list[dict], max_workers: int = 10
    ) -> list[dict]:
        """批量获取 PR 详情

        Args:
            candidates: 候选事件列表
            max_workers: 最大并发线程数（默认 10）

        Returns:
            PR 详情列表
        """
        if not candidates:
            return []

        pr_tasks = []
        for event in candidates:
            if event.get("type") == "PullRequestEvent":
                repo_name = event["repo"]["name"]
                pr_number = event["payload"]["pull_request"]["number"]
                pr_tasks.append((repo_name, pr_number))

        if not pr_tasks:
            return []

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_task = {
                executor.submit(self.fetch_pr_details, repo, num): (repo, num)
                for repo, num in pr_tasks
            }

            for future in as_completed(future_to_task):
                repo, num = future_to_task[future]
                try:
                    details = future.result()
                    results.append(details)
                except GithubException as e:
                    logger.debug(
                        f"获取 PR {repo}#{num} 失败: {e}",
                        extra={"repo": repo, "pr_number": num},
                    )
                    continue

        return results
