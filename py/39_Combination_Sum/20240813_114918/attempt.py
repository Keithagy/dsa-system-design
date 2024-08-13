from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # asymptotically, this isn't significant, but lets us return early on many paths on the "rate limiting" step
        result = []

        def inner(
            idx: int, target: int, path: List[int]
        ) -> (
            None
        ):  # recurisve call mutates `result` which accumulates paths found across entire call graph
            if target == 0:
                result.append(path[:])  # copy out the successful path
            if target < 0:
                return  # backtrack because you've exceeded the target
            # At each point, you have two options available: take or skip
            for i in range(idx, len(candidates), 1):
                inner(i, target - candidates[i], path + [candidates[i]])
                # skip is implicit, modelled by the recusive call returning and for loop ticking up the candidate to try

        inner(0, target, [])
        return result

