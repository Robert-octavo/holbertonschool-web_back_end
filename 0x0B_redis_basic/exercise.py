#!/usr/bin/env python3
"""
How to use redis for basic operations
"""

import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
