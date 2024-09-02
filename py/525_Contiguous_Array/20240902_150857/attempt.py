from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen_diff = {}
        count = 0
        max_len = 0
        for idx, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count == 0:
                max_len = idx + 1
            else:
                if count in first_seen_diff:
                    max_len = max(max_len, idx - first_seen_diff[count])
                else:
                    first_seen_diff[count] = idx
        return max_len

