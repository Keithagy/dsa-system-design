from typing import List


class Solution:
    # Naive solution, just because I don't know how to do it
    # This is O(n) memory for the output array
    # Runtime-wise, this is O(n log n), because
    # there are n + 1 numbers to check, and
    # each of those n + 1 numbers has log n bits to check, at most, in a binary representation
    def countBitsNaive(self, n: int) -> List[int]:
        result = []
        for i in range(0, n + 1):
            count = 0
            while i:
                count += i & 1  # tells you if i's least significant bit is set (1 or 0)
                i >>= 1
            result.append(count)
        return result

    # Core intuition: E::(i,n,k): i = (2 ^ n) + k
    # In English: Any number can be expressed as some power of 2 + some stub
    #
    # For instance: 10 = (2 ^ 3) + 2
    # 10 => 1010
    #  8 => 1000
    #  2 => 0010
    #
    # Observe:
    # When counting bits for 10, notice that you can reuse the result from counting bits for 2
    # In fact, the number of set bits from 8 - 15 can be calculated by adding 1 to the number of set bits from (0 - 7)
    # More generally, set_bits[i] == set_bits[i - nearest_power_2] + 1
    #
    # It's kind of like the ways-to-climb-n-stairs problem!
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        nearest_power_of_two = 1
        for i in range(1, n + 1):
            if nearest_power_of_two * 2 == i:
                # Getting here indicates i is a new power of 2
                nearest_power_of_two = i
            result[i] = 1 + result[i - nearest_power_of_two]
        return result

