class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            if s[i] == "#":
                backspace_count = 1
                while i >= 0 and backspace_count >= 0:
                    i -= 1
                    backspace_count += 1 if s[i] == "#" else -1

            if t[j] == "#":
                backspace_count = 1
                while j >= 0 and backspace_count >= 0:
                    j -= 1
                    backspace_count += 1 if t[j] == "#" else -1

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True

