from typing import List


class Solution:
    # for any nums, the empty list always exists as an option ("skip all")
    # for [1], you have [] and [1]
    # for [1,2], you have [], [1], [2], [1,2]
    # [1,2] and [2,1] are considered duplicates
    # but you can avoid duplicate sets by allowing the Solution
    # to take only elements that come after
    # you can break the recurrence relation down in terms of take and skip for some ith element
    #
    # 0,[]
    #       1,[1]
    #               2,[1,2] >> return
    #               2,[1] >> return
    #       1,[]
    #               2,[2] >> return
    #               2,[] >> return
    #       return
    # return
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def inner(idx: int, taken: List[int]) -> List[List[int]]:
            if idx == len(nums):
                return [taken[:]]

            taken.append(nums[idx])
            take = inner(idx + 1, taken)
            taken.pop()
            skip = inner(idx + 1, taken)
            return take + skip

        return inner(0, [])

