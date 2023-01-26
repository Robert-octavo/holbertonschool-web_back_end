#!/usr/bin/env python3

"""Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The function will measure the total runtime and return
    it. Notice that the total runtime is roughly 10 seconds,
    explain it to yourself."""
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return end - start

if __name__ == '__main__':
    print(asyncio.run(measure_runtime()))
