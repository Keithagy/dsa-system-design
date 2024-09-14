from collections import defaultdict
from typing import List


class Solution:
    # Core intuition
    # For the imbalance score of sum subarray nums,
    # If you've previously seen that imbalance score in an earlier subarray,
    # then the subarray in between here there and must be balanced.
    # For every imbalance score, if you have multiple such imbalance scores
    # You want to choose the earliest one, so as to find the earliest subarray
    def findMaxLength(self, nums: List[int]) -> int:
        score = 0
        first_seen_score = {}
        first_seen_score[0] = -1

        longest = 0
        for i in range(len(nums)):
            score += 1 if nums[i] == 1 else -1
            if score not in first_seen_score:
                first_seen_score[score] = i
            else:
                longest = max(longest, i - first_seen_score[score])
        return longest

