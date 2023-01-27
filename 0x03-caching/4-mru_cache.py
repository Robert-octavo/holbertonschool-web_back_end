#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching
and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Create a class MRUCache that inherits from BaseCaching
    and is a caching system:"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
