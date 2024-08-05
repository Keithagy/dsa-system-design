# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMiddle(self, head: ListNode) -> Tuple[ListNode, bool]:
        fast = slow = head
        # if even nodes, while loop stops with fast at penultimate node
        # if odd nodes, while loop stops with fast at last node
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return (
            slow,
            fast.next is not None,
        )  # true reflects even number of nodes in list

    def reverse(self, head: ListNode) -> ListNode:
        curr = head.next
        prev = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        (middle, even_node_count) = self.findMiddle(head)
        tail = self.reverse(middle)

        while (
            (tail.next is not head and head.next is not tail)
            if even_node_count
            else (head.next is not middle and tail.next is not middle)
        ):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return head.val == tail.val

