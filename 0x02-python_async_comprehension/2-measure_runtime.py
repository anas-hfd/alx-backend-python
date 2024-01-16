#!/usr/bin/env python3
""" measure runtime"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """parallel comprehensions"""
    start = time()
    comp_loop = [async_comprehension for i in range(4)]
    await asyncio.gather(*comp_loop)
    end = time()
    return end - start
