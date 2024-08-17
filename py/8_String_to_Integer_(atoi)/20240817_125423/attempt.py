class Solution:
    # This algorithm has four steps, likely easiest to achieve by implementing a predicate-based scanning approach.
    # Precedence of steps appears to matter
    # 1) Ignore any leading whitespace
    # 2) Determine signedness
    # 3) Read integers until end of string or non-digit. Leading 0s are ignored (realistically, this just means you add it)
    # 4) Round it by checking bounds (check the difference between the number and the bounds, only increment if the difference is less than)
    # Bounds checking requires more thought
    # When you increment a number by a digit: n = ( (n * 10) + new_digit )
    # n grows by 9 times, then by the new new_digit, and there is a risk that this growth exceeds the difference between the bound and n
    # so, you need to calculate bound_difference, and make sure it is at least 9n + new_digit
    # i.e (bound_difference - new_digit) // n >= 9
    def myAtoi(self, s: str) -> int:
        min_int = -(2**31)
        max_int = 2**31 - 1
        cur = 0

        # 1) Ignore leading whitespace
        while cur < len(s) and s[cur] == " ":
            cur += 1

        # Determine signedness
        is_negative = False
        if cur < len(s):
            if s[cur] == "-":
                is_negative = True
            if s[cur] == "-" or s[cur] == "+":
                cur += 1

        bound = min_int if is_negative else max_int
        num = 0

        # Here's a slightly modified version of your willOverflowBound function that might be more efficient and easier to understand:
        # def willOverflowBound(new_digit: int) -> bool:
        #     if is_negative:
        #         return num < (min_int + new_digit) // 10
        #     else:
        #         return num > (max_int - new_digit) // 10

        def willOverflowBound(new_digit: int) -> bool:
            if num == 0:
                return False
            bound_diff = bound + num if is_negative else bound - num
            quotient = bound_diff + new_digit if is_negative else bound_diff - new_digit
            return (quotient // (num * (-1 if is_negative else 1))) < 9

        while cur < len(s) and "0" <= s[cur] <= "9":
            new_digit = int(s[cur])
            if willOverflowBound(new_digit):
                return bound
            # Increment like so only after bounds check
            num = (num * 10) + int(new_digit)  # handles leading zeroes
            cur += 1
        return num * (
            -1 if is_negative else 1
        )  # if loop completes, you're at a non-digit character, or EOS

