#!/usr/bin/env python3
"""
    make multiplier
"""


def make_multiplier(multiplier: float) -> float:
    """
    return the multiplier and square of floate
    """
    def multiplier(n: float):
        return n**2, multiplier
