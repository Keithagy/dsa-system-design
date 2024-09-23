class Solution:
    def calculate(self, s: str) -> int:
        """
        The key here is to utilize stack mechanics
        It makes things simpler that we don't have times and divide
        I think that basically means you can process expressions eagerly
        or you just evaluate all the subexpressions as stack elements
        then reduce by the summation
        """

        scopes = []
        stack = []

        i = 0
        should_negate_next = False
        while i < len(s):
            if s[i].isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur *= 10
                    cur += int(s[i])
                    i += 1
                else:
                    stack.append(cur * (-1 if should_negate_next else 1))
                    if should_negate_next:
                        should_negate_next = False
            elif s[i] == "+":
                i += 1
            elif s[i] == "-":
                should_negate_next = True
                i += 1
            elif s[i] == "(":
                scopes.append((stack, should_negate_next))
                stack = []
                should_negate_next = False
                i += 1
            elif s[i] == ")":
                eval = sum(stack)
                stack, should_negate_next = scopes.pop()
                stack.append(eval * (-1 if should_negate_next else 1))
                if should_negate_next:
                    should_negate_next = False
                i += 1
            else:
                i += 1

        return sum(stack)

