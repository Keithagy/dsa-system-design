from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1

        memo = {}

        def dp(remaining: int) -> int:
            if remaining < 0:
                return impossible
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            min_coins = impossible
            for coin in coins:
                min_coins = min(min_coins, dp(remaining - coin) + 1)
            memo[remaining] = min_coins
            return memo[remaining]

        return dp(amount) if dp(amount) != impossible else -1

