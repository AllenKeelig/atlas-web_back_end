#!/usr/bin/env python3
"""
Authentication class for the API
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class that handles the authentication methods."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required for a path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user from the request."""
        return None
