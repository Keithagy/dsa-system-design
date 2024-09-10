class Solution:
    # the sign of the input number should be preserved
    # check for bounds BEFORE reading in the next digit (and potentially exceeding the bounds)
    def reverse(self, x: int) -> int:
        def readingNextExceedsBounds(n: int, x: int, is_neg: bool) -> bool:
            # bounds are inclusive
            lower_bound = -(2**31)
            upper_bound = (2**31) - 1
            bound = abs(lower_bound if is_neg else upper_bound)
            one_digit_before = bound // 10
            last_digit_bound = bound % 10
            return n > one_digit_before or (
                n == one_digit_before and (x % 10) > last_digit_bound
            )

        is_neg = x < 0
        if is_neg:
            x = -x  # process digits independently of sign
        result = 0
        while x > 0:
            if readingNextExceedsBounds(result, x, is_neg):
                return 0
            digit = x % 10
            result *= 10
            result += digit
            x //= 10
        return -result if is_neg else result

