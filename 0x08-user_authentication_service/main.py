#!/usr/bin/env python3
"""
Main file
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Register a user"""
    url = "http://localhost:5000/users"
    data = {"email": email, "password": password}
    r = requests.post(url, data=data)
    assert r.status_code == 200
    assert r.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""
    url = "http://localhost:5000/sessions"
    data = {"email": email, "password": password}
    r = requests.post(url, data=data)
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """Log in"""
    url = "http://localhost:5000/sessions"
    data = {"email": email, "password": password}
    r = requests.post(url, data=data)
    assert r.status_code == 200
    session_id = r.cookies.get("session_id")
    assert session_id
    return session_id


def profile_unlogged() -> None:
    """Get profile when not logged in"""
    url = "http://localhost:5000/profile"
    r = requests.get(url)
    assert r.status_code == 403


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
