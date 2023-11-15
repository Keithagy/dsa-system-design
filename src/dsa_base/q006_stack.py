from __future__ import annotations

from typing import Generic, Optional, TypeVar
from q005_linked_list import LinkedList

T = TypeVar("T")


class Stack(Generic[T]):
    _internal: LinkedList[T] = LinkedList()

    def push(self, value: T) -> None:
        self._internal.append(value)

    def pop(self) -> Optional[T]:
        return self._internal.removeAt(self._internal.length - 1)

    def peek(self) -> Optional[T]:
        return self._internal.tail.value if self._internal.tail else None
