from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = amount + 1
        coins.sort(reverse=True)

        def backtrack(idx: int, remaining: int, coin_count: int) -> None:
            nonlocal min_coins
            if idx == len(coins) or remaining < 0 or coin_count >= min_coins:
                return
            if remaining == 0:
                min_coins = min(min_coins, coin_count)
            backtrack(idx, remaining - coins[idx], coin_count + 1)
            backtrack(idx + 1, remaining, coin_count)

        backtrack(0, amount, 0)
        return min_coins if 0 <= min_coins <= amount else -1

