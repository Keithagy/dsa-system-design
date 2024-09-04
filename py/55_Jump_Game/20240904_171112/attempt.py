from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_reachable = 0
        for idx, num in enumerate(nums):
            if idx <= furthest_reachable:
                furthest_reachable = max(furthest_reachable, idx + num)
                if furthest_reachable >= len(nums) - 1:
                    return True
        return furthest_reachable >= len(nums) - 1

