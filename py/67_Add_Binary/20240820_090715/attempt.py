class Solution:
    def addBinary(self, a: str, b: str) -> str:
        iterations = max(len(a), len(b))
        carry = 0
        result = []
        for i in range(
            1, iterations + 1, 1
        ):  # start processing from least significant bit
            a_digit = int(a[-i]) if i <= len(a) else 0
            b_digit = int(b[-i]) if i <= len(b) else 0
            sum = a_digit + b_digit + carry
            next_digit = sum % 2
            result.append("0" if next_digit == 0 else "1")
            carry = sum >> 1
        if carry != 0:
            result.append("1")
        return "".join(result[::-1])

