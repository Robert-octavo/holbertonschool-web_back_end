#!/usr/bin/env python3
"""Basic app Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    """Get locale"""
    local = request.args.get('locale')
    print(local)
    if local in app.config['LANGUAGES'] and local is not None:
        return local
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@app.route('/')
def index():
    """Return index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
