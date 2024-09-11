from typing import List


class Solution:
    """
    sorting does not help because you always have the chance that nums aren't adjacent
    i will just write the n^2 solution
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = None
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while 0 <= j < k < len(nums):
                sum = nums[i] + nums[j] + nums[k]
                if closest_sum is None:
                    closest_sum = sum
                else:
                    diff = sum - target
                    cur_diff = closest_sum - target
                    closest_sum = closest_sum if abs(diff) > abs(cur_diff) else sum
                    if diff == 0:
                        return sum
                    if diff < 0:  # try make sum larger
                        while j < k and nums[j + 1] == nums[j]:
                            j += 1
                        j += 1
                        continue
                    if diff > 0:
                        while j < k and nums[k - 1] == nums[k]:
                            k -= 1
                        k -= 1
        assert closest_sum is not None
        return closest_sum

