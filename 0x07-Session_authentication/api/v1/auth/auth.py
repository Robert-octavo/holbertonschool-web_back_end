#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p[-1] != '/':
                p += '/'
            if p == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None

    def session_cookie(self, request=None):
        """session_cookie method"""
        if request is None:
            return None
        session_id = getenv('SESSION_NAME')
        return request.cookies.get(session_id)
