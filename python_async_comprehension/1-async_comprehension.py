#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments.
"""


import asyncio
import importlib
from typing import List
async_generator = getattr(importlib.import_module("0-async_generator"), "async_generator")


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async comprehension"""
    result = [num async for num in async_generator()]
    return result
