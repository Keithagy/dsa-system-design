class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = "+"
        stack = []
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num * 10 + int(c)

            if (not c.isnumeric() and c != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))

                num = 0
                sign = c
        result = 0
        while stack:
            result += stack.pop()
        return result

