# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def advanceFastAndCheck(
        self, fast: Optional[ListNode], slow: Optional[ListNode]
    ) -> Tuple[Optional[bool], Optional[ListNode]]:
        if not fast:
            return (False, fast)

        fast = fast.next
        if not fast:
            # fast pointer has found end of list
            return (False, fast)

        if fast is slow:
            return (True, fast)

        return (None, fast)

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and slow:
            fast_movements_per_slow_movement = 2
            for _ in range(fast_movements_per_slow_movement):
                has_cycle, fast = self.advanceFastAndCheck(fast, slow)
                if has_cycle is not None:
                    return has_cycle
            slow = slow.next

        return False

