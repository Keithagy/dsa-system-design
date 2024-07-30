from typing import Dict


class Solution:
    def __init__(self) -> None:
        self.memo: Dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo:
            return self.memo[n]
        # for 3, you can take the 2 prev ways and add 1 step to
        # or you can take the 1 prev ways and add 2 steps 2
        ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = ways
        return ways

    def climbStairs_opt(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            tmp = curr
            curr = prev + curr
            prev = tmp
        return curr

