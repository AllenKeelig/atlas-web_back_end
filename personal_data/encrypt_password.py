#!/usr/bin/env python3
"""returns a salted, hashed password, which is a byte string."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with a randomly generated salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the stored hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
