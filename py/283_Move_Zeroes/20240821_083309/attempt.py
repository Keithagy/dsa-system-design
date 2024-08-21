from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != non_zero_pos:
                    nums[i], nums[non_zero_pos] = nums[non_zero_pos], nums[i]
                non_zero_pos += 1

