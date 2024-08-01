class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = len(s) - 1
        j = len(t) - 1
        backspace_char = "#"

        while i > 0 or j > 0:
            # Handle backspace (and sequences thereof)
            s_num_chars_to_skip = 0
            while i >= 0 and s[i] == backspace_char:
                s_num_chars_to_skip += 1
                i -= 1
            t_num_chars_to_skip = 0
            while j >= 0 and t[j] == backspace_char:
                t_num_chars_to_skip += 1
                j -= 1

            # Handle character skipping
            while s_num_chars_to_skip > 0:
                s_num_chars_to_skip += 1 if i >= 0 and s[i] == backspace_char else -1
                i -= 1

            while t_num_chars_to_skip > 0:
                t_num_chars_to_skip += 1 if j >= 0 and t[j] == backspace_char else -1
                j -= 1

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
                    continue
            elif i < 0:
                if t[j] == backspace_char:
                    continue
                else:
                    return False
            else:
                if s[i] == backspace_char:
                    continue
                else:
                    return False

        return True

