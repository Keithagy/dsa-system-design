# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMiddleAndTail(
        self, head: ListNode
    ) -> Tuple[
        ListNode, ListNode, bool
    ]:  # (true_middle if `didOverrun` else first_middle, tail, `didOverrun`)
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return (
            slow,
            fast.next if fast.next is not None else fast,
            fast.next is not None,
        )

    def reverse(self, head: ListNode) -> ListNode:
        prev = head
        curr = head.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        (middle, tail, even_node_count) = self.findMiddleAndTail(head)
        tail = self.reverse(middle if not even_node_count else middle.next)
        while (
            (head.next is not tail and tail.next is not head)
            if even_node_count
            else (head.next is not middle and tail.next is not middle)
        ):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return head.val == tail.val

