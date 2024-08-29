from typing import List


class Solution:
    # [2,3,-2,4]
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]  # 6
        end = 0  # 1
        for i, num in enumerate(nums[1:]):  # 3,4
            idx = i + 1
            continue_or_new = max(
                num, result * num if end == idx - 1 else num
            )  # max(4, 4) >> 4
            result = max(result, continue_or_new)  # 6
            if result == continue_or_new:
                end = idx

        return result

