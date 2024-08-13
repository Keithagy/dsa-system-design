from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # result = [[] for _ in range(target + 1)]
        candidates.sort()

        memo = {}

        def dp(idx: int, subtarget: int) -> List[List[int]]:
            if subtarget < 0 or idx >= len(candidates):
                return []  # problem out of range since minimum coin value is 2
            if subtarget == 0:
                return [[]]

            if (idx, subtarget) in memo:
                return memo[(idx, subtarget)]
            # At each state of the recursion, you can either take the current coin, or you can skip
            skip = dp(idx + 1, subtarget)
            paths_if_take = dp(idx, subtarget - candidates[idx])

            take = []
            for path in paths_if_take:
                take.append(path + [candidates[idx]])
            memo[(idx, subtarget)] = skip + take
            return skip + take

        return dp(0, target)

