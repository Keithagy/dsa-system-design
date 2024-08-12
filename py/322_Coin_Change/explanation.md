# Explanation: Coin Change Problem

## Analysis of problem & input data

This is a classic dynamic programming problem, specifically falling under the category of "minimum coin change" or "coin change with fewest coins". The key aspects of this problem are:

1. We're dealing with a combination problem, where order doesn't matter (5+1+5 is the same as 5+5+1).
2. We have an unlimited supply of each coin denomination.
3. We're looking for the minimum number of coins, not just any valid combination.
4. The problem has optimal substructure: the optimal solution for a larger amount can be constructed from optimal solutions of smaller amounts.
5. There are overlapping subproblems: we might need to calculate the solution for the same subamount multiple times.

The key principle that makes this question tractable is that we can build up the solution for larger amounts from solutions to smaller amounts. For any amount `n`, the minimum number of coins needed is 1 (if `n` is in `coins`) plus the minimum number of coins needed for `n - coin` for some coin in `coins`.

The input characteristics are also important:

- We have a relatively small number of coin denominations (≤ 12).
- The coin values can be quite large (up to 2^31 - 1).
- The target amount is relatively small (≤ 10^4).

These characteristics suggest that a bottom-up dynamic programming approach might be more efficient than a top-down recursive approach, as we'll be dealing with a manageable number of subproblems (10^4 at most).

### Test cases

Let's consider some important test cases:

1. Basic case:

   ```python
   coins = [1, 2, 5], amount = 11
   # Expected output: 3 (5 + 5 + 1)
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

4. Large amount, small coins:

   ```python
   coins = [1, 2, 5], amount = 100
   # Expected output: 20 (5 * 20)
   ```

5. Large coins, small amount:

   ```python
   coins = [186, 419, 83, 408], amount = 6249
   # Expected output: 20
   ```

6. Greedy approach fails:

   ```python
   coins = [1, 3, 4], amount = 6
   # Expected output: 2 (3 + 3), not 3 (4 + 1 + 1)
   ```

Here's the executable Python code for these test cases:

```python
def coin_change(coins: List[int], amount: int) -> int:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1, 2, 5], 100, 20),
    ([186, 419, 83, 408], 6249, 20),
    ([1, 3, 4], 6, 2)
]

for i, (coins, amount, expected) in enumerate(test_cases, 1):
    result = coin_change(coins, amount)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    print(f"  Input: coins = {coins}, amount = {amount}")
    print(f"  Expected: {expected}, Got: {result}\n")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Bottom-up Dynamic Programming (Tabulation)
2. Top-down Dynamic Programming (Recursion with Memoization)
3. BFS (Breadth-First Search)

Count: 3 solutions

#### Rejected solutions

1. Greedy Algorithm: Doesn't always give the optimal solution.
2. Recursive solution without memoization: Extremely inefficient due to redundant calculations.
3. Brute force (generate all combinations): Time complexity would be exponential.

### Worthy Solutions

#### 1. Bottom-up Dynamic Programming (Tabulation)

```python
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # Initialize dp array with amount + 1 (impossible value) for all amounts
    dp = [amount + 1] * (amount + 1)
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Iterate through all amounts from 1 to target amount
    for i in range(1, amount + 1):
        # For each coin, if it's less than or equal to the current amount
        for coin in coins:
            if coin <= i:
                # Update dp[i] if using this coin leads to fewer total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] was not updated, return -1 (impossible), else return dp[amount]
    return dp[amount] if dp[amount] != amount + 1 else -1
```

Time Complexity: O(amount \* len(coins))
Space Complexity: O(amount)

Intuition and invariants:

- We build up solutions for all amounts from 0 to the target amount.
- For each amount, we consider using each coin and choose the option that leads to the minimum number of coins.
- dp[i] always represents the minimum number of coins needed to make amount i.
- The final answer is in dp[amount].

#### 2. Top-down Dynamic Programming (Recursion with Memoization)

```python
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # Memoization dictionary to store results of subproblems
    memo = {}

    def dp(remaining):
        # Base case: if remaining amount is 0, we need 0 coins
        if remaining == 0:
            return 0
        # Base case: if remaining amount is negative, it's impossible
        if remaining < 0:
            return float('inf')

        # Check if we've already solved this subproblem
        if remaining in memo:
            return memo[remaining]

        # Initialize min_coins to an impossible value
        min_coins = float('inf')

        # Try using each coin and recursively solve for the remaining amount
        for coin in coins:
            result = dp(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        # Memoize the result for this remaining amount
        memo[remaining] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1
```

Time Complexity: O(amount \* len(coins)) in the worst case, but often better in practice due to memoization.
Space Complexity: O(amount) for the memoization dictionary and the recursion stack.

Intuition and invariants:

- We recursively break down the problem into smaller subproblems.
- For each amount, we try using each coin and recursively solve for the remaining amount.
- We use memoization to avoid redundant calculations.
- The base cases handle amounts of 0 (solved) and negative amounts (impossible).

#### 3. BFS (Breadth-First Search)

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

    return -1  # If we can't reach the target amount
```

Time Complexity: O(amount \* len(coins)) in the worst case.
Space Complexity: O(amount) for the queue and visited set.

Intuition and invariants:

- We treat the problem as a graph, where each node represents an amount.
- We use BFS to find the shortest path (minimum number of coins) to reach the target amount.
- The first time we reach the target amount is guaranteed to be the solution with the minimum number of coins.
- We use a visited set to avoid revisiting the same amounts and prevent infinite loops.

### Rejected Approaches

1. Greedy Algorithm: While tempting due to its simplicity, a greedy approach (always choosing the largest coin possible) doesn't always give the optimal solution. For example, with coins [1, 3, 4] and amount 6, the greedy approach would give 3 coins (4 + 1 + 1), while the optimal solution is 2 coins (3 + 3).

2. Recursive solution without memoization: This would work correctly but would be extremely inefficient due to redundant calculations. The time complexity would be exponential, making it impractical for larger inputs.

3. Brute force (generate all combinations): This approach would generate all possible combinations of coins and then find the one with the minimum number of coins. While correct, its time complexity would be exponential, making it impractical for all but the smallest inputs.

### Final Recommendations

The bottom-up dynamic programming solution (Tabulation) is the best one to learn and use in an interview setting. Here's why:

1. It's the most efficient in terms of both time and space complexity.
2. It's iterative, which is often easier to implement correctly under pressure than recursive solutions.
3. It clearly demonstrates understanding of dynamic programming principles.
4. It's easier to analyze and explain its time and space complexity.

The top-down dynamic programming solution (Recursion with Memoization) is also worth knowing, as it can be more intuitive for some people and can be quickly adapted to solve variations of the problem.

The BFS solution, while interesting and demonstrating good problem-solving skills, is less commonly used for this specific problem and might be overkill in an interview setting.

Avoid the greedy approach in the interview, as it doesn't always give the correct answer and might suggest a lack of thorough problem analysis.

## Visualization(s)

To visualize the bottom-up dynamic programming solution, let's create a simple table showing how the dp array is filled for a small example:

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
      <p className="mb-2">
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
          {steps.map((step, index) => (
            <tr key={index}>
              <td className="border border-gray-400 px-2 py-1 font-bold">
                {index + 1}
              </td>
              {step.map((value, cellIndex) => (
                <td
                  key={cellIndex}
                  className={`border border-gray-400 px-2 py-1 ${
                    value === amount + 1 ? "bg-gray-200" : "bg-green-200"
                  }`}
                >
                  {value === amount + 1 ? "∞" : value}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <p className="mt-4">
        Green cells show updated values. The final answer is in the last cell of
        the last row.
      </p>
    </div>
  );
};

export default CoinChangeVisualization;
```

This visualization shows how the dp array is filled step by step. Each row represents the state of the dp array after processing the amount indicated in the leftmost column. The final answer can be found in the last cell of the last row.
