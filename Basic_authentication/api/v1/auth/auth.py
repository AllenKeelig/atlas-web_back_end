#!/usr/bin/env python3
"""
Authentication class for the API
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class that handles the authentication methods."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a path."""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        normalized_path = path.rstrip('/')
        for excluded in excluded_paths:
            if normalized_path == excluded.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header."""
        if request is None:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user from the request."""
        return None
