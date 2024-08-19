from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pool = defaultdict(int)
        for c in magazine:
            pool[c] += 1
        for c in ransomNote:
            if c not in pool:
                return False
            pool[c] -= 1
            if pool[c] == 0:
                del pool[c]
        return True

