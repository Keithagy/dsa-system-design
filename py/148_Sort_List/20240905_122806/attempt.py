# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def split(self, node: Optional[ListNode], step: int) -> Optional[ListNode]:
        if not node:
            return node
        cur = node
        prev = None
        while step > 0 and cur:
            prev = cur
            cur = cur.next
            step -= 1
        prev.next = None
        return cur

    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode], tail: ListNode
    ) -> ListNode:
        while l1 and l2:
            tail.next = l1 if l1.val <= l2.val else l2
            tail = tail.next
            if tail is l1:
                l1 = l1.next
            else:
                l2 = l2.next
        tail.next = l1 if l1 else l2
        while tail.next:
            tail = tail.next
        return tail

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < length:
            tail = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = self.split(cur, step)
                cur = self.split(right, step)
                tail = self.merge(left, right, tail)
            step *= 2
        return dummy.next

