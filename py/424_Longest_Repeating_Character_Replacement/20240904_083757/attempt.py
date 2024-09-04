from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def validIdx(idx: int) -> bool:
            return 0 <= idx < len(s) - 1

        def walkOutFrom(idx: int) -> int:
            if not validIdx(idx):
                return -1  # invalid
            subs_left = k
            subbing = "_"

            left = right = idx
            result = 1
            while validIdx(right) and validIdx(right + 1):
                next = s[right + 1]
                if s[right + 1] != s[right]:
                    if subbing == "_":
                        subbing = s[right + 1]

            return result

        result = 0
        for i in range(len(s)):
            result = max(walkOutFrom(i), result)
        return result

