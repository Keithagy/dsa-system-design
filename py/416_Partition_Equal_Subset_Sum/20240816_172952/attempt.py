from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False  # target sum has to be an integer
        target_sum = sum_nums // 2

        # Can i make some target sum with some coins?
        # I can amount 0 with any number of coins.
        # That means i can make (0, 1) if coins [1] if i take or skip
        # That means i can make (0,1,2,3) if coins [1,2] if i take or skip at each point
        # For a given set of coins, i can know if i can make amount k by asking if i can make amount (k-c[idx]), where idx is the latest coin to be considered.
        # that subtraction can get me to 0, or it can get me to negative.
        # if negative, then i can't.
        # if 0 (or something that leads to 0), then i can.
        memo = {}

        def canMakeAmtWithCoinsToIdx(amt: int, idx: int) -> bool:
            if amt < 0:
                memo[(amt, idx)] = False
                return False
            if amt == 0:
                return True
            if idx == -1:
                return False
            if (amt, idx) in memo:
                return memo[(amt, idx)]
            result = canMakeAmtWithCoinsToIdx(
                amt - nums[idx], idx - 1
            ) or canMakeAmtWithCoinsToIdx(amt, idx - 1)
            memo[(amt, idx)] = result
            return result

        return canMakeAmtWithCoinsToIdx(target_sum, len(nums) - 1)

