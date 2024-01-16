#!/usr/bin/env python3
"""measure runtime"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ runtime for 4 funcs"""
    start = time()
    comp_loop = [async_comprehension() for i in range(4)]
    await gather(*comp_loop)
    end = time()
    return (end - start)
