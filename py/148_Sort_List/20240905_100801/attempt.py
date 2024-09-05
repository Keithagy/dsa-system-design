# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # traverse list >> O n
    # heapify >> O(n log n)
    # heap pop >> O(n log n)
    # if you want constant memory, you need to use quicksort?
    # ok... maybe you can adapt merge sort to this
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def getMidTail(
            head: ListNode, bookend: Optional[ListNode]
        ) -> Tuple[ListNode, ListNode]:
            # if not head:
            #     return head
            slow, fast = head, head
            # if even, slow is first-mid, fast is second-last
            # if odd, slow is mid, fast is last
            while (
                slow is not bookend
                and fast is not bookend
                and fast.next is not bookend
                and fast.next.next is not bookend
            ):
                slow = slow.next
                fast = fast.next.next
            if fast.next:
                fast = fast.next  # move fast if even
            assert slow and fast
            return (slow, fast)

        def mergeSort(start: ListNode, end: Optional[ListNode]):
            if start is end:
                return start
            inner_mid, inner_tail = getMidTail(start, end)
            left = mergeSort(start, inner_mid)
            right = mergeSort(inner_mid, inner_tail)
            merge(left, right)

        mergeSort(head, None)
        return head

