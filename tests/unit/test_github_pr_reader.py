"""GitHub PR Reader 测试。"""

from unittest.mock import Mock, patch

from trendpluse.collectors.github_pr_reader import GitHubPRReader
from trendpluse.models.source import SourceRef


def test_refs_from_candidates_filters_non_pr_events():
    candidates = [
        {
            "type": "PullRequestEvent",
            "repo": {"name": "owner/repo"},
            "payload": {"pull_request": {"number": 1}},
        },
        {
            "type": "ReleaseEvent",
            "repo": {"name": "owner/repo"},
            "payload": {},
        },
    ]

    refs = GitHubPRReader.refs_from_candidates(candidates)

    assert len(refs) == 1
    assert refs[0].external_id == "1"


@patch("trendpluse.collectors.github_pr_reader.GitHubDetailFetcher")
def test_read_many_returns_analysis_materials(mock_fetcher_class):
    mock_fetcher = Mock()
    mock_fetcher.fetch_pr_details.return_value = {
        "number": 1,
        "title": "Test PR",
        "body": "Test body",
        "author": "alice",
        "url": "https://github.com/owner/repo/pull/1",
        "created_at": "2026-01-01T00:00:00Z",
        "closed_at": "2026-01-02T00:00:00Z",
    }
    mock_fetcher_class.return_value = mock_fetcher

    reader = GitHubPRReader(token="test-token")
    refs = [
        SourceRef(
            source_type="pull_request",
            provider="github",
            repo="owner/repo",
            external_id="1",
            url="https://github.com/owner/repo/pull/1",
        )
    ]

    materials = reader.read_many(refs, max_workers=2)

    assert len(materials) == 1
    assert materials[0].source_ref.repo == "owner/repo"
    assert materials[0].title == "Test PR"
    assert materials[0].raw_payload["repo_name"] == "owner/repo"
