#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    return reduce(lambda a, n: a + n, mxd_lst)
