#!/usr/bin/env python3
"""
    takes a str, then a float/int
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple with a string and float, then get
    the square of the float
    """
    return (k, float(v) ** 2)
