from collections import defaultdict
from typing import List


class Solution:
    # substrings within s have to be of length `len(p)`
    # They have to be substrings, which means they have to be contiguous
    # Could you just move a window through and check for count?
    # start ranging at 0, end range at len(s) - len(p) +1, increment by 1
    # maintain a counter for the window. if counter matches then append to list
    # So you can single-pass solve this with O((len(s))) time and O((len(p))) space.
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = defaultdict(int)
        for c in p:
            p_counter[c] += 1

        def check_equal(s_counter, p_counter):
            if len(p_counter) != len(s_counter) or len(
                set(list(p_counter.keys()) + list(s_counter.keys()))
            ) != len(p_counter.keys()):
                return False
            for c in p_counter:
                if c not in s_counter:
                    return False
                count = p_counter[c]
                if count != s_counter[c]:
                    return False
            return True

        s_counter = defaultdict(int)
        for i in range(0, len(s) - len(p) + 1, 1):
            possible_anagram = s[i : i + len(p)]
            if i == 0:
                for c in possible_anagram:
                    s_counter[c] += 1
            else:
                s_counter[s[i - 1]] -= 1
                if s_counter[s[i - 1]] == 0:
                    del s_counter[s[i - 1]]
                s_counter[possible_anagram[-1]] += 1
            if check_equal(s_counter, p_counter):
                result.append(i)
        return result

