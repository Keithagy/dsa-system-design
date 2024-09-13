from collections import Counter, defaultdict


class Solution:
    # what we can have is the counter of t
    # we essentially want to find the indices for some substring of s
    # for which the counter matches up to the counter of t
    # there is at one or zero answer.
    # there is definitely a repeated subproblem aspect of this
    # consider:
    # s: "abczde" t: "cd"
    #       ^ ^
    # implies
    # s: "aaaaaaaaabczde" t:"cd" >> has the same answer
    # so you can consider substrings? but then if you want to consider every single substring that's pretty long (2^n)
    # but maybe the dp window is a 2 dimensional array
    # suppose "abcde", of length 5, gives you... n^2?
    #   0 1 2 3 4
    # 0 a a a a a>> starting from 0, ending at 0 you can build up all the way to starting from 0 and ending at 4
    # 1 - b  >> starting at 1, ending at 1 and so on
    # 2 - -
    # 3 - - -
    # 4 - - - -
    # so this is a dp approach that reduces 2^n to n^2. you look for the minimum length and use those indices
    #
    # Do you have a sliding windows solution?
    # you do! because after you find a match for some substring, there is no point extending that substring. there wouldn't be an answer there.
    # you should move your head and tail and try to find a smaller window in the preceding.
    #
    # Input: s = "ADOBECODEBANC", t = "ABC"
    #                   ^
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        min_indices = None  # 0, 6
        t_counts = Counter(t)
        left = 0  # 6
        s_sub_counts = Counter()

        def containsTCounter(s: Counter) -> bool:
            for c in t_counts:
                if c in s and t_counts[c] <= s[c]:
                    continue
                return False
            return True

        for right in range(len(s)):  # 12
            s_sub_counts[s[right]] = s_sub_counts.setdefault(s[right], 0) + 1
            if containsTCounter(s_sub_counts):
                while containsTCounter(s_sub_counts):
                    print(left, right)
                    print(s_sub_counts)
                    print(t_counts)
                    s_sub_counts[s[left]] -= 1
                    if s_sub_counts[s[left]] == 0:
                        del s_sub_counts[s[left]]
                    left += 1
                left -= 1
                min_indices = (
                    min_indices
                    if min_indices is not None
                    and (min_indices[1] - min_indices[0]) < (right - left)
                    else (left, right + 1)
                )
                left = right
                s_sub_counts = Counter()
        return s[min_indices[0] : min_indices[1]] if min_indices is not None else ""

