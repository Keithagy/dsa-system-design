from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Remember that binary search is about finding the smallest i such that nums[i] still satisfies predicate k
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1

