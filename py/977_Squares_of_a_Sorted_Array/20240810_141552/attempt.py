from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1

        while left <= right:
            left_abs, right_abs = abs(nums[left]), abs(nums[right])
            larger_abs = max(left_abs, right_abs)
            if larger_abs == left_abs:
                next_square = left_abs**2
                result.append(next_square)
                left += 1
            else:
                next_square = right_abs**2
                result.append(next_square)
                right -= 1
        return result[::-1]

