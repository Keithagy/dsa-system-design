from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def cont(x):
            return nums[x]

        # Phase 1: Detect cycle
        tortoise = cont(0)
        hare = cont(cont(0))
        while tortoise != hare:
            tortoise = cont(tortoise)
            hare = cont(cont(hare))

        # Phase 2: Find the start of the cycle
        tortoise = 0
        while tortoise != hare:
            tortoise = cont(tortoise)
            hare = cont(hare)

        return tortoise  # This is the duplicate number
