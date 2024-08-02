class Solution:
    def nextValidIndex(self, string: str, idx: int) -> int:
        # Cases to handle:
        # Now on a valid character
        # Now on a single backspace
        # Now on a contiguous sequence of backspaces
        # Think about:
        # Visiting character while having backspaces
        # Getting to the head of `string`
        backspace_count = 0
        while idx >= 0 or backspace_count > 0:
            backspace_count += 1 if string[idx] == "#" else -1
            idx -= 1 if backspace_count >= 0 else 0
            if backspace_count < 0 or idx < 0:
                break
        return idx

    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = self.nextValidIndex(s, i)
            j = self.nextValidIndex(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                # Why does this work? Why can you say that the strings aren't equal so long as one is able to get to the end before the other?
                # In particular, don't you worry about the case of s = "ab##" and t = "c#d#"?
                # Because you use `nextValidIndex to make sure that you are never visiting a backspace in this loop.
                return False
            i -= 1
            j -= 1
        return True

