from typing import List, Set

"""
        false
        [1,5,3]
        [1,7,6,5]

        true
        [1,100,99]
        [1,2,6,7]

        observations:
        for a sum to exist, since they are integers, half of the sum of all numbers must be an interger
        i.e sum must be divisable by 2
        target_sum = sum(nums) / 2 where sum(nums) % 2 == 0
        the goal here is to find some collection of elements which would add up to target_sum


        [1,100,99]
        target_sum = 100

        ---
        target = 100
        used = {}
        ---
            ---
            target = 99
            used = {0}
            ---
                ---
                target = -1
                used = {0,1}
                ---
                ---
                target = 0
                used = {0,2}
                ---
        """


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target_sum = sum_nums // 2

        memo = {}

        def canMakeTarget(target: int, idx: int) -> bool:
            if target < 0 or idx == len(nums):
                return False
            if target == 0:
                return True
            if (target, idx) in memo:
                return memo[(target, idx)]
            memo[(target, idx)] = canMakeTarget(
                target - nums[idx], idx + 1
            ) or canMakeTarget(target, idx + 1)
            return memo[(target, idx)]

        return canMakeTarget(target_sum, 0)

