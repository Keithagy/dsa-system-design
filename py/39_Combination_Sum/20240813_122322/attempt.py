from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = [[] for _ in range(target + 1)]

        for subtarget in range(target + 1):
            if subtarget <= 1:
                continue  # out of problem range since smallest coin is 2
            paths = []
            for i in range(len(candidates)):
                remaining = subtarget - candidates[i]
                if remaining == 0:
                    paths.append(
                        [candidates[i]]
                    )  # e.g. [7] is a way to make 7 with coin 7
                elif remaining == 1 or remaining < 0:
                    continue  # smallest coin is 2, so no ways to make 1 with coin 2
                else:
                    # E.g if coin is 5, subtarget is 7, then you can get ways to make 7 with coin 5 by adding [5] to all the ways to make 2 calculated earlier
                    ways_to_make_remaining = result[remaining]
                    for way in ways_to_make_remaining:
                        if candidates[i] >= way[-1]:
                            paths.append(way + [candidates[i]])
            result[subtarget] = paths
        return result[-1]

