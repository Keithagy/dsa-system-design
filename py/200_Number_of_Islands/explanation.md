# Explanation: Number of Islands

## Analysis of problem & input data

This problem is a classic graph traversal and connected components problem. The key characteristics and insights are:

1. The grid represents a graph where each land cell ('1') is a node, and adjacent land cells are connected.
2. We need to count the number of disconnected groups of land cells (islands).
3. The problem can be solved using either Depth-First Search (DFS) or Breadth-First Search (BFS).
4. The grid can be modified in-place to mark visited cells, which can save space.
5. The edges of the grid are surrounded by water, simplifying boundary checks.
6. The input is guaranteed to be a valid 2D grid with at least one cell.

The key principle that makes this question simple is that we can use a flood fill algorithm to mark all connected land cells as visited, and each time we start a new flood fill, we've found a new island.

### Test cases

Here are some test cases to consider:

1. Single island:

   ```python
   [["1","1","1"],
    ["1","1","1"],
    ["1","1","1"]]
   ```

   Expected output: 1

2. No islands:

   ```python
   [["0","0","0"],
    ["0","0","0"],
    ["0","0","0"]]
   ```

   Expected output: 0

3. Multiple small islands:

   ```python
   [["1","0","1","0","1"],
    ["0","1","0","1","0"],
    ["1","0","1","0","1"]]
   ```

   Expected output: 9

4. Island with hole:

   ```python
   [["1","1","1"],
    ["1","0","1"],
    ["1","1","1"]]
   ```

   Expected output: 1

5. Single cell island:

   ```python
   [["1"]]
   ```

   Expected output: 1

6. Large grid with various island shapes:

   ```python
   [["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]]
   ```

   Expected output: 3

Here's the code to run these test cases:

```python
def numIslands(grid: List[List[str]]) -> int:
    # Implementation will be added later
    pass

# Test cases
test_cases = [
    [["1","1","1"],
     ["1","1","1"],
     ["1","1","1"]],

    [["0","0","0"],
     ["0","0","0"],
     ["0","0","0"]],

    [["1","0","1","0","1"],
     ["0","1","0","1","0"],
     ["1","0","1","0","1"]],

    [["1","1","1"],
     ["1","0","1"],
     ["1","1","1"]],

    [["1"]],

    [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]]
]

expected_outputs = [1, 0, 9, 1, 1, 3]

for i, (test_case, expected) in enumerate(zip(test_cases, expected_outputs)):
    result = numIslands(test_case)
    print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
    print(f"Expected: {expected}, Got: {result}")
    print()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Depth-First Search (DFS) with in-place modification
2. Breadth-First Search (BFS) with in-place modification
3. Union-Find (Disjoint Set Union)
4. DFS with additional visited set
5. BFS with additional visited set

Count: 5 solutions

#### Rejected solutions

1. Brute force counting of contiguous regions without graph traversal
2. Using a general-purpose graph library (overkill for this problem)
3. Dynamic programming (not suitable for this type of problem)

### Worthy Solutions

#### 1. Depth-First Search (DFS) with in-place modification

```python
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    islands = 0

    def dfs(i: int, j: int) -> None:
        # Base case: out of bounds or water
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return

        # Mark current cell as visited
        grid[i][j] = '0'

        # Recursively visit all adjacent cells
        dfs(i+1, j)  # down
        dfs(i-1, j)  # up
        dfs(i, j+1)  # right
        dfs(i, j-1)  # left

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                # Found a new island, start DFS
                islands += 1
                dfs(i, j)

    return islands
```

Time Complexity: O(m _n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m_ n) in the worst case for the recursion stack (in case of a grid filled with land).

Intuition and invariants:

- Each cell is visited at most once.
- DFS explores all connected land cells before returning.
- Modifying the grid in-place saves space and marks visited cells.
- The number of times we initiate DFS is equal to the number of islands.

#### 2. Breadth-First Search (BFS) with in-place modification

```python
from typing import List
from collections import deque

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    islands = 0

    def bfs(i: int, j: int) -> None:
        queue = deque([(i, j)])
        while queue:
            curr_i, curr_j = queue.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + di, curr_j + dj
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == '1':
                    grid[next_i][next_j] = '0'  # Mark as visited
                    queue.append((next_i, next_j))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
                grid[i][j] = '0'  # Mark as visited
                bfs(i, j)

    return islands
```

Time Complexity: O(m \* n)
Space Complexity: O(min(m, n)) for the queue in the worst case

Intuition and invariants:

- BFS explores all connected land cells level by level.
- The queue contains at most min(m, n) elements (width of the grid).
- In-place modification marks visited cells and saves space.
- Each cell is enqueued at most once.

#### 3. Union-Find (Disjoint Set Union)

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

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    uf = UnionFind(m * n)
    land_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                land_count += 1
                for di, dj in [(1, 0), (0, 1)]:  # Only need to check right and down
                    ni, nj = i + di, j + dj
                    if ni < m and nj < n and grid[ni][nj] == '1':
                        uf.union(i * n + j, ni * n + nj)

    return land_count - (m * n - uf.count)

```

Time Complexity: O(m _n_ α(m _n)), where α is the inverse Ackermann function (nearly constant in practice)
Space Complexity: O(m_ n) for the UnionFind data structure

Intuition and invariants:

- Each land cell is initially its own set (island).
- We union adjacent land cells, reducing the number of sets.
- The final number of islands is the number of land cells minus the number of unions performed.
- Union-Find with path compression and union by rank provides near-constant time operations.

#### 4. DFS with additional visited set

```python
from typing import List, Set, Tuple

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(i: int, j: int) -> None:
        if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return

        visited.add((i, j))

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + di, j + dj)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i, j) not in visited:
                islands += 1
                dfs(i, j)

    return islands
```

Time Complexity: O(m _n)
Space Complexity: O(m_ n) for the visited set and recursion stack

Intuition and invariants:

- Similar to the in-place DFS, but uses an additional set to track visited cells.
- Preserves the original grid, which might be required in some scenarios.
- Each cell is visited at most once.

#### 5. BFS with additional visited set

```python
from typing import List, Set, Tuple
from collections import deque

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(i: int, j: int) -> None:
        queue = deque([(i, j)])
        visited.add((i, j))

        while queue:
            curr_i, curr_j = queue.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + di, curr_j + dj
                if (0 <= next_i < m and 0 <= next_j < n and
                    grid[next_i][next_j] == '1' and (next_i, next_j) not in visited):
                    visited.add((next_i, next_j))
                    queue.append((next_i, next_j))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i, j) not in visited:
                islands += 1
                bfs(i, j)

    return islands
```

Time Complexity: O(m _n)
Space Complexity: O(min(m, n)) for the queue and O(m_ n) for the visited set

Intuition and invariants:

- Similar to the in-place BFS, but uses an additional set to track visited cells.
- Preserves the original grid, which might be required in some scenarios.
- Each cell is visited and added to the queue at most once.

### Rejected Approaches

1. Brute force counting of contiguous regions without graph traversal:

   - This approach would involve checking each cell and its neighbors repeatedly, leading to a time complexity worse than O(m \* n).
   - It's more error-prone and harder to implement correctly compared to graph traversal methods.

2. Using a general-purpose graph library:

   - While it would work, it's overkill for this problem and would likely be less efficient in both time and space.
   - It doesn't demonstrate understanding of the underlying algorithms as well as implementing the solution directly.

3. Dynamic programming:
   - This problem doesn't have the optimal substructure property that makes DP effective.
   - The islands can have arbitrary shapes, making it difficult to define a meaningful DP state.

### Final Recommendations

The best solution to learn and implement for a technical coding interview would be the Depth-First Search (DFS) with in-place modification (Solution 1). Here's why:

1. It's the most straightforward to implement and explain.
2. It has optimal time complexity O(m _n) and space complexity O(m_ n) in the worst case, but often much better in practice.
3. It demonstrates understanding of graph traversal algorithms.
4. In-place modification shows awareness of space optimization.
5. The recursive implementation is clean and easy to understand.

The Breadth-First Search (BFS) solution is also worth knowing, as it can be preferred in some scenarios (e.g., when you need to find the shortest path or when the graph is very deep).

The Union-Find solution, while interesting and powerful for certain graph problems, is a bit overkill for this specific problem and might be harder to implement correctly under interview pressure.

Solutions using an additional visited set (4 and 5) are worth mentioning if asked about preserving the original grid, but they're not the primary recommendation due to the extra space usage.

A common mistake to avoid is trying to implement a solution that doesn't use graph traversal. For example, trying to count islands by scanning the grid row by row and column by column without proper backtracking will fail for complex island shapes.

Another pitfall is forgetting to mark visited cells, which can lead to infinite loops or overcounting islands. Always ensure each cell is processed only once.

## Visualization(s)

To visualize the DFS algorithm, we can use a simple ASCII representation of the grid and show how the algorithm progresses:

```
Initial grid:
1 1 0
1 0 1
0 1 1

Step 1: Start DFS at (0,0)
X X 0  (X represents visited cells)
X 0 1
0 1 1

Step 2: Continue DFS
X X 0
X 0 1
0 1 1

Step 3: Start new DFS at (1,2)
X X 0
X 0 X
0 X X

Final result: 2 islands found

X X 0
X 0 X
0 X X

```

This ASCII visualization helps to understand how the DFS algorithm works:

1. It starts at the top-left corner (0,0) and marks all connected '1's as visited (X).
2. Once it can't find any more connected '1's, it moves to the next unvisited '1' (1,2).
3. It marks all '1's connected to (1,2) as visited.
4. The process ends when all cells have been checked.

For a more interactive visualization, we could create a simple React component that shows the grid and allows stepping through the DFS process. Here's a basic implementation:

```tsx
import React, { useState } from "react";

const IslandVisualization = () => {
  const [grid, setGrid] = useState([
    ["1", "1", "0"],
    ["1", "0", "1"],
    ["0", "1", "1"],
  ]);
  const [step, setStep] = useState(0);
  const [islandCount, setIslandCount] = useState(0);

  const steps = [
    { row: 0, col: 0 },
    { row: 0, col: 1 },
    { row: 1, col: 0 },
    { row: 1, col: 2 },
    { row: 2, col: 1 },
    { row: 2, col: 2 },
  ];

  const nextStep = () => {
    if (step < steps.length) {
      const newGrid = [...grid];
      const { row, col } = steps[step];
      if (newGrid[row][col] === "1") {
        newGrid[row][col] = "X";
        setGrid(newGrid);
        if (step === 0 || step === 3) {
          setIslandCount((prev) => prev + 1);
        }
      }
      setStep((prev) => prev + 1);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Island Count Visualization</h2>
      <div className="grid grid-cols-3 gap-2 mb-4">
        {grid.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className={`w-12 h-12 flex items-center justify-center border ${
                cell === "1"
                  ? "bg-blue-500"
                  : cell === "X"
                    ? "bg-red-500"
                    : "bg-gray-200"
              }`}
            >
              {cell}
            </div>
          )),
        )}
      </div>
      <button
        onClick={nextStep}
        disabled={step >= steps.length}
        className="bg-green-500 text-white px-4 py-2 rounded disabled:bg-gray-400"
      >
        Next Step
      </button>
      <p className="mt-4">Islands found: {islandCount}</p>
      <p>
        Step: {step} / {steps.length}
      </p>
    </div>
  );
};

export default IslandVisualization;
```

This React component provides an interactive visualization of the island counting process:

1. It starts with the initial grid.
2. Each click on "Next Step" simulates a step in the DFS process.
3. Cells are color-coded: blue for land ('1'), red for visited land ('X'), and gray for water ('0').
4. The island count updates as new islands are discovered.

This visualization helps to understand:

1. How the DFS algorithm traverses the grid.
2. When new islands are discovered.
3. The final count of islands.

Key takeaways from this visualization:

1. The algorithm visits each cell exactly once.
2. It's efficient because it marks cells as visited, preventing redundant checks.
3. The number of times we start a new search (changing island count) equals the number of islands.

Understanding these visualizations can help in grasping the core concepts of the problem and its solution:

1. Graph representation: The grid is essentially an undirected graph where each cell is a node, and adjacent land cells are connected.
2. Connected components: Each island is a connected component in this graph.
3. DFS/BFS traversal: These algorithms efficiently explore all cells of an island once it's discovered.

By visualizing the process, it becomes clear why graph traversal algorithms are so effective for this problem. They naturally group connected land cells into islands, which is exactly what we need to count.
