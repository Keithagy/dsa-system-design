## Explanation: Coin Change

### Analysis of problem & input data

This problem is a classic example of the "Coin Change" problem, which falls under the category of dynamic programming. The key characteristics of this problem are:

1. We have a set of coin denominations (given in the `coins` array).
2. We need to find the minimum number of coins to make up a given `amount`.
3. We have an infinite supply of each coin denomination.

The problem's structure lends itself well to dynamic programming because:

1. It has overlapping subproblems: To find the minimum coins for amount n, we might need to know the minimum coins for smaller amounts.
2. It has optimal substructure: The optimal solution for a larger amount can be constructed from optimal solutions of smaller amounts.

The key principle that makes this question simple is the concept of building up solutions for larger amounts from solutions for smaller amounts. This is the essence of dynamic programming.

### Test cases

Here are some relevant test cases:

1. Standard case: `coins = [1,2,5], amount = 11`
2. Impossible case: `coins = [2], amount = 3`
3. Zero amount case: `coins = [1], amount = 0`
4. Large amount with small coins: `coins = [1,2,5], amount = 100`
5. Single coin exact match: `coins = [5], amount = 15`
6. Multiple possible solutions: `coins = [1,4,5], amount = 8`

Here's the Python code for these test cases:

```python
def coin_change(coins: List[int], amount: int) -> int:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([1,2,5], 11),
    ([2], 3),
    ([1], 0),
    ([1,2,5], 100),
    ([5], 15),
    ([1,4,5], 8)
]

for coins, amount in test_cases:
    result = coin_change(coins, amount)
    print(f"coins = {coins}, amount = {amount}, result = {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Bottom-up Dynamic Programming (Tabulation)
2. Top-down Dynamic Programming (Recursion with Memoization)
3. Breadth-First Search (BFS)

Count: 3

##### Rejected solutions

1. Greedy approach (always choosing the largest coin possible)
2. Brute force recursion without memoization

#### Worthy Solutions

##### Bottom-up Dynamic Programming (Tabulation)

```python
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # Initialize dp array with amount + 1 (impossible value) for all amounts
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate through all amounts from 1 to target amount
    for i in range(1, amount + 1):
        # For each coin, if it's less than or equal to current amount
        for coin in coins:
            if coin <= i:
                # Update dp[i] if using this coin results in fewer total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, or -1 if no solution found
    return dp[amount] if dp[amount] <= amount else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

- This approach builds a table (dp array) bottom-up, where dp[i] represents the minimum number of coins needed to make amount i.
- The key intuition is that for any amount i, the minimum number of coins is either:
  1. The current value of dp[i] (initialized to an impossible value)
  2. 1 + the minimum number of coins needed for (i - coin), for any coin <= i
- We choose the minimum of these options, effectively considering all possible last coins.
- The base case dp[0] = 0 represents that 0 coins are needed to make amount 0.

##### Top-down Dynamic Programming (Recursion with Memoization)

```python
from typing import List
from functools import lru_cache

def coin_change(coins: List[int], amount: int) -> int:
    @lru_cache(None)
    def dp(remaining):
        # Base case: exact amount reached
        if remaining == 0:
            return 0
        # Base case: amount went below 0 (invalid)
        if remaining < 0:
            return float('inf')

        # Try all coins and take the minimum valid result
        min_coins = float('inf')
        for coin in coins:
            result = dp(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1

# Note: In a real interview, you might implement your own memoization instead of using lru_cache
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount) for the memoization cache

- This approach uses recursion with memoization to solve the problem top-down.
- The key intuition is that for any amount, we try using each coin and recursively solve for the remaining amount.
- Memoization prevents redundant calculations by caching results for each unique remaining amount.
- The base cases handle when we've reached the exact amount (return 0) or gone below 0 (return infinity to indicate invalid).
- We use float('inf') to represent invalid or impossible solutions, which allows us to use min() effectively.

##### Breadth-First Search (BFS)

```python
from typing import List
from collections import deque

def coin_change(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    queue = deque([(0, 0)])  # (current_amount, coins_used)
    visited = set()

    while queue:
        current_amount, coins_used = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin
            if next_amount == amount:
                return coins_used + 1
            if next_amount < amount and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, coins_used + 1))

    return -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount) for the visited set

- This approach treats the problem as a graph traversal, where each node represents an amount and edges represent coin values.
- The key intuition is that BFS will find the shortest path (minimum number of coins) to the target amount.
- We use a queue to keep track of amounts to explore and the number of coins used to reach them.
- The visited set prevents revisiting the same amount, avoiding cycles and redundant work.
- This approach can be more intuitive for those familiar with graph algorithms and can be efficient for smaller amounts.

#### Rejected Approaches

1. Greedy Approach: Always choosing the largest coin possible doesn't always lead to the optimal solution. For example, with coins [1, 3, 4] and amount 6, greedy would choose [4, 1, 1] (3 coins), but the optimal is [3, 3] (2 coins).

2. Brute Force Recursion: This would involve trying all possible combinations of coins. While correct, it has an exponential time complexity, making it impractical for larger inputs.

#### Final Recommendations

The Bottom-up Dynamic Programming (Tabulation) approach is recommended as the best solution to learn for this problem. It's efficient, relatively easy to implement, and demonstrates a clear understanding of dynamic programming principles. It's also the most commonly expected solution in interview settings.

### Visualization(s)

To visualize the Bottom-up DP approach, we can create a simple table showing how the dp array is filled:

```tsx
import React from "react";

const CoinChangeVisualization = () => {
  const coins = [1, 2, 5];
  const amount = 11;
  const dp = Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  const steps = [];

  for (let i = 1; i <= amount; i++) {
    for (let coin of coins) {
      if (coin <= i) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
    steps.push([...dp]);
  }

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Coin Change DP Visualization</h2>
      <p className="mb-4">
        Coins: {coins.join(", ")}, Amount: {amount}
      </p>
      <table className="border-collapse border border-gray-400">
        <thead>
          <tr>
            <th className="border border-gray-400 px-2 py-1">Amount</th>
            {Array.from({ length: amount + 1 }, (_, i) => (
              <th key={i} className="border border-gray-400 px-2 py-1">
                {i}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {steps.map((step, index) => (
            <tr key={index}>
              <td className="border border-gray-400 px-2 py-1 font-bold">
                {index + 1}
              </td>
              {step.map((value, i) => (
                <td
                  key={i}
                  className={`border border-gray-400 px-2 py-1 ${value === amount + 1 ? "bg-gray-200" : "bg-green-200"}`}
                >
                  {value === amount + 1 ? "∞" : value}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CoinChangeVisualization;
```

This visualization shows how the dp array is filled step by step. Each row represents the state of the dp array after processing the corresponding amount. The green cells show the updated minimum coin counts, while the gray cells (∞) represent amounts that haven't been reached yet.
