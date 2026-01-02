"""日志模块的测试用例。"""

import logging

from trendpluse.logger import (
    console,
    get_logger,
    print_error,
    print_header,
    print_info,
    print_success,
    print_warning,
    setup_logger,
)


class TestLoggerSetup:
    """日志设置功能的测试用例。"""

    def test_setup_logger_basic(self, tmp_path):
        """测试基本的日志设置。"""
        logger = setup_logger(
            name="test_logger",
            level=logging.DEBUG,
            log_to_file=True,
            log_dir=tmp_path,
            log_file="test.log",
        )

        assert logger.name == "test_logger"
        assert logger.level == logging.DEBUG
        assert len(logger.handlers) == 2  # 控制台和文件处理器

        # 检查日志文件是否已创建
        log_file = tmp_path / "test.log"
        assert log_file.exists()

    def test_setup_logger_no_file(self):
        """测试不记录文件的日志设置。"""
        logger = setup_logger(name="test_no_file", log_to_file=False)

        assert logger.name == "test_no_file"
        assert len(logger.handlers) == 1  # 只有控制台处理器

    def test_get_logger(self):
        """测试获取日志记录器实例。"""
        logger = get_logger("test_get_logger")
        assert logger.name == "test_get_logger"
        assert len(logger.handlers) > 0

    def test_logger_levels(self, tmp_path, capsys):
        """测试不同的日志级别。"""
        logger = setup_logger(
            name="test_levels",
            level=logging.DEBUG,
            log_to_file=True,
            log_dir=tmp_path,
        )

        logger.debug("调试消息")
        logger.info("信息消息")
        logger.warning("警告消息")
        logger.error("错误消息")
        logger.critical("严重消息")

        # 检查日志文件是否包含所有消息
        log_file = tmp_path / "trendpluse.log"
        content = log_file.read_text()
        assert "调试消息" in content
        assert "信息消息" in content
        assert "警告消息" in content
        assert "错误消息" in content
        assert "严重消息" in content


class TestConsoleFunctions:
    """Rich 控制台输出函数的测试用例。"""

    def test_print_success(self, capsys):
        """测试成功消息打印。"""
        print_success("测试成功")
        # 只验证不会引发错误
        # 使用 rich 格式的实际输出测试比较复杂

    def test_print_error(self):
        """测试错误消息打印。"""
        print_error("测试错误")

    def test_print_warning(self):
        """测试警告消息打印。"""
        print_warning("测试警告")

    def test_print_info(self):
        """测试信息消息打印。"""
        print_info("测试信息")

    def test_print_header(self):
        """测试标题打印。"""
        print_header("测试标题")

    def test_console_instance(self):
        """测试控制台实例是否可用。"""
        assert console is not None
        assert hasattr(console, "print")


class TestLoggerIntegration:
    """日志模块的集成测试。"""

    def test_logger_with_exception(self, tmp_path):
        """测试记录异常信息。"""
        logger = setup_logger(
            name="test_exception", log_dir=tmp_path, log_file="exception.log"
        )

        try:
            raise ValueError("测试异常")
        except ValueError:
            logger.error("发生错误", exc_info=True)

        log_file = tmp_path / "exception.log"
        content = log_file.read_text()
        assert "发生错误" in content
        assert "ValueError" in content

    def test_multiple_loggers(self, tmp_path):
        """测试创建多个独立的日志记录器。"""
        logger1 = setup_logger(name="logger1", log_dir=tmp_path, log_file="log1.log")
        logger2 = setup_logger(name="logger2", log_dir=tmp_path, log_file="log2.log")

        logger1.info("来自 logger1 的消息")
        logger2.info("来自 logger2 的消息")

        log1_content = (tmp_path / "log1.log").read_text()
        log2_content = (tmp_path / "log2.log").read_text()

        assert "来自 logger1 的消息" in log1_content
        assert "来自 logger2 的消息" in log2_content
