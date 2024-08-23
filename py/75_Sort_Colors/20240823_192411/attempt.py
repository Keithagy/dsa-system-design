from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        input: [2,0,1,0,2]
        output: [0,0,1,2,2]

        [2,0,1,0,2]
         i,j     k

        [2,0,1,0,2]
         i,j   k

        [0,0,1,2,2]
         i,j k

             k
        [0,0,1,2,2]
             i j
        --------
             k
        [2,0,1]
        i,j

           k
        [1,0,2]
         i j

        """
        i = 0
        j = 0
        k = len(nums) - 1
        while i <= j <= k:
            if nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1  # Do not increment mid because you need to check if this number is correct
                continue
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                continue
            if nums[j] == 1:
                j += 1

