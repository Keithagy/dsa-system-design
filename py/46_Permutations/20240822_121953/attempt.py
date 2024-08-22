from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        memo = {}

        def permutations(k: int) -> List[List[int]]:
            if k == 0:
                return [[nums[0]]]
            if k in memo:
                return memo[k]
            result = []
            sub_problem = permutations(k - 1)
            for perm in sub_problem:
                gaps = len(perm) + 1
                for i in range(gaps):
                    result.append(perm[:i] + [nums[k]] + perm[i:])
            memo[k] = result
            return memo[k]

        return permutations(len(nums) - 1)

