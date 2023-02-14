#!/usr/bin/env python3
""" Module of Session Authentication views"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id: str = None) -> str:
        """create_session method"""
        if user_id is None:
            return None
        from models.user_session import UserSession
        session_id = super().create_session(user_id)
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method"""
        if session_id is None:
            return None
        from models.user_session import UserSession
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None
        return user_sessions[0].user_id

    def destroy_session(self, request=None):
        """destroy_session method"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        from models.user_session import UserSession
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False
        user_sessions[0].remove()
        return True
