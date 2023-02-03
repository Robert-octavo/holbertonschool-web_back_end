#!/urs/bin/env python3
""" Write a function that takes in a password
string and returns a salted,"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ returns hashed password, which is a byte string """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ returns True if the password is valid for the
    hashed password, otherwise it returns False """
    return bcrypt.checkpw(password.encode(), hashed_password)
