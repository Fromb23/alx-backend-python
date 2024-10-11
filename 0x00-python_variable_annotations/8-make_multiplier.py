#!/usr/bin/env python3
"""
    make multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return the multiplier and square of floate
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier

    return multiplier_func
