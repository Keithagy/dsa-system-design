# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        def findMiddle(head: ListNode) -> ListNode:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow  # second middle if even, middle if odd

        def reverseFrom(node: ListNode) -> ListNode:
            if not node.next:
                return node
            new_head = reverseFrom(node.next)
            node.next.next = node
            return new_head

        middle = findMiddle(head)
        tail = reverseFrom(middle)
        while (
            head
            and tail
            and not (
                (head.next is tail.next) or (head.next is tail or tail.next is head)
            )
        ):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return head.val == tail.val

