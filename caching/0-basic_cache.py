#!/usr/bin/python3
"""class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
