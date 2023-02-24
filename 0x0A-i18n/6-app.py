#!/usr/bin/env python3
"""Basic app Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """Get user"""
    if login_as is None:
        return None
    try:
        return users[int(login_as)]
    except Exception:
        return None


def get_locale():
    """Get locale"""
    local = request.args.get('locale')
    print(local)
    if local in app.config['LANGUAGES'] and local is not None:
        return local
    if g.get("user") and g.user['locale'] in app.config['LANGUAGES'] and \
            g.user['locale'] is not None:
        return g.user['locale']
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('6-app.Config')


@app.before_request
def before_request():
    """Before request"""
    user = get_user(request.args.get('login_as'))
    g.user = user


@app.route('/')
def index():
    """Return index page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
