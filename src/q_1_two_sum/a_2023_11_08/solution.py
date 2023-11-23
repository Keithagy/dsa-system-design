from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentary_values = {}
        for i in range(len(nums)):
            complimentary_value = target - nums[i]
            if complimentary_value in complimentary_values:
                return [i, complimentary_values[complimentary_value]]

            complimentary_values[complimentary_value] = i
        raise Exception()
