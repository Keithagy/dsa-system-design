## Explanation: Flood Fill

### Analysis of problem & input data

This problem is a classic example of a graph traversal problem, specifically suited for depth-first search (DFS) or breadth-first search (BFS) algorithms. The key characteristics of the problem are:

1. 2D Grid Representation: The image is represented as a 2D grid, which can be treated as a graph where each cell is a node.
2. 4-Directional Connectivity: The flood fill spreads to adjacent cells only in four directions (up, down, left, right), not diagonally.
3. Color-based Propagation: The fill only applies to cells that match the starting cell's color.
4. In-place Modification: The algorithm modifies the original image rather than creating a new one.

The pattern-matching here leads us to graph traversal algorithms. The choice between DFS and BFS depends on the specific requirements, but both will work. DFS is often simpler to implement recursively and uses less additional memory for this particular problem.

The key principle that makes this question simple is the recursive nature of the flood fill operation. Each cell that needs to be filled can be treated as a new starting point for the same operation, naturally lending itself to a recursive solution.

### Test cases

1. Standard case: As given in Example 1
2. No change needed: As given in Example 2
3. Single cell image: `[[1]]`, `sr = 0`, `sc = 0`, `color = 2`
4. Large image with single color: `[[1] * 50] * 50`, `sr = 25`, `sc = 25`, `color = 2`
5. Image with alternating colors: `[[1,0,1,0],[0,1,0,1],[1,0,1,0]]`, `sr = 1`, `sc = 1`, `color = 2`

Here's the Python code for these test cases:

```python
def test_flood_fill(func):
    tests = [
        ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),
        ([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]]),
        ([[1]], 0, 0, 2, [[2]]),
        ([[1] * 50] * 50, 25, 25, 2, [[2] * 50] * 50),
        ([[1,0,1,0],[0,1,0,1],[1,0,1,0]], 1, 1, 2, [[1,0,1,0],[0,2,0,1],[1,0,1,0]])
    ]

    for i, (image, sr, sc, color, expected) in enumerate(tests):
        result = func(image, sr, sc, color)
        assert result == expected, f"Test case {i+1} failed. Expected {expected}, got {result}"
    print("All test cases passed!")

# Usage:
# test_flood_fill(flood_fill)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Depth-First Search (DFS) - Recursive: Most intuitive and concise solution.
2. Depth-First Search (DFS) - Iterative: Useful for understanding stack-based approaches.
3. Breadth-First Search (BFS): Optimal for level-order traversal, though not necessarily needed here.

Count: 3 solutions

##### Rejected solutions

1. Brute Force: Checking every cell in the image is inefficient.
2. Union-Find: While it could work, it's overly complex for this problem.

#### Worthy Solutions

1. Depth-First Search (DFS) - Recursive

```python
from typing import List

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or image[sr][sc] == color:
        return image

    original_color = image[sr][sc]
    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != original_color:
            return

        image[r][c] = color  # Fill the current cell

        # Recursively fill in all four directions
        dfs(r-1, c)  # Up
        dfs(r+1, c)  # Down
        dfs(r, c-1)  # Left
        dfs(r, c+1)  # Right

    dfs(sr, sc)
    return image
```

Time Complexity: O(N), where N is the number of pixels in the image. In the worst case, we might need to visit every pixel.
Space Complexity: O(N) in the worst case (for a fully connected component of the same color), due to the recursive call stack.

- The algorithm leverages the recursive nature of the flood fill operation.
- It maintains the invariant that only cells of the original color are filled.
- The base case checks prevent out-of-bounds access and unnecessary recursion.
- The algorithm naturally stops when it reaches cells of a different color or the image boundaries.

2. Depth-First Search (DFS) - Iterative

```python
from typing import List

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or image[sr][sc] == color:
        return image

    original_color = image[sr][sc]
    rows, cols = len(image), len(image[0])
    stack = [(sr, sc)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while stack:
        r, c = stack.pop()
        if image[r][c] == original_color:
            image[r][c] = color

            # Add valid neighboring cells to the stack
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    stack.append((nr, nc))

    return image
```

Time Complexity: O(N), where N is the number of pixels in the image.
Space Complexity: O(N) in the worst case, due to the stack.

- This solution mimics the recursive approach using an explicit stack.
- It maintains the same invariants as the recursive solution.
- The stack ensures that we process cells in a depth-first manner.
- By checking the color before adding to the stack, we avoid redundant operations.

3. Breadth-First Search (BFS)

```python
from typing import List
from collections import deque

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or image[sr][sc] == color:
        return image

    original_color = image[sr][sc]
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        r, c = queue.popleft()
        if image[r][c] == original_color:
            image[r][c] = color

            # Add valid neighboring cells to the queue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    queue.append((nr, nc))

    return image
```

Time Complexity: O(N), where N is the number of pixels in the image.
Space Complexity: O(N) in the worst case, due to the queue.

- This solution processes cells in a breadth-first manner.
- It ensures that cells are filled in order of their distance from the starting point.
- The queue data structure efficiently manages the order of cell processing.
- While not necessarily more efficient for this problem, BFS can be useful in scenarios where level-order traversal is important.

#### Rejected Approaches

1. Brute Force: Iterating through every cell in the image and checking if it's connected to the starting cell would work, but it's inefficient with a time complexity of O(N^2) where N is the total number of pixels.

2. Union-Find: While this data structure could theoretically be used to group connected components, it's overly complex for this problem and doesn't leverage the natural order of traversal that DFS or BFS provide.

#### Final Recommendations

The recursive DFS approach is recommended as the best solution to learn for this problem. It's concise, intuitive, and directly maps to the problem description. It also demonstrates a good understanding of recursive problem-solving, which is valuable in many graph and tree-based problems.

However, it's also worth understanding the iterative DFS and BFS approaches, as they demonstrate important concepts (explicit stack management and level-order traversal) that are applicable to a wide range of problems.

### Visualization(s)

Here's a simple visualization of how the flood fill algorithm works using the recursive DFS approach:

```tsx
import React, { useState, useEffect } from "react";

const FloodFillVisualization = () => {
  const [grid, setGrid] = useState([
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
  ]);
  const [step, setStep] = useState(0);

  const steps = [
    { r: 1, c: 1 },
    { r: 1, c: 0 },
    { r: 0, c: 1 },
    { r: 0, c: 0 },
    { r: 0, c: 2 },
    { r: 2, c: 0 },
  ];

  useEffect(() => {
    if (step < steps.length) {
      const newGrid = grid.map((row) => [...row]);
      const { r, c } = steps[step];
      newGrid[r][c] = 2;
      setGrid(newGrid);
    }
  }, [step]);

  return (
    <div className="p-4">
      <div className="grid grid-cols-3 gap-2 mb-4">
        {grid.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className={`w-12 h-12 border ${
                cell === 0
                  ? "bg-gray-300"
                  : cell === 1
                    ? "bg-blue-300"
                    : "bg-red-300"
              }`}
            />
          )),
        )}
      </div>
      <button
        onClick={() => setStep((prev) => Math.min(prev + 1, steps.length))}
        className="px-4 py-2 bg-blue-500 text-white rounded"
      >
        Next Step
      </button>
      <p className="mt-2">
        Step: {step} / {steps.length}
      </p>
    </div>
  );
};

export default FloodFillVisualization;
```

This visualization demonstrates how the flood fill algorithm progresses through the grid, changing the color of connected cells one by one. The red cells represent the new color (2 in our example), while blue cells represent the original color (1) and gray cells represent the color 0 which is not changed.
