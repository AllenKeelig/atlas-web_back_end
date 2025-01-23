#!/usr/bin/python3
""" LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize LRUCache"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.access_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
