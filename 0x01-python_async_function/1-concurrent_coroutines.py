#!/usr/bin/env python3
"""complex coroutines"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with max_delay"""
    spwn = []
    for _ in range(n):
        spwn.append(asyncio.create_task(wait_random(max_delay)))
        delays = await asyncio.gather(*spwn)
    return sorted(delays)
