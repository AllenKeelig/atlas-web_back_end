#!/usr/bin/env python3
""" Create logger """
import re
from typing import List,
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """enact filter"""
        unencrypted = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            unencrypted,
            self.SEPARATOR)


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


def get_logger() -> logging.Logger:
    """Creates and configures the logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """
    Returns a connector to the MySQL database.

    The function retrieves database connection details from environment variables:
    - PERSONAL_DATA_DB_USERNAME: The database username (default: "root").
    - PERSONAL_DATA_DB_PASSWORD: The database password (default: an empty string).
    - PERSONAL_DATA_DB_HOST: The database host (default: "localhost").
    - PERSONAL_DATA_DB_NAME: The name of the database.

    Returns:
        MySQLConnection: A connection object to the MySQL database.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
