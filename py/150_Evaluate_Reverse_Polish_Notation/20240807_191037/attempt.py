from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                left, right = stack.pop(), stack.pop()
                result = left + right
                stack.append(result)
                continue
            if token == "-":
                left, right = stack.pop(), stack.pop()
                result = right - left
                stack.append(result)
                continue
            if token == "*":
                left, right = stack.pop(), stack.pop()
                result = left * right
                stack.append(result)
                continue
            if token == "/":
                left, right = stack.pop(), stack.pop()
                result = int(right / left)
                stack.append(result)
                continue
            else:
                stack.append(int(token))
                continue
        return stack.pop()

