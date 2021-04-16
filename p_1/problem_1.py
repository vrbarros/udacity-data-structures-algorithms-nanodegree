# Least Recently Used Cache

from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity if capacity is not None else 0
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value

            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.capacity == 0:
                return
            else:
                if len(self.cache) >= self.capacity:
                    self.cache.popitem(last=False)

        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1), "expect 1")  # returns 1
print(our_cache.get(2), "expect 2")  # returns 2
print(our_cache.get(9), "expect -1")  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3), "expect -1")
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(None)
our_cache.set(1, 1)
print(our_cache.get(1), "expect -1")
# returns -1

our_cache = LRU_Cache(3)
our_cache.set(1, 5)
our_cache.set(2, 10)
our_cache.set(3, 15)
print(our_cache.get(1), "expect 5")  # returns 5
print(our_cache.get(2), "expect 10")  # returns 10
print(our_cache.get(3), "expect 15")  # returns 15
our_cache.set(4, 20)
print(our_cache.get(1), "expect -1")  # returns -1

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1), "expect -1")
# returns -1