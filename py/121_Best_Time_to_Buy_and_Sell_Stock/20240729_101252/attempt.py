class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = len(prices) - 1
        max_profit = prices[sell_day] - prices[buy_day]

        for i in range(len(prices)):
            




