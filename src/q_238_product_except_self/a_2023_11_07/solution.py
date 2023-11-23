from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Concept of this solution is that you can memoize the mutliplications of elements to left in one pass
        # And then memoize the multiplications of elements to the right in a second pass
        length = len(nums)
        result = [1] * length
        for left in range(1, length, 1):
            result[left] = nums[left - 1] * result[left - 1]

        right_accumulator = nums[length - 1]
        for right in range(length - 2, -1, -1):
            result[right] = result[right] * right_accumulator
            right_accumulator *= nums[right]
        return result
