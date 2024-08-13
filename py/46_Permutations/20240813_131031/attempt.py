from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # e.g. path = [0]
        def permutations(path: List[int]) -> List[List[int]]:
            next = set(nums)
            for already in path:
                next.remove(already)

            if not next:
                return [path[:]]

            paths_from_here = []
            for step in next:
                # permutations([0, 1]) >> permutations([0,1,2])
                # permutations([0, 2]) >> permutations([0,2,1])
                paths_from_here.extend(permutations(path + [step]))
            return paths_from_here

        return permutations([])

