#!/usr/bin/env python3
""" Module of Session Authentication views"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login a user
    """
    data = request.form
    if not data:
        return jsonify({"error": "email missing"}), 400
    email = data.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = data.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': data.get('email')})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(data.get('password')):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
