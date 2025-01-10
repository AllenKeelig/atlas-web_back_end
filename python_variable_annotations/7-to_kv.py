#!/usr/bin/env python3
"""type-annotated function to_kv that takes a string k and an int/float v"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes string k and int/float v as arguments and returns tuple"""
    return k, float(v ** 2)
