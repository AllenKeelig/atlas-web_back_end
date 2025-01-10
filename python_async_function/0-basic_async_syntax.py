#!/usr/bin/env python3
"""
 asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in an integer argument named wait_random
    that waits for a random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
