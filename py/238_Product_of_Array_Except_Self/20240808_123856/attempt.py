from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        right_accumulator = 1
        for j in range(len(nums) - 2, 0, -1):
            right_accumulator *= nums[j + 1]
            result[j] = right_accumulator * result[j]

