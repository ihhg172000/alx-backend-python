#!/usr/bin/env python3
"""
5-sum_list.py
"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument
    and returns their sum as a float
    """
    return reduce(lambda a, n: a + n, input_list)
