from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left_accumulator = 1
        for i in range(1, len(nums), 1):
            left_accumulator *= nums[i - 1]
            result[i] *= left_accumulator

        right_accumulator = 1
        for j in range(len(nums) - 2, -1, -1):
            right_accumulator *= nums[j + 1]
            result[j] *= right_accumulator
        return result

