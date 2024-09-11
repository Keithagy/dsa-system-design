# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        You probably want to run a fast pointer to the penultimate node,
        keep a slow pointer at the head,
        then interleave head and tail until they meet in the middle.

        Key concern: will you create a cycle?
        1 x> 2 -> 3 -> 4
        H         T

        1 -> 4 -> 2

        tail.next.next = head.next (creates cycle)
        head.next = tail.next
        head = tail.next

        Don't think this works because you will always not be able to backtrack.
        You probably need to reverse the second half of the list first, then interleave.
        1->2->3->4 >> 1->2 4->3 >> 1->4->2->3
        1>2>3>4>5 || 1>2>3 5>4 >> 1>5>2>4>3

        O(n) time, O(1) space
        """
        if not head or not head.next:
            return

        def split(head: ListNode) -> ListNode:
            slow, fast = head, head
            while (
                fast and fast.next and fast.next.next
            ):  # in even node case, we want the left-half
                fast = fast.next.next
                slow = slow.next
            h2_head = slow.next
            slow.next = None  # avoid cycle
            return h2_head

        def rev(node: ListNode) -> ListNode:
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        def interleave(h1: ListNode, h2: ListNode) -> None:

            p1, p2 = h1, h2
            while p1 and p2:
                tmp1, tmp2 = p1.next, p2.next
                p2.next = p1.next
                p1.next = p2
                p1 = tmp1
                p2 = tmp2

        h2_head = split(head)
        rev_head = rev(h2_head)
        interleave(head, rev_head)

