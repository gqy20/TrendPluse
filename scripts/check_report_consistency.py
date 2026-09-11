"""报告文件一致性校验。

规则：reports/daily 与 reports/weekly 中，有 JSON 必有同名 MD
（JSON 是机器真源，MD 是派生视图，缺 MD 说明渲染层断链）。
仅有 MD 无 JSON 允许存在（历史孤儿），但会列出供人工核对。

用法::

    uv run python scripts/check_report_consistency.py [--reports-dir reports]

退出码：0 通过；1 存在缺 MD 的 JSON。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def check_consistency(reports_dir: Path) -> tuple[list[str], list[str]]:
    """校验 daily/weekly 报告的 JSON 与 MD 配对。

    Returns:
        (missing_md, orphan_md) 元组：缺 MD 的 JSON 列表与仅有 MD 的日期列表。
    """
    missing_md: list[str] = []
    orphan_md: list[str] = []

    for sub in ("daily", "weekly"):
        sub_dir = reports_dir / sub
        if not sub_dir.is_dir():
            continue
        jsons = {p.stem for p in sub_dir.glob("*.json")}
        mds = {p.stem for p in sub_dir.glob("*.md")}
        for stem in sorted(jsons - mds):
            missing_md.append(f"{sub}/{stem}")
        for stem in sorted(mds - jsons):
            orphan_md.append(f"{sub}/{stem}")

    return missing_md, orphan_md


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reports-dir", type=Path, default=Path("reports"), help="报告根目录"
    )
    args = parser.parse_args()

    missing_md, orphan_md = check_consistency(args.reports_dir)

    if missing_md:
        print(f"[FAIL] 以下 {len(missing_md)} 个 JSON 缺少同名 MD：")
        for name in missing_md:
            print(f"  - {name}")
    if orphan_md:
        print(
            f"[WARN] 以下 {len(orphan_md)} 个 MD 无对应 JSON（历史孤儿，请人工核对）："
        )
        for name in orphan_md:
            print(f"  - {name}")

    if missing_md:
        return 1
    if not orphan_md:
        print("[OK] 报告文件一致性校验通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
