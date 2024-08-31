from typing import List


class Solution:
    # no ordering to elements
    # Single pass solution?
    # start pointer at first element, run till second last
    # compare cur with next; if next > cur, increment run_len
    # update max_len with max(run_len, max_len)
    # if next <= cur, end iteration by reseting run_len to 0
    #
    # test input: [1,0,2,1,2,3] >> 3 [0,2,3]
    # [(0,1),(1,0),(2,2),(3,1),(4,2),(5,3)]
    # [(0,1),(1,0),(2,2),(3,1),(4,2),(5,3)]
    # [(1,0),(0,1),(3,1),(2,2),(4,2),(5,3)]
    # >> use a monotonic stack; prefer lowest-index for a given value
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                stack.append(num)
        return len(stack)

