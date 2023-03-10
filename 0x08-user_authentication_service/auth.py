#!/usr/bin/env python3
"""Auth module"""

from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    if not password:
        return None
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a UUID"""
    return str(uuid.uuid4())


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
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_password = _hash_password(password)
            new_user = self._db.add_user(email, hash_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login"""
        encoded = password.encode('utf-8')
        try:
            user = self._db.find_user_by(email=email)
            password = _hash_password(user.hashed_password)
            if bcrypt.checkpw(encoded, password):
                return True
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session"""
        try:
            if email is None or email == "":
                return None
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Returns a user"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session"""
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a token"""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return user.reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates the password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if not user:
                raise ValueError
            hash_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hash_password,
                                 reset_token=None)
        except Exception:
            raise ValueError
