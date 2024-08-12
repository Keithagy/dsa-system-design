from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            if (
                nums[left] < nums[mid]
            ):  # left half is the sorted half (assuming worst case of only one sorted half)
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # you get here only if there is exactly one sorted half, and it's the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if 0 <= left < len(nums) and nums[left] == target else -1

