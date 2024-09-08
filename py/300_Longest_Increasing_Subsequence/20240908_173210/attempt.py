from typing import List


class Solution:
    # dynamic programming approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def listForSubarrayStarting(i: int) -> int:
            if i == len(nums) - 1:
                return 1
            if i in memo:
                return memo[i]
            lis = 1  # you can always consider the element itself
            for j in range(i, len(nums)):
                explore_extend_seq = (
                    0 if nums[i] >= nums[j] else 1 + listForSubarrayStarting(j)
                )
                lis = max(lis, explore_extend_seq)
            memo[i] = lis
            return memo[i]

        return max([listForSubarrayStarting(i) for i in range(len(nums))])

