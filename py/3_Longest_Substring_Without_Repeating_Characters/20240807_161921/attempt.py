class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        chars = {}
        start = 0
        max_length = 0
        for i, c in enumerate(s):
            if c in chars and chars[c] >= start:
                start = chars[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            chars[c] = i
        return max_length

