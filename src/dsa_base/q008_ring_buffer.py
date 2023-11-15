from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class RingBufferDeque(Generic[T]):
    _internal: List[T] = []  # RingBuffer's capacity == len(self._internal)
    _head: int = 0
    _tail: int = 0
    _default_value: T

    def __init__(self, capacity: int, default_value: T) -> None:
        self._default_value = default_value
        self._internal = [default_value] * capacity

    def push_head(self, val: T) -> None:
        prospective_head = self._calc_index_offset(self._head, -1)
        if prospective_head == self._tail:
            self._increase_capacity(len(self._internal))
        self._head = self._calc_index_offset(self._head, -1)
        self._internal[self._head] = val

    def push_tail(self, val: T) -> None:
        prospective_tail = self._calc_index_offset(self._tail, 1)
        if prospective_tail == self._head:
            self._increase_capacity(len(self._internal))
        self._tail = self._calc_index_offset(self._tail, 1)
        self._internal[self._tail] = val

    def pop_head(self) -> Optional[T]:
        if self._is_empty():
            return None
        popped = self._internal[self._head]
        self._head = self._calc_index_offset(self._head, 1)
        return popped

    def pop_tail(self) -> Optional[T]:
        if self._is_empty():
            return None
        popped = self._internal[self._tail]
        self._tail = self._calc_index_offset(self._tail, -1)
        return popped

    def peek_head(self) -> Optional[T]:
        if self._is_empty():
            return None
        return self._internal[self._head]

    def peek_tail(self) -> Optional[T]:
        if self._is_empty():
            return None
        return self._internal[self._tail]

    def _calc_index_offset(self, starting_i: int, increment: int) -> int:
        raw_incremented = starting_i + increment
        if raw_incremented < len(self._internal) and raw_incremented >= 0:
            return raw_incremented
        if raw_incremented < 0:
            return len(self._internal) + raw_incremented
        return raw_incremented % len(
            self._internal
        )  # if increment hits length, wrap around

    # NOTE: This method mutates internal state, updating them to the correct new markers. All copies of _head and _tail prior to calling this method should be considered invalid
    def _increase_capacity(self, additional: int) -> None:
        new_backing = [self._default_value] * (len(self._internal) + additional)
        i = self._head
        j = 0
        while i != self._tail:
            new_backing[j] = self._internal[i]
            i = self._calc_index_offset(i, 1)
            j += 1
        self._head = 0
        self._tail = j
        self._internal = new_backing

    def _is_empty(self) -> bool:
        return self._head == self._tail
