from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}

        def inner(amount: int) -> int:
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            coin_count_for_options = float("inf")
            for coin in coins:
                coin_count_for_options = min(
                    coin_count_for_options, inner(amount - coin) + 1
                )
            memo[amount] = coin_count_for_options
            return coin_count_for_options

        return -1 if inner(amount) == float("inf") else inner(amount)

