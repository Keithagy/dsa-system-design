class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        result = float("inf")

        memo = {}

        def numCoinsToMakeWith(starting: int, soFar: int) -> int:
            if soFar > amount or starting >= len(coins):
                return float("inf")
            if soFar == amount:
                return 0
            if (starting, soFar) in memo:
                return memo[(starting, soFar)]
            take_this = 1 + numCoinsToMakeWith(starting, soFar + coins[starting])
            skip_this = numCoinsToMakeWith(starting + 1, soFar)
            memo[(starting, soFar)] = min(take_this, skip_this)
            return memo[(starting, soFar)]

        result = numCoinsToMakeWith(0, 0)

        return -1 if result == float("inf") else result

