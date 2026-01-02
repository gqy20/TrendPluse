"""项目质量检查脚本。

运行所有代码质量检查工具和测试。
"""

import subprocess
import sys


def run_command(cmd: list[str], description: str) -> int:
    """运行命令并返回退出码。

    Args:
        cmd: 要运行的命令列表
        description: 命令描述

    Returns:
        命令的退出码
    """
    print(f"\n{'=' * 60}")
    print(f"运行: {description}")
    print(f"命令: {' '.join(cmd)}")
    print(f"{'=' * 60}\n")

    result = subprocess.run(cmd)
    return result.returncode


def main():
    checks = [
        (["ruff", "check", "."], "Ruff 代码检查"),
        (["ruff", "format", "--check", "."], "Ruff 格式检查"),
        (["pytest", "-v"], "运行测试"),
    ]

    failed = []

    for cmd, description in checks:
        if run_command(cmd, description) != 0:
            failed.append(description)

    if failed:
        print(f"\n{'!' * 60}")
        print("失败的检查:")
        for check in failed:
            print(f"  ✗ {check}")
        print(f"{'!' * 60}\n")
        sys.exit(1)
    else:
        print(f"\n{'✓' * 60}")
        print("所有检查通过！")
        print(f"{'✓' * 60}\n")


if __name__ == "__main__":
    main()
