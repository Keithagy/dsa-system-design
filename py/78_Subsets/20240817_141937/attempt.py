from typing import List


class Solution:
    # start from idx 0, acc [], nums [1,2,3]
    # add result to empty List
    # take first item >> add [1]
    # skip first item >> add []
    # take second item >> add [1,2]
    # take third item >> add [1,2,3]
    # take fourth item >> return
    # skip fourth item >> return
    # skip third item >> add [1,2]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def inner(idx: int, acc: List[int]) -> None:
            if idx >= len(nums):
                return
            result.add(
                tuple(acc)
            )  # automatically drops things like repeat empty list, repeat ([1,2])
            # don'e have to worry about (1,2) and (2,1) because recursion only considers upwards and all nums are unique
            # take or skip
            inner(idx + 1, [nums[idx]] + acc)
            inner(idx + 1, acc)

        inner(-1, [])
        return [list(tup) for tup in result]

