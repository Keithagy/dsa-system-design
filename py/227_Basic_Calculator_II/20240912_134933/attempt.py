from typing import Optional, Tuple


class Solution:
    # Main thing to account for here is operator precedence
    # e.g. * / >> +/-
    # "3+2*2" vs "3*2 + 2"
    # When you parse the right operand of an infix operator, you need to consider operator precedence
    # you need to skip whitespaces
    # evaluate right as binary op if its precedence is at least yours
    # evluate right as numbere if its precedence is lower
    # no need to consider negatives
    #
    # "3/2+2"
    #

    def calculate(self, s: str) -> int:
        ops = {
            "+": (0, lambda a, b: a + b),
            "-": (0, lambda a, b: a - b),
            "*": (1, lambda a, b: a * b),
            "/": (2, lambda a, b: int(a / b)),
        }

        def at_num(idx: int) -> bool:
            return "0" <= s[idx] <= "9"

        def at_op(idx: int) -> bool:
            return s[idx] in ops

        def next_token_idx(idx: int) -> int:
            while idx < len(s):
                if s[idx] == " ":
                    idx += 1
                    continue
                if at_num(idx) or at_op(idx):
                    break
            return idx

        def operator(idx: int) -> Tuple[Optional[str], int]:
            if not 0 <= idx < len(s):
                return (None, idx)
            assert s[idx] in ops
            return s[idx], next_token_idx(idx + 1)

        def number(idx: int) -> Tuple[int, int]:
            num = 0
            while idx < len(s):
                if s[idx] == " ":
                    idx += 1
                    continue
                if not at_num(idx):
                    break
                num *= 10
                num += int(s[idx])
                idx += 1
            return num, idx

        def calculateFrom(idx: int) -> Tuple[int, int]:
            left, idx = number(idx)

            op, idx = operator(idx)
            if op is None:
                return (left, idx)

            next_op, _ = operator(number(idx)[1])
            print("next op", next_op)
            right, idx = (
                number(idx)
                if next_op is None or (ops[next_op][0] < ops[op][0])
                else calculateFrom(idx)
            )
            result = ops[op][1](left, right)
            print("result idx", result, idx)
            if next_op is None or idx > len(s) - 1:
                return (result, idx)
            return (ops[next_op][1](result, calculateFrom((operator(idx)[1]))[0]), idx)

        return calculateFrom(0)[0]

