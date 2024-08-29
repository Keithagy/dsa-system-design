from typing import List


class Solution:
    # You are given nums, which contains information about element counts
    # nums has its own arrangement which sits on some lexicographical order
    # You need to give the next permutation on this order (or wrap around if it is highest)
    # if it is the highest, then the array will be sorted in non-asc order (largest to smallest)
    # if it is the lowest, similarly will be non-desc order (smallest to largest)
    # when visiting a number, how do i know whether to increment that?
    # observation: from input to output, there is always just 1 swap
    # [123] [321] [115]
    # [132] [123] [151]
    #  ^ ^   ^ ^    ^^
    # For each place, you can ask yourself the question: am i largest in my tier?
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 

