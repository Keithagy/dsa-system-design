## Explanation: 01 Matrix

### Analysis of problem & input data

This problem is a classic example of a distance-based matrix traversal, which can be efficiently solved using graph traversal algorithms. The key characteristics of this problem are:

1. Binary matrix input: The input is a matrix containing only 0s and 1s.
2. Distance calculation: We need to find the Manhattan distance from each cell to the nearest 0.
3. Multi-source problem: There can be multiple 0s in the matrix, each acting as a source.

The key principle that makes this question simple is the realization that this is essentially a multi-source breadth-first search (BFS) problem. BFS guarantees that we always find the shortest path first, which in this case translates to the shortest distance to a 0.

Pattern-matching wise, this problem falls into the category of:

- Graph traversal problems
- Matrix traversal problems
- Distance calculation problems

The optimal solution leverages the fact that BFS explores all cells at a given distance before moving to cells at a greater distance, naturally giving us the shortest distance to a 0 for each cell.

### Test cases

1. Edge case: Single cell matrix
   Input: [[0]]
   Output: [[0]]

2. Edge case: Matrix with all 0s
   Input: [[0,0],[0,0]]
   Output: [[0,0],[0,0]]

3. Edge case: Matrix with all 1s except one 0
   Input: [[1,1,1],[1,0,1],[1,1,1]]
   Output: [[2,1,2],[1,0,1],[2,1,2]]

4. General case: Mixed 0s and 1s
   Input: [[0,0,0],[0,1,0],[1,1,1]]
   Output: [[0,0,0],[0,1,0],[1,2,1]]

5. Larger matrix case:
   Input: [[1,1,1,1],[1,1,1,1],[1,1,1,0],[1,1,1,1],[1,1,1,1]]
   Output: [[4,3,2,1],[3,2,1,1],[2,1,1,0],[3,2,1,1],[4,3,2,1]]

Here's the Python code for these test cases:

```python
def test_update_matrix(func):
    test_cases = [
        ([[0]], [[0]]),
        ([[0,0],[0,0]], [[0,0],[0,0]]),
        ([[1,1,1],[1,0,1],[1,1,1]], [[2,1,2],[1,0,1],[2,1,2]]),
        ([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
        ([[1,1,1,1],[1,1,1,1],[1,1,1,0],[1,1,1,1],[1,1,1,1]],
         [[4,3,2,1],[3,2,1,1],[2,1,1,0],[3,2,1,1],[4,3,2,1]])
    ]

    for i, (input_matrix, expected_output) in enumerate(test_cases):
        result = func(input_matrix)
        assert result == expected_output, f"Test case {i+1} failed. Expected {expected_output}, but got {result}"
    print("All test cases passed!")

# Usage:
# test_update_matrix(update_matrix)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Multi-source BFS (optimal)
2. Dynamic Programming (DP) with two passes
3. DFS with memoization

Count: 3 solutions

##### Rejected solutions

1. Brute Force approach (checking distance to every 0 for each cell)
2. Single-source BFS from each 1 (inefficient for large matrices)

#### Worthy Solutions

##### Multi-source BFS

```python
from collections import deque
from typing import List

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    queue = deque()
    visited = set()

    # Initialize queue with all 0s and mark them as visited
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))

    # BFS
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 4-directional
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx, ny))
                visited.add((nx, ny))

    return mat
```

Time Complexity: O(m _n), where m and n are the dimensions of the matrix
Space Complexity: O(m_ n) for the queue and visited set in the worst case

- Intuition:

  - Start BFS from all 0 cells simultaneously
  - Each step of BFS represents increasing distance from 0
  - First time a cell is visited gives its shortest distance to a 0

- Invariants:
  - Cells in the queue are always processed in order of increasing distance from 0
  - Each cell is visited only once, ensuring optimal distance calculation

##### Dynamic Programming (DP) with two passes

```python
from typing import List

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    MAX_DIST = m + n  # Maximum possible distance in the matrix

    # First pass: check for left and top
    for i in range(m):
        for j in range(n):
            if mat[i][j] != 0:
                top = mat[i - 1][j] if i > 0 else MAX_DIST
                left = mat[i][j - 1] if j > 0 else MAX_DIST
                mat[i][j] = min(top, left) + 1

    # Second pass: check for bottom and right
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if mat[i][j] != 0:
                bottom = mat[i + 1][j] if i < m - 1 else MAX_DIST
                right = mat[i][j + 1] if j < n - 1 else MAX_DIST
                mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

    return mat
```

Time Complexity: O(m \* n)
Space Complexity: O(1) (in-place modification)

- Intuition:

  - Distance to nearest 0 can be calculated by considering distances from four directions
  - Two passes ensure we consider all directions efficiently

- Invariants:
  - After first pass, each cell contains minimum distance considering only left and top neighbors
  - After second pass, each cell contains global minimum distance considering all four directions

##### DFS with memoization

```python
from typing import List, Tuple

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    memo = {}

    def dfs(i: int, j: int) -> int:
        if (i, j) in memo:
            return memo[(i, j)]
        if mat[i][j] == 0:
            return 0

        min_dist = float('inf')
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                min_dist = min(min_dist, dfs(ni, nj) + 1)

        memo[(i, j)] = min_dist
        return min_dist

    for i in range(m):
        for j in range(n):
            mat[i][j] = dfs(i, j)

    return mat
```

Time Complexity: O(m _n)
Space Complexity: O(m_ n) for memoization

- Intuition:

  - For each cell, recursively explore all directions to find the nearest 0
  - Memoization prevents redundant calculations

- Invariants:
  - Once a cell's distance is calculated and memoized, it's never recalculated
  - The recursive calls always terminate at cells with value 0

#### Rejected Approaches

1. Brute Force approach:

   - For each cell, check its distance to every 0 in the matrix
   - Time complexity: O((mn)^2), which is inefficient for large matrices

2. Single-source BFS from each 1:
   - Perform a separate BFS starting from each 1 to find its nearest 0
   - Time complexity: O((mn)^2) in the worst case, inefficient for matrices with many 1s

These approaches are correct but not optimal due to their high time complexity, making them impractical for larger inputs.

#### Final Recommendations

The Multi-source BFS approach is the best solution to learn for this problem. It's intuitive, efficient, and demonstrates a good understanding of graph traversal algorithms. The DP solution is also worth learning as it showcases a different problem-solving paradigm and has the advantage of in-place modification. The DFS with memoization, while correct, is less intuitive and potentially less efficient due to the overhead of recursive calls.

### Visualization(s)

To visualize the Multi-source BFS approach, we can use a simple React component that shows the step-by-step process of the BFS algorithm on a sample matrix.

```tsx
import React, { useState, useEffect } from "react";

const BfsVisualization = () => {
  const [matrix, setMatrix] = useState([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
  ]);
  const [step, setStep] = useState(0);
  const [queue, setQueue] = useState([]);

  useEffect(() => {
    const initialQueue = [];
    const newMatrix = matrix.map((row, i) =>
      row.map((cell, j) => {
        if (cell === 0) {
          initialQueue.push([i, j]);
          return { value: 0, visited: true };
        }
        return { value: Infinity, visited: false };
      }),
    );
    setMatrix(newMatrix);
    setQueue(initialQueue);
  }, []);

  const nextStep = () => {
    if (queue.length === 0) return;

    const [x, y] = queue.shift();
    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    const newMatrix = [...matrix];
    directions.forEach(([dx, dy]) => {
      const nx = x + dx;
      const ny = y + dy;
      if (
        nx >= 0 &&
        nx < matrix.length &&
        ny >= 0 &&
        ny < matrix[0].length &&
        !newMatrix[nx][ny].visited
      ) {
        newMatrix[nx][ny] = {
          value: newMatrix[x][y].value + 1,
          visited: true,
        };
        queue.push([nx, ny]);
      }
    });

    setMatrix(newMatrix);
    setQueue([...queue]);
    setStep(step + 1);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">01 Matrix BFS Visualization</h2>
      <div className="grid grid-cols-4 gap-2 mb-4">
        {matrix.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className={`w-12 h-12 flex items-center justify-center border ${
                cell.visited ? "bg-blue-200" : "bg-gray-200"
              }`}
            >
              {cell.value === Infinity ? "∞" : cell.value}
            </div>
          )),
        )}
      </div>
      <button
        onClick={nextStep}
        className="bg-blue-500 text-white px-4 py-2 rounded"
        disabled={queue.length === 0}
      >
        Next Step
      </button>
      <p className="mt-2">Step: {step}</p>
    </div>
  );
};

export default BfsVisualization;
```

This visualization demonstrates how the BFS algorithm updates the matrix step by step, starting from the initial 0 cells and propagating the distances outward. The blue cells represent visited cells, and the numbers in each cell show the current distance from the nearest 0. You can click the "Next Step" button to see how the algorithm progresses.
