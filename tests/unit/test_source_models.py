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
