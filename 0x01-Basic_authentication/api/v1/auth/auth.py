#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class that manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the given path requires authentication
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            if path == excluded_path or path + '/' == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request
        """
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request
        """
        return None
