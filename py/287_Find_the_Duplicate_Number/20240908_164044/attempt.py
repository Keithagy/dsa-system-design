from typing import List


class Solution:
    # Application of the pidgeonhole principle; treating the elements as indices, you can find the second value that points to a repeated slot
    # If you have 4 slots and 5 possible values, then 1 of those slots has to have 2 values.
    # Cycle detection algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        def next(i: int) -> int:
            return nums[i]

        slow = next(0)
        fast = next(next(0))
        while fast != slow:
            slow = next(slow)
            fast = next(next(fast))
        slow = 0
        while slow != fast:
            slow = next(slow)
            fast = next(fast)
        return slow

