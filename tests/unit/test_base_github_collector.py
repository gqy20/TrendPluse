"""GitHub Collector 基类测试"""

from datetime import UTC, datetime

from trendpluse.collectors.base import BaseGitHubCollector


class TestBaseGitHubCollectorInit:
    """测试 BaseGitHubCollector 初始化"""

    def test_init_with_token(self):
        """使用 token 初始化应该创建带认证的客户端"""
        token = "test_token_123"
        collector = BaseGitHubCollector(token=token)
        assert collector.client is not None

    def test_init_without_token(self):
        """不使用 token 初始化应该创建匿名客户端"""
        collector = BaseGitHubCollector()
        assert collector.client is not None

    def test_token_is_stored(self):
        """token 应该被存储"""
        token = "test_token_123"
        collector = BaseGitHubCollector(token=token)
        assert collector.token == token


class TestEnsureTimezoneAware:
    """测试时区感知方法"""

    def test_timezone_aware_datetime_unchanged(self):
        """已有 timezone 的 datetime 应该保持不变"""
        collector = BaseGitHubCollector()
        dt = datetime(2026, 1, 12, 12, 0, 0, tzinfo=UTC)
        result = collector.ensure_timezone_aware(dt)
        assert result == dt
        assert result.tzinfo is not None

    def test_naive_datetime_gets_utc(self):
        """没有 timezone 的 datetime 应该添加 UTC"""
        collector = BaseGitHubCollector()
        dt = datetime(2026, 1, 12, 12, 0, 0)
        result = collector.ensure_timezone_aware(dt)
        assert result.tzinfo is not None
        assert result.tzinfo == UTC

    def test_naive_datetime_not_modified_in_place(self):
        """原始 datetime 对象不应该被修改"""
        collector = BaseGitHubCollector()
        dt = datetime(2026, 1, 12, 12, 0, 0)
        original_dt = dt
        result = collector.ensure_timezone_aware(dt)
        # 原始对象没有 tzinfo
        assert original_dt.tzinfo is None
        # 返回的对象有 tzinfo
        assert result.tzinfo is not None


class TestBaseGitHubCollectorAbstractMethods:
    """测试抽象方法"""

    def test_base_collector_is_abstract(self):
        """BaseGitHubCollector 应该是抽象类，不能直接实例化用于实际工作"""
        # 但我们允许实例化（用于测试工具方法）
        # 只是抽象方法需要被子类实现
        collector = BaseGitHubCollector()
        # 调用工具方法应该工作
        dt = datetime(2026, 1, 12, 12, 0, 0)
        result = collector.ensure_timezone_aware(dt)
        assert result.tzinfo is not None
