from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        max_profit = 0
        for price in prices:
            lowest_price = min(lowest_price, price)
            profit = price - lowest_price
            max_profit = max(max_profit, profit)
        return int(max_profit)
