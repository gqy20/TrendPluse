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
                    }
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
                    }
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
                    }
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
                    }
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
                    }
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
                    }
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
