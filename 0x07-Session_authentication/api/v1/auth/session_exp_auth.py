#!/usr/bin/env python3
""" Module of Session Authentication views"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
import datetime


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """Constructor"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_id = self.user_id_by_session_id[session_id]
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """User id for session"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if self.user_id_by_session_id[session_id]['created_at']:
            return None
        expire_time = self.user_id_by_session_id[session_id]['created_at'] + \
            datetime.timedelta(seconds=self.session_duration)
        if expire_time < datetime.now():
            return None
        return self.user_id_by_session_id[session_id]['user_id']
