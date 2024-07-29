# Heap condition: every node below be is larger (if minheap)
# To add to heap, add to end then bubble up
# To pop from the heap, you just get the first element on the heap. then, you swap the bottom-most node to the top
# Remember that bottom-most node, means that at all levels, it is larger than its parent
# Then you bubble it down to re-establish the heap property
# left child: 2i + 1
# right child: 2i + 2
# parent: (i - 1) // 2
# Last item: array length

from __future__ import annotations

import unittest
from typing import Optional, List


# Implementing a min-heap here, since getting from a min-heap to a max-heap is quite trivial
class PriorityQueue:
    inner: List[int]

    def __init__(self) -> None:
        self.inner = []

    def push(self, val: int) -> None:
        self.inner.append(val)
        self._heapify_up()

    def pop(self) -> Optional[int]:
        if self._is_empty():
            return None
        self.inner[0], self.inner[len(self.inner) - 1] = (
            self.inner[len(self.inner) - 1],
            self.inner[0],
        )
        popped = self.inner.pop()
        self._heapify_down()
        return popped

    def peek(self) -> Optional[int]:
        if self._is_empty():
            return None
        return self.inner[0]

    def _is_empty(self) -> bool:
        return len(self.inner) == 0

    def _heapify_down(self) -> None:
        if self._is_empty():
            return
        i = 0
        while i < len(self.inner):
            val = self.inner[i]
            left_i = self._left_child(i)
            right_i = self._right_child(i)
            if left_i >= len(self.inner) and right_i >= len(self.inner):
                return
            if left_i >= len(self.inner) or right_i >= len(self.inner):
                if self._min_heap_condition(self.inner[left_i], val):
                    return
                self.inner[i], self.inner[left_i] = (
                    self.inner[left_i],
                    self.inner[i],
                )
                i = left_i
                continue

            smaller_child_i = (
                left_i
                if min(self.inner[left_i], self.inner[right_i]) == self.inner[left_i]
                else right_i
            )
            if self._min_heap_condition(self.inner[smaller_child_i], val):
                return
            self.inner[i], self.inner[smaller_child_i] = (
                self.inner[smaller_child_i],
                self.inner[i],
            )
            i = smaller_child_i

    def _left_child(self, i: int) -> int:
        return (i * 2) + 1

    def _right_child(self, i: int) -> int:
        return (i * 2) + 2

    def _heapify_up(self) -> None:
        if self._is_empty():
            return
        i = len(self.inner) - 1
        while i > 0:
            val = self.inner[i]
            parent = self.inner[self._parent(i)]
            if self._min_heap_condition(val, parent):
                return
            self.inner[i], self.inner[self._parent(i)] = (
                self.inner[self._parent(i)],
                self.inner[i],
            )
            i = self._parent(i)

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _min_heap_condition(self, child_val: int, parent_val: int) -> bool:
        return child_val >= parent_val


class TestPriorityQueue(unittest.TestCase):
    def test_push_and_peek(self):
        print("------")
        print("push_and_seek")
        pq = PriorityQueue()
        pq.push(5)
        self.assertEqual(pq.peek(), 5)
        pq.push(3)
        self.assertEqual(pq.peek(), 3)
        pq.push(7)
        self.assertEqual(pq.peek(), 3)
        print("------")

    def test_pop(self):
        print("------")
        print("pop")
        pq = PriorityQueue()
        pq.push(5)
        pq.push(3)
        pq.push(7)
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 5)
        self.assertEqual(pq.pop(), 7)
        self.assertIsNone(pq.pop())
        print("------")

    def test_empty_queue(self):
        print("------")
        print("empty_q")
        pq = PriorityQueue()
        self.assertIsNone(pq.pop())
        self.assertIsNone(pq.peek())
        self.assertTrue(pq._is_empty())
        print("------")

    def test_heap_property_maintained(self):
        print("------")
        print("test_heap_property_maintained")
        pq = PriorityQueue()
        elements = [5, 3, 8, 1, 4, 9, 7]
        for e in elements:
            pq.push(e)

        results = []
        while not pq._is_empty():
            results.append(pq.pop())

        self.assertEqual(results, sorted(elements))
        print("------")

    def test_internal_heapify_down(self):
        print("------")
        print("test_internal_heapify_down")
        pq = PriorityQueue()
        pq.inner = [7, 6, 5, 4, 3, 2, 1]
        pq._heapify_down()
        self.assertEqual(pq.inner, [5, 6, 1, 4, 3, 2, 7])
        print("------")

    def test_internal_heapify_up(self):
        print("------")
        print("test_internal_heapify_up")
        pq = PriorityQueue()
        pq.inner = [5, 4, 3, 2, 1]
        pq._heapify_up()
        self.assertEqual(pq.inner, [1, 5, 3, 2, 4])
        print("------")


if __name__ == "__main__":
    unittest.main()
