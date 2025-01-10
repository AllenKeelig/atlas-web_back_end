#!/usr/bin/env python3
"""
 asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
"""


from typing import List
from 0-basic_async_syntax import wait_random
import asyncio

async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 int arguments n and max_delay and spawns wait_random"""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for task in asyncio.as_completed(delays):
        completed_delays.append(await task)

    return completed_delays
