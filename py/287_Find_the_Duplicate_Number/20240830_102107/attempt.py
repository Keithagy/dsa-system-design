from typing import List


class Solution:
    # [3,1,3,4,2]
    #
    # [1,2,3,4,5]
    # [2,-1,0,0,-3]
    # n = 3
    # len(nums) = 4
    # [1,2,2,2] can be [1,3]
    # range(1,4)
    def findDuplicate2(self, nums: List[int]) -> int:
      nums.sort()
      for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
          return nums[i]
      
    def findDuplicate(self, nums: List[int]) -> int:
      count = 0
      for possible in range(1,len(nums)):
        for num in nums:
          if num == possible:
            count+=1
          if count >1:
            return possible
        count = 0
      return -1
