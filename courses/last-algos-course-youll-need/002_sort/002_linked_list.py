from typing import List, Optional
import unittest


class LinkedList:
    class Node:
        def __init__(
            self,
            val: int,
            next: Optional["LinkedList.Node"] = None,
            prev: Optional["LinkedList.Node"] = None,
        ) -> None:
            self.val = val
            self.next: Optional[LinkedList.Node] = next
            self.prev: Optional[LinkedList.Node] = prev

    @staticmethod
    def of(vals: Optional[List[int]] = None) -> "LinkedList":
        new = LinkedList()
        if vals:
            for val in vals:
                new.append(val)
        return new

    def __init__(self) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.__length: int = 0

    def length(self) -> int:
        return self.__length

    def insert_at(self, val: int, index: int) -> None:
        """
        0 (equivalent to prepend) <= index <= self.length (equivalent to append)
        E.g: If inserting at 3, previous index 3 will now be index 4.
        """
        if index <= 0:
            self.prepend(val)
            return
        if index >= self.length() or self.length() == 0:
            self.append(val)
            return

        i = 0
        ptr = self.head
        while i < index:
            i += 1
            assert ptr
            ptr = ptr.next
        if not ptr:
            # End of list
            self.append(val)
            return

        new = LinkedList.Node(val)

        assert ptr.prev
        new.next = ptr
        new.prev = ptr.prev
        ptr.prev = new
        new.prev.next = new
        self.__length += 1

    def remove(self, val: int) -> Optional[int]:
        if self.length() == 0:
            return None
        assert self.head and self.tail
        if self.length() == 1 and self.head.val == val:
            return self.__remove_final__()

        ptr = self.head
        while ptr and ptr.val != val:
            ptr = ptr.next

        if not ptr:
            return None

        if ptr is self.head:
            return self.pop_left()
        if ptr is self.tail:
            return self.pop()

        assert ptr.next and ptr.prev
        ptr.next.prev = ptr.prev
        ptr.prev.next = ptr.next
        ptr.next = ptr.prev = None

        self.__length -= 1

        return ptr.val

    def pop_left(self) -> Optional[int]:
        if self.length() == 0:
            # Nothing to remove
            return None
        if self.length() == 1:
            return self.__remove_final__()

        assert self.head and self.head.next
        popped = self.head
        self.head = self.head.next
        self.head.prev = None

        popped.next = None
        self.__length -= 1

        return popped.val

    def pop(self) -> Optional[int]:
        if self.length() == 0:
            # Nothing to remove
            return None
        if self.length() == 1:
            return self.__remove_final__()

        assert self.tail and self.tail.prev
        popped = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        popped.prev = None
        self.__length -= 1

        return popped.val

    def __remove_final__(self) -> Optional[int]:
        assert self.head and self.tail and self.length() == 1
        removed = self.head.val
        self.head = self.tail = None
        self.__length -= 1
        return removed

    def remove_at(self, index: int) -> Optional[int]:
        """
        0 (remove at head) <= index <= self.length (remove at tail)
        E.g.: If removing at 2, previous index 3 will now be index 2.
        """
        if self.length() == 0:
            return None
        if self.length() == 1:
            return self.__remove_final__()

        if index <= 0:
            return self.pop_left()
        if index >= self.length():
            return self.pop()

        i = 0
        ptr = self.head
        while i < index:
            i += 1
            assert ptr
            ptr = ptr.next
        assert ptr and ptr.next and ptr.prev
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev

        ptr.next = ptr.prev = None
        self.__length -= 1
        return ptr.val

    def append(self, val: int) -> None:
        new = LinkedList.Node(val=val, prev=self.tail, next=None)
        if self.tail:
            self.tail.next = new
        self.tail = new
        if not self.head:
            self.head = new
        self.__length += 1

    def prepend(self, val: int) -> None:
        new = LinkedList.Node(val=val, prev=None, next=self.head)
        if self.head:
            self.head.prev = new
        self.head = new
        if not self.tail:
            self.tail = new
        self.__length += 1

    def get(self, index: int) -> Optional[int]:
        """
        0 (peek left) <= index <= self.length (peek right)
        """
        if self.length() == 0:
            return None
        assert self.head and self.tail
        if index <= 0:
            return self.head.val
        if index >= self.length():
            return self.tail.val

        i = 0
        ptr = self.head
        while i < index:
            i += 1
            assert ptr
            ptr = ptr.next
        return ptr and ptr.val


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.length(), 0)
        self.assertIsNone(ll.get(0))
        self.assertIsNone(ll.pop())
        self.assertIsNone(ll.pop_left())

    def test_append_and_length(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.length(), 1)
        ll.append(2)
        self.assertEqual(ll.length(), 2)

    def test_prepend_and_length(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual(ll.length(), 1)
        ll.prepend(2)
        self.assertEqual(ll.length(), 2)

    def test_get(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(2), 3)
        self.assertEqual(ll.get(3), 3)  # Out of bounds, should return tail
        self.assertEqual(ll.get(-1), 1)  # Out of bounds, should return head

    def test_insert_at(self):
        ll = LinkedList.of([1, 3])
        ll.insert_at(2, 1)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(2), 3)
        ll.insert_at(0, 0)  # Insert at head
        self.assertEqual(ll.get(0), 0)
        self.assertEqual(ll.get(3), 3)
        ll.insert_at(4, 10)  # Insert beyond tail
        self.assertEqual(ll.get(4), 4)

    def test_remove(self):
        ll = LinkedList.of([1, 2, 3, 2])
        self.assertEqual(ll.remove(2), 2)
        self.assertEqual(ll.length(), 3)
        self.assertEqual(ll.get(1), 3)
        self.assertIsNone(ll.remove(4))  # Remove non-existent element

    def test_pop_left(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.pop_left(), 1)
        self.assertEqual(ll.length(), 2)
        self.assertEqual(ll.get(0), 2)

    def test_pop(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.pop(), 3)
        self.assertEqual(ll.length(), 2)
        self.assertEqual(ll.get(1), 2)

    def test_remove_at(self):
        ll = LinkedList.of([1, 2, 3, 4])
        self.assertEqual(ll.remove_at(1), 2)
        self.assertEqual(ll.length(), 3)
        self.assertEqual(ll.get(1), 3)
        self.assertEqual(ll.remove_at(0), 1)  # Remove head
        self.assertEqual(ll.remove_at(10), 4)  # Remove tail (out of bounds)

    def test_edge_cases(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.pop(), 1)
        self.assertEqual(ll.length(), 0)
        ll.prepend(2)
        self.assertEqual(ll.pop_left(), 2)
        self.assertEqual(ll.length(), 0)

    def test_of_method(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.length(), 3)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(2), 3)

    def test_remove_head(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.remove(1), 1)
        self.assertEqual(ll.length(), 2)
        self.assertEqual(ll.get(0), 2)

    def test_remove_tail(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertEqual(ll.remove(3), 3)
        self.assertEqual(ll.length(), 2)
        self.assertEqual(ll.get(1), 2)

    def test_remove_only_element(self):
        ll = LinkedList.of([1])
        self.assertEqual(ll.remove(1), 1)
        self.assertEqual(ll.length(), 0)
        self.assertIsNone(ll.get(0))

    def test_remove_from_empty_list(self):
        ll = LinkedList()
        self.assertIsNone(ll.remove(1))
        self.assertEqual(ll.length(), 0)

    def test_remove_nonexistent_element(self):
        ll = LinkedList.of([1, 2, 3])
        self.assertIsNone(ll.remove(4))
        self.assertEqual(ll.length(), 3)


if __name__ == "__main__":
    unittest.main()
