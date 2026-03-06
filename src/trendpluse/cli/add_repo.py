"""添加仓库命令入口。"""

from trendpluse.automation.add_repo import main as automation_main


def main() -> None:
    """委托到 automation 实现。"""
    automation_main()


if __name__ == "__main__":
    main()
