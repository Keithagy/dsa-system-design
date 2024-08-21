from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            target = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                diff = sum - target
                if diff == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # cannot have duplicate triplets, so need to consider next unique j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                elif diff > 0:  # need to make smaller
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:  # need to make bigger
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return result

