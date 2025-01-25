#!/usr/bin/env python3
""" Regex-ing """
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """returns the log message obfuscated"""
    pattern = f"({'|'.join((field) for field in fields)})=.+?{separator}"
    return re.sub(
        pattern,
        lambda match: f"{match.group(1)}={redaction}{separator}",
        message)
