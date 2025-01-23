#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ initialize FIFO class """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    