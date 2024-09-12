# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # need to normalize k >> so, need to count length first, which you will need in any case in order to get k+1th node from back
    # split the list, then connect tail to head, then return the split
    # O(n) time O(1) space
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def findTail(node: ListNode) -> Tuple[int, ListNode]:
            length = 1
            while node.next:
                length += 1
                node = node.next
            return (length, node)

        def splitAt(node: ListNode, idx: int) -> ListNode:
            i = 1
            while node and i != idx:
                node = node.next
                i += 1
            split = node.next
            node.next = None
            return split

        (length, tail) = findTail(head)
        k %= length  # normalize
        if k == 0:
            return head
        newHead = splitAt(head, length - k)
        tail.next = head
        return newHead

