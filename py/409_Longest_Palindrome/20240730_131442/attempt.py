from typing import Counter, Dict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts: Dict[str, int] = Counter(s)

        sum_even_fragment_lengths = 0
        odd_fragments = []
        most_frequent_odd_char = ("", 0)

        for c, count in counts.items():
            if count % 2 == 0:
                sum_even_fragment_lengths += count
            else:
                odd_fragments.append((c, count))
                if count > most_frequent_odd_char[1]:
                    most_frequent_odd_char = (c, count)

        result = sum_even_fragment_lengths
        for c, count in odd_fragments:
            if c == most_frequent_odd_char[0]:
                result += count
            else:
                result += count - 1

        return result

