#!/usr/bin/env python3
"""
Class SessionAuth
"""

from api.v1.auth.auth import Auth
from models.user import User
from os import getenv
from uuid import uuid4


class SessionAuth(Auth):
    """Session Auth Class"""
    pass
