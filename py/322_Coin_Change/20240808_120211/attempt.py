from typing import List


class Solution:
    # trying top down dp solution
    # intuition: testing each amount == testing (amount - coin) for all coins
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def inner(amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            min_coins = float("inf")
            for coin in coins:
                next = amount - coin
                result = float("inf")
                if next in memo:
                    result = memo[next]
                else:
                    result = inner(next)
                    memo[next] = result
                min_coins = min(min_coins, result + 1)
            return min_coins

        count = inner(amount)
        return count if count != float("inf") else -1
