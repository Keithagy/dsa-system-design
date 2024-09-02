# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # input: [] ok
    # input: [1] ok
    # input: [1,2] ok
    # input: [1->2->3]
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        # even
        #   head 1->2->3
        #   tail 1 -> 3 <<
        # odd
        #   head 2
        #   tail 2
        even_head, even_tail, odd_head, odd_tail = None, None, None, None

        cur = head  # 3
        i = 0  # 2
        while cur:
            cur_even = i % 2 == 0  # True
            if cur_even:
                if not even_head:
                    even_head = even_tail = cur
                else:
                    even_tail.next = cur
                    even_tail = cur
            else:
                if not odd_head:
                    odd_head = odd_tail = cur
                else:
                    odd_tail.next = cur
                    odd_tail = cur
            cur = cur.next
            i += 1
        even_tail.next = odd_head
        odd_tail.next = None
        return even_head

