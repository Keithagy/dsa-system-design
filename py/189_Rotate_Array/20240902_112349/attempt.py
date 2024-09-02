from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rots = k % n
        if rots == 0:
            return
        count = 0

        def swapStarting(start_point: int) -> None:
            nonlocal count
            pivot_idx = start_point
            tmp = nums[pivot_idx]
            while True:
                target_idx = (pivot_idx + k) % n
                tmp, nums[target_idx] = nums[target_idx], tmp
                pivot_idx = target_idx
                count += 1
                if pivot_idx == start_point:
                    break

        for start in range(n):
            if count >= n:
                return
            swapStarting(start)

