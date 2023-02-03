#!/usr/bin/env python3
""" encrypt_password.py """

import bcrypt


def hash_password(password: str) -> bytes:
    """ return a password hashed with bcrypt """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password is valid
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
