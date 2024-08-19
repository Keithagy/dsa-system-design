class Solution:
    # For a given step count, ways to get to it is the sum of ways to get to one step before (take 1 step up from there), and ways to get to two steps before (take 2 steps up from there)
    def climbStairs(self, n: int) -> int:
        memo = {}

        def waysToTake(n: int) -> int:
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            ways = waysToTake(n - 1) + waysToTake(n - 2)
            memo[n] = ways
            return ways

        return waysToTake(n)

