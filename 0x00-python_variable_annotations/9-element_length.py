#!/usr/bin/env python3
"""
     duck type an iterable object
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    return  duck type an iterable object
    """
    return [(i, len(i)) for i in lst]
