from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        start = 0
        count = 0
        while count < n:
            i = (start + k) % n
            tmp = nums[start]
            while count < n and i != start:
                tmp, nums[i] = nums[i], tmp
                i = (i + k) % n
                count += 1

            tmp, nums[i] = nums[i], tmp
            count += 1
            start += 1

