"""IssueSnapshot 快照管理器测试

测试 Issue 分析快照的保存、加载和去重功能。
"""

import json
from pathlib import Path

from trendpluse.snapshots.issue_snapshot import IssueSnapshot


class TestIssueSnapshot:
    """IssueSnapshot 测试"""

    def test_create_snapshot_manager(self, temp_dir):
        """测试创建快照管理器"""
        # Arrange
        snapshot_dir = temp_dir / "snapshots"

        # Act
        snapshot = IssueSnapshot(str(snapshot_dir))

        # Assert
        assert snapshot.snapshot_dir == Path(snapshot_dir)
        assert snapshot.snapshot_dir.exists()

    def test_save_and_load_analyzed_ids(self, temp_dir):
        """测试保存和加载已分析的 Issue IDs"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        date = "2026-01-31"
        analyzed_issues = [
            {"repo": "anthropics/claude-code", "issue_id": 123, "categories": ["bug"]},
            {
                "repo": "openai/openai-python",
                "issue_id": 456,
                "categories": ["feature"],
            },
        ]

        # Act - 保存
        snapshot.save(date, analyzed_issues)

        # Assert - 验证文件存在
        snapshot_path = temp_dir / "2026-01-31.json"
        assert snapshot_path.exists()

        # Act - 加载
        loaded_ids = snapshot.load_analyzed_ids(date)

        # Assert - 验证内容
        expected_ids = {
            ("anthropics/claude-code", 123),
            ("openai/openai-python", 456),
        }
        assert loaded_ids == expected_ids

    def test_load_empty_snapshot_when_file_not_exists(self, temp_dir):
        """测试加载不存在的快照返回空集合"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))

        # Act
        loaded_ids = snapshot.load_analyzed_ids("2026-01-31")

        # Assert
        assert loaded_ids == set()

    def test_load_empty_snapshot_when_date_is_empty(self, temp_dir):
        """测试传入空日期字符串时返回空集合"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))

        # Act
        loaded_ids = snapshot.load_analyzed_ids("")

        # Assert
        assert loaded_ids == set()

    def test_save_creates_correct_json_format(self, temp_dir):
        """测试保存的 JSON 格式符合 Issue #39 要求"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        date = "2026-01-31"
        analyzed_issues = [
            {"repo": "owner/repo", "issue_id": 1234, "categories": ["bug"]},
        ]

        # Act
        snapshot.save(date, analyzed_issues)

        # Assert - 读取并验证 JSON 格式
        snapshot_path = temp_dir / "2026-01-31.json"
        with open(snapshot_path) as f:
            data = json.load(f)

        assert data["date"] == "2026-01-31"
        assert data["analyzed_count"] == 1
        assert len(data["analyzed_issues"]) == 1
        assert data["analyzed_issues"][0] == {
            "repo": "owner/repo",
            "issue_id": 1234,
            "categories": ["bug"],
        }

    def test_save_multiple_snapshots(self, temp_dir):
        """测试保存多个快照"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))

        # Act - 保存多个快照
        snapshot.save(
            "2026-01-30", [{"repo": "owner/repo", "issue_id": 1, "categories": []}]
        )
        snapshot.save(
            "2026-01-31", [{"repo": "owner/repo", "issue_id": 2, "categories": []}]
        )

        # Assert - 验证两个快照都存在
        assert (temp_dir / "2026-01-30.json").exists()
        assert (temp_dir / "2026-01-31.json").exists()

    def test_get_available_dates(self, temp_dir):
        """测试获取所有可用快照日期"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        snapshot.save("2026-01-29", [{"repo": "a/a", "issue_id": 1, "categories": []}])
        snapshot.save("2026-01-31", [{"repo": "b/b", "issue_id": 2, "categories": []}])
        snapshot.save("2026-01-30", [{"repo": "c/c", "issue_id": 3, "categories": []}])

        # Act
        dates = snapshot.get_available_dates()

        # Assert - 应该按日期倒序排列
        assert dates == ["2026-01-31", "2026-01-30", "2026-01-29"]

    def test_get_available_dates_when_empty(self, temp_dir):
        """测试没有快照时返回空列表"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))

        # Act
        dates = snapshot.get_available_dates()

        # Assert
        assert dates == []

    def test_get_available_dates_ignores_non_json_files(self, temp_dir):
        """测试忽略非 JSON 文件"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        snapshot.save("2026-01-31", [{"repo": "a/a", "issue_id": 1, "categories": []}])
        # 创建一个非 JSON 文件
        (temp_dir / "README.md").write_text("# test")

        # Act
        dates = snapshot.get_available_dates()

        # Assert - 只返回 JSON 文件对应的日期
        assert dates == ["2026-01-31"]

    def test_save_overwrites_existing_snapshot(self, temp_dir):
        """测试保存会覆盖已存在的快照"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        date = "2026-01-31"

        # Act - 第一次保存
        snapshot.save(date, [{"repo": "a/a", "issue_id": 1, "categories": ["bug"]}])
        # 第二次保存（覆盖）
        snapshot.save(date, [{"repo": "b/b", "issue_id": 2, "categories": ["feature"]}])

        # Assert - 验证被覆盖
        loaded_ids = snapshot.load_analyzed_ids(date)
        assert loaded_ids == {("b/b", 2)}

    def test_save_with_empty_analyzed_issues(self, temp_dir):
        """测试保存空的 Issue 列表"""
        # Arrange
        snapshot = IssueSnapshot(str(temp_dir))
        date = "2026-01-31"

        # Act
        snapshot.save(date, [])

        # Assert
        snapshot_path = temp_dir / "2026-01-31.json"
        assert snapshot_path.exists()

        with open(snapshot_path) as f:
            data = json.load(f)

        assert data["analyzed_count"] == 0
        assert data["analyzed_issues"] == []
