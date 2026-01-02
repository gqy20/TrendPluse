"""日志模块 - Rich 格式化支持"""

import logging
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install as install_rich_traceback

install_rich_traceback(show_locals=True)

console = Console()


class LoggerConfig:
    """日志系统配置类"""

    DEFAULT_LOG_DIR = Path("logs")
    DEFAULT_LOG_FILE = "trendpluse.log"
    DEFAULT_LEVEL = logging.INFO
    DEFAULT_FORMAT = "%(message)s"
    FILE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def setup_logger(
    name: str = "trendpluse",
    level: int = LoggerConfig.DEFAULT_LEVEL,
    log_to_file: bool = True,
    log_dir: Path | None = None,
    log_file: str | None = None,
) -> logging.Logger:
    """
    设置带有 Rich 格式化和可选文件输出的日志记录器

    参数:
        name: 日志记录器名称
        level: 日志级别 (例如: logging.INFO, logging.DEBUG)
        log_to_file: 是否记录到文件
        log_dir: 日志文件目录，默认为 'logs/'
        log_file: 日志文件名，默认为 'trendpluse.log'

    返回:
        配置好的日志记录器实例

    示例:
        >>> logger = setup_logger("my_module", level=logging.DEBUG)
        >>> logger.info("应用程序已启动")
        >>> logger.debug("调试信息")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.handlers.clear()

    console_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
    )
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(LoggerConfig.DEFAULT_FORMAT))
    logger.addHandler(console_handler)

    if log_to_file:
        log_dir = log_dir or LoggerConfig.DEFAULT_LOG_DIR
        log_file = log_file or LoggerConfig.DEFAULT_LOG_FILE
        log_path = log_dir / log_file

        log_dir.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(LoggerConfig.FILE_FORMAT))
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str = "trendpluse") -> logging.Logger:
    """
    获取或创建日志记录器实例

    参数:
        name: 日志记录器名称

    返回:
        日志记录器实例

    示例:
        >>> logger = get_logger(__name__)
        >>> logger.info("模块已加载")
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name)
    return logger


logger = setup_logger()


def debug(message: str, **kwargs) -> None:
    logger.debug(message, **kwargs)


def info(message: str, **kwargs) -> None:
    logger.info(message, **kwargs)


def warning(message: str, **kwargs) -> None:
    logger.warning(message, **kwargs)


def error(message: str, **kwargs) -> None:
    logger.error(message, **kwargs)


def critical(message: str, **kwargs) -> None:
    logger.critical(message, **kwargs)


def print_success(message: str) -> None:
    console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message: str) -> None:
    console.print(f"[bold red]✗[/bold red] {message}")


def print_warning(message: str) -> None:
    console.print(f"[bold yellow]⚠[/bold yellow] {message}")


def print_info(message: str) -> None:
    console.print(f"[bold blue]ℹ[/bold blue] {message}")


def print_header(message: str) -> None:
    console.print(f"\n[bold cyan]{message}[/bold cyan]")
    console.print("[cyan]" + "=" * len(message) + "[/cyan]")


def print_section(message: str) -> None:
    console.print(f"\n[bold]{message}[/bold]")
