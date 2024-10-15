#!/usr/bin/env python3
"""
    measure time difference
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    return the time difference
    """
    start_time = time.time()
    await asyncio.gather(
                        async_comprehension(), async_comprehension(),
                        async_comprehension(), async_comprehension()
                        )
    end_time = time.time()

    return end_time - start_time
