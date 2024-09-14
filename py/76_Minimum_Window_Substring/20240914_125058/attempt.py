from collections import Counter
from typing import Optional, Tuple


class Solution:
    # ADOBECODEBANC ABC
    #          ^  ^
    def minWindow(self, s: str, t: str) -> str:
        # {
        #   A:1
        #   B:1
        #   C:1
        # }
        t_counts = Counter(t)
        need = len(t_counts)  # 3

        # {
        #   A:1
        #   B:1
        #   C:1
        # }
        s_counts = Counter()
        have = 0  # 3

        result_bounds: Optional[Tuple[int, int]] = None  # 0,5

        def updateResultBounds(left: int, right: int) -> Optional[Tuple[int, int]]:
            return (
                (left, right)
                if result_bounds is None
                or (result_bounds[1] - result_bounds[0] > right - left)
                else result_bounds
            )

        left = 0  # 6
        for right in range(len(s)):  # 12
            c = s[right]  # C
            if c not in t_counts:
                continue
            s_counts[c] += 1
            if s_counts[c] == t_counts[c]:
                have += 1  # we are incrementing the counts here, so we increment `have` if we get to the target count post-increment
            if have == need:
                result_bounds = updateResultBounds(left, right)
                while left <= right and have == need:
                    result_bounds = updateResultBounds(left, right)
                    if s[left] in s_counts:  # C
                        s_counts[s[left]] -= 1
                        if s_counts[s[left]] < t_counts[s[left]]:
                            have -= 1
                    if have == need:
                        result_bounds = updateResultBounds(left, right)
                    left += 1
        return (
            "" if result_bounds is None else s[result_bounds[0] : result_bounds[1] + 1]
        )

