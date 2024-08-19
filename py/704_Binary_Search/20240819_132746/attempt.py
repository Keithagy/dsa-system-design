from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def predicate(num: int) -> bool:
            return num >= target

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if predicate(nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1

