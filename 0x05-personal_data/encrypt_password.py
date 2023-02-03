#!/urs/bin/env python3
""" Write a function that takes in a password
string and returns a salted,"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ returns hashed password, which is a byte string """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
