"""分析材料构建器测试。"""

from trendpluse.collectors.commit_material_builder import CommitMaterialBuilder
from trendpluse.collectors.release_material_builder import ReleaseMaterialBuilder


def test_build_commit_materials():
    commits = [
        {
            "repo": "owner/repo",
            "sha": "abc123",
            "message": "feat: add feature",
            "author": "alice",
            "timestamp": "2026-01-01T00:00:00Z",
        }
    ]

    materials = CommitMaterialBuilder.build(commits)

    assert len(materials) == 1
    assert materials[0].source_ref.source_type == "commit"
    assert materials[0].source_ref.external_id == "abc123"


def test_build_release_materials():
    releases = [
        {
            "repo": "owner/repo",
            "tag_name": "v1.0.0",
            "name": "v1.0.0",
            "body": "Release notes",
            "html_url": "https://github.com/owner/repo/releases/tag/v1.0.0",
        }
    ]

    materials = ReleaseMaterialBuilder.build(releases)

    assert len(materials) == 1
    assert materials[0].source_ref.source_type == "release"
    assert materials[0].source_ref.external_id == "v1.0.0"
