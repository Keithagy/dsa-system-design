from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = defaultdict(int)
        for c in s:
            s_counts[c] += 1
        t_counts = defaultdict(int)
        for c in t:
            t_counts[c] += 1
        s_chars = list(s_counts.keys())
        for c in s_chars:
            if c not in t_counts or s_counts[c] != t_counts[c]:
                return False
            del s_counts[c]
            del t_counts[c]
        return not s_counts and not t_counts

