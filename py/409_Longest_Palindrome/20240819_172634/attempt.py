from collections import defaultdict


class Solution:
    # We need a case-sensitive count of all the characters.
    # All the even chars can be used wholesale
    # Odd-count chars can be used if you drop 1
    # If there is at least one odd-count char, you can add one to your final total (middle character)
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        at_least_one_oddcount_char = False
        result = 0
        for c in counts:
            count = counts[c]
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                if not at_least_one_oddcount_char:
                    at_least_one_oddcount_char = True
        return result if not at_least_one_oddcount_char else result + 1

