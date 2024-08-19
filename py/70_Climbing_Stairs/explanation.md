## Explanation: Climbing Stairs

### Analysis of problem & input data

This problem is a classic example of dynamic programming and is closely related to the Fibonacci sequence. The key characteristics of this problem are:

1. **Discrete steps**: You can only take 1 or 2 steps at a time.
2. **Distinct ways**: We're counting unique combinations, not permutations.
3. **Linear progression**: The problem grows linearly with n.
4. **Overlapping subproblems**: The number of ways to reach step n depends on the ways to reach steps n-1 and n-2.
5. **Optimal substructure**: The optimal solution can be constructed from optimal solutions of its subproblems.

The key principle that makes this question simple is the recurrence relation: F(n) = F(n-1) + F(n-2). This means that the number of ways to reach the nth step is the sum of the ways to reach the (n-1)th step (and then take 1 step) and the (n-2)th step (and then take 2 steps).

This problem is about pattern-matching to dynamic programming solutions, specifically those involving linear sequences with simple recurrence relations. Recognizing this pattern allows us to apply efficient DP techniques.

### Test cases

1. Edge cases:
   - n = 1 (minimum input)
   - n = 45 (maximum input)
2. Simple cases:
   - n = 2
   - n = 3
3. Larger case:
   - n = 10

Here's the executable Python code for these test cases:

```python
def climb_stairs(n: int) -> int:
    # Placeholder function, to be replaced with actual implementation
    pass

# Test cases
test_cases = [1, 45, 2, 3, 10]
for case in test_cases:
    result = climb_stairs(case)
    print(f"n = {case}: {result} ways")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Dynamic Programming (Bottom-Up)
2. Dynamic Programming (Top-Down with Memoization)
3. Fibonacci Formula (Binet's Formula)
4. Matrix Exponentiation

Count: 4 solutions

##### Rejected solutions

1. Naive Recursive Approach
2. Iterative Approach with Generating All Combinations

#### Worthy Solutions

##### Dynamic Programming (Bottom-Up)

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1  # Base case: 1 way to climb 1 step
    dp[2] = 2  # Base case: 2 ways to climb 2 steps

    for i in range(3, n + 1):
        # Number of ways to reach step i is sum of ways to reach i-1 and i-2
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

Time Complexity: O(n)
Space Complexity: O(n)

- Intuition: We build the solution incrementally from the bottom up.
- Invariant: At each step i, dp[i] represents the number of ways to reach step i.
- The recurrence relation dp[i] = dp[i-1] + dp[i-2] captures all possible ways to reach step i.

##### Dynamic Programming (Top-Down with Memoization)

```python
from typing import Dict

def climb_stairs(n: int) -> int:
    memo: Dict[int, int] = {}

    def dp(i: int) -> int:
        if i <= 2:
            return i
        if i in memo:
            return memo[i]

        # Recurrence relation: ways to reach i = ways to reach i-1 + ways to reach i-2
        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]

    return dp(n)
```

Time Complexity: O(n)
Space Complexity: O(n)

- Intuition: We solve the problem recursively but store intermediate results to avoid redundant calculations.
- Invariant: For any step i, we only calculate dp(i) once and store it in the memo.
- The memoization ensures that we don't recalculate values for the same step multiple times.

##### Fibonacci Formula (Binet's Formula)

```python
import math

def climb_stairs(n: int) -> int:
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2

    # Binet's formula for the nth Fibonacci number
    return round((math.pow(phi, n+1) - math.pow(psi, n+1)) / sqrt5)
```

Time Complexity: O(1)
Space Complexity: O(1)

- Intuition: The climbing stairs problem follows the Fibonacci sequence, which has a closed-form solution.
- Invariant: The nth Fibonacci number accurately represents the number of ways to climb n stairs.
- This solution leverages the mathematical properties of the golden ratio (phi) to calculate the result directly.

##### Matrix Exponentiation

```python
import numpy as np

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    # Define the base matrix
    base_matrix = np.array([[1, 1], [1, 0]], dtype=np.int64)

    def matrix_power(matrix: np.ndarray, power: int) -> np.ndarray:
        result = np.eye(2, dtype=np.int64)
        while power > 0:
            if power % 2 == 1:
                result = np.matmul(result, matrix) % (10**9 + 7)
            matrix = np.matmul(matrix, matrix) % (10**9 + 7)
            power //= 2
        return result

    # Calculate the n-1 power of the base matrix
    result_matrix = matrix_power(base_matrix, n-1)

    # The top-left element of the result matrix gives the answer
    return result_matrix[0][0]
```

Time Complexity: O(log n)
Space Complexity: O(1)

- Intuition: We can represent the Fibonacci recurrence as a matrix equation and use fast exponentiation.
- Invariant: The matrix [[1, 1], [1, 0]]^n produces the (n+1)th and nth Fibonacci numbers in its first row.
- This method is particularly efficient for very large n values and can handle modular arithmetic easily.

#### Rejected Approaches

1. Naive Recursive Approach:

   ```python
   def climb_stairs(n: int) -> int:
       if n <= 2:
           return n
       return climb_stairs(n-1) + climb_stairs(n-2)
   ```

   This approach, while correct, has a time complexity of O(2^n), making it extremely inefficient for larger values of n. It repeatedly calculates the same subproblems, leading to exponential time complexity.

2. Iterative Approach with Generating All Combinations:
   This approach would involve generating all possible combinations of 1 and 2 steps that sum up to n. While it would work for small n, it becomes impractical for larger n due to the large number of combinations to generate and count.

#### Final Recommendations

For learning and interview purposes, I recommend focusing on the Dynamic Programming (Bottom-Up) approach. It's intuitive, efficient, and demonstrates a solid understanding of dynamic programming principles. The Top-Down approach with memoization is also valuable to learn as it showcases recursive problem-solving with optimization.

The Fibonacci Formula approach, while extremely efficient, might be seen as a "trick" solution and doesn't demonstrate as much about your problem-solving skills. The Matrix Exponentiation method is advanced and might be overkill for this problem, but it's a powerful technique to know for more complex problems involving linear recurrences.

### Visualization(s)

To visualize the Dynamic Programming (Bottom-Up) approach, we can use a simple React component to show how the solution is built up:

```tsx
import React, { useState, useEffect } from "react";

const ClimbingStairsVisualization = () => {
  const [n, setN] = useState(5);
  const [dp, setDp] = useState([]);

  useEffect(() => {
    const calculateDP = () => {
      const newDp = new Array(n + 1).fill(0);
      newDp[1] = 1;
      newDp[2] = 2;
      for (let i = 3; i <= n; i++) {
        newDp[i] = newDp[i - 1] + newDp[i - 2];
      }
      setDp(newDp);
    };

    calculateDP();
  }, [n]);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">
        Climbing Stairs DP Visualization
      </h2>
      <div className="mb-4">
        <label htmlFor="n-input" className="mr-2">
          Number of stairs (n):
        </label>
        <input
          id="n-input"
          type="number"
          min="1"
          max="45"
          value={n}
          onChange={(e) =>
            setN(Math.min(45, Math.max(1, parseInt(e.target.value) || 1)))
          }
          className="border rounded px-2 py-1"
        />
      </div>
      <div className="flex flex-wrap gap-2">
        {dp.map((ways, i) => (
          <div key={i} className="border rounded p-2 text-center">
            <div className="font-bold">Step {i}</div>
            <div>{ways} ways</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ClimbingStairsVisualization;
```

This visualization shows how the DP array is filled from the bottom up, with each step showing the number of ways to reach that step. You can adjust the number of stairs to see how the solution changes.
