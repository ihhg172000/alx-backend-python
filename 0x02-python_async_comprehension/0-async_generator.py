#!/usr/bin/env python3
"""
0-async_generator.py
"""
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, each time asynchronously wait 1 second,
    then yields a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
