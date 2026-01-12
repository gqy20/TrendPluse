"""并行采集辅助模块

提供线程池执行的并行采集功能，用于加速 GitHub API 调用。
"""

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any


def parallel_map[T](
    func: Callable[..., T],
    items: list[Any],
    max_workers: int | None = None,
    *args,
    **kwargs,
) -> list[T]:
    """并行执行函数并收集结果

    Args:
        func: 要执行的函数
        items: 要处理的项目列表
        max_workers: 最大线程数（默认为 min(32, len(items) + 4)）
        *args, **kwargs: 传递给 func 的额外参数

    Returns:
        结果列表，顺序与输入 items 一致
    """
    if not items:
        return []

    # 默认线程数：参考 ThreadPoolExecutor 的默认值
    if max_workers is None:
        max_workers = min(32, len(items) + 4)

    results: dict[int, T] = {}
    errors: list[tuple[int, Exception]] = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_index = {}
        for index, item in enumerate(items):
            future = executor.submit(func, item, *args, **kwargs)
            future_to_index[future] = index

        # 收集结果
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                results[index] = future.result()
            except Exception as e:
                # 记录错误但继续处理其他任务
                errors.append((index, e))

    # 如果有错误，打印出来
    for index, error in errors:
        print(f"处理项目 {items[index] if index < len(items) else index} 失败: {error}")

    # 返回结果（按原始顺序）
    sorted_results = [results[i] for i in sorted(results.keys())]
    return sorted_results


def parallel_execute[T](
    func: Callable[..., T],
    items: list[Any],
    max_workers: int | None = None,
    ignore_errors: bool = True,
) -> list[T]:
    """并行执行函数，忽略错误的任务

    Args:
        func: 接受单个参数的函数
        items: 参数列表
        max_workers: 最大线程数
        ignore_errors: 是否忽略错误（默认 True）

    Returns:
        成功执行的结果列表
    """
    if not items:
        return []

    if max_workers is None:
        max_workers = min(32, len(items) + 4)

    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(func, item): item for item in items}

        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                if not ignore_errors:
                    raise
                item = futures[future]
                print(f"处理失败: {item}, 错误: {e}")

    return results
