class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []  # address case of out of order brackets
        for c in s:
            if c not in pairs:  # c is open paren
                stack.append(c)
                continue
            else:
                if len(stack) == 0:
                    return False  # encountered close bracket when stack is empty => mismatch
                should_be_open_paren = stack.pop()
                expected_matching = pairs[c]
                if should_be_open_paren != expected_matching:
                    return False  # address case of improperly closed brackets
        return (
            len(stack) == 0
        )  # address case of unmatched number of open and closed parens

