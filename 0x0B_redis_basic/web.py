#!/usr/bin/env python3
"""
How to use redis for basic operations
"""

import requests
import redis


def get_page(url: str) -> str:
    """track how many times a particular URL was accessed"""
    r = redis.Redis()
    key = "count:" + url
    if r.get(key):
        r.incr(key)
    else:
        r.set(key, 1)
    html = r.get(url)
    if html:
        return html.decode('utf-8')
    else:
        html = requests.get(url).text
        r.setex(url, 10, html)
        return html
