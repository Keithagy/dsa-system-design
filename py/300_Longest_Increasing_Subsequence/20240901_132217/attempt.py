from typing import List


class Solution:
    # The core question you need to answer, for each element, is whether there is some increasing subsequence you are a part of
    # The final question is ultimately to take or to skip
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def lis(idx: int, prev: int) -> int:
            if idx == len(nums):
                return 0  # Impossible option
            if (idx, prev) in memo:
                return memo[(idx, prev)]
            take = 0
            if nums[idx] > prev:
                # Because you can always have the option of considering an element on its own
                # if you choose to take it
                take = 1 + lis(idx + 1, nums[idx])
            skip = lis(idx + 1, prev)
            memo[(idx, prev)] = max(take, skip)
            return memo[(idx, prev)]

        return lis(0, float("-inf"))

