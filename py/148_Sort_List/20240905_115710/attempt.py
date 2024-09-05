# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2
        result = tail = ListNode(-1)
        while l1 and l2:
            next_node = l1 if l1.val <= l2.val else l2
            tail.next = next_node
            tail = tail.next
            if next_node is l1:
                l1 = l1.next
            else:
                l2 = l2.next
        tail.next = l1 if l1 else l2
        return result.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head
        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            fast = fast.next

        mid = slow.next
        slow.next = None

        # you call sortlist on head again, which is the entry point of the algo.
        # but notice that at this point, the list that head is head of is half as long
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

