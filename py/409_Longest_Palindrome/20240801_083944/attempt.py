class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_chars = set()
        for c in s:
            if c in odd_chars:
                odd_chars.remove(c)
            else:
                odd_chars.add(c)
        return len(s) - len(odd_chars) + (1 if odd_chars else 0)

