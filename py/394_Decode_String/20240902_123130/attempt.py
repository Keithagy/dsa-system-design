from typing import Tuple


class Solution:
    def decodeString(self, s: str) -> str:
        def inner(i: int, outer_count: int) -> Tuple[str, int]:
            fragment = ""
            inner_count = 0
            while i < len(s):
                c = s[i]
                if "0" <= c <= "9":
                    digit = int(c)
                    inner_count = inner_count * 10 + digit
                elif c == "[":
                    expanded, new_i = inner(i + 1, inner_count)
                    fragment += expanded
                    i = new_i
                    inner_count = 0
                elif c == "]":
                    return (fragment * outer_count if outer_count != 0 else fragment, i)
                else:
                    fragment += c
                i += 1
            return (fragment, i)

        return inner(0, 0)[0]

