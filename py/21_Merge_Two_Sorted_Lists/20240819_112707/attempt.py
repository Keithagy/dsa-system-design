# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        next_smallest = list1 if list1.val <= list2.val else list2
        next_smallest.next = self.mergeTwoLists(
            list1.next if next_smallest is list1 else list1,
            list2.next if next_smallest is list2 else list2,
        )
        return next_smallest

