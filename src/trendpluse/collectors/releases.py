"""Release 数据采集器

收集 GitHub Releases 数据，包括版本号、发布时间、发布说明等。
"""

from datetime import UTC, datetime
from re import match
from typing import Any

from github import Github, GithubException

from trendpluse.models.signal import ReleaseInfo, ReleasesData


class ReleaseCollector:
    """Release 数据采集器

    收集以下信息：
    - 总 Release 数量
    - 有 Release 的仓库数量
    - 各仓库的 Release 详情
    - 版本号解析（major.minor.patch）
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

    def collect_releases(
        self,
        repos: list[str],
        since: datetime,
        include_prereleases: bool = False,
    ) -> tuple[ReleasesData, list[dict]]:
        """收集 Release 数据

        Args:
            repos: 仓库列表
            since: 起始时间
            include_prereleases: 是否包含预发布版本

        Returns:
            (ReleasesData 对象, 详细 Release 列表)
        """
        # 确保 since 有时区信息
        if since.tzinfo is None:
            since = since.replace(tzinfo=UTC)

        # 收集所有 Release
        all_releases: list[ReleaseInfo] = []
        all_detailed_releases: list[dict] = []

        total_count = 0
        unique_repos_count = 0

        for repo_name in repos:
            try:
                repo_releases, detailed = self._collect_repo_releases(
                    repo=repo_name,
                    since=since,
                    include_prereleases=include_prereleases,
                )

                if repo_releases:
                    all_releases.extend(repo_releases)
                    all_detailed_releases.extend(detailed)
                    unique_repos_count += 1
                    total_count += len(repo_releases)

            except GithubException as e:
                print(f"获取仓库 {repo_name} releases 失败: {e}")
                continue
            except Exception as e:
                print(f"处理仓库 {repo_name} 时发生错误: {e}")
                continue

        # 按 created_at 降序排列
        all_releases.sort(key=lambda x: x.date, reverse=True)

        # 构建 ReleasesData
        releases_data = ReleasesData(
            total_count=total_count,
            unique_repos_count=unique_repos_count,
            releases=all_releases,
        )

        return releases_data, all_detailed_releases

    def _collect_repo_releases(
        self,
        repo: str,
        since: datetime,
        include_prereleases: bool = False,
    ) -> tuple[list[ReleaseInfo], list[dict]]:
        """收集单个仓库的 Releases

        Args:
            repo: 仓库名称
            since: 起始时间
            include_prereleases: 是否包含预发布版本

        Returns:
            (ReleaseInfo 对象列表, 详细 Release 列表)
        """
        repo_obj = self.client.get_repo(repo)
        all_releases = repo_obj.get_releases()

        release_infos: list[ReleaseInfo] = []
        detailed_releases: list[dict] = []

        for release in all_releases:
            # 检查日期
            if release.created_at < since:
                continue

            # 检查是否为预发布版本
            if not include_prereleases and release.prerelease:
                continue

            # 解析版本号
            version_info = self._parse_version(release.tag_name)

            # 构建 ReleaseInfo 对象
            release_info = ReleaseInfo(
                repo=repo,
                version=release.tag_name,
                author=release.author.login if release.author else "Unknown",
                date=release.created_at.date().isoformat(),
                summary=release.body or "",
                assets_count=len(release.assets),
                url=release.html_url,
            )
            release_infos.append(release_info)

            # 构建详细 Release 信息（用于 ReleaseAnalyzer）
            detailed = {
                "repo": repo,
                "tag_name": release.tag_name,
                "name": release.title or release.tag_name,
                "prerelease": release.prerelease,
                "created_at": release.created_at.isoformat(),
                "published_at": (
                    release.published_at.isoformat() if release.published_at else None
                ),
                "body": release.body or "",
                "author": release.author.login if release.author else "Unknown",
                "html_url": release.html_url,
                "assets": [
                    {
                        "name": asset.name,
                        "size": asset.size,
                        "download_count": asset.download_count,
                    }
                    for asset in release.assets
                ],
                "version_info": version_info,
            }
            detailed_releases.append(detailed)

        return release_infos, detailed_releases

    def _parse_version(self, tag_name: str) -> dict[str, Any] | None:
        """解析版本号

        Args:
            tag_name: Git 标签名（如 v1.2.3, 2.0.0-beta）

        Returns:
            版本信息字典，包含 major, minor, patch, is_prerelease
        """
        # 移除 'v' 前缀
        version = tag_name.lstrip("v")

        # 检查是否为预发布版本
        is_prerelease = any(
            marker in version.lower()
            for marker in ["alpha", "beta", "rc", "pre", "dev", "nightly"]
        )

        # 解析版本号
        pattern = r"^(\d+)\.(\d+)\.(\d+)"
        m = match(pattern, version)

        if m:
            major, minor, patch = m.groups()
            return {
                "major": int(major),
                "minor": int(minor),
                "patch": int(patch),
                "is_prerelease": is_prerelease,
            }

        # 尝试解析 v1.0 或 v2 格式
        pattern_simple = r"^(\d+)\.(\d+)(?:\.(\d+))?"
        m_simple = match(pattern_simple, version)

        if m_simple:
            major = int(m_simple.group(1))
            minor = int(m_simple.group(2))
            patch = int(m_simple.group(3)) if m_simple.group(3) else 0
            return {
                "major": major,
                "minor": minor,
                "patch": patch,
                "is_prerelease": is_prerelease,
            }

        return None
