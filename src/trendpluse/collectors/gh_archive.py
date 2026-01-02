"""GH Archive 数据采集器

从 GH Archive 的 BigQuery 数据集获取 GitHub 事件。
"""
from datetime import datetime

from google.cloud import bigquery


class GHArchiveCollector:
    """从 GH Archive 收集数据"""

    def __init__(self):
        """初始化 BigQuery 客户端"""
        self.client = bigquery.Client()

    def fetch_events(
        self,
        repos: list[str],
        since: datetime,
    ) -> list[dict]:
        """获取指定仓库的 GitHub 事件

        Args:
            repos: 仓库列表，格式 ["owner/repo", ...]
            since: 起始时间

        Returns:
            事件列表
        """
        # 构建表名（使用 GH Archive 的日表）
        table_date = since.strftime("%Y%m%d")  # 例如：20260102
        table_id = f"githubarchive.day.{table_date}"

        # 构建 SQL 查询
        query = f"""
        SELECT
            type,
            repo.name as repo_name,
            payload,
            created_at,
        FROM
            `{table_id}`
        WHERE
            repo.name IN UNNEST(@repos)
            AND type IN ('PullRequestEvent', 'ReleaseEvent')
            AND created_at > @since
        ORDER BY created_at DESC
        """

        # 配置查询参数
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("repos", "array", repos),
                bigquery.ScalarQueryParameter(
                    "since", "timestamp", since.isoformat()
                ),
            ]
        )

        # 执行查询
        query_job = self.client.query(query, job_config=job_config)

        # 返回结果
        results = list(query_job.result())

        # 转换为统一格式
        events = []
        for row in results:
            events.append({
                "type": row.type,
                "repo": {"name": row.repo_name},
                "payload": dict(row.payload) if row.payload else {},
                "created_at": row.created_at.isoformat(),
            })

        return events
