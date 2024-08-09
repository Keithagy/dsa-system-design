# Explanation: Rotting Oranges

## Analysis of problem & input data

This problem presents several key characteristics that guide us towards an optimal solution:

1. Grid-based problem: The input is a 2D grid, which often suggests traversal or search algorithms.

2. State propagation: The rotting process spreads from rotten oranges to fresh ones, indicating a spreading or infection-like pattern.

3. Time-based progression: The question asks for the minimum time, which suggests we need to track the progression of the rotting process over time.

4. 4-directional adjacency: The rotting only occurs in four directions (up, down, left, right), which limits the spreading pattern.

5. Multiple starting points: There can be multiple rotten oranges at the beginning, each acting as a source of rot.

6. Termination conditions: We need to either find the time when all oranges are rotten, or determine if it's impossible.

7. Small grid size: The constraints (1 <= m, n <= 10) indicate that the grid is relatively small, which means computational complexity might not be a significant concern.

The key principle that simplifies this question is that it's essentially a multi-source breadth-first search (BFS) problem. BFS is ideal because:

- It naturally models the simultaneous spreading of rot from all sources.
- It guarantees the shortest path (or in this case, the minimum time) to reach each cell.
- The level-by-level expansion of BFS corresponds perfectly to the minute-by-minute progression of rot.

## Solutions

### Solution 1: Multi-source BFS with Queue

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Step 2: Perform BFS
        max_time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        while queue and fresh_oranges > 0:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark as rotten
                    fresh_oranges -= 1
                    queue.append((nr, nc, time + 1))

        # Step 3: Check if all oranges are rotten
        return max_time if fresh_oranges == 0 else -1
```

#### Explanation

- We use a queue to perform BFS, starting with all initially rotten oranges.
- Each element in the queue is a tuple (row, col, time) representing the position and the time at which the orange at that position became rotten.
- We keep track of the number of fresh oranges and decrement it as oranges rot.
- The BFS continues until either all fresh oranges are rotten or we can't rot any more oranges.
- The maximum time encountered during BFS is our answer, unless there are still fresh oranges left.

#### Time Complexity: O(m \* n), where m and n are the dimensions of the grid

- We potentially visit each cell once.

#### Space Complexity: O(m \* n)

- In the worst case, the queue might contain all cells of the grid.

### Solution 2: In-place BFS with Queue (Space Optimized)

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Step 2: Perform BFS
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh_oranges -= 1
                        queue.append((nr, nc))

        # Step 3: Check if all oranges are rotten
        return minutes if fresh_oranges == 0 else -1
```

#### Explanation

- This solution is similar to Solution 1, but it optimizes space usage by not storing the time in the queue.
- Instead, we process all oranges at the current time level before moving to the next minute.
- We use the grid itself to keep track of rotten oranges, avoiding the need for an additional visited set.

#### Time Complexity: O(m \* n), where m and n are the dimensions of the grid

- We potentially visit each cell once.

#### Space Complexity: O(min(m\*n, k)), where k is the number of rotten oranges

- The queue only contains the rotten oranges at the current time level.

## Recommendation

I recommend learning and implementing Solution 2 (In-place BFS with Queue) for the following reasons:

1. Space Efficiency: It optimizes space usage by not storing time in the queue and using the grid for marking.
2. Time Efficiency: It maintains the optimal time complexity of O(m \* n).
3. Simplicity: The code is straightforward and easy to understand.
4. Practical Application: This approach can be adapted to similar problems where you need to track the spread of something through a grid over time.

While Solution 1 is also correct and intuitive, Solution 2 demonstrates how to optimize space usage in BFS problems, which is a valuable skill in algorithm design.

## Test cases

```python
def test_oranges_rotting():
    solution = Solution()

    # Test case 1: Normal case
    assert solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

    # Test case 2: Impossible case
    assert solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

    # Test case 3: Already all rotten
    assert solution.orangesRotting([[0,2]]) == 0

    # Test case 4: Empty grid
    assert solution.orangesRotting([[]]) == 0

    # Test case 5: No fresh oranges
    assert solution.orangesRotting([[0,2,2],[0,2,2],[0,2,2]]) == 0

    # Test case 6: All fresh oranges
    assert solution.orangesRotting([[1,1,1],[1,1,1],[1,1,1]]) == -1

    # Test case 7: Complex case
    assert solution.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2

    print("All test cases passed!")

test_oranges_rotting()
```

## Overview of rejected approaches

1. Depth-First Search (DFS):

   - While DFS could potentially solve this problem, it's not optimal because it doesn't naturally model the simultaneous spreading of rot from multiple sources.
   - DFS would also make it harder to keep track of the minimum time, as it explores paths to their full depth before backtracking.

2. Brute Force Simulation:

   - An approach that simulates the rotting process minute by minute, checking all cells in each iteration, would work but would be less efficient.
   - Time complexity would be O((m\*n)^2) in the worst case, which is not optimal.

3. Union-Find:

   - While Union-Find is great for connected components problems, it doesn't naturally handle the time progression aspect of this problem.
   - It would be challenging to determine the minimum time using Union-Find alone.

4. Dynamic Programming:
   - DP is typically used when we have overlapping subproblems and optimal substructure, which isn't the case here.
   - The rotting process depends on the current state of neighboring cells, making it difficult to formulate a DP solution.

These approaches are either incorrect for this specific problem or significantly less efficient than the BFS approach, which is why they are not recommended.

## Visualization(s)

To visualize the BFS process, we can create a simple animation using ASCII characters. Here's a function that can be added to the Solution class to print the grid state at each minute:

```python
def visualize_rotting_process(self, grid: List[List[int]]) -> None:
    original_grid = [row[:] for row in grid]
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes = 0

    print(f"Initial state (Minute 0):")
    self.print_grid(grid)

    while queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc))

        print(f"\nAfter Minute {minutes}:")
        self.print_grid(grid)

    if fresh_oranges > 0:
        print("\nImpossible to rot all oranges!")
    else:
        print(f"\nAll oranges rotted in {minutes} minutes!")

def print_grid(self, grid: List[List[int]]) -> None:
    for row in grid:
        print(" ".join(["🟩" if cell == 0 else "🍊" if cell == 1 else "🦠" for cell in row]))

# Usage:
solution = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
solution.visualize_rotting_process(grid)
```

This visualization will print the state of the grid at each minute, using emojis to represent empty cells (🟩), fresh oranges (🍊), and rotten oranges (🦠). This helps in understanding how the rotting process spreads over time.
