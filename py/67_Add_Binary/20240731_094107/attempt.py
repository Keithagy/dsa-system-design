from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        i = 0
        loops = min(len(a), len(b))
        result = deque()
        while i < loops:
            a_bit = a[-(i + 1)]
            b_bit = b[-(i + 1)]
            operands = [a_bit, b_bit, carry]

            result_bit = (
                "1"
                if (
                    len(list(filter(lambda operand: operand == "1", operands))) % 2 != 0
                )
                else "0"
            )

            result.appendleft(result_bit)
            carry = (
                "1"
                if (
                    result_bit == "0"
                    and len(list(filter(lambda operand: operand == "1", operands))) > 0
                )
                else "0"
            )
            i += 1

        for c in (a if loops == len(b) else b)[i:]:
            operands = [c, carry]

            result_bit = (
                "1"
                if (
                    len(list(filter(lambda operand: operand == "1", operands))) % 2 != 0
                )
                else "0"
            )
            result.appendleft(result_bit)
            carry = (
                "1"
                if (
                    result_bit == "0"
                    and len(list(filter(lambda operand: operand == "1", operands))) > 0
                )
                else "0"
            )
        if carry == "1":
            result.appendleft("1")

        return "".join(result)

