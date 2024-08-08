from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        for starting in range(len(coins))[::-1]:
            remaining = amount
            result = 0
            for i in range(starting + 1)[::-1]:
                denom = coins[i]
                count = remaining // denom
                remaining -= count * denom
                result += count
                if remaining == 0:
                    return result
        return -1

