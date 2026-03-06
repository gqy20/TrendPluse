"""GitHub PR 读取器。"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from github import GithubException

from trendpluse.collectors.github_api import GitHubDetailFetcher
from trendpluse.logger import get_logger
from trendpluse.models.source import AnalysisMaterial, SourceRef

logger = get_logger(__name__)


class GitHubPRReader:
    """读取 PR 引用并产出可分析材料。"""

    def __init__(self, token: str):
        self.fetcher = GitHubDetailFetcher(token=token)

    @staticmethod
    def refs_from_candidates(candidates: list[dict[str, Any]]) -> list[SourceRef]:
        """从候选事件构建 PR 引用列表。"""
        refs: list[SourceRef] = []
        for candidate in candidates:
            if candidate.get("type") != "PullRequestEvent":
                continue
            refs.append(SourceRef.from_pr_candidate(candidate))
        return refs

    def read(self, ref: SourceRef) -> AnalysisMaterial:
        """读取单个 PR 引用。"""
        details = self.fetcher.fetch_pr_details(ref.repo, int(ref.external_id))
        raw_payload = {
            **details,
            "repo_name": ref.repo,
            "url": details.get("url") or ref.url,
        }
        return AnalysisMaterial(
            source_ref=ref,
            title=str(details.get("title", "")),
            body=str(details.get("body", "")),
            author=str(details.get("author", "")),
            created_at=details.get("created_at"),
            updated_at=details.get("closed_at"),
            raw_payload=raw_payload,
        )

    def read_many(
        self, refs: list[SourceRef], max_workers: int = 10
    ) -> list[AnalysisMaterial]:
        """并发读取多个 PR 引用。"""
        if not refs:
            return []

        materials: list[AnalysisMaterial] = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_ref = {executor.submit(self.read, ref): ref for ref in refs}
            for future in as_completed(future_to_ref):
                ref = future_to_ref[future]
                try:
                    materials.append(future.result())
                except GithubException as e:
                    logger.debug(
                        f"读取 PR {ref.repo}#{ref.external_id} 失败: {e}",
                        extra={"repo": ref.repo, "pr_number": ref.external_id},
                    )
                    continue

        return materials
