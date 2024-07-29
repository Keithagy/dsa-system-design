# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    @staticmethod
    def identifyNextNode(
        node1: Optional[ListNode], node2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if node1 is None and node2 is None:
            return node1
        if node1 is None:
            return node2
        if node2 is None:
            return node1

        return node1 if node1.val <= node2.val else node2

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = Solution.identifyNextNode(list1, list2)
        if head is None:
            return head

        tail = head
        if tail is list1:
            list1 = list1.next
        if tail is list2:
            list2 = list2.next

        while list1 is not None and list2 is not None:
            tail.next = Solution.identifyNextNode(list1, list2)
            tail = tail.next

            if tail is list1:
                list1 = list1.next
            if tail is list2:
                list2 = list2.next

        tail.next = Solution.identifyNextNode(list1, list2)

        return head

