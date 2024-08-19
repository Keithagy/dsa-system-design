class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(": ")", "[": "]", "{": "}"}
        opens = matches.keys()
        closes = matches.values()
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if not stack or stack[-1] not in matches or matches[stack.pop()] != c:
                    return False
            else:
                raise ValueError("Should only be open or close parenthesis.")
        return not stack

