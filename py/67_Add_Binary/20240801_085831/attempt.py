import collections


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = collections.deque()
        while i or j or carry:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            sum = a_digit + b_digit + carry
            carry = sum // 2
            result.appendleft(str(sum % 2))
            i -= 1
            j -= 1
        return "".join(result)

