from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # input
    # (34) l1: 4 -> 3 -> None
    #                    ^
    # (166)l2: 6 -> 6 -> 1 -> None
    #                         ^
    #
    #
    #
    # (200) 0 -> 0 -> 2
    #
    # they've already done some work for us by giving us the nodes reversed
    # node sequencing already matches digit placing
    # for each node, sum up the digits and apply the carry if there is
    # if sum exceeds 9, truncate into carry and modulo into node
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if (not l1 and not l2) or (not l1 or not l2):
            raise ValueError("both lists assured to be non-empty")

        carry = 0  # 1

        # -1 -> 0 -> 0 -> 2
        #  ^              ^
        res = ListNode(val=-1)
        res_tail = res  # 0
        while l1 or l2:
            sum = carry  # 2
            sum += l1.val if l1 else 0  # 0
            sum += l2.val if l2 else 0  # 1
            digit, carry = sum % 10, int(sum / 10)  # 2, 0
            res_tail.next = ListNode(val=digit)
            res_tail = res_tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            res_tail.next = ListNode(val=carry)
        return res.next

