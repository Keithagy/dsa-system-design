class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        pos = 0

        while n > 0:
            bit = n & 1
            n >>= 1
            reversed_bit = bit << (31 - pos)
            rev |= reversed_bit
            pos += 1
        return rev

