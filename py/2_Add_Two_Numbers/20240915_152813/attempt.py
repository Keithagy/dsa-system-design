# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(0)  # initialize dummy node
        tail = result
        carry = 0
        while l1 or l2 or carry != 0:
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            digit = sum % 10
            carry = sum // 10
            nextNode = ListNode(digit)
            tail.next = nextNode
            tail = tail.next
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
        return result.next

