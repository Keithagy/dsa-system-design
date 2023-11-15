from __future__ import annotations

from typing import Generic, Optional, TypeVar

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
