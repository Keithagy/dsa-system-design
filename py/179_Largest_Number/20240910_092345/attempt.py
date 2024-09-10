from typing import List
import functools


class Solution:
    # You have a few components to this question:
    # picking permutation
    # comparing 2 numbers on the basis of their string representations
    # tracking largest seen so far
    #
    # there is an n! answer that is based on visiting every single possible permutation.
    # can we do better than that, since nums can have decently large length?
    # You probably want to put the largest digit first.
    # You can get the largest number by placing the largest digit first.
    # Somewhat akin to lexicographical comparison
    # edge case: first digit is same, but one is longer
    # 3, 30 >> 303 vs 330. should put 3 first
    # 7,79 >> 779 vs 797. should put 79 first
    # 3,30,34 >> largest is 34 | 3 | 30
    # basically, if ints share a first digit, then place the longer 1 first unless the trailing digit is 0
    # You can use a queue, append left if should come first... but this doesn't handle cases where a middle number shows up later in the list.
    def largestNumber(self, nums: List[int]) -> str:
        def lex_mod(s1: str, s2: str) -> int:
            if s1 + s2 < s2 + s1:
                # s2 should come first
                return 1
            else:
                return -1

        result = sorted([str(num) for num in nums], key=functools.cmp_to_key(lex_mod))
        return "".join(result) if result[0] != "0" else "0"

