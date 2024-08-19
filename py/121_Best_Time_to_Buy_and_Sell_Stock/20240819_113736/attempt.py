from os import curdir
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0  # You can never sell so you should never buy
        max_profit = -float("inf")
        buy_day = 0
        for day in range(len(prices)):
            if prices[day] < prices[buy_day]:
                buy_day = day
            cur_profit = prices[day] - prices[buy_day]
            max_profit = max(max_profit, cur_profit)
        return int(max_profit)

