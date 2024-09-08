from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0
        for num in nums:
            if num - 1 in numSet:
                continue
            seq_len = 1
            cur = num
            while cur + 1 in numSet:
                cur += 1
                seq_len += 1
            result = max(result, seq_len)
        return result

