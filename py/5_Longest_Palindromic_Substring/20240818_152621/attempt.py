class Solution:
    # You can represent the longest palindromic substring with some start idx, and some length
    # This length should be the maximum palindrome length possible.
    # In order to figure this out, you probably need to iterate through each character,
    # Walk out the longest palindrome possible with each character as the starting point
    # then overwrite the length and the start if it is in fact the longest
    # You should check for both the cases where you have an even length palindrome, as well as an odd one
    # most challenging input is probably "bbb"
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start = 0  # min s length is 1
        max_length = 0

        def walk_out(left: int, right: int) -> int:
            pal_len = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    pal_len += 2 if right != left else 1
                    right += 1
                    left -= 1
                else:
                    break
            return pal_len

        for i in range(len(s) - 1):  # needs lookahead of 1
            odd_pal_len = walk_out(i, i)
            even_pal_len = walk_out(i, i + 1)
            longest_from_cur = max(odd_pal_len, even_pal_len)

            if longest_from_cur >= max_length:
                max_length = longest_from_cur
                start = i - ((max_length - 1) // 2)
        return s[start : start + max_length]

