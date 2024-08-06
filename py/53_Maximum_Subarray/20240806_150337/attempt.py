from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            # decide if starting a new subarray or extending the existing one
            current_sum = max(num, current_sum + num)
            #  keep track of current_sum if it is highest seen thus far
            max_sum = max(max_sum, current_sum)
        return max_sum

