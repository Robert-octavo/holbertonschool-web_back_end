#!/usr/bin/env python3
"""Auth module"""

from db import DB
import bcrypt


def _hash_password(password: str) -> str:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
