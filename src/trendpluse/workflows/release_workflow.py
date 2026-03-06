"""Release 工作流服务。"""

from trendpluse.app.release_processor import (  # noqa: F401
    ReleaseProcessor,
    ReleaseWorkflowResult,
)


class ReleaseWorkflowService(ReleaseProcessor):
    """兼容旧命名的 release 工作流服务。"""
