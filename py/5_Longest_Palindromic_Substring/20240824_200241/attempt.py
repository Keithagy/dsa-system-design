class Solution:
    # n factorial brute force
    # n^2 approach of walking out from every char as center
    # there might be a dynamic programming approach..
    # s is a substring if s[0] and s[-1] are equal, and s[1:-1] is a palindrome
    # but then you would still have to carry this out on every character which makes it unlikely to be able to reuse computations
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def walk_from(left: int, right: int) -> int:
            length = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    length += 1 if right == left else 2
                    left -= 1
                    right += 1
            return length

        start = 0
        max_len = 0
        for i in range(len(s) - 1):
            len_odd = walk_from(i, i)
            len_even = walk_from(i, i + 1)
            max_len = max(len_odd, len_even, max_len)
            if max_len == len_odd:
                start = i - int(len_odd / 2)
            elif max_len == len_even:
                start = i - int(len_even / 2) + 1
        return s[start : (start + max_len)]

