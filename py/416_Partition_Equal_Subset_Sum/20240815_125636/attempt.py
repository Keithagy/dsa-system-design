from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        nums.sort()  # n log n
        left_accu = 0
        right_accu = sum(nums)
        for pivot in range(len(nums)):
            left_accu += nums[pivot]
            right_accu -= nums[pivot]
            if left_accu == right_accu:
                return True
        return False

