#!/usr/bin/env python3
"""
101-safely_get_value.py
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Takes a dictionary, a key, and an optional default value
    if the key exists in the dictionary, it returns the associated value
    otherwise, it returns the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
