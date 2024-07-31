from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        # start from least significant bits
        i, j = len(a) - 1, len(b) - 1
        result = deque()

        while i >= 0 or j >= 0 or carry:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            sum = a_digit + b_digit + carry
            carry = sum // 2
            result.appendleft(str(sum % 2))
            i -= 1
            j -= 1
        return "".join(result)

