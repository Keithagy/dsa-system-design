from collections import defaultdict
from typing import Dict


class Solution:
    # anagrams ==> equal character count
    # can solve this with a sliding window
    # when window moves through s, can just add the latest char and remove the earliest one for O(1) window update
    # O(n) time where n is len(s)
    # O(m) space where m is len(p)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # {
        #   "a": 1,
        #   "b": 1,
        # }
        p_counts = defaultdict(int)
        for c in p:
            p_counts[c] += 1

        result = []  # [0,1]

        s_sub_counts = defaultdict(int)

        def deep_eq(d1: Dict[str, int], d2: Dict[str, int]) -> bool:
            if len(d1) != len(d2):
                return False
            for key in set(list(d1.keys()) + list(d2.keys())):
                if not (key in d1 and key in d2):
                    return False
                if not (d1[key] == d2[key]):
                    return False
            return True

        # {
        #  "b": 1
        #  "a": 1
        # }
        for i in range(len(s)):  # 2
            if i >= len(p):  # 2
                s_sub_counts[s[i - len(p)]] -= 1
                if s_sub_counts[s[i - len(p)]] == 0:
                    del s_sub_counts[s[i - len(p)]]
            s_sub_counts[s[i]] += 1
            if deep_eq(s_sub_counts, p_counts):
                result.append(i - len(p) + 1)
        return result

