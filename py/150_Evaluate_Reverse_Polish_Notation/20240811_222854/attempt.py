from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        stack = []
        for token in tokens:
            if token in operations:
                y, x = stack.pop(), stack.pop()
                stack.append(operations[token](x, y))
                continue
            stack.append(int(token))
        return stack[0]

