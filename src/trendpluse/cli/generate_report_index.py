"""生成报告索引命令入口。"""

import argparse
from pathlib import Path

from trendpluse.app.generate_report_index import run_generate_report_index


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="生成报告索引并同步文档")
    parser.parse_args()
    run_generate_report_index(Path.cwd().resolve())


if __name__ == "__main__":
    main()
