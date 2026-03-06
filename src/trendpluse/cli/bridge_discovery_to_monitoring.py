"""discovery 桥接命令入口。"""

from trendpluse.automation.bridge_discovery_to_monitoring import (
    main as automation_main,
)


def main() -> int:
    """委托到 automation 实现。"""
    return automation_main()


if __name__ == "__main__":
    raise SystemExit(main())
