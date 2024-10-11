#!/usr/bin/env python3
"""
    sum mixed list, int and float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    return the sum as a float
    """
    total = 0
    for i in mxd_list:
        total += i
    return total
