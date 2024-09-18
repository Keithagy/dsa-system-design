package q121

func maxProfit(prices []int) int {
	max_profit := 0
	buy_day := 0
	for day, price := range prices {
		if price < prices[buy_day] {
			buy_day = day
		}
		profit := price - prices[buy_day]
		max_profit = max(max_profit, profit)
	}
	return max_profit
}

