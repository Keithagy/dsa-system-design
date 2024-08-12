from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + ((right - left) // 2)
            candidate = nums[middle]
            if candidate == target:
                return middle
            if nums[left] < candidate:  # left half is sorted, so use that to check
                if nums[left] <= target < candidate:
                    right = middle
                else:
                    left = middle + 1
            else:  # right half is sorted
                if candidate < target <= nums[right - 1]:
                    left = middle + 1
                else:
                    right = middle
        return left if left < len(nums) and nums[left] == target else -1

