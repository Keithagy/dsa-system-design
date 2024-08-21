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
            match token:
                case token if token in operations:
                    b, a = stack.pop(), stack.pop()
                    stack.append(operations[token](a, b))
                case _:
                    stack.append(int(token))
        return stack[-1]

