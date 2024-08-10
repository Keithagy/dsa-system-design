class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while n > 0:
            bit = n & 1
            n >>= 1
            reversed_bit = bit << (31 - i)
            i += 1
            result |= reversed_bit

        return result

