from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1
        while left <= right:
            left_abs = abs(nums[left])
            right_abs = abs(nums[right])
            larger_abs = max(left_abs, right_abs)
            result.append(larger_abs**2)
            if larger_abs == left_abs:
                left += 1
            else:
                right -= 1
        return result[::-1]
