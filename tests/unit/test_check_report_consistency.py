"""报告一致性校验脚本测试。"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1].parent / "scripts"))

from check_report_consistency import check_consistency  # type: ignore[import-not-found]


class TestCheckConsistency:
    def test_paired_reports_pass(self, tmp_path):
        (tmp_path / "daily").mkdir()
        (tmp_path / "daily/report-2026-01-01.json").write_text("{}")
        (tmp_path / "daily/report-2026-01-01.md").write_text("# x")
        missing, orphan = check_consistency(tmp_path)
        assert missing == []
        assert orphan == []

    def test_json_without_md_reported(self, tmp_path):
        (tmp_path / "daily").mkdir()
        (tmp_path / "daily/report-2026-01-01.json").write_text("{}")
        missing, orphan = check_consistency(tmp_path)
        assert missing == ["daily/report-2026-01-01"]
        assert orphan == []

    def test_md_without_json_is_orphan_warning(self, tmp_path):
        (tmp_path / "weekly").mkdir()
        (tmp_path / "weekly/weekly-2026-W04.md").write_text("# x")
        missing, orphan = check_consistency(tmp_path)
        assert missing == []
        assert orphan == ["weekly/weekly-2026-W04"]

    def test_missing_dirs_ok(self, tmp_path):
        missing, orphan = check_consistency(tmp_path)
        assert missing == []
        assert orphan == []
