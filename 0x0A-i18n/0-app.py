#!/usr/bin/env python3
"""Basic app Flask app"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Return index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
