"""GraphQL 客户端测试

测试 GraphQL 客户端的基本功能，包括查询执行、错误处理和速率限制。
"""

from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.base import BaseGitHubCollector


# 定义临时异常类（gql 未安装时）
class TransportQueryError(Exception):
    """GraphQL 传输层错误"""


class TestGraphQLClient:
    """测试 GraphQL 客户端功能"""

    def test_init_creates_graphql_client(self):
        """测试初始化时创建 GraphQL 客户端"""
        # Arrange
        token = "test_token"

        # Act
        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Assert
            assert hasattr(collector, "graphql_client")
            assert collector.graphql_client is not None

    def test_execute_query_with_valid_response(self):
        """测试执行查询并返回有效响应"""
        # Arrange
        token = "test_token"
        query = """
        query($owner: String!, $repo: String!) {
            repository(owner: $owner, name: $repo) {
                name
            }
        }
        """
        variables: dict[str, str] = {"owner": "test", "repo": "repo"}
        expected_result = {"repository": {"name": "repo"}}

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = expected_result
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Act
            result = collector.execute_query(query, variables)  # type: ignore[attr-defined]

            # Assert
            assert result == expected_result
            mock_client.execute.assert_called_once()

    def test_execute_query_handles_transport_error(self):
        """测试处理传输层错误"""
        # Arrange
        token = "test_token"
        query = "query { viewer { login } }"
        variables: dict[str, str] = {}

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.side_effect = TransportQueryError("Network error")
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Act & Assert
            with pytest.raises(TransportQueryError):
                collector.execute_query(query, variables)  # type: ignore[attr-defined]

    def test_get_rate_limit_status(self):
        """测试获取速率限制状态"""
        # Arrange
        token = "test_token"
        expected_rate_limit = {
            "limit": 5000,
            "remaining": 4999,
            "resetAt": "2025-01-25T10:00:00Z",
        }

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = {"rateLimit": expected_rate_limit}
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Act
            rate_limit = collector.get_rate_limit()  # type: ignore[attr-defined]

            # Assert
            assert rate_limit == expected_rate_limit

    def test_check_rate_limit_when_remaining_low(self):
        """测试当剩余点数较低时返回 True"""
        # Arrange
        token = "test_token"

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = {
                "rateLimit": {
                    "limit": 5000,
                    "remaining": 50,  # 低于阈值
                    "used": 4950,
                    "resetAt": "2025-01-25T10:00:00Z",
                }
            }
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Act
            is_low = collector.is_rate_limit_low(threshold=100)  # type: ignore[attr-defined]

            # Assert
            assert is_low is True

    def test_check_rate_limit_when_remaining_sufficient(self):
        """测试当剩余点数充足时返回 False"""
        # Arrange
        token = "test_token"

        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.execute.return_value = {
                "rateLimit": {
                    "limit": 5000,
                    "remaining": 1000,  # 高于阈值
                    "used": 4000,
                    "resetAt": "2025-01-25T10:00:00Z",
                }
            }
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)

            # Act
            is_low = collector.is_rate_limit_low(threshold=100)  # type: ignore[attr-defined]

            # Assert
            assert is_low is False
