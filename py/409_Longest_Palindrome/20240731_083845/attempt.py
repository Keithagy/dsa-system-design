class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_chars = set()
        for c in s:
            if c not in odd_chars:
                odd_chars.add(c)
            else:
                odd_chars.remove(c)

        return len(s) - len(odd_chars) + (1 if len(odd_chars) > 0 else 0)

