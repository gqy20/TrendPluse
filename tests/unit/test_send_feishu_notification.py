"""测试飞书通知脚本的辅助函数"""


class TestFindReportJson:
    """测试报告 JSON 文件查找功能"""

    def test_find_json_in_reports_daily_directory(self, tmp_path, monkeypatch):
        """测试：在 reports/daily 目录中找到 JSON 文件"""
        # Arrange
        report_date = "2026-01-05"
        reports_daily_dir = tmp_path / "reports" / "daily"
        reports_daily_dir.mkdir(parents=True)
        json_file = reports_daily_dir / f"report-{report_date}.json"
        json_file.write_text('{"date": "2026-01-05"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from trendpluse.app.feishu_notifications import find_daily_report_json

        result = find_daily_report_json(report_date)

        # Assert
        assert result == json_file
        assert result.exists()

    def test_find_json_returns_none_when_not_found(self, tmp_path, monkeypatch):
        """测试：文件不存在时返回 None"""
        # Arrange
        report_date = "2026-01-05"
        monkeypatch.chdir(tmp_path)

        # Act
        from trendpluse.app.feishu_notifications import find_daily_report_json

        result = find_daily_report_json(report_date)

        # Assert
        assert result is None

    def test_find_latest_daily_report_json(self, tmp_path, monkeypatch):
        """测试：空日期时应找到最新日报。"""
        reports_daily_dir = tmp_path / "reports" / "daily"
        reports_daily_dir.mkdir(parents=True)
        older_file = reports_daily_dir / "report-2026-03-05.json"
        latest_file = reports_daily_dir / "report-2026-03-06.json"
        older_file.write_text("{}", encoding="utf-8")
        latest_file.write_text("{}", encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        from trendpluse.app.feishu_notifications import find_latest_daily_report_json

        result = find_latest_daily_report_json()

        assert result is not None
        assert result.resolve() == latest_file.resolve()


class TestResolveReportDate:
    """测试日报日期解析。"""

    def test_resolve_report_date_uses_value_when_present(self):
        """测试：显式日期应原样返回。"""
        from trendpluse.cli.send_feishu_notification import resolve_report_date

        assert resolve_report_date("2026-03-06") == "2026-03-06"

    def test_resolve_report_date_returns_none_for_empty_value(self):
        """测试：空值应返回 None，由调用方决定默认策略。"""
        from trendpluse.cli.send_feishu_notification import resolve_report_date

        assert resolve_report_date("") is None


class TestWeeklyNotificationHelpers:
    """测试周报通知辅助。"""

    def test_build_weekly_notification_content(self):
        """测试：生成周报通知正文。"""
        from trendpluse.app.feishu_notifications import (
            build_weekly_notification_content,
        )
        from trendpluse.models.signal import WeeklyReport

        report = WeeklyReport(
            week_id="2026-W10",
            start_date="2026-03-02",
            end_date="2026-03-08",
            summary_brief="本周聚焦 SDK 与 Agent 编排。",
            core_trends=[
                {
                    "title": "SDK",
                    "theme": "tooling",
                    "description": "SDK 迭代明显",
                    "signal_ids": [],
                    "impact_level": 4,
                },
                {
                    "title": "Agent",
                    "theme": "architecture",
                    "description": "Agent 编排活跃",
                    "signal_ids": [],
                    "impact_level": 4,
                },
            ],
            engineering_signals=[],
            research_signals=[],
            daily_reports_count=7,
            total_prs_analyzed=12,
            high_impact_signals=3,
            total_commits=20,
            total_releases=2,
        )

        content = build_weekly_notification_content(report)

        assert "2026-03-02 ~ 2026-03-08" in content
        assert "本周聚焦 SDK 与 Agent 编排。" in content
        assert "日报天数: 7" in content

    def test_build_weekly_notification_url(self):
        """测试：生成周报通知链接。"""
        from trendpluse.app.feishu_notifications import build_weekly_notification_url
        from trendpluse.models.signal import WeeklyReport

        report = WeeklyReport(
            week_id="2026-W10",
            start_date="2026-03-02",
            end_date="2026-03-08",
            summary_brief="摘要",
            core_trends=[],
            engineering_signals=[],
            research_signals=[],
            daily_reports_count=7,
            total_prs_analyzed=12,
            high_impact_signals=3,
            total_commits=20,
            total_releases=2,
        )

        url = build_weekly_notification_url(report)

        assert url.endswith("/weekly-2026-W10/")
