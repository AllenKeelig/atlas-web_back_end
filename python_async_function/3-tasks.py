#!/usr/bin/env python3
"""
Write a function task_wait_random that takes an integer max_delay
"""


import asyncio
import importlib
wait_random = getattr(importlib.import_module("0-basic_async_syntax"),
                      "wait_random")


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
