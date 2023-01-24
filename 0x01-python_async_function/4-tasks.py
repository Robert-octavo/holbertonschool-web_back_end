#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        list: [description]
    """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
