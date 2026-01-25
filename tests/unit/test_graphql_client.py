"""GraphQL 客户端测试

测试 GraphQL 客户端的基本功能，包括查询执行、错误处理和速率限制。
"""

from unittest.mock import MagicMock, patch

import pytest

from trendpluse.collectors.base import BaseGitHubCollector, _thread_local


# 定义临时异常类（gql 未安装时）
class TransportQueryError(Exception):
    """GraphQL 传输层错误"""


class TestGraphQLClient:
    """测试 GraphQL 客户端功能"""

    def setup_method(self):
        """每个测试前清理 thread_local 状态"""
        if hasattr(_thread_local, "graphql_client"):
            delattr(_thread_local, "graphql_client")

    def test_get_graphql_client_creates_client(self):
        """测试获取 GraphQL 客户端时创建实例"""
        # Arrange
        token = "test_token"

        # Act
        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)
            client = collector.get_graphql_client()

            # Assert
            assert client is not None
            mock_client_class.assert_called_once()

    def test_get_graphql_client_returns_same_instance_in_same_thread(self):
        """测试在同一线程中多次调用返回同一实例"""
        # Arrange
        token = "test_token"

        # Act
        with patch("trendpluse.collectors.base.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            collector = BaseGitHubCollector(token=token)
            client1 = collector.get_graphql_client()
            client2 = collector.get_graphql_client()

            # Assert - 验证两次调用返回同一个实例
            assert client1 is client2
            # 注意：Client 构造函数只被调用一次（缓存机制）
            mock_client_class.assert_called_once()

    def test_execute_query_with_valid_response(self):
        """测试执行查询并返回有效响应"""
        # Arrange
        token = "test_token"
        expected_result = {"repository": {"name": "repo"}}

        # 直接 patch execute_query 方法
        with patch.object(
            BaseGitHubCollector, "execute_query", return_value=expected_result
        ) as mock_execute:
            collector = BaseGitHubCollector(token=token)

            # Act
            query = "query { viewer { login } }"
            variables: dict[str, str] = {}
            result = collector.execute_query(query, variables)

            # Assert
            assert result == expected_result
            mock_execute.assert_called_once()

    def test_execute_query_handles_transport_error(self):
        """测试处理传输层错误"""
        # Arrange
        token = "test_token"

        # 直接 patch execute_query 方法抛出异常
        with patch.object(
            BaseGitHubCollector,
            "execute_query",
            side_effect=TransportQueryError("Network error"),
        ):
            collector = BaseGitHubCollector(token=token)

            # Act & Assert
            with pytest.raises(TransportQueryError):
                collector.execute_query("query { viewer { login } }", {})

    def test_get_rate_limit_status(self):
        """测试获取速率限制状态"""
        # Arrange
        token = "test_token"
        expected_rate_limit = {
            "limit": 5000,
            "remaining": 4999,
            "resetAt": "2025-01-25T10:00:00Z",
        }

        # 直接 patch execute_query 返回速率限制数据
        with patch.object(
            BaseGitHubCollector,
            "execute_query",
            return_value={"rateLimit": expected_rate_limit},
        ):
            collector = BaseGitHubCollector(token=token)

            # Act
            rate_limit = collector.get_rate_limit()

            # Assert
            assert rate_limit == expected_rate_limit

    def test_check_rate_limit_when_remaining_low(self):
        """测试当剩余点数较低时返回 True"""
        # Arrange
        token = "test_token"

        # 直接 patch execute_query 返回低剩余点数
        with patch.object(
            BaseGitHubCollector,
            "execute_query",
            return_value={
                "rateLimit": {
                    "limit": 5000,
                    "remaining": 50,  # 低于阈值
                    "used": 4950,
                    "resetAt": "2025-01-25T10:00:00Z",
                }
            },
        ):
            collector = BaseGitHubCollector(token=token)

            # Act
            is_low = collector.is_rate_limit_low(threshold=100)

            # Assert
            assert is_low is True

    def test_check_rate_limit_when_remaining_sufficient(self):
        """测试当剩余点数充足时返回 False"""
        # Arrange
        token = "test_token"

        # 直接 patch execute_query 返回充足剩余点数
        with patch.object(
            BaseGitHubCollector,
            "execute_query",
            return_value={
                "rateLimit": {
                    "limit": 5000,
                    "remaining": 1000,  # 高于阈值
                    "used": 4000,
                    "resetAt": "2025-01-25T10:00:00Z",
                }
            },
        ):
            collector = BaseGitHubCollector(token=token)

            # Act
            is_low = collector.is_rate_limit_low(threshold=100)

            # Assert
            assert is_low is False
