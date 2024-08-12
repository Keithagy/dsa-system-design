from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            # the for loop ticking i up is how we prune the search space with each recursion
            # branches (len(candidates)) ways at every recursion
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result

        # candidates are at least 2 whilst target is at least 1
        # no repeats in candidates
        # can use a particular candidate any number of times
        # required to output the exact combination of elements >> need to track path
        #   backtracking required?
        # finding a way to make 7 from [2,3,6,7] at the onset
        # might be equivalent to finding 5 from [2,3,6,7], with [2] already selected
        # You might want to memoize a list of lists...
        # does it matter that we get sorted?
        #   no, because ordering doesn't matter and we are assured of uniqueness of elements,
        #   which means we aren't worried about repeating calculations
        # number of unique combinations is relatively small <15, so possibly able to consider an n^2 runtime complexity solution

        # memo = {}
        # def explore(path: List[int], target: int, i: int) -> List[int]:
        #     if target < 0:
        #         return []
        #     if target == 0:
        #         return path
        #     if
        #     # recurrence propagation: inner returns output for subproblem
        #     stay = explore(path + [candidates[i]], target - candidates[i], i)
        #     move_on = explore(
        #         path + [candidates[i + i]], target - candidates[i + 1], i + 1
        #     )
        #     return stay + move_on

        # tried a bottom up tabulation approach but brain exploded...
        # dp: List[Optional[List[int]]] = [None for _ in range(target)]
        # dp[0] = []  # zero ways to make 1
        # for subtarget in range(2, target):
        #     i = subtarget - 1 # offset to account for minimum target value of 1
        #     for candidate in candidates:

