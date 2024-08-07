class Solution:
    def hasRepeats(self, s: str) -> bool:
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
                continue
            return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                candidate = s[i:j]
                if self.hasRepeats(candidate):
                    continue
                max_length = max(len(candidate), max_length)
        return max_length

