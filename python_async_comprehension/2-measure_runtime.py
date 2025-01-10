#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension
"""


import asyncio
import importlib
import time
from typing import Coroutine
async_comprehension: Coroutine = getattr(
    importlib.import_module("1-async_comprehension"), "async_comprehension"
)


async def measure_runtime() -> float:
    """will execute async_comprehension four times in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
