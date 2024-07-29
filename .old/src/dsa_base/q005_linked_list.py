from __future__ import annotations

from typing import Generic, Optional, TypeVar
import unittest

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self,
        value: T,
        next: Optional[Node[T]] = None,
        prev: Optional[Node[T]] = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(Generic[T]):
    head: Optional[Node[T]] = None
    tail: Optional[Node[T]] = None
    length: int = 0

    def __init__(self) -> None:
        return

    def remove(self, value: T) -> Optional[T]:
        to_remove = self.head

        while to_remove is not None and to_remove.value != value:
            to_remove = to_remove.next

        if to_remove is None:
            return None  # value passed in does not exist; also covers empty list case

        if to_remove.prev is not None:
            to_remove.prev.next = to_remove.next
        if to_remove.next is not None:
            to_remove.next.prev = to_remove.prev
        if to_remove is self.head:
            self.head = to_remove.next
        if to_remove is self.tail:
            self.tail = to_remove.prev
        self.length -= 1
        return to_remove.value

    def insertAt(self, index: int, val: T) -> None:
        if index < 0 or index > self.length:
            return
        i = 0
        cur = self.head
        prev = None
        while i < index:
            if cur is None:
                raise Exception(
                    "Unexpected empty node while traversing list for insertAt operation"
                )
            prev = cur
            cur = cur.next
            i += 1

        new_node = Node(val)

        new_node.next = cur
        new_node.prev = prev

        if prev:
            prev.next = new_node
        if cur:
            cur.prev = new_node

        if index == 0:
            self.head = new_node

        if index == self.length:
            self.tail = new_node

        self.length += 1

    def removeAt(self, index: int) -> Optional[T]:
        if index < 0 or index > self.length - 1:
            return None  # list is not that long
        to_remove = self.head

        for _ in range(index):
            if to_remove is None:
                return None
            to_remove = to_remove.next
        if to_remove is None:
            return None

        if to_remove.prev is not None:
            to_remove.prev.next = to_remove.next
        if to_remove.next is not None:
            to_remove.next.prev = to_remove.prev
        if to_remove is self.head:
            self.head = to_remove.next
        if to_remove is self.tail:
            self.tail = to_remove.prev
        self.length -= 1
        return to_remove.value

    def append(self, item: T) -> None:
        node = Node(value=item)
        self.length += 1
        if self.head is None:
            assert self.tail is None
            self.head = self.tail = node
            return
        assert self.tail is not None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, item: T) -> None:
        node = Node(value=item)
        self.length += 1
        if self.head is None:
            assert self.tail is None
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def get(self, index: int) -> Optional[T]:
        if index > self.length - 1:
            return None  # list is not that long
        retrieved = self.head
        for _ in range(index):
            if retrieved is None:
                return None
            retrieved = retrieved.next
        return retrieved.value if retrieved else None


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.length, 1)

        ll.append(2)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.length, 1)

        ll.prepend(2)
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.length, 2)

    def test_remove(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.remove(1)
        self.assertEqual(ll.length, 1)

        removed = ll.remove(3)
        self.assertIsNone(removed)
        self.assertEqual(ll.length, 1)

        ll.remove(2)
        self.assertIsNone(ll.head)

    def test_insertAt(self):
        ll = LinkedList()
        ll.insertAt(0, 1)
        self.assertEqual(ll.get(0), 1)

        ll.insertAt(1, 2)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.length, 2)

        ll.insertAt(1, 3)
        self.assertEqual(ll.get(1), 3)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 3)

    def test_removeAt(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        ll.removeAt(1)
        self.assertEqual(ll.get(1), 3)
        self.assertEqual(ll.length, 2)

        ll.removeAt(0)
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.length, 1)

        ll.removeAt(0)
        self.assertIsNone(ll.head)

    def test_get(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(2), 3)
        self.assertIsNone(ll.get(3))

    def test_list_integrity(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.prepend(0)
        ll.removeAt(1)
        ll.insertAt(1, 1.5)

        self.assertEqual(ll.get(0), 0)
        self.assertEqual(ll.get(1), 1.5)
        self.assertEqual(ll.get(2), 2)
        self.assertEqual(ll.length, 3)

    def test_error_handling(self):
        ll = LinkedList()
        ll.insertAt(1, 1)  # Inserting at index 1 in an empty list
        self.assertEqual(ll.length, 0)


if __name__ == "__main__":
    unittest.main()
