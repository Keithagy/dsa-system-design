from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        left_acc = nums[0]
        for i in range(1, len(nums), 1):
            result[i] *= left_acc
            left_acc *= nums[i]
        right_acc = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] *= right_acc
            right_acc *= nums[i]
        return result

