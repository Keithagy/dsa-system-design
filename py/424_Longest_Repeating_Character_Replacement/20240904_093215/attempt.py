from collections import defaultdict


class Solution:
    # input: ABAB, k: 1, expect: 3
    def characterReplacement(self, s: str, k: int) -> int:
        # {
        #   A: 1
        #   B: 2
        # }
        counts = defaultdict(int)
        left = 0  # 1
        res = 0  # 3
        max_freq = 0  # 3

        def subLen(left: int, right: int) -> int:
            return right - left + 1

        def acceptableSubCount(subLen: int, max_freq: int) -> bool:
            return subLen - max_freq <= k

        for right in range(len(s)):  # 3
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])
            while not acceptableSubCount(subLen(left, right), max_freq):
                counts[s[left]] -= 1
                left += 1
            res = max(subLen(left, right), res)
        return res

