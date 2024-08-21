from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        memo = {}

        def dp(remaining: int) -> int:
            if remaining < 0:
                return amount + 1
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            min_coins = amount + 1
            for coin in coins:
                min_coins = min(min_coins, dp(remaining - coin) + 1)
            memo[remaining] = min_coins
            return memo[remaining]

        return dp(amount) if 0 <= dp(amount) <= amount else -1

