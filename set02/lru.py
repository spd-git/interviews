"""
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should
support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the
cache, otherwise return -1. set(key, value) - Set or insert the value if the key is not
already present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.
"""


class LRUCache:

    def __init__(self, capacity: int = 10):
        self.capacity = capacity

    def get(self, key: int) -> int:
        pass

    def set(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    pass
