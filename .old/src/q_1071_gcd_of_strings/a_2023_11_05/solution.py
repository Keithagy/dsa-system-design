import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if there exists a GCD string for str1 and str2,
        # order of contenation should not matter.
        if str1 + str2 != str2 + str1:
            return ""
        # since there exists some GCD string, its length has to be the GCD of both
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]
