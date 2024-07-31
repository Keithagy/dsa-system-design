from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        next_node = head.next
        while next_node:
            tmp = next_node.next
            curr.next = prev
            next_node.next = curr

            prev = curr
            curr = next_node
            next_node = tmp
        return curr

