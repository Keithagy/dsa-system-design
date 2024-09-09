class Solution:
    # x can be negative 100 to 100
    # either x is not zero or n is positive.
    # if x is zero, n is positive.
    # if n is negative or zero, x is zero.
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        power_is_neg = n < 0
        n = abs(n)
        result = 1
        for _ in range(n):
            result *= x
        return result if not power_is_neg else (1 / result)

