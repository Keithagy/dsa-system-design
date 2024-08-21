class Solution:
    # You can solve this optimally by reversing only half the digits and comparing that.
    # However you need to handle the edge case of trailing zero. e.g. 50, 100 etc; only zero would be palindromic in that case.
    def isPalindrome(self, x: int) -> bool:
        if (x % 10 == 0 and x != 0) or x < 0:
            return False
        rev = 0
        while x > rev:
            digit = x % 10
            x //= 10
            rev *= 10
            rev += digit
        return x == rev or x == (rev // 10)

