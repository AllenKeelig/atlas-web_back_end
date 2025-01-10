#!/usr/bin/env python3
"""function takes iterable sequence"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes iterable sequence and returns sequence length"""
    return [(i, len(i)) for i in lst]
