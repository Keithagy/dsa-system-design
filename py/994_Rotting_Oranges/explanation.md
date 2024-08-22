## Explanation: Rotting Oranges

### Analysis of problem & input data

This problem presents a grid-based simulation where the state of each cell changes over time based on its neighbors. The key characteristics of this problem are:

1. Grid-based structure: The input is a 2D grid, which immediately suggests potential for graph-like algorithms.
2. State propagation: The "rotting" state spreads from cell to cell, reminiscent of infection or wave propagation problems.
3. Time component: We need to track the progression of the simulation over discrete time steps.
4. Multiple starting points: There can be multiple rotten oranges at the beginning, each acting as a source of rot.
5. Termination conditions: The simulation ends when either all oranges are rotten or some oranges can't be reached.

The subtleties that make this problem tricky and easy to get wrong include:

1. Simultaneous propagation: All rotten oranges spread rot at the same time in each minute. This is not a depth-first process but a breadth-first one.
2. Unreachable fresh oranges: It's possible to have fresh oranges that can never rot, which requires careful checking for termination.
3. Empty spaces: The presence of empty cells (0) can block the spread of rot, creating isolated regions.
4. Edge cases: Grids with no fresh oranges initially, or grids with only one cell, require special consideration.

The key principle that makes this question conceptually simple is the idea of level-order traversal in a graph, where each "level" represents a minute in the simulation. This naturally maps to a Breadth-First Search (BFS) approach, but with the added complexity of multiple starting points and a grid-based structure instead of a traditional graph.

### Test cases

Here are some test cases that cover various scenarios:

1. Normal case (from Example 1):

   ```python
   grid1 = [[2,1,1],[1,1,0],[0,1,1]]
   # Expected output: 4
   ```

2. Impossible to rot all oranges (from Example 2):

   ```python
   grid2 = [[2,1,1],[0,1,1],[1,0,1]]
   # Expected output: -1
   ```

3. No fresh oranges initially (from Example 3):

   ```python
   grid3 = [[0,2]]
   # Expected output: 0
   ```

4. Single cell grid:

   ```python
   grid4 = [[1]]
   # Expected output: -1
   ```

5. Multiple sources of rot:

   ```python
   grid5 = [[2,1,1],[2,1,1],[1,1,2]]
   # Expected output: 2
   ```

6. Complex layout with obstacles:

   ```python
   grid6 = [[2,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,1,1,1,2]]
   # Expected output: 4
   ```

7. All rotten initially:

   ```python
   grid7 = [[2,2,2],[2,2,2],[2,2,2]]
   # Expected output: 0
   ```

Here's the Python code to run these test cases:

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
    ([[2,1,1],[2,1,1],[1,1,2]], 2),
    ([[2,1,1,1,1],
      [1,0,0,0,1],
      [1,0,1,0,1],
      [1,0,0,0,1],
      [1,1,1,1,2]], 4),
    ([[2,2,2],[2,2,2],[2,2,2]], 0)
]

for i, (grid, expected) in enumerate(test_cases, 1):
    result = orangesRotting(grid)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Breadth-First Search (BFS) with queue
2. In-place simulation with multiple passes
3. Depth-First Search (DFS) with memoization

Count: 3 solutions

##### Rejected solutions

1. Naive simulation (updating grid in-place in a single pass)
2. Depth-First Search (DFS) without memoization
3. Union-Find (Disjoint Set Union)

#### Worthy Solutions

##### Breadth-First Search (BFS) with queue

```python
from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # If there are no fresh oranges, return 0
    if fresh_oranges == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    max_time = 0

    while queue and fresh_oranges > 0:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2  # Mark as rotten
                fresh_oranges -= 1
                queue.append((new_row, new_col, time + 1))

    return max_time if fresh_oranges == 0 else -1
```

Time Complexity: O(rows \* cols), where rows and cols are the dimensions of the grid.
Space Complexity: O(rows \* cols) in the worst case, when all oranges are rotten initially.

- This solution uses a queue to perform a breadth-first search from all initially rotten oranges simultaneously.
- We keep track of the time for each orange as it rots, which naturally gives us the minimum time for the process to complete.
- The use of a queue ensures that we process all oranges at a given "time step" before moving to the next, simulating simultaneous rotting.
- By counting fresh oranges initially and decrementing as we rot them, we can easily check if all oranges have been rotten at the end.

##### In-place simulation with multiple passes

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    minutes = 0

    while True:
        rotted = False
        next_grid = [row[:] for row in grid]  # Create a copy of the grid

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # If the orange is rotten
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                            next_grid[new_r][new_c] = 2  # Mark as rotten in the next minute
                            rotted = True

        if not rotted:  # If no new oranges were rotted, we're done
            break

        grid = next_grid
        minutes += 1

    # Check if there are any fresh oranges left
    return minutes if all(2 not in row for row in grid) else -1
```

Time Complexity: O(rows \* cols \* max(rows, cols)) in the worst case, where the grid is a long snake-like path.
Space Complexity: O(rows \* cols) for creating the next_grid in each iteration.

- This solution simulates the rotting process minute by minute, creating a new grid for each minute.
- We iterate through the grid in each minute, marking fresh oranges adjacent to rotten ones as rotten in the next minute's grid.
- The process continues until no new oranges are rotted in a minute.
- This approach is more intuitive and closely mimics the problem description, but it's less efficient than BFS for large grids.

##### Depth-First Search (DFS) with memoization

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    memo = {}  # (row, col) -> minimum time to rot

    def dfs(r: int, c: int, time: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
            return

        if (r, c) in memo and memo[(r, c)] <= time:
            return

        memo[(r, c)] = time

        if grid[r][c] == 1:
            return

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, time + 1)

    # Start DFS from each rotten orange
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                dfs(r, c, 0)

    max_time = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if (r, c) not in memo:
                    return -1  # Fresh orange that can't be reached
                max_time = max(max_time, memo[(r, c)])

    return max_time
```

Time Complexity: O(rows \* cols) as each cell is visited at most once due to memoization.
Space Complexity: O(rows \* cols) for the memoization dictionary and recursion stack.

- This solution uses DFS with memoization to calculate the minimum time for each orange to rot.
- We start DFS from each initially rotten orange, spreading the "rot" to neighboring cells.
- Memoization prevents revisiting cells with a longer time, ensuring optimal paths.
- After DFS, we check if all fresh oranges were reachable and find the maximum time among them.

#### Rejected Approaches

##### Naive simulation (updating grid in-place in a single pass)

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    minutes = 0

    while True:
        rotted = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            rotted = True

        if not rotted:
            break
        minutes += 1

    return minutes if all(1 not in row for row in grid) else -1
```

Time Complexity: O(rows \* cols \* max(rows, cols))
Space Complexity: O(1)

This approach is incorrect because:

- It updates the grid in-place during a single pass, which can cause cascading rot within a single minute.
- This violates the problem's requirement that rot should spread simultaneously in discrete time steps.
- For example, in a grid [[2,1,1,1,1]], this approach would rot all oranges in a single minute, which is incorrect.

##### Depth-First Search (DFS) without memoization

```python
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int, time: int) -> int:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
            return time

        if grid[r][c] == 1:
            grid[r][c] = 2
            return time + 1

        max_time = time
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            max_time = max(max_time, dfs(r + dr, c + dc, time + 1))

        return max_time

    max_time = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                max_time = max(max_time, dfs(r, c, 0))

    return max_time if all(1 not in row for row in grid) else -1
```

Time Complexity: O(4^(rows \* cols)) in the worst case
Space Complexity: O(rows \* cols) for the recursion stack

This approach is correct but inefficient because:

- Without memoization, it explores all possible paths from each rotten orange, leading to redundant computations.
- The time complexity is exponential, making it impractical for larger grids.
- It doesn't capture the simultaneous nature of the rot spreading as effectively as BFS.

##### Union-Find (Disjoint Set Union)

```python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)
    fresh = set()
    rotten = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh.add(r * cols + c)
            elif grid[r][c] == 2:
                rotten.add(r * cols + c)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[r][c] != 0 and grid[new_r][new_c] != 0:
                    uf.union(r * cols + c, new_r * cols + new_c)

    if not fresh:
        return 0

    minutes = 0
    while fresh:
        for orange in list(fresh):
            if any(uf.find(orange) == uf.find(rot) for rot in rotten):
                fresh.remove(orange)
                rotten.add(orange)
        if not fresh:
            return minutes
        minutes += 1

    return -1
```

Time Complexity: O((rows _cols)^2) in the worst case
Space Complexity: O(rows_ cols)

This approach is correct but not optimal because:

- It doesn't capture the time component of the problem naturally. We have to simulate the rotting process manually.
- The Union-Find data structure is typically used for problems involving connectivity in undirected graphs, but this problem has a directed, time-dependent nature that isn't well-suited to Union-Find.
- The time complexity is quadratic in the worst case, making it less efficient than BFS for this specific problem.
- It's more complex to implement and understand compared to the BFS solution, which more naturally maps to the problem description.

#### Final Recommendations

The Breadth-First Search (BFS) with queue approach is the best solution to learn and use for this problem. Here's why:

1. Efficiency: It has the best time complexity (O(rows \* cols)) among all solutions, visiting each cell exactly once.
2. Intuitive: It naturally simulates the simultaneous spreading of rot in discrete time steps, which aligns perfectly with the problem description.
3. Space efficiency: While it uses extra space for the queue, it's still O(rows \* cols) in the worst case, which is acceptable.
4. Ease of implementation: The BFS solution is straightforward to implement and understand, making it a good choice for coding interviews.
5. Versatility: The BFS approach can be easily adapted to similar problems with different conditions or grid structures.

While the other solutions (in-place simulation and DFS with memoization) are worth understanding for their unique perspectives, the BFS approach stands out as the most elegant and efficient solution for this specific problem.

### Visualization(s)

To help visualize the BFS approach, we can create a simple React component that demonstrates how the rot spreads over time:

```tsx
import React, { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";

const OrangeGrid = ({ grid, step }) => {
  const getColor = (cell) => {
    if (cell === 0) return "bg-gray-200";
    if (cell === 1) return "bg-orange-400";
    if (cell === 2) return "bg-red-600";
    return "bg-white";
  };

  return (
    <div className="grid grid-cols-3 gap-1 mb-4">
      {grid.map((row, i) =>
        row.map((cell, j) => (
          <div
            key={`${i}-${j}`}
            className={`w-8 h-8 ${getColor(cell)} rounded-full flex items-center justify-center text-white font-bold`}
          >
            {cell !== 0 ? cell : ""}
          </div>
        )),
      )}
    </div>
  );
};

const RottingOrangesVisualization = () => {
  const initialGrid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
  ];

  const [grid, setGrid] = useState(initialGrid);
  const [step, setStep] = useState(0);
  const [isComplete, setIsComplete] = useState(false);

  const simulateStep = () => {
    const newGrid = grid.map((row) => [...row]);
    let changed = false;

    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[0].length; j++) {
        if (grid[i][j] === 2) {
          [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
          ].forEach(([di, dj]) => {
            const ni = i + di,
              nj = j + dj;
            if (
              ni >= 0 &&
              ni < grid.length &&
              nj >= 0 &&
              nj < grid[0].length &&
              grid[ni][nj] === 1
            ) {
              newGrid[ni][nj] = 2;
              changed = true;
            }
          });
        }
      }
    }

    if (changed) {
      setGrid(newGrid);
      setStep(step + 1);
    } else {
      setIsComplete(true);
    }
  };

  const reset = () => {
    setGrid(initialGrid);
    setStep(0);
    setIsComplete(false);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Rotting Oranges Visualization</h2>
      <OrangeGrid grid={grid} step={step} />
      <div className="mb-4">Step: {step}</div>
      <Button onClick={simulateStep} disabled={isComplete} className="mr-2">
        Next Step
      </Button>
      <Button onClick={reset}>Reset</Button>
      {isComplete && (
        <div className="mt-4 text-green-600 font-bold">
          Simulation complete!
        </div>
      )}
    </div>
  );
};

export default RottingOrangesVisualization;
```

This visualization helps to understand:

1. How the rot spreads from multiple sources simultaneously.
2. The discrete nature of the time steps in the simulation.
3. How obstacles (empty cells) affect the spread of rot.
4. The termination condition when no more fresh oranges can be rotten.

By interacting with this visualization, you can see how the BFS algorithm naturally maps to the problem's behavior, making it easier to understand why it's the optimal solution for this problem.
