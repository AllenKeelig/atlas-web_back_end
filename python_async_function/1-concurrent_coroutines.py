#!/usr/bin/env python3
"""
 async routine called wait_n that takes in 2 int arguments
"""


from typing import List
import asyncio
import importlib
wait_random = getattr(importlib.import_module("0-basic_async_syntax"),
                      "wait_random")


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 int arguments n and max_delay and spawns wait_random"""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for task in asyncio.as_completed(delays):
        completed_delays.append(await task)

    return completed_delays
