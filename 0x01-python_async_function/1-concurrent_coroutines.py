#!/usr/bin/env python3
"""complex coroutines"""

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """spawns wait_random n times with max_delay"""
    spwn = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*spwn)
    return sorted(delays)
