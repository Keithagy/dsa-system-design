from typing import List
from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @cache
        def inner(amount: int, coins_so_far: int, trying_coin: int) -> int:
            if amount - trying_coin < 0:
                return -1
            if amount == 0:
                return coins_so_far
            remaining = amount - trying_coin
            min_coins = float("inf")
            for coin in coins:
                coin_count = inner(remaining, coins_so_far + 1, coin)
                if coin_count < 0:
                    continue
                min_coins = min(coin_count, min_coins)
            return -1 if min_coins == float("inf") else int(min_coins)

        return inner(amount, 0, coins[0])

