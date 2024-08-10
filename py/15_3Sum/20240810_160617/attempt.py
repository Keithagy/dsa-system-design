from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort to eliminate duplicates
        n = len(nums)
        result = []
        i = 0
        while i < n - 2:
            # ok to hardcode initial values given that n >= 3
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
            while i < n - 3 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return result

