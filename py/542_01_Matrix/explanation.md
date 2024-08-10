# Explanation: 01 Matrix

## Analysis of problem & input data

This problem involves finding the distance to the nearest 0 for each cell in a binary matrix. Several key aspects of the problem are worth noting:

1. The input is a binary matrix, containing only 0s and 1s.
2. We need to calculate distances for all cells, not just the 1s.
3. The distance is defined as the Manhattan distance (L1 norm) between cells.
4. The problem has a spatial relationship - we're dealing with adjacent cells in a 2D grid.
5. There's a guarantee of at least one 0 in the matrix, ensuring a valid solution always exists.
6. The matrix can be large (up to 10^4 x 10^4), so efficiency is crucial.

The key principle that makes this question approachable is that the distance to the nearest 0 for any cell can be built up from the distances of its neighbors. This suggests both dynamic programming and graph traversal approaches could be effective.

Solution approaches include:

1. Multi-source BFS (Breadth-First Search)
2. Dynamic Programming (two-pass)
3. Brute Force with optimization
   (3 in total)

## Solutions

### Multi-source BFS

```python
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = set()

        # Initialize queue with all 0s and mark them as visited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        # BFS to update distances
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 4-directional
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    mat[nx][ny] = mat[x][y] + 1  # Update distance
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        return mat
```

Time Complexity: O(mn), where m and n are the dimensions of the matrix. Each cell is processed at most once.
Space Complexity: O(mn) in the worst case, for the queue and visited set.

Key intuitions and invariants:

- Start BFS from all 0 cells simultaneously (multi-source).
- The first time we reach a cell, it's guaranteed to be the shortest path due to BFS properties.
- We're essentially building a wavefront that expands from all 0s concurrently.
- The distance increases by 1 for each step away from a 0.

### Dynamic Programming (two-pass)

```python
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # First pass: check for left and top
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if i > 0 else float('inf')
                    left = mat[i][j - 1] if j > 0 else float('inf')
                    mat[i][j] = min(top, left) + 1

        # Second pass: check for bottom and right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if i < m - 1 else float('inf')
                    right = mat[i][j + 1] if j < n - 1 else float('inf')
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat
```

Time Complexity: O(mn), where m and n are the dimensions of the matrix. We make two passes over the matrix.
Space Complexity: O(1), as we modify the input matrix in-place.

Key intuitions and invariants:

- The distance to the nearest 0 can be calculated by considering the minimum distance from four directions.
- We can break this down into two passes: top-left to bottom-right, and then bottom-right to top-left.
- In each pass, we're effectively propagating distance information from two directions.
- This approach works because the Manhattan distance is separable in x and y directions.

### Brute Force with optimization

```python
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def find_nearest_zero(i: int, j: int) -> int:
            if mat[i][j] == 0:
                return 0

            min_dist = float('inf')
            for x in range(m):
                for y in range(n):
                    if mat[x][y] == 0:
                        dist = abs(x - i) + abs(y - j)
                        if dist < min_dist:
                            min_dist = dist
                        if min_dist <= 1:  # Early termination
                            return min_dist
            return min_dist

        return [[find_nearest_zero(i, j) for j in range(n)] for i in range(m)]
```

Time Complexity: O(m^2 \* n^2) in the worst case, but often better due to early termination.
Space Complexity: O(1) if we don't count the output matrix.

Key intuitions and invariants:

- For each cell, we search the entire matrix for the nearest 0.
- We can optimize by terminating early if we find a 0 at distance 1.
- This approach is straightforward but inefficient for large matrices.

## Recommendation

The Multi-source BFS approach is the best one to learn and present in an interview setting. It's efficient, elegant, and demonstrates a good understanding of graph algorithms and their application to matrix problems. It has optimal time complexity and is relatively easy to explain and implement.

The Dynamic Programming solution is also excellent and worth learning. It's very efficient and shows a deep understanding of how to break down the problem into subproblems. In an interview, you could discuss both approaches, starting with BFS and then mentioning DP as an alternative that uses constant extra space.

The Brute Force approach, while correct, is not recommended for large matrices due to its high time complexity. However, it's worth mentioning in an interview as a starting point to demonstrate your problem-solving process.

## Test cases

```python
# Test case 1
mat1 = [[0,0,0],[0,1,0],[0,0,0]]
expected1 = [[0,0,0],[0,1,0],[0,0,0]]

# Test case 2
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
expected2 = [[0,0,0],[0,1,0],[1,2,1]]

# Test case 3 (edge case: single cell)
mat3 = [[0]]
expected3 = [[0]]

# Test case 4 (edge case: all 1s except one 0)
mat4 = [[1,1,1],[1,0,1],[1,1,1]]
expected4 = [[2,1,2],[1,0,1],[2,1,2]]

# Test case 5 (larger matrix)
mat5 = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,0,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]
expected5 = [
    [4,3,2,3,4],
    [3,2,1,2,3],
    [2,1,0,1,2],
    [3,2,1,2,3],
    [4,3,2,3,4]
]

solution = Solution()
assert solution.updateMatrix(mat1) == expected1
assert solution.updateMatrix(mat2) == expected2
assert solution.updateMatrix(mat3) == expected3
assert solution.updateMatrix(mat4) == expected4
assert solution.updateMatrix(mat5) == expected5

print("All test cases passed!")
```

## Overview of rejected approaches

1. Dijkstra's Algorithm: While this would work, it's overkill for this problem. The edges in our implicit graph all have weight 1, so BFS is more efficient and simpler.

2. Floyd-Warshall Algorithm: This all-pairs shortest path algorithm would be extremely inefficient (O(n^3) for n cells) and unnecessary given the structure of the problem.

3. DFS (Depth-First Search): While DFS could be used, it's not as efficient as BFS for finding shortest paths in unweighted graphs. DFS might explore unnecessarily long paths before finding the optimal solution.

4. Union-Find: This data structure is typically used for disjoint set problems and doesn't directly apply to finding distances in a matrix.

These approaches are either overkill, inefficient, or not well-suited to the specific characteristics of this problem, which is why they were not included in the main solution approaches.

## Visualization(s)

For the Multi-source BFS approach, we can visualize the process using a simple React component:

```tsx
import React, { useState, useEffect } from "react";

const BFSVisualization = () => {
  const [matrix, setMatrix] = useState([
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
  ]);
  const [step, setStep] = useState(0);

  const colors = [
    "#4CAF50",
    "#8BC34A",
    "#CDDC39",
    "#FFEB3B",
    "#FFC107",
    "#FF9800",
    "#FF5722",
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setStep(
        (prevStep) => (prevStep + 1) % (matrix.length * matrix[0].length),
      );
    }, 1000);
    return () => clearInterval(timer);
  }, [matrix]);

  const getCellColor = (value) => {
    if (value === 0) return "#2196F3";
    return colors[Math.min(value - 1, colors.length - 1)];
  };

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-xl font-bold mb-4">BFS Visualization</h2>
      <div className="grid grid-cols-4 gap-1">
        {matrix.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className="w-12 h-12 flex items-center justify-center text-white font-bold"
              style={{
                backgroundColor: getCellColor(cell),
                opacity: i * matrix[0].length + j <= step ? 1 : 0.3,
              }}
            >
              {cell}
            </div>
          )),
        )}
      </div>
      <p className="mt-4">Step: {step + 1}</p>
    </div>
  );
};

export default BFSVisualization;
```

This visualization shows how the BFS algorithm progresses through the matrix, updating the distances from 0 cells. The colors represent the distance from the nearest 0, with blue being 0 and warmer colors representing increasing distances. The visualization updates every second to show the progression of the algorithm.
