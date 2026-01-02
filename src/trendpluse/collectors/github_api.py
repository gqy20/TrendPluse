"""GitHub API 详情获取器

使用 PyGithub 获取 PR/Release 的详细信息。
"""

from github import Github, GithubException
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


class GitHubDetailFetcher:
    """从 GitHub API 获取详细信息"""

    def __init__(self, token: str = ""):
        """初始化 GitHub 客户端

        Args:
            token: GitHub API token（可选，无 token 时有严格的速率限制）
        """
        if token:
            self.client = Github(login_or_token=token)
        else:
            # 无 token 时仍然可以访问公开仓库，但有速率限制
            self.client = Github()
        self._rate_limit_wait = wait_exponential(multiplier=1, min=4, max=60)

    @retry(
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(GithubException),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        reraise=True,
    )
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

    @retry(
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(GithubException),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        reraise=True,
    )
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

    @retry(
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(GithubException),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        reraise=True,
    )
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

    def fetch_multiple_pr_details(self, candidates: list[dict]) -> list[dict]:
        """批量获取 PR 详情

        Args:
            candidates: 候选事件列表

        Returns:
            PR 详情列表
        """
        details_list = []

        for event in candidates:
            if event.get("type") == "PullRequestEvent":
                repo_name = event["repo"]["name"]
                pr_number = event["payload"]["pull_request"]["number"]

                try:
                    details = self.fetch_pr_details(repo_name, pr_number)
                    details_list.append(details)
                except GithubException as e:
                    # 记录错误但继续处理其他 PR
                    print(f"获取 PR {repo_name}#{pr_number} 失败: {e}")
                    continue

        return details_list
