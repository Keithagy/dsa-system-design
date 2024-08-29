from typing import List


class Solution:
    # Key intuition: for any (sub)series, the smallest / largest permutation strictly increases / decreases
    # so you find the first i for which nums[i:] isn't strictly decreasing
    # then, you find smallest j in nums[i+1:] s.t nums[j] > nums[i]
    # swap i and j -> after this, nums[i+1:] retains decreasing order, since you found the smallest j that is larger than i
    # so you reverse that subarray to get the next permutation
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if not i >= 0:
            reverse(0, len(nums) - 1)
            return

        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        reverse(i + 1, len(nums) - 1)

