#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.most_recent_key in self.cache_data:
                    del self.cache_data[self.most_recent_key]
                    print(f"DISCARD: {self.most_recent_key}")
            self.cache_data[key] = item
        self.most_recent_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.most_recent_key = key
        return self.cache_data[key]
