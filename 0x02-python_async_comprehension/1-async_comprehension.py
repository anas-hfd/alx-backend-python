#!/usr/bin/env python3
""""async comprehension"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers from last task"""
    return [i async for i in async_generator()]
