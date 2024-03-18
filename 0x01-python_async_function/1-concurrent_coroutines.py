#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
from typing import List
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine that takes in two integer arguments,
    spawns 'wait_random' 'n' times with the specified 'max_delay',
    and returns the list of all the delays.
    """
    delays = [random.uniform(0, max_delay) for _ in range(n)]
    delays.sort()

    for delay in delays:
        await asyncio.sleep(delay)

    return delays
