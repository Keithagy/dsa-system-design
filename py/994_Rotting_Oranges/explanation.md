# Explanation: Rotting Oranges

## Analysis of problem & input data

This problem is a classic example of a grid-based simulation with spreading effect, which can be effectively solved using a breadth-first search (BFS) approach. The key characteristics and insights of this problem are:

1. Grid representation: The problem uses a 2D grid to represent the state of oranges.
2. Discrete time steps: The rotting process occurs in discrete time steps (minutes).
3. 4-directional spread: Rotting spreads only in four directions (up, down, left, right).
4. Simultaneous spread: All rotten oranges spread rot to their neighbors simultaneously.
5. Termination conditions: The process ends when either all oranges are rotten or no more oranges can be reached.

The key principle that makes this question conceptually simple is that BFS naturally models the simultaneous spread of rot from multiple sources, with each level of the BFS representing one time step.

## Test cases

### Test cases

1. Normal case (from Example 1):

   ```python
   grid1 = [[2,1,1],[1,1,0],[0,1,1]]
   # Expected output: 4
   ```

2. Impossible case (from Example 2):

   ```python
   grid2 = [[2,1,1],[0,1,1],[1,0,1]]
   # Expected output: -1
   ```

3. Already finished case (from Example 3):

   ```python
   grid3 = [[0,2]]
   # Expected output: 0
   ```

4. Single fresh orange:

   ```python
   grid4 = [[1]]
   # Expected output: -1
   ```

5. No fresh oranges:

   ```python
   grid5 = [[2,2,2],[2,2,2],[2,2,2]]
   # Expected output: 0
   ```

6. Complex case with multiple rotten sources:

   ```python
   grid6 = [[2,1,1,1,2],[1,1,0,1,1],[0,1,1,1,0]]
   # Expected output: 2
   ```

### Executable Python code for tests

```python
def orangesRotting(grid: List[List[int]]) -> int:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([[2,1,1],[1,1,0],[0,1,1]], 4),
    ([[2,1,1],[0,1,1],[1,0,1]], -1),
    ([[0,2]], 0),
    ([[1]], -1),
    ([[2,2,2],[2,2,2],[2,2,2]], 0),
    ([[2,1,1,1,2],[1,1,0,1,1],[0,1,1,1,0]], 2)
]

for i, (grid, expected) in enumerate(test_cases):
    result = orangesRotting(grid)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. BFS with queue (optimal)
2. DFS with recursion
3. In-place BFS simulation

Count: 3 solutions

#### Rejected solutions

1. Brute force simulation
2. Dijkstra's algorithm
3. Union-Find

### Worthy Solutions

#### 1. BFS with queue (optimal)

```python
from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # Initialize queue with rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_oranges += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    max_time = 0

    # BFS
    while queue and fresh_oranges > 0:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Mark as rotten
                fresh_oranges -= 1
                queue.append((nr, nc, time + 1))

    return max_time if fresh_oranges == 0 else -1
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n) in the worst case when all oranges are rotten.

Intuition and invariants:

- BFS naturally models the simultaneous spread of rot.
- The queue stores the coordinates of rotten oranges and the time they became rotten.
- We process all oranges that rot at the same time before moving to the next time step.
- The maximum time in the queue represents the total time for the process.
- Keeping track of fresh oranges allows early termination and detection of impossible cases.

#### 2. DFS with recursion

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    fresh_oranges = 0
    max_time = 0

    def dfs(r: int, c: int, time: int) -> None:
        nonlocal fresh_oranges, max_time
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return

        grid[r][c] = 2  # Mark as rotten
        fresh_oranges -= 1
        max_time = max(max_time, time)

        # Spread to neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, time + 1)

    # Count fresh oranges and start DFS from rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_oranges += 1
            elif grid[r][c] == 2:
                grid[r][c] = 0  # Mark as visited
                dfs(r, c, 0)

    return max_time if fresh_oranges == 0 else -1
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n) in the worst case due to recursive call stack.

Intuition and invariants:

- DFS simulates the spread of rot from each rotten orange.
- We keep track of the maximum time reached during DFS.
- The recursive nature of DFS models the spread of rot over time.
- We need to manually ensure all rotten oranges are processed as starting points.

#### 3. In-place BFS simulation

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    fresh_oranges = 0
    rotten = set()

    # Initialize rotten set and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.add((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    minutes = 0
    while rotten and fresh_oranges > 0:
        new_rotten = set()
        for r, c in rotten:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    new_rotten.add((nr, nc))
        rotten = new_rotten
        minutes += 1 if new_rotten else 0

    return minutes if fresh_oranges == 0 else -1
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n) in the worst case when all oranges are rotten.

Intuition and invariants:

- This approach simulates BFS without using a queue.
- We use sets to keep track of rotten oranges at each time step.
- The grid is modified in-place to mark oranges as they rot.
- Each iteration of the outer while loop represents one minute.

### Rejected Approaches

1. Brute force simulation: Repeatedly scanning the entire grid to spread rot would be inefficient, with a time complexity of O((m \* n)^2) in the worst case.

2. Dijkstra's algorithm: While it could work, it's overkill for this problem as all edges (connections between adjacent cells) have the same weight of 1. BFS is more efficient for uniform-weight graphs.

3. Union-Find: This data structure is typically used for disjoint set problems and doesn't naturally model the time-based spread of rot.

### Final Recommendations

The BFS with queue approach is the most recommended solution for this problem. It naturally models the simultaneous spread of rot from multiple sources, with each level of the BFS representing one time step. It's intuitive, efficient, and directly maps to the problem statement.

The DFS approach, while correct, is less intuitive for this problem because it doesn't naturally represent the simultaneous spread from all rotten oranges. It could be confusing in an interview setting.

The in-place BFS simulation is a space-optimized version of BFS, but it modifies the input grid, which might not be desirable in all scenarios.

Approaches like brute force simulation or using more complex algorithms like Dijkstra's are either inefficient or unnecessary for this specific problem.

## Visualization(s)

To visualize the BFS approach, we can use a simple ASCII representation of the grid at each time step. Here's a visualization of the process for the grid in Example 1:

```
Initial state:
2 1 1
1 1 0
0 1 1

After 1 minute:
2 2 1
2 1 0
0 1 1

After 2 minutes:
2 2 2
2 2 0
0 1 1

After 3 minutes:
2 2 2
2 2 0
0 2 1

After 4 minutes:
2 2 2
2 2 0
0 2 2

Process complete in 4 minutes.
```

This visualization helps to understand how the rot spreads over time, always to adjacent fresh oranges in the four cardinal directions.
