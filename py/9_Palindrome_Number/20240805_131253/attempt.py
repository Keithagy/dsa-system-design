from typing import List


class Solution:
    def digits(self, x: int) -> List[int]:
        result = []
        places = 1
        while x // (10**places) > 0:
            places += 1
        while places > 0:
            divisor = 10 ** (places - 1)
            digit = x // divisor
            x = x % divisor
            places -= 1
            result.append(digit)
        return result

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = self.digits(x)
        for i in range(len(digits) // 2):
            mirror = len(digits) - i - 1
            if digits[i] != digits[mirror]:
                return False
        return True

