#!/usr/bin/env python3
""" returns the log message obfuscated """
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    pattern = f"({'|'.join((field) for field in fields)})=.+?{separator}"
    return re.sub(pattern, lambda match: f"{match.group(1)}={redaction}{separator}", message)
