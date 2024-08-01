# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr, prev = head, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # handles edge input of empty list, AND recursion base case of getting to the end of the list
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None  # for now, this node is the new tail, so let the next recursion handle the breakage if there is one
        return new_head

