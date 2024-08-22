from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(idx: int, amount: int) -> None:
            if idx == len(candidates) or amount < 0:
                return  # used all coins
            if amount == 0:
                result.append(path[:])
                return  # Found a valid makeup
            for i in range(idx, len(candidates)):
                visit(i, amount - candidates[i])

        def visit(idx: int, amount: int) -> None:
            path.append(candidates[idx])
            backtrack(idx, amount)
            path.pop()

        backtrack(0, target)
        return result

