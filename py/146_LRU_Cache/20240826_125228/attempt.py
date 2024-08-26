class LRUCache:

    def __init__(self, capacity: int):
        self.rank = {}
        self.inner = {}
        self.counter = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.inner:
            return self.inner[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.inner) < self.capacity:
            self.inner[key] = value
        else:
            del self.inner[leastRecentlyUsed()]
            self.rank[]
        if key in self.inner:
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
