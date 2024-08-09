# Explanation: Number of Islands

## Analysis of problem & input data

This problem is a classic graph traversal problem, specifically dealing with a 2D grid. Here are the key aspects to consider:

1. Grid representation: The input is a 2D binary grid where '1' represents land and '0' represents water.
2. Connectivity: Islands are formed by connecting adjacent lands horizontally or vertically (not diagonally).
3. Boundary condition: All edges of the grid are surrounded by water.
4. Goal: Count the number of distinct islands.

Key principles that make this problem approachable:

1. Graph exploration: Each land cell can be considered a node in a graph, with edges to its adjacent land cells.
2. Connected components: Each island is essentially a connected component in this graph.
3. Visited tracking: Once a land cell is visited, it doesn't need to be revisited.
4. In-place modification: The input grid can be modified to mark visited cells, saving space.

This problem can be pattern-matched to:

1. Depth-First Search (DFS) on a 2D grid
2. Breadth-First Search (BFS) on a 2D grid
3. Union-Find (Disjoint Set) algorithm

The key principle that makes this question simple is that we can "sink" (mark as visited) each land cell as we explore it, effectively removing it from future consideration and avoiding double-counting.

## Solutions

### Solution 1: Depth-First Search (DFS)

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i: int, j: int) -> None:
            # Check if current cell is out of bounds or is water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            # Mark current land cell as visited by changing it to '0'
            grid[i][j] = '0'

            # Recursively explore adjacent cells
            dfs(i+1, j)  # down
            dfs(i-1, j)  # up
            dfs(i, j+1)  # right
            dfs(i, j-1)  # left

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1  # Found a new island
                    dfs(i, j)  # Explore and mark all connected land cells

        return islands
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n) in the worst case for the recursion stack (in case of a grid filled with lands).

Intuition and invariants:

- Each unvisited land cell represents a new island.
- Once we start exploring from a land cell, we mark all connected land cells as visited.
- The number of times we initiate DFS is equal to the number of islands.

### Solution 2: Breadth-First Search (BFS)

```python
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1  # Found a new island
                    grid[i][j] = '0'  # Mark as visited
                    queue = deque([(i, j)])

                    # BFS to explore all connected land cells
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            r, c = row + dr, col + dc
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                                queue.append((r, c))
                                grid[r][c] = '0'  # Mark as visited

        return islands
```

Time Complexity: O(m \* n)
Space Complexity: O(min(m, n)) for the queue in the worst case

Intuition and invariants:

- Similar to DFS, but explores land cells level by level.
- The queue ensures we visit all adjacent land cells before moving to the next level.
- BFS can be more efficient in terms of stack space compared to DFS for large grids.

### Solution 3: Union-Find (Disjoint Set)

```python
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1  # Decrease the number of components

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        land_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    land_count += 1
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(i*n + j, (i-1)*n + j)
                    if j > 0 and grid[i][j-1] == '1':
                        uf.union(i*n + j, i*n + (j-1))

        return uf.count - (m * n - land_count)
```

Time Complexity: O(m \* n α(m \* n)), where α is the inverse Ackermann function, which grows very slowly and is effectively constant for all practical values of m and n.
Space Complexity: O(m \* n) for the UnionFind data structure.

Intuition and invariants:

- Each cell is initially its own set (island).
- We union adjacent land cells, effectively merging islands.
- The final number of islands is the number of sets minus the number of water cells.

## Recommendation

For this problem, I recommend learning and implementing the DFS solution (Solution 1). Here's why:

1. Simplicity: The DFS solution is the most intuitive and easiest to understand and implement.
2. Space efficiency: It can be implemented recursively, which is clean and doesn't require explicit stack management.
3. In-place modification: It directly modifies the input grid, saving space.
4. Interview performance: It's quick to code in an interview setting and easy to explain.

While the BFS and Union-Find solutions are also valid and have their merits, the DFS solution provides the best balance of simplicity, efficiency, and ease of explanation for this particular problem.

## Test cases

```python
def test_num_islands():
    solution = Solution()

    # Test case 1: Single island
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution.numIslands(grid1) == 1

    # Test case 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert solution.numIslands(grid2) == 3

    # Test case 3: No islands
    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert solution.numIslands(grid3) == 0

    # Test case 4: All islands
    grid4 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    assert solution.numIslands(grid4) == 1

    # Test case 5: Single cell island
    grid5 = [["1"]]
    assert solution.numIslands(grid5) == 1

    print("All test cases passed!")

test_num_islands()
```

## Overview of rejected approaches

1. Brute Force Counting:

   - Approach: Count each '1' as an island without considering connectivity.
   - Why it's incorrect: This would count each land cell as a separate island, ignoring the fact that adjacent land cells form a single island.

2. Flood Fill without marking visited cells:

   - Approach: Explore connected land cells but don't mark them as visited.
   - Why it's incorrect: This would lead to infinite loops or double-counting of islands, as the same land cells would be explored multiple times.

3. Diagonal Connectivity:

   - Approach: Consider diagonally adjacent cells as part of the same island.
   - Why it's incorrect: The problem specifically states that islands are formed by connecting adjacent lands horizontally or vertically, not diagonally.

4. Using a separate visited array:

   - Approach: Maintain a separate 2D array to keep track of visited cells instead of modifying the input grid.
   - Why it's not recommended: While this approach is correct, it uses unnecessary extra space. Modifying the input grid (if allowed) is more space-efficient.

5. Complex data structures:
   - Approach: Using complex data structures like graphs or trees to represent the grid.
   - Why it's not recommended: While these approaches might work, they add unnecessary complexity. The 2D grid itself is already an efficient representation for this problem.

## Visualization(s)

To visualize the DFS process, we can create a simple animation that shows how the algorithm explores and marks islands. Here's a React component that demonstrates this:

```tsx
import React, { useState, useEffect } from "react";
import { Card, CardHeader, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const initialGrid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];

const IslandDFSVisualization = () => {
  const [grid, setGrid] = useState(initialGrid);
  const [islandCount, setIslandCount] = useState(0);
  const [currentStep, setCurrentStep] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  const resetGrid = () => {
    setGrid(initialGrid.map((row) => [...row]));
    setIslandCount(0);
    setCurrentStep(0);
    setIsRunning(false);
  };

  const dfs = (i, j, visitedCells) => {
    if (
      i < 0 ||
      i >= grid.length ||
      j < 0 ||
      j >= grid[0].length ||
      grid[i][j] === "0"
    ) {
      return visitedCells;
    }

    visitedCells.push([i, j]);
    grid[i][j] = "0";

    dfs(i + 1, j, visitedCells);
    dfs(i - 1, j, visitedCells);
    dfs(i, j + 1, visitedCells);
    dfs(i, j - 1, visitedCells);

    return visitedCells;
  };

  const runDFS = () => {
    setIsRunning(true);
    let islands = 0;
    const allVisitedCells = [];

    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[0].length; j++) {
        if (grid[i][j] === "1") {
          islands++;
          const visitedCells = dfs(i, j, []);
          allVisitedCells.push(...visitedCells);
        }
      }
    }

    setIslandCount(islands);

    let step = 0;
    const interval = setInterval(() => {
      if (step < allVisitedCells.length) {
        const [i, j] = allVisitedCells[step];
        setGrid((prevGrid) => {
          const newGrid = prevGrid.map((row) => [...row]);
          newGrid[i][j] = "2"; // Mark as visited
          return newGrid;
        });
        setCurrentStep(step + 1);
        step++;
      } else {
        clearInterval(interval);
        setIsRunning(false);
      }
    }, 200);
  };

  return (
    <Card>
      <CardHeader>Number of Islands DFS Visualization</CardHeader>
      <CardContent>
        <div className="grid grid-cols-5 gap-1 mb-4">
          {grid.map((row, i) =>
            row.map((cell, j) => (
              <div
                key={`${i}-${j}`}
                className={`w-8 h-8 border ${
                  cell === "1"
                    ? "bg-blue-500"
                    : cell === "2"
                      ? "bg-red-500"
                      : "bg-gray-200"
                }`}
              />
            )),
          )}
        </div>
        <div className="mb-4">
          <p>Islands found: {islandCount}</p>
          <p>Current step: {currentStep}</p>
        </div>
        <div className="flex space-x-2">
          <Button onClick={runDFS} disabled={isRunning}>
            Run DFS
          </Button>
          <Button onClick={resetGrid} disabled={isRunning}>
            Reset
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default IslandDFSVisualization;
```

This visualization demonstrates how the DFS algorithm explores the grid, marking land cells as visited (red) as it goes. The blue cells represent unvisited land, and gray cells represent water. The component allows you to run the DFS algorithm step by step, showing how islands are discovered and marked.

To use this visualization:

1. The grid is initially displayed with land (blue) and water (gray) cells.
2. Click "Run DFS" to start the visualization.
3. Watch as the algorithm explores the grid, turning land cells red as they are visited.
4. The island count and current step are updated in real-time.
5. Once complete, you can reset the grid to its initial state and run the visualization again.

This visual representation helps to understand how the DFS algorithm systematically explores connected land cells to identify and count distinct islands. It illustrates the key concepts of the algorithm:

1. Starting from an unvisited land cell (blue).
2. Exploring all connected land cells in depth-first manner.
3. Marking visited cells (changing them to red) to avoid revisiting.
4. Counting each disconnected group of land cells as a separate island.

This visualization can be particularly helpful for understanding:

1. How the algorithm avoids double-counting islands by marking visited cells.
2. The recursive nature of DFS, as it explores all connected cells before backtracking.
3. How the algorithm naturally handles different island shapes and sizes.

To further enhance understanding, we could add additional features to the visualization:

1. Speed control: Allow users to adjust the speed of the visualization.
2. Step-by-step mode: Enable users to step through the algorithm one cell at a time.
3. Custom grid input: Allow users to create their own grid configurations.
4. Comparison view: Show side-by-side visualizations of DFS and BFS approaches.

These enhancements would provide a more interactive and comprehensive learning experience for users trying to understand the Number of Islands problem and its solutions.
