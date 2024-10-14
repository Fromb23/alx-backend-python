#!/usr/bin/env python3
"""
    min delays
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n return a list of min delays
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    ordered_delays = []

    while delays:
        min_delay = min(delays)
        ordered_delays.append(min_delay)
        delays.remove(min_delay)

    return ordered_delays
