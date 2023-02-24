#!/usr/bin/env python3
"""Basic app Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale"""
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang


@app.route('/')
def index():
    """Return index page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
