#!/usr/bin/env python3
"""type-annotated function sum_list"""


from typing import List


def sum_list(input_lists: List[float]) -> float:
    """takes a list input_list of floats and returns their sum as a float."""
    return sum(input_lists)
