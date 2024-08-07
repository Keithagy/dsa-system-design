class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        pos = 0
        while n > 0:
            next_bit = n & 1
            reversed = next_bit << (31 - pos)
            result |= reversed
            n >>= 1
            pos += 1
        return result

