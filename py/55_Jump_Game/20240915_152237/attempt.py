from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_reachable = 0
        for i, num in enumerate(nums):
            if furthest_reachable < i:
                return False
            furthest_from_here = i + num
            furthest_reachable = max(furthest_reachable, furthest_from_here)
        return True

