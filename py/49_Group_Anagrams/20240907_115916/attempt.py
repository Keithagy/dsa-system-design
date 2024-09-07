from collections import defaultdict
from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        def sig(s: str) -> Tuple[int, ...]:
            ascii_lower_count = 26
            result = [0 for _ in range(ascii_lower_count)]
            for c in s:
                idx = ord(c) - ord("a")
                result[idx] += 1
            return tuple(result)

        for s in strs:
            groupings[sig(s)].append(s)
        return [group for group in groupings.values()]

