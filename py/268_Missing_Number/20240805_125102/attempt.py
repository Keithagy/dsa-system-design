from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums) + 1):
            sum += i
        for num in nums:
            sum -= num
        return sum

