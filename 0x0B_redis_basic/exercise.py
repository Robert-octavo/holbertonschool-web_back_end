#!/usr/bin/env python3
"""
How to use redis for basic operations
"""

import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Call history"""
    input_list = method.__qualname__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.rpush(input_list, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_list, str(result))
        return result
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get data from redis as a string"""
        return self.get(key, str)
        # return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """Get data from redis as an int"""
        return self.get(key, int)
        # return int(self._redis.get(key))
