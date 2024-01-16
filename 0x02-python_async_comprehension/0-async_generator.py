#!/usr/bin/env python3
"""async generator"""

import random
import asyncio


async def async_generator():
    """loop 10 times, wait 1 sec and yield a rand(0-10)"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
