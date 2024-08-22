from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        memo = {}

        def waysToMakeAmtWithCandidates(idx: int, amount: int) -> List[List[int]]:
            if amount < 0 or idx >= len(candidates):
                return []  # 0 ways
            if amount == 0:
                return [[]]  # 1 way, involving no coins at all
            if (idx, amount) in memo:
                return memo[(idx, amount)]
            ways_if_take_cur = [
                way + [candidates[idx]]
                for way in waysToMakeAmtWithCandidates(idx, amount - candidates[idx])
            ]
            ways_if_skip = waysToMakeAmtWithCandidates(idx + 1, amount)
            memo[(idx, amount)] = ways_if_take_cur + ways_if_skip
            return memo[(idx, amount)]

        return waysToMakeAmtWithCandidates(0, target)

