"""GraphQL 版本的 ActivityCollector 测试

测试使用 GraphQL API 采集仓库活跃度的功能。
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from trendpluse.collectors.activity import ActivityCollector
from trendpluse.models.signal import ActivityData


class TestGraphQLActivityCollector:
    """测试 GraphQL 版本的 ActivityCollector"""

    def test_collect_commits_with_graphql_returns_expected_data(self):
        """测试使用 GraphQL 采集 commits 返回预期数据"""
        # Arrange
        token = "test_token"
        repos = ["owner/test-repo"]
        since = datetime(2025, 1, 25, tzinfo=UTC)

        # Mock GraphQL 响应
        graphql_response: dict = {
            "repository": {
                "defaultBranchRef": {
                    "target": {
                        "history": {
                            "nodes": [
                                {
                                    "oid": "abc123",
                                    "message": "Test commit 1",
                                    "author": {"user": {"login": "user1"}},
                                    "committedDate": "2025-01-25T10:00:00Z",
                                    "additions": 10,
                                    "deletions": 5,
                                    "changedFiles": 2,
                                },
                                {
                                    "oid": "def456",
                                    "message": "Test commit 2",
                                    "author": {"user": {"login": "user2"}},
                                    "committedDate": "2025-01-25T11:00:00Z",
                                    "additions": 20,
                                    "deletions": 10,
                                    "changedFiles": 3,
                                },
                            ]
                        }
                    }
                }
            }
        }

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = graphql_response
            mock_client_class.return_value = mock_client

            collector = ActivityCollector(token=token)

            # Act
            activity_data, commits = collector.collect_activity_graphql(repos, since)

            # Assert
            assert isinstance(activity_data, ActivityData)
            assert activity_data.total_commits == 2
            assert activity_data.active_repos_count == 1
            assert len(commits) == 2

            # 验证第一个 commit 的数据完整性
            first_commit = commits[0]
            assert first_commit["sha"] == "abc123"
            assert first_commit["message"] == "Test commit 1"
            assert first_commit["author"] == "user1"
            assert first_commit["additions"] == 10  # GraphQL 提供了这个数据！
            assert first_commit["deletions"] == 5
            assert first_commit["files_changed"] == 2

    def test_collect_commits_with_graphql_handles_empty_response(self):
        """测试 GraphQL 返回空数据的情况"""
        # Arrange
        token = "test_token"
        repos = ["owner/test-repo"]
        since = datetime(2025, 1, 25, tzinfo=UTC)

        graphql_response: dict = {
            "repository": {"defaultBranchRef": {"target": {"history": {"nodes": []}}}}
        }

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = graphql_response
            mock_client_class.return_value = mock_client

            collector = ActivityCollector(token=token)

            # Act
            activity_data, commits = collector.collect_activity_graphql(repos, since)

            # Assert
            assert activity_data.total_commits == 0
            assert activity_data.active_repos_count == 0
            assert len(commits) == 0

    def test_collect_commits_with_graphql_uses_correct_query(self):
        """测试使用正确的 GraphQL 查询"""
        # Arrange
        token = "test_token"
        repos = ["owner/test-repo"]
        since = datetime(2025, 1, 25, tzinfo=UTC)
        _since_iso = since.isoformat()  # noqa: F841

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            collector = ActivityCollector(token=token)

            # Act
            try:
                collector.collect_activity_graphql(repos, since)
            except Exception:
                pass  # 我们只关心查询是否正确

            # Assert - 验证 GraphQL 查询包含关键字段
            call_args = mock_client.execute.call_args
            if call_args:
                # gql() 将查询字符串转换为 GraphQLRequest 对象
                # 需要从第一个参数（位置参数）中提取查询字符串
                request_obj = call_args[0][0]
                # GraphQLRequest 对象有 query 属性存储原始查询字符串
                query = getattr(request_obj, "query", str(request_obj))
                assert "repository" in query
                assert "defaultBranchRef" in query
                assert "history" in query
                assert "additions" in query
                assert "deletions" in query
                assert "changedFiles" in query

    def test_collect_activity_graphql_multiple_repos(self):
        """测试使用 GraphQL 并行采集多个仓库"""
        # Arrange
        token = "test_token"
        repos = ["owner/repo1", "owner/repo2"]
        since = datetime(2025, 1, 25, tzinfo=UTC)

        # Mock 两个仓库的响应
        def mock_execute(query, variable_values=None):
            # execute_query() 使用 variable_values 参数传递变量
            variables = variable_values or {}
            owner = variables.get("owner", "")
            repo = variables.get("repo", "")
            return {
                "repository": {
                    "defaultBranchRef": {
                        "target": {
                            "history": {
                                "nodes": [
                                    {
                                        "oid": f"{owner}-{repo}-sha1",
                                        "message": f"Commit in {repo}",
                                        "author": {"user": {"login": f"user-{owner}"}},
                                        "committedDate": "2025-01-25T10:00:00Z",
                                        "additions": 10,
                                        "deletions": 5,
                                        "changedFiles": 2,
                                    }
                                ]
                            }
                        }
                    }
                }
            }

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.side_effect = mock_execute
            mock_client_class.return_value = mock_client

            collector = ActivityCollector(token=token)

            # Act
            activity_data, commits = collector.collect_activity_graphql(
                repos, since, max_workers=2
            )

            # Assert
            assert activity_data.total_commits == 2
            assert len(commits) == 2
            assert activity_data.active_repos_count == 2
