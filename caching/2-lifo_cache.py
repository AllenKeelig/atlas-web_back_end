#!/usr/bin/python3
""" LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
