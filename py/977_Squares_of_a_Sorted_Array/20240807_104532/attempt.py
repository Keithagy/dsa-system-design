from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums))[::-1]:
            left_abs = abs(nums[left])
            right_abs = abs(nums[right])
            larger_abs = max(left_abs, right_abs)
            if larger_abs == left_abs:
                result[i] = left_abs**2
                left += 1
            else:
                result[i] = right_abs**2
                right -= 1
        return result

