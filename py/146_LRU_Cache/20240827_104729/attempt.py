from typing import Optional


class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node) -> None:
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def __cache_add(self, key: int, value: int) -> None:
        new = Node(key, value)
        self.cache[key] = new
        self.insert(new)

    def put(self, key: int, value: int) -> None:
        # key already exists, update
        if key in self.cache:
            #   update cache value
            node = self.cache[key]
            node.val = value
            #   update recency linked list
            self.remove(node)
            self.insert(node)
            return

        # key not exists, add capacity contrained
        if self.capacity <= len(self.cache):
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        self.__cache_add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

