from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = int((n * (n + 1)) / 2)
        for num in nums:
            total_sum -= num
        return total_sum

