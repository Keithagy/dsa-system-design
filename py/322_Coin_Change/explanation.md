# Explanation: Coin Change

## Analysis of problem & input data

This problem is a classic example of the "Coin Change" problem, which is a type of dynamic programming problem. The key characteristics and insights are:

1. We're dealing with an optimization problem - finding the minimum number of coins.
2. The problem has an optimal substructure - the solution to a larger amount can be built from solutions to smaller amounts.
3. There are overlapping subproblems - we may need to calculate the solution for the same subamount multiple times.
4. We have an infinite supply of each coin denomination.
5. The order of coin selection doesn't matter - only the total count.
6. The input constraints are relatively small, allowing for polynomial time solutions.

The key principle that makes this question approachable is that for any amount A, the minimum number of coins needed is 1 (the coin itself, if it exists in the set) plus the minimum number of coins needed for (A - coin value). This recursive relationship forms the basis of our dynamic programming approach.

### Test cases

Here are some test cases to consider:

1. Basic case:

   ```python
   coins = [1, 2, 5], amount = 11
   # Expected output: 3
   ```

2. Impossible case:

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

5. Single coin denomination:

   ```python
   coins = [5], amount = 15
   # Expected output: 3
   ```

6. Multiple valid solutions:

   ```python
   coins = [1, 4, 5], amount = 8
   # Expected output: 2 (4+4 or 5+1+1+1)
   ```

7. Large coin values:

   ```python
   coins = [186, 419, 83, 408], amount = 6249
   # Expected output: 20
   ```

Here's the executable Python code for these test cases:

```python
def coinChange(coins: List[int], amount: int) -> int:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1, 2, 5], 100),
    ([5], 15),
    ([1, 4, 5], 8),
    ([186, 419, 83, 408], 6249)
]

expected_outputs = [3, -1, 0, 20, 3, 2, 20]

for i, (coins, amount) in enumerate(test_cases):
    result = coinChange(coins, amount)
    print(f"Test case {i+1}: {'Passed' if result == expected_outputs[i] else 'Failed'}")
    print(f"Input: coins = {coins}, amount = {amount}")
    print(f"Output: {result}")
    print(f"Expected: {expected_outputs[i]}\n")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Bottom-up Dynamic Programming (Tabulation)
2. Top-down Dynamic Programming (Recursion with Memoization)
3. BFS (Breadth-First Search)

Count: 3 solutions

#### Rejected solutions

1. Greedy Algorithm
2. Brute Force (Recursive without memoization)
3. Integer Linear Programming

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
                # Update dp[i] if using this coin leads to fewer total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result, or -1 if no solution found
    return dp[amount] if dp[amount] <= amount else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

Intuition and invariants:

- We build up the solution from smaller subproblems to larger ones.
- dp[i] represents the minimum number of coins needed to make amount i.
- For each amount, we consider using each coin and choose the minimum.
- The final answer is stored in dp[amount].
- We use amount + 1 as an impossible value because we know we need at most 'amount' coins (if all coins are 1).

#### 2. Top-down Dynamic Programming (Recursion with Memoization)

```python
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    # Memoization dictionary to store computed results
    memo = {}

    def dp(remaining):
        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')

        # Check if we've already computed this subproblem
        if remaining in memo:
            return memo[remaining]

        # Compute the minimum coins needed for this amount
        min_coins = float('inf')
        for coin in coins:
            result = dp(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        # Memoize the result before returning
        memo[remaining] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount) for memoization and recursion stack

Intuition and invariants:

- We solve the problem recursively, breaking it down into smaller subproblems.
- We use memoization to avoid redundant computations.
- For each amount, we try all possible coins and choose the minimum.
- We use float('inf') to represent impossible solutions.
- The base case is when the remaining amount is 0.

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

    return -1  # If we can't reach the target amount
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

Intuition and invariants:

- We treat the problem as a graph where nodes are amounts and edges are coin denominations.
- We perform a breadth-first search from 0 to the target amount.
- The first time we reach the target amount is guaranteed to be the shortest path (minimum coins).
- We use a visited set to avoid revisiting the same amounts.
- Each step in the BFS represents adding one coin.

### Rejected Approaches

1. Greedy Algorithm:

   - While tempting due to its simplicity, a greedy approach of always choosing the largest possible coin doesn't work for all cases.
   - Example: coins = [1, 5, 11], amount = 15. Greedy would give 5 coins (11 + 1 + 1 + 1 + 1), but optimal is 3 coins (5 + 5 + 5).

2. Brute Force (Recursive without memoization):

   - This approach would work correctly but is extremely inefficient.
   - It recalculates the same subproblems multiple times, leading to exponential time complexity.

3. Integer Linear Programming:
   - While this could solve the problem, it's overkill and not typically expected in coding interviews.
   - It requires specialized solvers and knowledge beyond standard programming techniques.

### Final Recommendations

The Bottom-up Dynamic Programming (Tabulation) approach is the best one to learn and use in an interview setting. Here's why:

1. It's the most efficient in terms of both time and space complexity.
2. It's iterative, which is often easier to understand and explain than recursive solutions.
3. It avoids the potential stack overflow issues that could occur with recursive solutions for large inputs.
4. It's a classic example of how to apply dynamic programming, which is a crucial concept in algorithm design.

The Top-down Dynamic Programming (Recursion with Memoization) approach is also worth knowing, as it can be more intuitive for some people and is a good way to introduce the concept of memoization.

The BFS approach, while interesting, is less common and might be harder to come up with in an interview setting. However, it's a good example of how graph algorithms can be applied to non-graph problems.

Avoid the greedy approach, as it's incorrect for this problem and could lead you astray in an interview. Also, avoid the brute force recursive approach without memoization, as it's inefficient and doesn't demonstrate understanding of dynamic programming concepts.

## Visualization(s)

To visualize the Bottom-up Dynamic Programming approach, let's create a simple table showing how the dp array is filled for a small example:

```tsx
import React from "react";

const CoinChangeVisualization = () => {
  const coins = [1, 2, 5];
  const amount = 11;
  const dp = Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  const steps = [];

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
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
            {steps[0].map((_, index) => (
              <th key={index} className="border border-gray-400 px-2 py-1">
                {index}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {steps.map((step, stepIndex) => (
            <tr key={stepIndex}>
              <td className="border border-gray-400 px-2 py-1 font-bold">
                {stepIndex + 1}
              </td>
              {step.map((value, index) => (
                <td key={index} className="border border-gray-400 px-2 py-1">
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

This visualization shows how the dp array is filled step by step. Each row represents the state of the dp array after considering all coins for that amount. The final row shows the minimum number of coins needed for each amount from 0 to 11. The value in dp[11] (which is 3) is the final answer.
