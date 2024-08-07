class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            digit = x % 10
            rev = (rev * 10) + digit
            x //= 10
        return x == rev or x == (rev // 10)

    def isPalindromeAlt(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        rev = 0
        while x > 0:
            digit = x % 10
            rev = (rev * 10) + digit
            x //= 10
        return rev == original

