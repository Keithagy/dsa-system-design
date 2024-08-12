from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [float("inf") for _ in range(amount + 1)]
        for subamount in range(amount + 1):
            if subamount == 0:
                dp[subamount] = 0
                continue
            for coin in coins:
                if subamount - coin < 0:
                    continue
                if dp[subamount - coin] == float("inf"):
                    continue  # already determined earlier you cannot make this number
                dp[subamount] = min(dp[subamount], dp[subamount - coin] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]

