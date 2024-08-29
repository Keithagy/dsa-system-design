from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums), 1):
            cur = nums[i]
            if_cnt_max = max_so_far * cur
            if_cnt_min = min_so_far * cur
            max_so_far = max(cur, if_cnt_max, if_cnt_min)
            min_so_far = min(cur, if_cnt_max, if_cnt_min)
            result = max(result, max_so_far)
        return result

