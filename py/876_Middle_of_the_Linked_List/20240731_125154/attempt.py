# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = 0

        curr = head
        while curr:
            curr = curr.next
            nodes += 1

        middle = nodes // 2
        slow = head
        while middle > 0:
            slow = slow.next
            middle -= 1
        return slow

