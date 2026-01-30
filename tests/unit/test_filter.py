"""事件筛选单元测试"""

from trendpluse.collectors.filter import EventFilter


class TestEventFilter:
    """测试事件筛选器"""

    def test_filter_candidates_by_pr_state(self):
        """测试：只返回已合并的 PR"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "merged": True,
                        "number": 1,
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "merged": False,  # 未合并
                        "number": 2,
                    },
                },
            },
        ]
        filter = EventFilter()

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 1

    def test_filter_candidates_by_labels(self):
        """测试：按标签过滤"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "merged": True,
                        "number": 1,
                        "labels": [{"name": "feature"}],
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "merged": True,
                        "number": 2,
                        "labels": [{"name": "bug"}],  # 不在候选标签中
                    },
                },
            },
        ]
        filter = EventFilter(labels=["feature"])

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 1

    def test_filter_candidates_max_count(self):
        """测试：限制返回数量"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": f"anthropics/repo{i}"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "merged": True,
                        "number": i,
                        "labels": [{"name": "feature"}],
                    },
                },
            }
            for i in range(10)
        ]
        filter = EventFilter(labels=["feature"], max_count=5)

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 5

    def test_filter_candidates_includes_releases(self):
        """测试：包含 Release 事件"""
        # Arrange
        events = [
            {
                "type": "ReleaseEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "published",
                    "release": {
                        "tag_name": "v1.0.0",
                        "name": "First release",
                    },
                },
            },
        ]
        filter = EventFilter()

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["type"] == "ReleaseEvent"

    def test_filter_candidates_empty_input(self):
        """测试：空输入返回空列表"""
        # Arrange
        filter = EventFilter()

        # Act
        candidates = filter.filter_candidates([])

        # Assert
        assert candidates == []

    def test_filter_candidates_includes_high_quality_open_prs(self):
        """测试：包含高质量 open PR（enable_open_prs=True）"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 1,
                        "title": "Add new feature",
                        "changed_files": 5,
                        "additions": 100,
                        "deletions": 20,
                        "labels": [{"name": "feature"}],
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": True,  # 草稿 PR 应被排除
                        "number": 2,
                        "changed_files": 1,
                        "additions": 5,
                        "deletions": 0,
                    },
                },
            },
        ]
        filter = EventFilter(enable_open_prs=True)  # type: ignore[call-arg]

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 1

    def test_filter_candidates_excludes_open_prs_when_disabled(self):
        """测试：enable_open_prs=False 时排除 open PR"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 1,
                        "changed_files": 10,
                        "additions": 200,
                        "deletions": 50,
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "closed",
                    "pull_request": {
                        "state": "closed",
                        "merged": True,  # 已合并的 PR 应包含
                        "number": 2,
                    },
                },
            },
        ]
        filter = EventFilter(enable_open_prs=False)  # type: ignore[call-arg]

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 2

    def test_filter_candidates_open_pr_min_changes_threshold(self):
        """测试：open PR 需要满足最小改动阈值"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 1,
                        "changed_files": 1,  # 文件太少
                        "additions": 10,
                        "deletions": 5,
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 2,
                        "changed_files": 5,  # 满足条件
                        "additions": 100,
                        "deletions": 30,
                    },
                },
            },
        ]
        filter = EventFilter(enable_open_prs=True, open_pr_min_changed_files=3)  # type: ignore[call-arg]

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 2

    def test_filter_candidates_open_pr_label_priority(self):
        """测试：带候选标签的 open PR 优先通过"""
        # Arrange
        events = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 1,
                        "changed_files": 5,
                        "additions": 50,
                        "deletions": 10,
                        "labels": [{"name": "feature"}],  # 有候选标签
                    },
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "anthropics/skills"},
                "payload": {
                    "action": "opened",
                    "pull_request": {
                        "state": "open",
                        "merged": False,
                        "draft": False,
                        "number": 2,
                        "changed_files": 5,
                        "additions": 50,
                        "deletions": 10,
                        "labels": [{"name": "misc"}],  # 无候选标签
                    },
                },
            },
        ]
        filter = EventFilter(enable_open_prs=True, labels=["feature"])  # type: ignore[call-arg]

        # Act
        candidates = filter.filter_candidates(events)

        # Assert
        assert len(candidates) == 1
        assert candidates[0]["payload"]["pull_request"]["number"] == 1
