from typing import Dict, Optional


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:

    # core idea centres around using a fixed-size hash map + doubly linked list to check recency
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}

        # dummy nodes to simplify edge case handling
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeFromList(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def insertAsMostRecent(self, node: Node) -> None:
        node.next = self.tail
        node.prev = self.tail.prev

        node.next.prev = node.prev.next = node

    def evictLRU(self) -> None:
        lru = self.head.next
        self.removeFromList(lru)
        del self.cache[lru.key]

    def refreshRecency(self, node: Node) -> None:
        self.removeFromList(node)
        self.insertAsMostRecent(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.refreshRecency(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        If creating new key, we need to worry about whether exceeding cache capacity.
            If exceeding cache capacity, we need to evict the least recently used (head of doubly linked list),
            and then write the incoming value.
        If updating existing key, we only need to update the existing value.
        In either case, we should make the node being accessed the most-recently-used one.
        """
        if key not in self.cache:
            # Creating new key
            if len(self.cache) == self.capacity:
                self.evictLRU()
            self.cache[key] = Node(key, value)
            self.insertAsMostRecent(self.cache[key])
        else:
            # Updating existing key
            self.cache[key].val = value
            self.refreshRecency(self.cache[key])

