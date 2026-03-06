"""来源引用与分析材料模型测试。"""

from trendpluse.models.source import AnalysisMaterial, SourceRef


def test_source_ref_from_pr_candidate():
    candidate = {
        "type": "PullRequestEvent",
        "repo": {"name": "owner/repo"},
        "payload": {
            "pull_request": {
                "number": 42,
                "state": "closed",
                "merged": True,
                "changed_files": 5,
            }
        },
    }

    ref = SourceRef.from_pr_candidate(candidate)

    assert ref.repo == "owner/repo"
    assert ref.external_id == "42"
    assert ref.url == "https://github.com/owner/repo/pull/42"
    assert ref.metadata["merged"] is True


def test_analysis_material_from_pr_details():
    details = {
        "number": 7,
        "repo_name": "owner/repo",
        "title": "Add feature",
        "body": "Details",
        "author": "alice",
        "url": "https://github.com/owner/repo/pull/7",
    }

    material = AnalysisMaterial.from_pr_details(details)

    assert material.source_ref.repo == "owner/repo"
    assert material.source_ref.external_id == "7"
    assert material.title == "Add feature"
    assert material.raw_payload["author"] == "alice"


def test_analysis_material_from_release_details():
    details = {
        "repo": "owner/repo",
        "tag_name": "v1.2.3",
        "name": "Release v1.2.3",
        "body": "Release notes",
        "html_url": "https://github.com/owner/repo/releases/tag/v1.2.3",
    }

    material = AnalysisMaterial.from_release_details(details)

    assert material.source_ref.source_type == "release"
    assert material.source_ref.external_id == "v1.2.3"
    assert material.source_ref.url.endswith("/v1.2.3")
    assert material.body == "Release notes"


def test_analysis_material_from_commit_details():
    details = {
        "repo": "owner/repo",
        "sha": "abc123",
        "message": "feat: add feature",
        "author": "alice",
        "timestamp": "2026-01-01T00:00:00Z",
    }

    material = AnalysisMaterial.from_commit_details(details)

    assert material.source_ref.source_type == "commit"
    assert material.source_ref.external_id == "abc123"
    assert material.source_ref.url.endswith("/abc123")
    assert material.title == "feat: add feature"
