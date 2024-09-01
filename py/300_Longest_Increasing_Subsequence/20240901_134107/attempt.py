from typing import List
import bisect


class Solution:
    # [10,9,2,5,3,7,101,18]
    def lengthOfLIS(self, nums: List[int]) -> int:
        smallest_end_at = []  # [2,3,7,18]
        for num in nums:  # 18
            if not smallest_end_at or smallest_end_at[-1] < num:
                smallest_end_at.append(num)
            else:
                idx = bisect.bisect_left(smallest_end_at, num)  # 0
                smallest_end_at[idx] = num
        return len(smallest_end_at)

