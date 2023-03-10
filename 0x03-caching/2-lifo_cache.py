#!/usr/bin/python3

"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Create a class LIFOCache that inherits from
    BaseCaching and is a caching system:"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return None

        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[-2]
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
