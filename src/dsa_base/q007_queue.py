from __future__ import annotations

from typing import Generic, Optional, TypeVar
from q005_linked_list import LinkedList

T = TypeVar("T")


class Queue(Generic[T]):
    _internal: LinkedList[T] = LinkedList()

    def enqueue(self, value: T) -> None:
        self._internal.append(value)

    def dequeue(self) -> Optional[T]:
        return self._internal.removeAt(0)

    def peek(self) -> Optional[T]:
        return self._internal.head.value if self._internal.head else None
