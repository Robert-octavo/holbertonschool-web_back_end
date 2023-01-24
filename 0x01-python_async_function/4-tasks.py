#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same
time with async
"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        list: [description]
    """
    return await asyncio.create_task(wait_n(n, max_delay))
