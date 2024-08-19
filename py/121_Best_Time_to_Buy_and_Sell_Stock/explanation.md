# Explanation: Best Time to Buy and Sell Stock

## Analysis of problem & input data

This problem is a classic example of finding the maximum difference between two elements in an array, with the additional constraint that the smaller element must come before the larger element.

Key characteristics of the problem:

1. We're dealing with a single array of integers (stock prices).
2. We need to find two days: one to buy and one to sell.
3. The buy day must come before the sell day.
4. We're looking for the maximum profit, which is the largest positive difference between a later price and an earlier price.
5. If no profit is possible, we should return 0.

Important aspects of the input data:

1. The array length is between 1 and 10^5, so our solution needs to be efficient.
2. Prices are non-negative integers between 0 and 10^4.
3. The order of prices matters, as it represents the chronological order of days.

The key principle that makes this question simple is that we only need to keep track of the minimum price we've seen so far and the maximum profit we can achieve up to the current point. This allows us to solve the problem in a single pass through the array.

## Solutions

### Solution 1: One-pass Linear Scan

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')  # Initialize to positive infinity
        max_profit = 0

        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)

            # Update the maximum profit if selling at current price
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit
```

Time Complexity: O(n), where n is the number of prices
Space Complexity: O(1), as we only use a constant amount of extra space

Explanation:

- We initialize `min_price` to positive infinity and `max_profit` to 0.
- We iterate through the prices once, doing two things at each step:
  1. Update the minimum price seen so far.
  2. Calculate the profit if we sell at the current price and update the maximum profit if it's higher.
- This approach ensures we always consider buying at the lowest price seen so far and selling at the current price.

### Solution 2: Kadane's Algorithm Variation

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            # Calculate the price difference
            price_diff = prices[i] - prices[i-1]

            # Update current profit
            current_profit = max(0, current_profit + price_diff)

            # Update max profit if current profit is larger
            max_profit = max(max_profit, current_profit)

        return max_profit
```

Time Complexity: O(n), where n is the number of prices
Space Complexity: O(1)

Explanation:

- This solution is a variation of Kadane's algorithm, which is typically used for the maximum subarray problem.
- Instead of working with the prices directly, we work with the differences between consecutive prices.
- We maintain a `current_profit` which represents the best profit ending at the current position.
- If `current_profit` becomes negative, we reset it to 0 (equivalent to choosing a new buying point).
- We update `max_profit` whenever we find a better profit.

## Recommendation

I recommend learning and using Solution 1 (One-pass Linear Scan) for this problem. Here's why:

1. It's more intuitive and easier to understand, especially for those new to this type of problem.
2. It directly models the problem statement (finding a minimum buying price and maximum selling price).
3. It's efficient, with O(n) time complexity and O(1) space complexity.
4. It's easier to explain in an interview setting.

While Solution 2 (Kadane's Algorithm Variation) is also correct and efficient, it's a bit more abstract and might be harder to come up with or explain under interview pressure. However, it's worth understanding as it demonstrates how this problem relates to the maximum subarray problem, which could be valuable knowledge for solving other problems.

## Test cases

```python
def test_max_profit():
    solution = Solution()

    # Test case 1: Normal case with profit
    assert solution.maxProfit([7,1,5,3,6,4]) == 5

    # Test case 2: Decreasing prices, no profit
    assert solution.maxProfit([7,6,4,3,1]) == 0

    # Test case 3: Single price, no profit
    assert solution.maxProfit([1]) == 0

    # Test case 4: Two prices, profit
    assert solution.maxProfit([1, 2]) == 1

    # Test case 5: Two prices, no profit
    assert solution.maxProfit([2, 1]) == 0

    # Test case 6: Prices with plateau
    assert solution.maxProfit([3,3,5,0,0,3,1,4]) == 4

    print("All test cases passed!")

test_max_profit()
```

## Overview of rejected approaches

1. Brute Force Approach:

   - Checking every possible pair of buy and sell days.
   - While correct, this approach has O(n^2) time complexity, which is too slow for the given constraints.
   - Not worth learning due to inefficiency.

2. Using Sorting:

   - Sorting the prices and taking the difference between the highest and lowest price.
   - This approach is incorrect because it loses the chronological order of prices, which is crucial for this problem.

3. Using a Stack:

   - While a stack can be used to solve this problem, it's unnecessarily complex for this particular variation.
   - It might be more suitable for problems where you need to keep track of multiple buy and sell opportunities.

4. Dynamic Programming with Memoization:
   - While it works, it's overkill for this problem and uses unnecessary extra space.
   - The problem can be solved more efficiently without memoization.

## Visualization(s)

To visualize the one-pass linear scan algorithm, we can create a simple line chart showing the stock prices, with annotations for the minimum price seen so far and the maximum profit at each step. Here's a basic React component that demonstrates this:

```tsx
import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine,
} from "recharts";

const StockPriceVisualization = () => {
  const prices = [7, 1, 5, 3, 6, 4];
  const data = prices.map((price, index) => ({ day: index + 1, price }));

  let minPrice = Infinity;
  let maxProfit = 0;
  const annotations = prices.map((price, index) => {
    minPrice = Math.min(minPrice, price);
    const currentProfit = price - minPrice;
    maxProfit = Math.max(maxProfit, currentProfit);
    return { day: index + 1, minPrice, maxProfit };
  });

  const buyDay =
    annotations.findIndex(
      (a) => a.minPrice === Math.min(...annotations.map((a) => a.minPrice)),
    ) + 1;
  const sellDay =
    annotations.findIndex(
      (a) => a.maxProfit === Math.max(...annotations.map((a) => a.maxProfit)),
    ) + 1;

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Stock Price Visualization</h2>
      <LineChart
        width={600}
        height={300}
        data={data}
        margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="day" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="price"
          stroke="#8884d8"
          activeDot={{ r: 8 }}
        />
        <ReferenceLine x={buyDay} stroke="green" label="Buy" />
        <ReferenceLine x={sellDay} stroke="red" label="Sell" />
      </LineChart>
      <div className="mt-4">
        <p>
          Buy on day {buyDay} at price {prices[buyDay - 1]}
        </p>
        <p>
          Sell on day {sellDay} at price {prices[sellDay - 1]}
        </p>
        <p>Maximum profit: {maxProfit}</p>
      </div>
    </div>
  );
};

export default StockPriceVisualization;
```

This visualization shows the stock prices as a line chart, with annotations for the buy and sell days. It also displays the maximum profit achieved. This helps in understanding how the algorithm identifies the best days to buy and sell the stock.
