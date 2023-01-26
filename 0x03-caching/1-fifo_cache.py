#!/usr/bin/python3

"""Create a class FIFOCache that inherits from
BaseCaching and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Create a class FIFOCache that inherits from
    BaseCaching and is a caching system:"""

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
                first = self.keys.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
