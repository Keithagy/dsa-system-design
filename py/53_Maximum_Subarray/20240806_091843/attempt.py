from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Everytime you encounter a negative number,
        # the question is simply about whether there is a positive subarray that sums up to a greater value beyond it.
        islands = []
        for i in range(len(nums)):
            start_incl = i
            end_excl = i
            if nums[i] < 0:
                # should start a new island




        
