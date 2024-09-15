from collections import defaultdict


class Solution:
    # Core idea here is that you want to go through the list keeping track of the most frequent character
    # anything else that isn't that character, you can substitute.
    # if you don't have enough substitutions, you have to drop that character by incrementing a start counter
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_length = 0
        most_freq = 0

        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            most_freq = max(most_freq, counts[s[right]])
            replacements = right - left + 1 - most_freq
            if replacements > k:
                while left < right and replacements > k:
                    to_drop = s[left]
                    counts[to_drop] -= 1
                    left += 1
                    replacements = right - left + 1 - most_freq
            max_length = max(max_length, right - left + 1)
        return max_length

