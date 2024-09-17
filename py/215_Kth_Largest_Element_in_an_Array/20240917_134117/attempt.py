import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = (
                nums[right],
                nums[pivot_idx],
            )  # swap pivot value to end

            ordered_end = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[ordered_end] = nums[ordered_end], nums[i]
                    ordered_end += 1
            nums[ordered_end], nums[right] = (
                nums[right],
                nums[ordered_end],
            )  # place pivot in its right place
            if len(nums) - (ordered_end) == k:
                return nums[ordered_end]
            elif len(nums) - (ordered_end) > k:
                left = ordered_end + 1
            else:
                right = ordered_end - 1
        return nums[left]

