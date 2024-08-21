from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        cur_sum = -float("inf")
        for num in nums:
            cur_sum = max(cur_sum + num, num)  # decide whether to start a new array
            max_sum = max(max_sum, cur_sum)
        return max_sum

