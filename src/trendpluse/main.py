"""trendpluse 应用程序的主入口"""

from rich.panel import Panel
from rich.table import Table

from trendpluse.core import add, greet
from trendpluse.logger import console, logger, print_header, print_success


def demo_basic_features() -> None:
    """演示基本功能"""
    print_header("基本功能演示")

    # 测试问候函数
    message = greet("Python 开发者")
    print_success(f"问候: {message}")

    # 测试加法函数
    result = add(10, 20)
    print_success(f"加法: 10 + 20 = {result}")


def demo_rich_output() -> None:
    """演示 Rich 格式化功能"""
    print_header("Rich 输出演示")

    # 创建表格
    table = Table(title="功能对比")
    table.add_column("功能", style="cyan", no_wrap=True)
    table.add_column("状态", style="magenta")
    table.add_column("描述", style="green")

    table.add_row("日志", "✓", "Rich 格式化日志，支持文件输出")
    table.add_row("测试", "✓", "pytest，100% 覆盖率")
    table.add_row("代码检查", "✓", "ruff")
    table.add_row("CI/CD", "✓", "GitHub Actions 自动化")

    console.print(table)


def demo_logging() -> None:
    """演示日志功能"""
    print_header("日志演示")

    logger.debug("这是一条调试消息")
    logger.info("这是一条信息消息")
    logger.warning("这是一条警告消息")
    logger.error("这是一条错误消息")

    console.print(
        Panel(
            "[bold green]日志已保存到 logs/trendpluse.log[/bold green]",
            title="日志文件位置",
            border_style="blue",
        )
    )


def main() -> None:
    """运行主程序"""
    console.print(
        Panel.fit(
            "[bold cyan]TrendPluse[/bold cyan] - ",
            border_style="cyan",
        )
    )

    logger.info("应用程序已启动")

    try:
        demo_basic_features()
        demo_rich_output()
        demo_logging()

        logger.info("应用程序成功完成")
        print_success("所有演示已完成！")

    except Exception as e:
        logger.error(f"应用程序错误: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
