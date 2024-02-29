# https://leetcode.com/problems/lru-cache/
# credits to: https://www.youtube.com/watch?v=IYqLP-KfXdQ

from collections import OrderedDict
    

class LRUCache:

    def __init__(self, capacity: int):
        self.items = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        self.items.move_to_end(key)
        return self.items[key]
        

    def put(self, key: int, value: int) -> None:
        # access makes it most recently used (ie, end of the line for removal)
        if key in self.items:
            self.items.move_to_end(key)

        self.items[key] = value

        # if we exceeded capacity we must remove an item from the front
        if len(self.items) > self.capacity:
            self.items.popitem(0)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
