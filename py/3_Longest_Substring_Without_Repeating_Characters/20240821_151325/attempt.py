class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c] + 1
            length = i - start + 1
            max_length = max(max_length, length)
            last_seen[c] = i
        return max_length

