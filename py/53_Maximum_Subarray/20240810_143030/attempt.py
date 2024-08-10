from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # core intuition: every time you visit a new number, you either start a new subarray or extend the previous
        max_sum = cur_sum = -(float("inf"))
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return int(max_sum)

