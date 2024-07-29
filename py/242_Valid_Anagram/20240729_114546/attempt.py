class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}  # key: char, val: count
        for c in s:
            char_count[c] = char_count.setdefault(c, 0) + 1

        for c2 in t:
            if c2 not in char_count:
                return False
            curr_count = char_count[c2]
            char_count[c2] = curr_count - 1
            if char_count[c2] == 0:
                del char_count[c2]
        return len(char_count) == 0

