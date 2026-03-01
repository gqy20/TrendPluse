"""脚本兼容壳层测试。

确保 scripts 入口仍可导入，并转发到 src 下的实现。
"""


def test_add_repo_wrapper_exports_automation_functions() -> None:
    """scripts.add_repo 应导出 automation.add_repo 的同名函数。"""
    from scripts.add_repo import add_repo_to_config as wrapped_func
    from trendpluse.automation.add_repo import add_repo_to_config as real_func

    assert wrapped_func is real_func


def test_bridge_wrapper_exports_automation_functions() -> None:
    """scripts.bridge_discovery_to_monitoring 应导出 automation 实现。"""
    from scripts.bridge_discovery_to_monitoring import (
        bridge_actionable_to_monitoring as wrapped_func,
    )
    from trendpluse.automation.bridge_discovery_to_monitoring import (
        bridge_actionable_to_monitoring as real_func,
    )

    assert wrapped_func is real_func


def test_generate_report_index_wrapper_exports_automation_functions() -> None:
    """scripts.generate_report_index 应导出 automation 实现。"""
    from scripts.generate_report_index import generate_index as wrapped_func
    from trendpluse.automation.generate_report_index import generate_index as real_func

    assert wrapped_func is real_func


def test_sync_repos_wrapper_exports_automation_functions() -> None:
    """scripts.sync_repos_to_docs 应导出 automation 实现。"""
    from scripts.sync_repos_to_docs import update_index_file as wrapped_func
    from trendpluse.automation.sync_repos_to_docs import update_index_file as real_func

    assert wrapped_func is real_func
