#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching
and is a caching system:"""

from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Create a class MRUCache that inherits from BaseCaching
    and is a caching system:"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            self.keys.appendleft(key)
            self.cache_data[key] = item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.keys.popleft()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.appendleft(key)
            return self.cache_data[key]
        return None
