#!/usr/bin/env python3



from typing import List
from 0_basic_async_syntax import wait_random
import asyncio

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for task in asyncio.as_completed(delays):
        delay = await task
        completed_delays.append(delay)

    return completed_delays
