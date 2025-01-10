#!/usr/bin/env python3
"""
 measure_time function with integers n and max_delay
"""


import asyncio
from time import perf_counter
import importlib
wait_n = getattr(importlib.import_module("1-concurrent_coroutines"),
                 "wait_n")


def measure_time(n: int, max_delay: int) -> float:
    """takes integers n and max_delay and mesures total execution time for wait_n"""
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start_time
    return total_time / n
