#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine that takes in two integer arguments
    then spawns 'task_wait_random' 'n' times with the specified 'max_delay',
    and returns the list of all the delays.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
