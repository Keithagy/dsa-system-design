from typing import List


class Solution:
    # constraints
    # nums has at least 1 element, at most 100 elements
    # elements of nums always positive ([0,400])
    #
    # # implications
    # amount you can rob is always positive
    # amount you can rob is minimally min(nums)
    #                       maxmimally ???
    #
    # core idea: you can take a given house, in which case you have to skip the next house,
    # or you can skip a given house, in which case you just move on and consider the next house
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(idx: int) -> int:
            if idx >= len(nums):
                return 0  # this is not a valid place to rob
            if idx == len(nums) - 1:
                return nums[idx]  # no further houses to consider
            if idx in memo:
                return memo[idx]
            take_this = nums[idx] + dp(idx + 2)
            skip_this = dp(idx + 1)
            memo[idx] = max(take_this, skip_this)
            return memo[idx]

        return dp(0)

