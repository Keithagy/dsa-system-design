# Explanation: Unique Paths

## Analysis of problem & input data

This problem is a classic example of a dynamic programming or combinatorics problem. The key characteristics that make this problem solvable are:

1. The robot can only move in two directions: right and down.
2. The grid has a fixed size (m x n).
3. We're asked to find the total number of unique paths, not the paths themselves.
4. The starting and ending points are fixed (top-left to bottom-right).

The key principle that makes this question simple is that the number of ways to reach any cell (i, j) is the sum of the number of ways to reach the cell above it (i-1, j) and the cell to its left (i, j-1). This is because the robot can only come from these two directions.

Another important observation is that this problem can be solved using combinatorics. The total number of moves the robot needs to make is always (m-1) + (n-1), and we need to choose which (m-1) of these moves will be downward moves (or equivalently, which (n-1) will be rightward moves).

### Test cases

1. Basic case:

   - Input: m = 3, n = 7
   - Expected Output: 28

2. Minimum grid size:

   - Input: m = 1, n = 1
   - Expected Output: 1

3. Square grid:

   - Input: m = 3, n = 3
   - Expected Output: 6

4. Long narrow grid:

   - Input: m = 1, n = 10
   - Expected Output: 1

5. Maximum grid size (according to constraints):
   - Input: m = 100, n = 100
   - Expected Output: 22750883079422934966181954039568885395604168260154104734000

Here's the Python code for these test cases:

```python
def test_unique_paths(func):
    test_cases = [
        ((3, 7), 28),
        ((1, 1), 1),
        ((3, 3), 6),
        ((1, 10), 1),
        ((100, 100), 22750883079422934966181954039568885395604168260154104734000)
    ]

    for (m, n), expected in test_cases:
        result = func(m, n)
        print(f"Input: m = {m}, n = {n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("Correct" if result == expected else "Wrong")
        print()

# You would call this function with your implementation, e.g.:
# test_unique_paths(unique_paths)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Dynamic Programming (Bottom-Up)
2. Dynamic Programming (Top-Down with Memoization)
3. Combinatorics Solution
4. Space-Optimized Dynamic Programming

Count: 4 solutions

#### Rejected solutions

1. Depth-First Search (DFS) / Backtracking
2. Breadth-First Search (BFS)

### Worthy Solutions

#### 1. Dynamic Programming (Bottom-Up)

```python
def unique_paths(m: int, n: int) -> int:
    # Initialize the DP table with 1s for the first row and column
    dp = [[1] * n for _ in range(m)]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            # Number of paths to (i,j) is sum of paths from above and left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # The bottom-right cell contains the total number of unique paths
    return dp[m-1][n-1]
```

Time Complexity: O(m _n)
Space Complexity: O(m_ n)

Intuition and invariants:

- The number of ways to reach any cell is the sum of ways to reach the cell above it and to its left.
- The first row and first column always have only one way to reach each cell (moving only right or only down).
- We build up the solution for larger subproblems using solutions to smaller subproblems.

#### 2. Dynamic Programming (Top-Down with Memoization)

```python
from typing import Dict, Tuple

def unique_paths(m: int, n: int) -> int:
    # Use a dictionary for memoization
    memo: Dict[Tuple[int, int], int] = {}

    def dp(i: int, j: int) -> int:
        # Base case: reached the destination
        if i == m - 1 and j == n - 1:
            return 1

        # Out of bounds
        if i >= m or j >= n:
            return 0

        # Check if we've already computed this subproblem
        if (i, j) in memo:
            return memo[(i, j)]

        # Recursive case: sum of paths from moving right and down
        memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
        return memo[(i, j)]

    return dp(0, 0)
```

Time Complexity: O(m _n)
Space Complexity: O(m_ n)

Intuition and invariants:

- We start from the top-left and recursively explore all paths.
- Memoization prevents redundant computations by storing results of subproblems.
- The base case is reaching the destination (bottom-right corner).
- Out-of-bounds moves are handled by returning 0 (no valid paths).

#### 3. Combinatorics Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to choose (m-1) down moves out of (m+n-2) total moves
        total_moves = m + n - 2
        down_moves = m - 1

        # Calculate (total_moves choose down_moves)
        numerator = 1
        denominator = 1

        # Calculate (total_moves choose down_moves) using the formula:
        # C(n,k) = n! / (k! * (n-k)!)
        # We can optimize this by cancelling out common factors
        for i in range(down_moves):
            numerator *= (total_moves - i)
            denominator *= (i + 1)

        return numerator // denominator

    def uniquePaths_with_explanation(self, m: int, n: int) -> int:
        total_moves = m + n - 2
        down_moves = m - 1

        print(f"Total moves: {total_moves}")
        print(f"Down moves: {down_moves}")

        numerator = 1
        denominator = 1

        print("\nCalculation steps:")
        for i in range(down_moves):
            numerator *= (total_moves - i)
            denominator *= (i + 1)
            print(f"Step {i+1}: numerator = {numerator}, denominator = {denominator}")

        result = numerator // denominator
        print(f"\nFinal result: {result}")
        return result
```

Time Complexity: O(min(m, n))
Space Complexity: O(1)
Intuition and invariants:

We're essentially calculating C(m+n-2, m-1) or C(m+n-2, n-1).
The formula for combinations is C(n,k) = n! / (k! \* (n-k)!).
We optimize the calculation by cancelling out common factors in the numerator and denominator.
This approach avoids overflow issues that might occur if we calculated the full factorials.

This solution demonstrates:

Understanding of the combinatorial nature of the problem.
Ability to implement a mathematical formula efficiently.
Awareness of potential numerical issues (like overflow) and how to avoid them.
Clear step-by-step calculation that could be explained in an interview setting.

The uniquePaths_with_explanation method provides detailed output that could be used to walk an interviewer through the solution process.

#### 4. Space-Optimized Dynamic Programming

```python
def unique_paths(m: int, n: int) -> int:
    # Use a single row to store the number of paths
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            # Update dp[j] using the previous value (left) and the value above (current dp[j])
            dp[j] += dp[j-1]

    return dp[-1]
```

Time Complexity: O(m \* n)
Space Complexity: O(n)

Intuition and invariants:

- We only need to keep track of the current row and the row above it.
- By updating the array in-place, we can use a single 1D array instead of a 2D array.
- Each iteration, dp[j] represents the number of paths to the cell in the current row and j-th column.

### Rejected Approaches

1. Depth-First Search (DFS) / Backtracking:

   - While this approach would work, it would be highly inefficient for large grids.
   - Time complexity would be O(2^(m+n)), which is exponential and much worse than the DP solution.
   - It doesn't leverage the overlapping subproblems structure of this problem.

2. Breadth-First Search (BFS):
   - Similar to DFS, this would work but be inefficient.
   - It would explore all possible paths, which is unnecessary when we only need the count.
   - Time and space complexity would be O(m\*n), but with a larger constant factor than DP.

### Final Recommendations

The Dynamic Programming (Bottom-Up) solution is the most recommended approach for several reasons:

1. It's intuitive and easy to understand.
2. It has optimal time complexity O(m\*n) and reasonable space complexity.
3. It's straightforward to implement and doesn't require recursion.

The Combinatorics solution is also worth learning as it provides the most efficient solution in terms of both time and space complexity. However, it requires a deeper understanding of combinatorics and might be less intuitive at first glance.

The Top-Down DP with memoization is a good alternative if you prefer recursive solutions, but it's slightly less efficient due to the overhead of recursion and dictionary lookups.

The Space-Optimized DP solution is an excellent optimization of the Bottom-Up approach and is worth knowing for interviews where space complexity is a concern.

Avoid using DFS or BFS for this problem, as they don't leverage the problem's structure and would be inefficient for larger inputs.

## Visualization(s)

Here's a simple visualization of how the Dynamic Programming (Bottom-Up) solution fills the grid:

```
   1   1   1   1   1   1   1
   1   2   3   4   5   6   7
   1   3   6  10  15  21  28
```

Each cell represents the number of unique paths to reach that cell. The bottom-right cell (3,7) contains the final answer, 28.
