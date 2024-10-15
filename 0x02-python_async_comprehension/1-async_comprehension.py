#!/usr/bin/env python3
"""
    generates a list of float
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    returning a list of number
    """
    return [num async for num in async_generator()]
