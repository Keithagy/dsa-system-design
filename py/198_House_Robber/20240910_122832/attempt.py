from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def maxIncomeStartingFrom(startIdx: int) -> int:
            if startIdx >= len(nums):
                return 0
            if startIdx in memo:
                return memo[startIdx]

            if_take = nums[startIdx] + maxIncomeStartingFrom(startIdx + 2)
            if_skip = maxIncomeStartingFrom(startIdx + 1)
            memo[startIdx] = max(if_take, if_skip)
            return memo[startIdx]

        return max([maxIncomeStartingFrom(houseIdx) for houseIdx in range(len(nums))])

