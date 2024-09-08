from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if_cnt_max = max_so_far * cur
            if_cnt_min = min_so_far * cur
            max_so_far = max(if_cnt_max, if_cnt_min, cur)
            min_so_far = min(if_cnt_max, if_cnt_min, cur)
            result = max(result, max_so_far)
        return result

