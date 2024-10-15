#!/usr/bin/env python3
"""
    defining async generator
"""
import random
import asyncio


async def async_generator():
    """
    returning random value in a range of 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
