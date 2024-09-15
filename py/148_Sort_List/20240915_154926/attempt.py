# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def split(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return node
            slow, fast = node, node
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            head2 = slow.next
            slow.next = None
            return head2

        def merge(
            head1: Optional[ListNode], head2: Optional[ListNode]
        ) -> Optional[ListNode]:
            result = ListNode(0)  # dummy
            tail = result
            while head1 and head2:
                nextNode = head1 if head1.val < head2.val else head2
                tail.next = nextNode
                tail = tail.next

                head1 = head1.next if nextNode is head1 else head1
                head2 = head2.next if nextNode is head2 else head2

            tail.next = head1 if head1 else head2
            return result.next

        head2 = split(head)
        return merge(self.sortList(head), self.sortList(head2))

