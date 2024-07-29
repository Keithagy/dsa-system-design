from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looking_out_for = {}
        for index, num in enumerate(nums):
            want = target - num
            if want in looking_out_for:
                return [looking_out_for[want], index]
            looking_out_for[num] = index
        return []
