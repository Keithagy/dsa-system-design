from typing import Dict, Optional


class Node:
    def __init__(
        self, key: int, val: int, next: Optional["Node"], prev: Optional["Node"]
    ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    # use a hash map to track the cache itself
    # use a doubly linked list to manage the ordering
    # head of linked list is least recent, tail is most
    # track capacity internally
    # input:
    # init(2)
    # put(2,2)
    # put(1,1)
    # put(3,3)
    # get(2) >> -1
    # get(1) >> 1
    # put(4,4)
    # get(1) >> -1
    def __init__(self, capacity: int):
        self.capacity = capacity
        # {
        #   1: Node(1)
        #   3: Node(3)
        # }
        self.cache: Dict[int, Node] = {}
        # dummy nodes to mark linked list ends and make rest of logic easier
        head = Node(-1, -1, None, None)
        tail = Node(-1, -1, None, None)
        head.next = tail
        tail.prev = head
        self.head: Node = head
        self.tail: Node = tail
        # -1 <=> 1 <=> 3 <=> -1
        #    2

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return self.cache[key].val

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def _add(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) < self.capacity:
                self.cache[key] = Node(key, value, None, None)
                self._add(self.cache[key])
            else:
                del self.cache[self.head.next.key]
                self._remove(self.head.next)
                self.put(key, value)
        else:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            node.val = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
