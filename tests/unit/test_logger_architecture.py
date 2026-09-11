"""日志系统改造测试（轮转 + 单 handler 树 + 重试可见）。"""

from __future__ import annotations

import logging
import ssl
from logging.handlers import TimedRotatingFileHandler
from unittest.mock import MagicMock

import pytest

from trendpluse.logger import ROOT_LOGGER_NAME, get_logger, setup_logger
from trendpluse.utils.retry import _log_retry_attempt


@pytest.fixture
def root_propagation():
    """临时开启根 logger 冒泡，让 pytest caplog 能捕获 trendpluse 日志。"""
    root = logging.getLogger(ROOT_LOGGER_NAME)
    original = root.propagate
    root.propagate = True
    yield root
    root.propagate = original


class TestLoggerArchitecture:
    def test_root_logger_has_single_handler_tree(self):
        """根 logger 挂 console + 轮转文件两个 handler。"""
        # 显式初始化再断言:避免依赖此前测试执行顺序留下的全局 logger 状态
        # (CI 全量套件下 root logger 可能被多次重配,断言"配置后"而非"遗留"状态)
        setup_logger()
        root = get_logger(ROOT_LOGGER_NAME)
        assert len(root.handlers) == 2
        file_handlers = [
            h for h in root.handlers if isinstance(h, TimedRotatingFileHandler)
        ]
        assert len(file_handlers) == 1
        assert file_handlers[0].backupCount == 30

    def test_child_loggers_bubble_without_handlers(self):
        """子 logger 不挂 handler，冒泡到根输出（避免轮转冲突）。"""
        child = get_logger("trendpluse.collectors.activity")
        assert not child.handlers
        assert child.propagate is True
        assert child.parent is logging.getLogger(ROOT_LOGGER_NAME)

    def test_non_trendpluse_loggers_stay_independent(self):
        """非 trendpluse 系名字保持独立配置（向后兼容）。"""
        other = get_logger("test_independent_logger_xyz")
        assert len(other.handlers) > 0

    def test_child_log_record_reaches_root_handler(self, tmp_path):
        """子 logger 的日志应写入根的轮转文件。"""
        setup_logger(log_dir=tmp_path, log_file="bubble.log")
        child = logging.getLogger("trendpluse.some.module")
        child.warning("子模块冒泡测试消息")
        for h in logging.getLogger(ROOT_LOGGER_NAME).handlers:
            h.flush()
        content = (tmp_path / "bubble.log").read_text(encoding="utf-8")
        assert "子模块冒泡测试消息" in content
        assert "trendpluse.some.module" in content  # 记录来源模块名


class TestRetryLogging:
    def _make_state(self, exc: BaseException, attempt: int = 1, sleep: float = 2.0):
        state = MagicMock()
        state.attempt_number = attempt
        state.outcome.failed = True
        state.outcome.exception.return_value = exc
        state.next_action.sleep = sleep
        return state

    def test_retry_logs_exception_type(self, caplog, root_propagation):
        state = self._make_state(ssl.SSLError("UNEXPECTED_EOF"), attempt=2)
        with caplog.at_level(logging.WARNING):
            _log_retry_attempt(state)
        assert "第 2 次尝试失败" in caplog.text
        assert "SSLError" in caplog.text
        assert "2.0s 后重试" in caplog.text

    def test_retry_logs_validation_error_compactly(self, caplog, root_propagation):
        from pydantic import ValidationError

        try:
            raise ValidationError.from_exception_data(
                "Model",
                [
                    {"type": "missing", "loc": ("first_field",), "input": {}},
                    {"type": "missing", "loc": ("second_field",), "input": {}},
                ],
            )
        except ValidationError as exc:
            state = self._make_state(exc)
        with caplog.at_level(logging.WARNING):
            _log_retry_attempt(state)
        assert "ValidationError" in caplog.text
        # 只记第一个错误，不倾倒全部 errors
        assert "first_field" in caplog.text
        assert "second_field" not in caplog.text

    def test_retry_decorator_emits_log(self, caplog, root_propagation):
        """真实 tenacity 装饰器触发 before_sleep 日志。"""
        from trendpluse.utils.retry import create_github_retry_decorator

        calls = [0]

        def flaky():
            calls[0] += 1
            if calls[0] < 2:
                raise ssl.SSLError("transient")
            return "ok"

        retry_fn = create_github_retry_decorator(max_attempts=3, wait_min=0, wait_max=0)
        with caplog.at_level(logging.WARNING):
            assert retry_fn(flaky)() == "ok"
        assert "第 1 次尝试失败" in caplog.text
        assert "SSLError" in caplog.text
