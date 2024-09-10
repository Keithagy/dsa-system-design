# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head, even_head = ListNode(), ListNode()
        odd_tail, even_tail = odd_head, even_head
        cur = head
        is_odd = True
        while cur:
            if is_odd:
                odd_tail.next = cur
                odd_tail = odd_tail.next
            else:
                even_tail.next = cur
                even_tail = even_tail.next
            cur = cur.next
            is_odd = not is_odd
        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next

