from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}  # could laos be a set
        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1
            if counts[num] > 1:
                return True
        return False

