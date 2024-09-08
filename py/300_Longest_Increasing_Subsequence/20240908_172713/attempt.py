from typing import List
import bisect


class Solution:
    # patience sorting approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []
        for num in nums:
            if not piles or piles[-1] < num:
                piles.append(num)
                continue
            idx = bisect.bisect_left(piles, num)
            piles[idx] = num
        return len(piles)

