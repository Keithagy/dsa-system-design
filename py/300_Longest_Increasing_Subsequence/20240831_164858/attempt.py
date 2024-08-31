from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def lis(idx: int) -> int:
            if idx == len(nums) - 1:
                return 1
            if idx in memo:
                return memo[idx]
            options = [1]
            options.extend(
                [
                    1 + lis(option)
                    for option in range(idx + 1, len(nums))
                    if nums[idx] < nums[option]
                ]
            )
            memo[idx] = max(options)
            return memo[idx]

        return max([lis(i) for i in range(len(nums))])
