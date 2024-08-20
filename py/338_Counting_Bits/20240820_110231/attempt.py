from typing import List


class Solution:
    # The number of 1's in a binary number can be calculated based on the nearest power of 2
    # 4 > 100  || new
    # 5 > 101  || ones[4] + 1
    # 6 > 110  || ones[4] + 2
    # 7 > 111  || ones[4] + 3
    # 8 > 1000 || new
    # n > ??? ## ones[nearest_pow_2] + (n-nearest_pow_2)
    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n + 1)]
        if n == 0:
            return result
        for i in range(1, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[(i // 2)] + 1
        return result

