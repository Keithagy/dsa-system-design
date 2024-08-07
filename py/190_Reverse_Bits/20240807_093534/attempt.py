class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        first_set_bit = n & -n
        places = 1
        while (1 << (places - 1)) & first_set_bit == 0:
            places += 1
        result = 0
        result |= 1 << (
            31 - (places - 1)
        )  # e.g. if first bit is set, you want the 32nd bit set in the reversed
        n >>= places
        places += 1
        while n > 0:
            next_bit = n & 1
            result = result | (next_bit << (31 - (places - 1)))
            n >>= 1
            places += 1
        return result

