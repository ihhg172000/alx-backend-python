#!/usr/bin/env python3
"""
8-make_multiplier.py
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    That takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    """
    def multiplier_callable(n: float) -> float:
        return n * multiplier
    return multiplier_callable
