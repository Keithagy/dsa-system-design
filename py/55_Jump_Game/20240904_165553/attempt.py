from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False for _ in range(len(nums))]
        reachable[0] = True

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                is_j_reachable = reachable[j]
                is_i_reachable_from_j = nums[j] >= (i - j)
                if is_j_reachable and is_i_reachable_from_j:
                    reachable[i] = True
                    break
        return reachable[-1]

