# Explanation: Coin Change

## Analysis of problem & input data

This problem is a classic dynamic programming question that falls under the category of "minimization problems." The key aspects to consider are:

1. We're dealing with a combination problem where order doesn't matter (e.g., 5+1+5 is the same as 5+5+1).
2. We can use each coin denomination an infinite number of times.
3. We're looking for the minimum number of coins needed.
4. The problem has an optimal substructure: the optimal solution for a larger amount can be constructed from optimal solutions of smaller amounts.
5. There are overlapping subproblems: we might need to calculate the minimum coins for the same amount multiple times.

The key principle that makes this question solvable is that we can build up the solution for larger amounts from the solutions of smaller amounts. For each amount from 1 to the target amount, we can consider using each coin denomination and choose the one that leads to the minimum number of coins.

## Test cases

Here are some test cases to consider:

1. Basic case:

   ```python
   coins = [1, 2, 5], amount = 11
   # Expected output: 3
   ```

2. No solution possible:

   ```python
   coins = [2], amount = 3
   # Expected output: -1
   ```

3. Zero amount:

   ```python
   coins = [1], amount = 0
   # Expected output: 0
   ```

4. Large amount with small coins:

   ```python
   coins = [1, 2, 5], amount = 100
   # Expected output: 20
   ```

5. Large coins with small amount:

   ```python
   coins = [186, 419, 83, 408], amount = 6249
   # Expected output: 20
   ```

6. Multiple optimal solutions:

   ```python
   coins = [1, 4, 5], amount = 8
   # Expected output: 2 (4+4 or 5+1+1+1)
   ```

Here's the executable Python code for these test cases:

```python
def coinChange(coins: List[int], amount: int) -> int:
    # Placeholder for the actual implementation
    pass

# Test cases
test_cases = [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1, 2, 5], 100),
    ([186, 419, 83, 408], 6249),
    ([1, 4, 5], 8)
]

for i, (coins, amount) in enumerate(test_cases, 1):
    result = coinChange(coins, amount)
    print(f"Test case {i}: coins = {coins}, amount = {amount}")
    print(f"Result: {result}\n")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Bottom-up Dynamic Programming (Tabulation)
2. Top-down Dynamic Programming (Memoization)
3. BFS (Breadth-First Search)

Count: 3 solutions

#### Rejected solutions

1. Greedy approach (always choose the largest coin possible)
2. Brute force recursion without memoization
3. Sorting the coins and using binary search

### Worthy Solutions

#### 1. Bottom-up Dynamic Programming (Tabulation)

```python
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    # Initialize dp array with amount + 1 (impossible value) for all amounts
    dp = [amount + 1] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Iterate through all amounts from 1 to target amount
    for i in range(1, amount + 1):
        # For each coin, check if it can contribute to current amount
        for coin in coins:
            if coin <= i:
                # Update dp[i] with minimum of current value and 1 + dp[i - coin]
                dp[i] = min(dp[i], 1 + dp[i - coin])

    # Return -1 if no solution, otherwise return the minimum coins for amount
    return dp[amount] if dp[amount] <= amount else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

Intuition and invariants:

- We build up solutions for smaller amounts to solve for larger amounts.
- dp[i] represents the minimum number of coins needed to make amount i.
- The invariant is that dp[i] always contains the optimal solution for amount i.
- We consider using each coin for each amount, ensuring we explore all possibilities.
- By using min(), we always keep the minimum number of coins for each amount.

#### 2. Top-down Dynamic Programming (Memoization)

```python
from typing import List
from functools import lru_cache

def coinChange(coins: List[int], amount: int) -> int:
    @lru_cache(None)
    def dfs(remaining):
        # Base case: exact amount reached
        if remaining == 0:
            return 0
        # Base case: amount went below 0
        if remaining < 0:
            return float('inf')

        # Try each coin and take the minimum
        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        return min_coins

    result = dfs(amount)
    return result if result != float('inf') else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

Intuition and invariants:

- We use recursion to break down the problem into smaller subproblems.
- The memoization (@lru_cache) ensures we don't recalculate the same subproblems.
- We explore all possible coin combinations recursively.
- The invariant is that dfs(remaining) always returns the minimum coins needed for the remaining amount.
- We use float('inf') to represent impossible solutions, which get filtered out.

#### 3. BFS (Breadth-First Search)

```python
from typing import List
from collections import deque

def coinChange(coins: List[int], amount: int) -> int:
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
Space Complexity: O(amount)

Intuition and invariants:

- We treat the problem as a graph, where each node is an amount and edges are coins.
- BFS ensures we find the shortest path (minimum number of coins) first.
- We use a queue to keep track of amounts to explore and the number of coins used.
- The visited set prevents us from exploring the same amount multiple times.
- The invariant is that when we reach the target amount, we've used the minimum number of coins.

### Rejected Approaches

1. Greedy Approach: Always choosing the largest coin possible doesn't work because it doesn't guarantee the optimal solution. For example, with coins [1, 3, 4] and amount 6, greedy would choose 4+1+1 (3 coins), but the optimal is 3+3 (2 coins).

2. Brute Force Recursion without Memoization: This would work correctly but is extremely inefficient, potentially recalculating the same subproblems many times. The time complexity would be exponential.

3. Sorting and Binary Search: While sorting the coins could potentially speed up some operations, it doesn't fundamentally change the problem's nature or provide a significant advantage in solving it optimally.

### Final Recommendations

The Bottom-up Dynamic Programming (Tabulation) approach is recommended as the best solution to learn for this problem. Here's why:

1. It's the most efficient in terms of both time and space complexity.
2. It's iterative, which often performs better than recursive solutions in practice.
3. It's more intuitive to understand and explain in an interview setting.
4. It clearly demonstrates understanding of dynamic programming principles.

The Top-down DP (Memoization) approach is also worth knowing as it can be easier to come up with initially and can be quickly optimized with memoization.

The BFS approach, while correct, is less common for this problem and might be harder to come up with or explain in an interview setting. However, it's a good demonstration of problem-solving skills if you can recognize the problem as a shortest path in a graph.

The greedy approach might seem tempting due to its simplicity, but it's crucial to recognize why it fails for this problem. Being able to provide a counterexample (like the one given above) demonstrates good problem-solving skills.

Remember, in an interview, it's often valuable to start with a simpler solution (even if suboptimal) and then optimize. Starting with the recursive solution and improving it to the memoized version, then recognizing how it can be transformed into the bottom-up solution, would be an excellent approach to showcase your problem-solving process.

## Visualization(s)

To visualize the bottom-up dynamic programming approach, let's create a simple React component that shows how the dp array is filled:

```tsx
import React, { useState, useEffect } from "react";

const CoinChangeVisualization = () => {
  const [coins, setCoins] = useState([1, 2, 5]);
  const [amount, setAmount] = useState(11);
  const [dp, setDp] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const newDp = Array(amount + 1).fill(amount + 1);
    newDp[0] = 0;
    setDp(newDp);
    setCurrentIndex(0);
  }, [coins, amount]);

  const nextStep = () => {
    if (currentIndex <= amount) {
      const newDp = [...dp];
      for (const coin of coins) {
        if (coin <= currentIndex) {
          newDp[currentIndex] = Math.min(
            newDp[currentIndex],
            1 + newDp[currentIndex - coin],
          );
        }
      }
      setDp(newDp);
      setCurrentIndex(currentIndex + 1);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Coin Change DP Visualization</h2>
      <div className="mb-4">
        <span className="font-bold">Coins:</span> {coins.join(", ")}
      </div>
      <div className="mb-4">
        <span className="font-bold">Target Amount:</span> {amount}
      </div>
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
        onClick={nextStep}
        disabled={currentIndex > amount}
      >
        Next Step
      </button>
      <div className="grid grid-cols-12 gap-2">
        {dp.map((value, index) => (
          <div
            key={index}
            className={`border p-2 text-center ${
              index === currentIndex - 1 ? "bg-yellow-200" : ""
            } ${index < currentIndex ? "bg-green-100" : ""}`}
          >
            <div className="text-sm font-bold">{index}</div>
            <div>{value > amount ? "∞" : value}</div>
          </div>
        ))}
      </div>
      <div className="mt-4">
        <span className="font-bold">Current Step:</span> {currentIndex}/
        {amount + 1}
      </div>
      <div className="mt-2">
        <span className="font-bold">Result:</span>{" "}
        {currentIndex > amount
          ? dp[amount] > amount
            ? "No solution"
            : dp[amount]
          : "In progress..."}
      </div>
    </div>
  );
};

export default CoinChangeVisualization;
```

This visualization shows how the dp array is filled step by step. Each cell represents an amount from 0 to the target amount. The value in each cell is the minimum number of coins needed to make that amount. The yellow cell indicates the current amount being processed, and green cells are amounts that have been processed. Clicking "Next Step" advances the algorithm by one step.
