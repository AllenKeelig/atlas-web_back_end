#!/usr/bin/env python3
""" Log formatter """
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        unencrypted = super().format(record)
        return filter_datum(self.fields, self.REDACTION, unencrypted, self.SEPARATOR)


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
