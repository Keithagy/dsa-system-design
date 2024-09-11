from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        min_prices = [float("inf") for _ in range(n)]
        min_prices[src] = 0  # you are starting here
        for _ in range(k + 1):  # k is the max number of intervening stops
            tmp_prices = (
                min_prices.copy()
            )  # copy in order to track round-local costs separately from global costs
            for [f, t, p] in flights:
                cost_to_t_under_i_stops = (
                    min_prices[f] + p if min_prices[f] != float("inf") else float("inf")
                )
                tmp_prices[t] = min(tmp_prices[t], cost_to_t_under_i_stops)
            min_prices = tmp_prices
        return min_prices[dst] if min_prices[dst] != float("inf") else -1

