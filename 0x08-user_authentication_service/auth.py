#!/usr/bin/env python3
"""Auth module"""

from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> str:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
