class Solution:
    # At each step, the robot as two choices:
    # It can step right, or step down
    # You have a repeating-subproblem structure which suggests possibility of dynamic programming
    # Number of ways to get to a square = number of ways to get to square to left (if valid, then go right) + # ways to get to square  to up
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def waysToGetTo(m: int, n: int) -> int:
            if m == 1 and n == 1:
                return 1
            if (m, n) in memo:
                return memo[(m, n)]
            count = 0
            if m > 1:  # We are right of some sqaure
                count += waysToGetTo(m - 1, n)
            if n > 1:  # We are up of some sqaure
                count += waysToGetTo(m, n - 1)
            memo[(m, n)] = count
            return count

        return waysToGetTo(m, n)

