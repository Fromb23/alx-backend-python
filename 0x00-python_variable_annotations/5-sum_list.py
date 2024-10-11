#!/usr/bin/python3
"""
    annotation of a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum a list then returns a float
    """
    total = 0
    for i in input_list:
        total += i
    return total
