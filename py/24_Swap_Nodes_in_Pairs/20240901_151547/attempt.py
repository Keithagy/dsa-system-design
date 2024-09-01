# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # empty >> empty
    # [0] >> [0]
    # [0] -> [1] >> [1] -> [0]
    # [0] -> [1] -> [2] >> [1] -> [0] -> [2]
    # [0] -> [1] -> [2] -> [3] >> [1] -> [0] -> [3] -> [2]
    #
    # even nodes case | odd nodes case
    # swap and process tail
    # None is None
    #
    # O(n) space, constant extra mem
    #
    # [0] -> [1] -> [2]
    # new_head = [0]->[1]-> tail = [2]
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:  # trailing node
            return head

        def swapAndReturnNewHead(head: ListNode) -> ListNode:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head

        # either trailing 2 nodes or [h1,h2, tail]
        tail = head.next.next
        if not tail:
            return swapAndReturnNewHead(head)
        new_head = swapAndReturnNewHead(head)
        new_head.next.next = self.swapPairs(tail)
        return new_head

