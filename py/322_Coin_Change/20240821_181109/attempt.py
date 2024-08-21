from typing import List


class Solution:
    # You can break down the problem into a subproblem with the same structure
    # if you need to make up 0, then you always need 0 coins
    # if you have coins [1], then how many coins to make up 11? 11, you just keep taking because that's your only option
    # if you have coins [1,2], then ""? 11 if you just keep taking, but you could also, at least juncture, attempt to skip.
    #   Which leads you the solution where you skip
    # also, after you take the coin, you would ask yourself instead, if you have coins [1], how many coins to amke up 10? and so on.
    # you always need 0 to make up 0 coins.
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        memo = {}

        def coins_needed_for_target_with_coin(
            idx: int, target: int, coin_count: int
        ) -> int:
            if target < 0 or idx < 0:
                return (
                    amount + 1
                )  # not possible, suggests you tried to e.g. take coin out of 2 out of target of 1, or that you moved out of bounds on the coins array
            if target == 0:
                return coin_count
            if (idx, target, coin_count) in memo:
                return memo[(idx, target, coin_count)]
            coin_needed_if_take = coins_needed_for_target_with_coin(
                idx, target - coins[idx], coin_count + 1
            )
            coin_needed_if_skip = coins_needed_for_target_with_coin(
                idx - 1, target, coin_count
            )
            memo[(idx, target, coin_count)] = min(
                coin_needed_if_take, coin_needed_if_skip
            )
            return memo[(idx, target, coin_count)]

        result = coins_needed_for_target_with_coin(len(coins) - 1, amount, 0)
        return result if 0 <= result <= amount else -1

